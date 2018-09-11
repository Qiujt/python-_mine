#理解进程的生命周期
# •  父进程fork出子进程并挂起
# •  子进程运行完毕后,释放大部分资源并通知父进程,这个时候,子进程被称作僵尸进程
# •  父进程获知子进程结束,子进程所有资源释放
#验证：一个终端watch -n1  ps  a ; 另外一个终端执行命令

import  os
import  time

pid=os.fork()
if pid:
    print('in parent, sleeping...')
    time.sleep(10)
    print(os.waitpid(-1,1))    #收拾子进程，如果子进程是僵尸进程，释放它#参考PDF
                                #如果不是，父进程什么也不做，继续向下执行
    time.sleep(10)

else:
    print('in child,sleeping...')
    time.sleep(15)

##父进程sleep(10)后，没有发现僵尸进程（子进程sleep(15)），所以没有实现杀死僵尸进程
##后手，os.waitpid(-1,1)，优先杀僵尸进程

#######################################################
# import  os
# import  time
#
# pid=os.fork()
# if pid:
#     print('in parent, sleeping...')
#     time.sleep(10)
# else:
#     print('in child,sleeping...')
#     time.sleep(15)


#父进程通过os.wait()来得到子进程是否终止的信息
#在子进程终止和父进程调用wait()之间的这段时间,子进程被称为zombie(僵尸)进程

# 如果子进程还没有终止,父进程先退出了,那么子进程会持续工作。系统自动将子进程的父进程设置为
# init进程,init将来负责清理僵尸进程   (rhel7用systemd)

# waitpid()接受两个参数
# 第一个参数设置为-1,表示与wait()函数相同;
# 第二参数如果设置为0表示挂起父进程,直到子程序退出,设置为1表示不挂起父进程
# waitpid()的返回值:如果子进程尚未结束则返回0,否则返回子进程的PID