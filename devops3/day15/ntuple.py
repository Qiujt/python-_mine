
#命名元组

'''
元组是序列类型的，它有下标，每一项没有名字。
命名的元组，可以为元组中的每一项起名，类似于字典的key
'''

import  collections

#p1=(10,20)
Point=collections.namedtuple('Point',['x','y','z'])   #namedtuple()函数,用于创建自定义的元组数据类型
                        #注意，前后的Point要求一致
p2=Point(10,30,40)      ###实例个数跟上面Point个数一致
p2[0]                   #像元组一样用下标来找到元素
p2[1:]                  #也可以切片
p2.x                    #也可以像OOP对象一样用实例，属性


def a():
    pass

def b():
    pass

def c():
    pass

def call_func(func):
    func()

call_func(a)
call_func(b)