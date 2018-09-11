#在远程主机上执行的命令
#安装paramiko模块

# paramiko实例
# •  编写用于实现ssh访问的脚本
# –  创建SSHClient实例          #ssh	=paramiko.SSHClient()
# –  设置添加主机密钥策略         #paramiko.AutoAddPolicy
# –  连接ssh服务器               #ssh.connect
# –  执行指定命令                 #ssh.exec_comand
# –  在shell命令行中接受用于连接远程服务器的密码以及在远程主机上执行的命令

import  paramiko

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
    rcmd=('192.168.4.20','123456','id  zhangsan')