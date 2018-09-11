
# 案例1:斐波那契数列
# fobj=[1,2]
# l=int(input('长度：'))
# for i in range(l-len(fobj)):
#     fobj.append(fobj[-1]+fobj[-2])
# print(fobj)


# #案例2:九九乘法表
# n=int(input('长度：'))
# for i in range(n+1):
#     for j in range(1,i):
#         print('%s*%s=%s ' %(j,i,(j*i)),  end=' ' )
#     print()

###模块导入的特性if __name__ == '__main__':
# def  get():
#     name=input('12345')
#     return  name
# if __name__ == '__main__':
#
#     print(get())


# # 创建randpass.py脚本,要求如下:
# # 1.  编写一个能生成8位随机密码的程序
# # 2.  使用random的choice函数随机取出字符
# # 3.  改进程序,用户可以自己决定生成多少位的密码
#
# from string  import ascii_letters,digits
# from random import  choice
#
# choines=ascii_letters+digits
#
# def randpass(l=8):
#     password=''
#     for i in range(l):
#         n=choice(choines)
#         password+=n
#
#     return password
#
# if __name__ == '__main__':
#     print(randpass())
#     l=int(input('自定义密码长度：'))
#     m=randpass(l)
#     print(m)




'''
1、思考一下，程序的运行场景
2、构思程序的结构，把每一个功能，写成一个函数
3、编写主程序代码，把这些函数串联起来
4、编写具体的函数代码部分
'''

# 案例1:创建文件
# 1.  编写一个程序,要求用户输入文件名
# 2.  如果文件已存在,要求用户重新输入
# 3.  提示用户输入数据,每行数据先写到列表中
# 4.  将列表数据写入到用户输入的文件名中


# import os
#
# def get_fname():
#     while True:
#         fname=input('filename:')
#         if not os.path.exists(fname):
#      #判断文件不存在时
#             break
#         print('%s already exists , Try again ' % fname)
#
#     return  fname
#
#
# def get_content():
#     content=[]
#     print('请输入正文，end结束')
#     while True:
#         line=input('>')
#         if line=='end':
#             break
#         content.append(line)
#
#     return content
#
#
# def wfile(fname,content):
#     with   open(fname, 'w') as fobj:
#         fobj.writelines(content)
#
#
# if __name__ == '__main__':
#     fname=get_fname()
#     content=get_content()
#     content=['%s\n' % line for line in content]
#     wfile(fname,content)


# user=['zhangsan','lisi','bob']
# # for ind,user  in enumerate(user):
# #     print('%s,%s' % (ind,user))
#
# a=list(enumerate(user))
# print(a)

# phone='qesyhere'
# print(phone[:-2])
# print(phone[1:3])
# print(phone[1:2:3])


# 案例2:检查标识符
# 1.  程序接受用户输入
# 2.  判断用户输入的标识符是否合法
# 3.  用户输入的标识符不能使用关键字
# 4.  有不合法字符,需要指明第几个字符不合法
# import keyword
# import string
#
# first_str=string.ascii_letters + '_'
# other_str=string.digits+first_str
#
# def check_id():
#     if keyword.iskeyword(id):
#         return '\033[31;1m%s is keyword\033[0m'  % id ,'Try again!!!'
#
#     if  id[0] not  in first_str:
#         return  '\033[31;1m首\033[0m字符不合法'
#
#     for ind,ch  in enumerate(id[1:]):
#         if  ch  not in other_str:
#             return  '\033[33;1m第%s个字符\033[31;1m不合法\033[0m'  % (ind+2)
#
#     return '%s\033[32;1m字符合法\033[0m' % id
#
#
#
# if __name__ == '__main__':
#     id=input('please input str:')
#     print(check_id())















