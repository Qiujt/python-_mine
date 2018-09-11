# 案例4:扫描存活主机
# 1.  通过ping测试主机是否可达
# 2.  如果ping不通,不管什么原因都认为主机不可用
# 3.  通过多线程方式实现并发扫描

##传递函数给Thread类

import  subprocess
import  threading

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
    for ip in ips:      #主线程用于产生工作线程
        t=threading.Thread(target=ping,args=(ip,))
        t.start()       #将会执行ping(ip)，执行完就停止了，不会有僵尸进程
        #主线程不会等待工作线程结束，直接进入下次循环

##threading.Thread(target=ping,args=(ip,))
#传递IP给函数ping    #格式熟记