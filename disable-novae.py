import paramiko
import time
from subprocess import check_output


def main():
    novaessh = paramiko.SSHClient()
    novaessh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    novaessh.connect("<ip address>", 22, "<username>", "<password>")
    novaessh.exec_command('/home/markz/novae/target/debug/cli disable')

    rossh = paramiko.SSHClient()
    rossh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    rossh.connect("<ip address>", 22, "<username>", "<password>")
    rossh.exec_command('/interface disable sstp-nv')
    rossh.exec_command('/ip firewall mangle disable [find comment="mark routing go-foreign"]')
    rossh.exec_command('/ip firewall mangle disable [find comment="mark routing go-domestic"]')
    rossh.exec_command('/ip route disable [find comment="policy route go-foreign"]')
    rossh.exec_command('/ip route disable [find comment="policy route go-domestic"]')
    rossh.exec_command('/ip route enable [find comment="backup default route"]')

    stdin, stdout, stderr = novaessh.exec_command('<disconnect>')
    for line in stdout.readlines():
        print(line.strip('\r\n'))

    check_output("ipconfig /flushdns", shell=True)
    time.sleep(1)


if __name__ == "__main__":
        main()
