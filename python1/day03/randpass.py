#方法一：
# import random
# import string
# #str_list='asdfghjklqwertyuioppzxcvbnm'
# str_list=string.ascii_letters+string.digits
# #passwd=random.choice('asdfghjklqwertyuioppzxcvbnm')
# def randpass(n=8):
#     password = ''
#     for i in range(n):
#         x=random.choice(str_list)
#         password+=x
#     return  password
# if __name__ == '__main__':
#     print('%s: %s' %('默认随机生成8位密码' , randpass()))
#     n=int(input('可以定义密码长度:'))
#     m=randpass(n)
#     print(m)


#方法二：
from random import  choice
from string import ascii_letters,digits

str_list=ascii_letters+digits

def  randpass(n=8):
    result=[choice(str_list)  for i in range(n)]
    return  ''.join(result)
if __name__ == '__main__':
    print('%s: %s' %('默认随机生成8位密码' , randpass()))
    n=int(input('可以定义密码长度:'))
    m=randpass(n)
    print(m)


