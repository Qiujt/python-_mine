#继承
#调用父类def(方法)(先执行子类的def（方法）          ##类局部变量与全局变量
class  BearToy:                               #类，玩具熊的基本属性
    def  __init__(self,name,size,color):      #在实例化时自动执行
        self.name=name
        self.size=size
        self.color=color

    def sing(self):                            #玩具熊sing
        print('I am %s,lalalal...' % self.name)

class  NewBear(BearToy):          #父类，也叫基类，是BearToy
    def  __init__(self,name,size,color,material):
        #BearToy.__init__(self,name,size,color)     ##等价于super.....
        super(NewBear,self).__init__(name,size,color)
        self.masterial=material

    def  run(self):                #定义新属性run
        print('running...')


if __name__ == '__main__':
    #把参数传给_init_,实例本身，如b1，自动作为第一个参数传递给self
    b1=NewBear('big_bear','Large','Brown','cotton')      #实例（对象是类的实例）b1
    b1.sing()
    b1.run()