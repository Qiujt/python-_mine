#day06
#案例4:测试程序运行效率
import  time

def timeit(func):
    start=time.time()
    func()
    end=time.time()
    print(end-start)

def  funca():
    time.sleep(5)

def  funcb():
    print('hello world!!!')

if __name__ == '__main__':
    timeit(funca)
    timeit(funcb)
