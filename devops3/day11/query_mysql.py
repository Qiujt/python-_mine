
##查询数据
#游标
#可以取出表中一条、多条或全部记录

import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tedu',
    charset = 'utf8'
)

cursor =  conn.cursor()  #打开游标（类指针）

query1='select  * from departments'
cursor.execute(query1)        #取出表中一条
r1=cursor.fetchone()
print(r1)
print('#' * 20)

r2	=	cursor.fetchmany(2)   #取出表中多条
print(r2)
print('#' * 20)

r3	=	cursor.fetchall()     #取出表中所有
print(r3)

conn.close()            #关闭



##########  查询结果  ####################
(1, '人事部')
####################
((2, '运维部'), (3, '开发部'))       ##第二次查询显示内容基于第一次查询（指针）
####################
((4, '测试部'),)
