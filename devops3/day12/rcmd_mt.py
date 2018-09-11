# 案例5:利用多线程实现ssh并发访问
# •  编写脚本程序
# 1.  在文件中取出所有远程主机IP地址
# 2.  在shell命令行中接受远程服务器IP地址文件、远程服务器密码以及在远程主机上执行的命令
# 3.  通过多线程实现在所有的远程服务器上并发执行命令

import threading
import  paramiko
import  sys
import  getpass
import  os

def  rcmd(host,password,cmd,port=22,username='root'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        port=port
    )

    stdin,stdout,stderr=ssh.exec_command(cmd)
    data = stdout.read().decode('utf8')
    error=stderr.read().decode('utf8')
    if data:
        print('[%s:OUT]:\n%s'  % (host,data))
    if error:
        print('[%s:ERROR]:/n%s' %(host,error))

    ssh.close()

if __name__ == '__main__':
    #rcmd=('192.168.4.20','123456','id  zhangsan')
    if  len(sys.argv)  !=3:
        print('Usage: %s  ipfile  "command"'  % sys.argv[0])
        exit(1)      ##给一个退出码（echo $?）
    pwd = getpass.getpass()
    ipfine = sys.argv[1]     #IP地址文件
    cmd =  sys.argv[2]
    if not os.path.isfile(ipfine):
        print('No such file:', ipfine)
        exit(2)

    with open(ipfine)as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=rcmd, args=(ip, pwd, cmd))
            t.start()
