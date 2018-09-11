######################熟悉，会查，次要##################
#shutil模块
#https://yiyibooks.cn
#1、复制和移动
#shutil.copyfileobj(fsrc, fdst[, length])               ##复制文件
#shutil.copyfile(src, dst, *, follow_symlinks=True)     ##复制文件
#shutil.copy(src, dst, *, follow_symlinks=True)         ##复制文件到目录下
#shutil.copy2(src, dst, *, follow_symlinks=True)        ##与copy()相同，
#shutil.move(src, dst, copy_function=copy2)             ##递归移动
# import shutil
# shutil.copyfile('/etc/passwd','/tmp/123.txt')

#2、目录操作：
#shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
            #递归地复制整个目录树到目标目录  ##目标目录事先不能存在
#shutil.rmtree (path, ignore_errors=False, onerror=None)
            #删除整个目录树; 路径必须指向目录(而不是指向目录的符号链接)。

#3、权限管理
#shutil.copymode(src, dst, *, follow_symlinks=True)
            #将权限位从src复制到dst。文件内容,所有者和组不受影响。src和dst是以字符串形式给出的路径名称。
#shutil.copystat(src, dst, *, follow_symlinks=True)
            #将权限位,最后访问时间,上次修改时间和标志从src复制到dst
#shutil.chown(path, user=None, group=None)      #更改给定路径的所有者用户和/或组

######################################################################

############重要##3###################################
#语法风格
#关键字        ##了解，少用
# import keyword
# print(keyword.kwlist)            ##查看关键字
# keyword.iskeyword()          ##（）判断是否为关键字

# import builtins
# builtins.


# #内建函数
# list('abcd')
# list((10, 20, 30))
# tuple('abcd')
# str(100)
# str((10, 20, 30))
# max([10, 200, 30])
# min([10, 200, 30])
# max('hello')		#按字母排序，往后为大
#
# users = ['bob', 'alice', 'john']
# for i in range(len(users)):  # [0, 1, 2]
#     print('#%s: %s' % (i, users[i]))
#
#list(enumerate(users))  # 应用时不必转换	#[(0, 'bob'), (1, 'zhangsan'), (2, 'john')]
# for item in enumerate(users):
#     print('#%s: %s' % (item[0], item[1]))
#
# for ind, user in enumerate(users):  # (0, bob), (1, alice)
#     print('#%s: %s' % (ind, user))

#效果一样
# 0 bob
# 1 zhangsan
# 2 john
##########################################
# for u in reversed(users):     ##逆序
#     print(u)
# users = ['bob', 'alice', 'john']
# for u in sorted(users):                 ##返回一个有序的列表(按字母大小)
#     print(u)
# 字符编码：ASCII, ISO8859-1/Latin1, GB2312/GBK/GB18030,
# ISO -> utf8
# 0b1100001 -> a; 0b1100010 -> b;

# 字符串操作符
# •  比较操作符:字符串大小按ASCII码值大小进行比较
# •  切片操作符:[ ]、[ : ]、[ : : ]
# •  成员关系操作符:in、not in



#格式化操作符(分主次)
# print('%s  %s' % ('bob',22))
# print('%s  %d'  % ('bob',22))
# print('%12s %8s'  % ('bob',22))           #右对齐
# print('%12s %8s'  % ('zhangsan',22))
#
# print('%-12s  %-8s' %('bob',22))            #左对齐
# print('%-12s  %-8s' %('zhangsan',22))

# #############以下内容不常用################
# '%c' % 98  # ascii为98的字符      ##a 为97
# '%#o' % 30  # 8进制数形式
# '%#x' % 30  # 16进制数形式
# '%e' % 100000  # 科学计数法
# '%f' % (5 / 3)  # 浮点数
# '%.2f' % (5 / 3)  # 小数占两位
# '%5.2f' % (5 / 3)  # 总宽度为5，小数占两位
# '%+d' % 10  # 正数前加上+号
# '%+d' % -10
# '% d' % 10  # 正数前加空格
# '% d' % -10
# '%010d' % 55  # 总宽度为10，不够宽度前面补0
# ############################
# #format函数
# a='{} is {} years old'.format('bob', 25)
# print(a)
# b='{1} is {0} years old'.format(25, 'bob')
# print(b)
# '{:<20}'.format('hello')
# '{:>20}'.format('hello')
# '{:^20}'.format('hello')
# ##################################











