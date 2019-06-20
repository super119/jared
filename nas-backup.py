import os
import win32file
import hashlib
import sys
import platform


SRCDIR = r'<Import folder path>'
PIPELINE = r'<Target folder path>'
PHOTOS = r'<Photo hash file path>'
VIDEOS = r'<Video hash file path>'


def hash_sha256(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def main():
    input('Make sure you have run photo-hashing & video-hashing scripts before continue... Go?')
    results = []
    phashes = []
    vhashes = []
    file_num = 0
    with open(PHOTOS, 'r', encoding='UTF-8') as f:
        for line in f:
            if line[0] == '#':
                continue
            phashes.append(line.rstrip())
    with open(VIDEOS, 'r', encoding='UTF-8') as f:
        for line in f:
            if line[0] == '#':
                continue
            vhashes.append(line.rstrip())

    for root, dirs, fnames in os.walk(SRCDIR):
        for file in fnames:
            file_num = file_num + 1
            fpath = os.path.join(root, file)
            fhash = hash_sha256(fpath)
            print('File ' + file + ' hash: ' + fhash)
            if fhash in phashes or fhash in vhashes:
                continue
            else:
                results.append(file)

    if len(results) == 0:
        print('Congratulations! No missing file is found.')
    else:
        input('Files in total: ' + str(file_num) + '. Found missing files: ' + str(len(results)) + '. Continue?')
        for r in results:
            print('Copying ' + r + "...   ", end='')
            win32file.CopyFile(SRCDIR + '\\' + r, PIPELINE + '\\' + r, 0)
            print('Done')
    input('Done.')


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        input('This script is only tested on Python 3. Please use Python 3 instead.')
        exit(1)
    if platform.system() != 'Windows':
        input('This script is only supported running on Windows.')
        exit(1)
    main()
