
# 多重继承
# •  python允许多重继承,即一个类可以是多个父类的子类,子类可以拥有所有父类的属性
class A:
    def foo(self):
        print('in A-foo')

class B:
    def bar(self):
        print('in B-bar')

class C(A, B):   #多重继承
    pass

if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()