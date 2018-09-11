##闭包

def couter(start=0):
    count=start
    def incr():
        nonlocal  count     #count既不是局部的,也不是全局的,用nonlocal
        count+=1
        return  count
    return  incr            #外层函数的返回值是

if __name__ == '__main__':
    a=couter()
    print(a())
    print(a())

    b=couter()
    print(b())
    print(b())
    print(a())
    print(b())