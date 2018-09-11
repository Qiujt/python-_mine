# OOP简介
# 基本概念
# •  类(Class):用来描述具有相同的属性和方法的对象的集合。
# 它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# •  实例化:创建一个类的实例,类的具体对象。
# •  方法:类中定义的函数。
# •  对象:通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法。

class  BearToy:                               #类，玩具熊的基本属性
    def  __init__(self,name,size,color):      #在实例化时自动执行
        self.name=name                        #tidy.name=name
        self.size=size
        self.color=color

    def sing(self):                            #玩具熊sing
        print('I am %s,lalalal...' % self.name)


if __name__ == '__main__':
    #把参数传给_init_,实例本身，如tidy，自动作为第一个参数传递给self
    tidy=BearToy('tidy','middle','yellow')      #实例（对象是类的实例）tidy；
                                                #类是蓝图,实例是根据蓝图（规则）创建出来的具体对象
    print(tidy.size)
    print(tidy.color)
    tidy.sing()