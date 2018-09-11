
#######################################################################
# #day03
#
# astr='abc'                          #字符窜
# alist=['bob','alice']               #列表
# atuple=(10,20,30)                   #元组
# adict={'name':'张三','age':22}        #字典
#
#
# for ch in astr:
#     print(ch)
#
# for name in alist:
#     print(name)
#
# for i in atuple:
#     print(i)
#
# for key in adict:
#     print('%s: %s'  % (key, adict[key]))



# range函数
# •  for循环常与range函数一起使用
# •  range函数提供循环条件
# •  range函数的完整语法为:
# range(start, end, step =1)

#1、for  range函数：
# print(list(range(10)))        #只写10，表示结束数字为10，但是不包含10，开始数字为0
# print(list(range(6,11)))       #列拜方式列出【6，7.8，9，10】
# print(list(range(1,10,2)))     #列出【1,3,5,7,9】
# print(list(range(10,0,-1)))    #列出[10....1]
#
# for i in range(3):
#     print('hello')         #打印3次hello
#
# sum100=0                    #100内整数和
# for i in range(1,101):
#     sum100+=i
# print(sum100)


# fib=[0,1]                   #使用for循环和range函数编写一个程序,计算有10个数字的斐波那契数列
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# fib=[0,1]                       #可以生成用户需要长度的斐波那契数列
# l=int(input('length：'))
# for i in range(l-len(fib)):
#     fib.append(fib[-1] + fib[-2])
# print(fib)


#输出三行,每行各三个hello,
# for i in range(3):                #外层循环控制行
#     for j in range(i+1):          #内层循环控制某一行
#         print('hello',end=' ')
#     print()


# #案例2:九九乘法表
# for i in range(10):
#     for j in range(1,i+1):
#         #print('%d*%d= %d'% (j,i,i*j) ,end='   ')
#         print('%s*%s=%s'% (j,i,j*i), end='  ')
#     print()
#
################################################################
# #列表解析：
# # 语法:
# # [expr	for	iter_var in	iterable]
# [10]
# [3+2]                               #执行10次3+2
# [3+i for i in range(10)]            #循环控制3+i运行次数
# [3+i for i in range(10) if i %2 ==1]    #加上条件
# ['192.168.4.%s' % i for i in range(1,255)]

##############################################################
# #文件打开方法（文件模式参考pdf）
# # cp /etc/passwd  /tmp/mima   #此留意每行换行有\n
# fobj=open('mima')           #不指定打开模式，以r方式打开；此文件路径文件不存在，报错
# fobj=open('/tmp/mima')         #正确

##文件输入
# data=fobj.read()            #read默认读取全部内容；
# #如果没有给定size参数(默认值为-1)或者size值为负,文件将被读取直至末尾
# print(data)
# data=fobi.read()            #因为文件指针已经移动到尾部，没有数据可读，所在data是空窜
# print(data)                 ##再次打印，没有东西
# fobj.close()                  ##执行完，要关闭文件
#
# fobj=open('/tmp/mima')
# fobj.read(4)                #指定读取4字节，建议一次读取1024的倍数（4==>4096 ）##下一次读取将从第5个字节读取到列表
# fobj.readline()             #适合文本文件，读一行#size参数(默认值为-1)
# fobj.readlines()            #适合文本文件，读取所有行到列表中
# fobj.close()

# fobj=open('/tmp/mima')
# for line in fobj:
#     print(line, end='')
# fobj.close()

##文件输出
#不会自动添加行结束标志,需要程序员手工输入
# fobj=open('/tmp/mima')
# fobj.write('Hello World!\n')    #写数据时，先放到缓冲区
#                                 #当数据量达到一定程度时，自动写入磁盘
# fobj.flush()                    #立即将数据同步到磁盘
# fobj.writelines(['3rd line.\n','new  line.\n'])
# fobj.close()                    #关闭文件时，数据自动写入磁盘

#with    open('/tmp/mima') as fobj
    #print(fobj.readline())


# #文件内移动
# •  seek(offset[, whence]):移动文件指针到不同的位
# –  offset是相对于某个位置的偏移量
# –  whence的值,0表示文件开头,1表示当前位置,2表示文件的结尾
# •  tell():返回当前文件指针的位置
# fobj=open('/tmp/mima','rb')        #非文本文件要加b，文本文件也可以加
# fobj.tell()                         #返回文件指针的位置
# fobj.seek(10,0)                     #第一个数字为偏移量，第二个数字为当前位置，0表示文件开头,1表示当前位置,2表示文件的结尾
# fobj.read(4)            #从当前位置读4个字节，因为是bytes方式打开，所以显示b'xxxx'
# fobj.seek(-5,2)         #移动到文件倒数第5 个字节的位置，以'rb'才能写负数，'r'不行
#
# import  sys
# a=sys.stdin.readlines


#案例3:模拟cp操作
#方法一：
# f1=open('/bin/ls','rb')
# f2=open('/root/ls','wb')
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()
#命令行验证两个文件
#md5sum f1  f2

# #方法二：
# src_fname='/bin/ls'
# dst_fname='/root/ls'
#
# src_fobj=open('/bin/ls','rb')
# dst_fobj=open('/root/ls','wb')
#
# while True:
#     date=src_fobj.read(4096)
#     if date==b'':
#     #if len(data)==0:   #或者
#     #if not data:       #或者
#         break
#     dst_fobj.write(date)
# src_fobj.close()
# dst_fobj.close()
# #命令行验证两个文件
# #md5sum f1  f2


#函数:
   #函数是用def语句来创建的,语法如下:
   # def	funcOon_name(arguments):
      # "funcOon_documentaOon_string"
       # funcOon_body_suite
       #...........

# #斐波那契数列(优化2)
# def gen_fib():                       #定义函数
#     fib=[0,1]                       #可以生成用户需要长度的斐波那契数列
#     l=int(input('length：'))
#     for i in range(l-len(fib)):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)
#
# gen_fib()                           #调用函数

# #斐波那契数列(优化3)
# def gen_fib(l):                       # l形式参数
#     fib=[0,1]
#     for i in range(l-len(fib)):
#         fib.append(fib[-1] + fib[-2])
#     return fib              #函数如果没有return，默认返回None
# print(gen_fib(10))           # 10实际参数
# n=int(input('length：'))
# alist=gen_fib(n)
# mylist=[10+i  for i in alist]
# print(mylist)

# #位置参数:
# import  sys
# print(sys.argv)         #argv是sys模块中的列表，用于存储位置参数
# print(sys.argv,'xxx','yyy')        #列出[0]  [1]  [2] ##相当于shell 的$0,$1,$2
#
#
# import  sys
# def copy(src_fname,dst_fname):
#     src_fobj=open(src_fname,'rb')
#     dst_fobj=open(dst_fname,'wb')
#
#     while True:
#         date=src_fobj.read(4096)
#         if date==b'':
#         #if len(data)==0:   #或者
#         #if not data:       #或者
#             break
#         dst_fobj.write(date)
#     src_fobj.close()
#     dst_fobj.close()
# copy(sys.argv[1],sys.argv[2])
# #命令行验证
# #[root@room9pc01 day03]# python3  aa.py  /bin/ls /tmp/aa
# # md5sum /tmp/aa  /bin/ls


