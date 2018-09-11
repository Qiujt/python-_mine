##传递可调用类给Thread类（OOP方法）        ##多线程

import threading        #thread和threading模块允许程序员创建和管理线程；后者更高级
import subprocess

class Ping:
    # def __init__(self, host):     #注释这，实例传到下面
    #     self.host = host

    def __call__(self, host):           ##多线程要求__call__
        result = subprocess.call(
            'ping -c2 %s &> /dev/null' % host,
            shell=True
        )
        if result == 0:  # result的值就是ping命令的退出码，即$?
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))
        t.start()  # Ping(ip)() <==> target()
#传递函数给Thread类

# 多线程编程有多种方法,传递函数给threading模块的Thread类是介绍的第一种方法
# Thread对象使用start()方法开始线程的执行,
# 使用join()方法挂起程序,直到线程结束

# 传递可调用类给Thread类是介绍的第二种方法
# 相对于一个或几个函数来说,由于类对象里可以使用类的强大的功能,\
# 可以保存更多的信息,这种方法更为灵活

