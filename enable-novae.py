import paramiko
import time
from subprocess import check_output


def main():
    rossh = paramiko.SSHClient()
    rossh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    rossh.connect("<ip address>", 22, "<username>", "<password>")
    rossh.exec_command('/interface enable sstp-nv')
    rossh.exec_command('/ip firewall mangle enable [find comment="mark routing go-foreign"]')
    rossh.exec_command('/ip firewall mangle enable [find comment="mark routing go-domestic"]')
    rossh.exec_command('/ip route disable [find comment="backup default route"]')
    rossh.exec_command('/ip route enable [find comment="policy route go-foreign"]')
    rossh.exec_command('/ip route enable [find comment="policy route go-domestic"]')

    novaessh = paramiko.SSHClient()
    novaessh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    novaessh.connect("<ip address>", 22, "<username>", "<password>")
    novaessh.exec_command('/home/markz/novae/target/debug/cli enable')
	
    check_output("ipconfig /flushdns", shell=True)
    time.sleep(1)


if __name__ == "__main__":
        main()
