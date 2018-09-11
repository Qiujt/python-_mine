# 案例2:扫描存活主机
# 1.  通过ping测试主机是否可达
# 2.  如果ping不通,不管什么原因都认为主机不可用
# 3.  通过fork方式实现并发扫描


import  subprocess
import  os

def  ping(host):
    result=subprocess.call(
        'ping -c2  %s  &>/dev/null' % host, shell=True
    )
    if result==0:    # result的值就是ping命令的退出码，即$?
        print('%s:up' % host)
    else:
        print('%s:down' % host)


if __name__ == '__main__':
    ips=['176.121.207.%s' % i for i  in range(1,255)]
    for ip in ips:
        pid=os.fork()   #父进程负责生成子进程
        if not pid:     #子进程负责ping
            ping(ip)
            exit()      #子进程ping完一个地址后结束，不要再循环
