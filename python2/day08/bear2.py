##组合
# •  类被定义后,目标就是要把它当成一个模块来使用,并把这些对象嵌入到你的代码中去
# •  组合就是让不同的类混合并加入到其它类中来增加功能和代码重用性
# •  可以在一个大点的类中创建其它类的实例,实现一些其它属性和方法来增强对原来的类对象
#
# 两个类明显不同，一个类是另一个类的组件（class Vendor是class BearToy的组件）

class Vendor:  ##制造商
    def  __init__(self,phone,email):
        self.phone=phone
        self.email=email

    def send_email(self):
        print('Send email to %s'  %self.email)
##组合

class  BearToy:
    def  __init__(self,name,size,color,phone,email):      #在实例化时自动执行
        self.name=name
        self.size=size
        self.color=color
        self.vendor=Vendor(phone,email)

    def sing(self):
        print('I am %s,lalalal...' % self.name)


if __name__ == '__main__':
    #把参数传给_init_,实例本身，如tidy，自动作为第一个参数传递给self
    tidy=BearToy('tidy','middle','yellow','020-888-888-88','admin@jay.cn')
    # print(tidy.size)
    # print(tidy.color)
    # tidy.sing()
    tidy.vendor.send_email()