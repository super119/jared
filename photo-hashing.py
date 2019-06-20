#!/usr/bin/env python3
import hashlib
import os
import sys
import platform


PHOTOS = r'<Photos folder path>'
RESULT = r'<Photo hash file saving path>'
IGNOREEXTS = [r'txt', r'py']


def hash_sha256(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def main():
    try:
        f_result = open(RESULT, 'w')
    except Exception as e:
        print('Open ' + RESULT + ' failed. Error: ' + str(e))
        return

    fexts = []
    for root, dirs, fnames in os.walk(PHOTOS):
        for f in fnames:
            fpath = os.path.join(root, f)
            if f[0] == '.':
                print('Ignore file: ' + fpath)
                continue
            '''
                This way can't handle filename like '.XXX'
                >>> a = '.Parent'
                >>> os.path.splitext(a)
                ('.Parent', '')
            '''
            ext = os.path.splitext(f)[1][1:]
            if ext not in fexts:
                fexts.append(ext)
            if ext in IGNOREEXTS:
                print('Ignore file: ' + fpath)
                continue

            fhash = hash_sha256(fpath)
            print('Hashing ' + fpath + ': ' + fhash)
            f_result.write('# ' + fpath + '\n')
            f_result.write(fhash + '\n')

    f_result.close()
    print('Got file extensions: ' + str(fexts))
    return


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print('This script is only tested on Python 3. Please use Python 3 instead.')
        exit(1)
    if platform.system() != 'Linux':
        print('This script is only supported running on Linux.')
        exit(1)
    main()
