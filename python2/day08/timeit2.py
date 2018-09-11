#day06
#案例4:测试程序运行效率
import  time
def  deco(func):
    def timeit():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
    return timeit

@deco
def  funca():
    time.sleep(5)

@deco
def  funcb():
    print('hello world!!!')

if __name__ == '__main__':
    funca
    funcb
