#生成器
#从句法上讲,生成器是一个带yield语句的函数


def mygen():
    yield 'hello world'
    a=10+20
    yield a
    yield  [10,20]



if __name__ == '__main__':
    a=mygen()
    for item in a:
        print(item)