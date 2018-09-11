import  os

# print('starting...')
# os.fork()               #生成子进程，后续代码将在父子进程中同时运行
# print('Hello  World')   #打印两次

print('starting...')
pid=os.fork()           #父进程返回值是子进程的PID，子进程的返回值是0
if pid:                  #熟记
    print('in parent')
else:
    print('in child')

print('done')


for i in range(5):
    pid = os.fork()   # 父进程负责生成子进程并挂起
    if not pid:  # 只有子进程才执行
        print('hello')
        exit()        ## 子进程遇到exit结束，不会回到循环条件处
#打印5个hello
#没有exit()打印11个hello

