#递归函数
#5!     ##5*4*3*2*1    ##5*4!


def  func(x):
    if x==1:
        return x

    return x * func(x-1)
        #3*func(2)
        #3*2*func(1)
        #3*2*1

if __name__ == '__main__':
    print(func(3))