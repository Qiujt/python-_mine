# 多进程，父进程将自身资源拷贝一份，生成子进程，程序在子进程中运行。所以，
# 子进程和父进程都有各自独立的运行空间
# 多线程（MT），包含在一个进程内，多个工作线程共享同一进程的资源。多线程没有僵尸问题

# GIL: 全局解释器锁。GIL的存在，导致某一时刻，只能把一个线程交给CPU处理
# 计算密集型程序：数据的提供不是问题，主要是CPU的效率，适合多进程  ##CPU多核
# IO密集型程序：CPU再快没用，因为它获得不到想要的数据，适合py多线程

# 作业：编写函数，函数接收一个字符串，将字符串左边、右边、两端空白字符去除
# 作业：百钱百鸡。鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
        # 公鸡一只5块，母鸡一只3块，小鸡3只一块。一百块钱买一百只鸡。
# 作业：通过多线程，编写TCP时间服务器
####################################################
#远程开机
#
#echer-wake -i enp1s0 c8:d3:ff:3c:32:1b     #//在同一个广播域里面的机器可以用广播的方法进行通讯
            #目标接收数据的网卡，   目标Mac地址
#获得Mac地址
# Ping -c2 -w1 192.163.12.1 &> /dev/null
# Arp -n 192.163.12.1   --->获得解析，再结合awk等

####################################################



import time
import  os
import  threading


def calc():
    result=0
    for i in range(50000000):
        result +=i
    print(result)

if __name__ == '__main__':
    # start=time.time()
    # calc()
    # calc()                      ##执行两次
    # end=time.time()
    # print(end-start)            ##没有开进程，用时3.8秒

############  开进程   ##########################
    # start=time.time()
    # pid=os.fork()                  #使用进程，用时零点多秒
    # if not pid:                     #两个加速原因，CPU核数，开进程
    #     calc()
    #     exit()
    # pid=os.fork()
    # if not pid:
    #     calc()
    #     exit()
    # os.waitpid(-1,0)        #处理子进程，挂起进程
    # os.waitpid(-1,0)
    # end=time.time()
    # print(end-start)

############  开线程  #########################
    start=time.time()
    t1=threading.Thread(target=calc)
    t1.start()
    t2=threading.Thread(target=calc)
    t2.start()
    t1.join()           #挂起主线程，等到t1线程结束后，再向下执行
    t2.join()
    end=time.time()
    print(end-start)
