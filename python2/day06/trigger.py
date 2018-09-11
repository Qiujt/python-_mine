#触发异常
#1、
def set_age(name,age):
    if not 0<age<120:
        raise  ValueError('年龄超出范围')     #ValueError可以其他报错
    print('%s is %d years old' % (name,age))

#2、断言是一句必须等价于布尔值为真的判定；此外,发生异常也意味着表达式为假
def set_age2(name,age):
    assert 0<age<120, '年龄超出范围'
    print('%s is %d years old' % (name,age))

if __name__ == '__main__':
    set_age('bob',23)
    set_age('bob',222)