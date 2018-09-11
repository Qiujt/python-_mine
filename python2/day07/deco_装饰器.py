#装饰器
# •  装饰器是在函数调用之上的修饰
# •  这些修饰仅是当声明一个函数或者方法的时候,才会应用的额外调用
# •  使用装饰器的情形有:
# –  引入日志
# –  增加计时逻辑来检测性能
# –  给函数加入事务的能力


def  colors(func):
    def  set_color():
        return '\033[31;1m%s\033[0m' % func()
    return  set_color()

@colors
def hello():
    return 'Hello  World!'

@colors
def  welcome():
    return 'How are you?'

if __name__ == '__main__':
    print(hello)        #因为有装饰器,此处不是调用hello函数,而是将hello作为colors的参数
    #print(hello())      #()实际上是对set_color的调用
    #print(welcome())