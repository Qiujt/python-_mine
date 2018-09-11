##移动游标
#如果希望不是从头取数据,可以先移动游标

#absolute以开头为起始点移动游标(绝对)
#relative以当前位置为参考点移动游标（相对）

import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tedu',
    charset = 'utf8'
)

cursor =  conn.cursor()  #打开游标

query1='select  * from departments'
cursor.execute(query1)                 #执行sql命令

cursor.scroll(2,mode='absolute')       #游标以开头为起始点移动（2单位）游标
r1=cursor.fetchone()
print(r1)

cursor.scroll(1,mode='absolute')       ## 以开头为起始点移动游标(绝对)
cursor.fetchone()
# 取出一行

cursor.scroll(1,mode='relative')        ##以当前位置为参考点移动游标（相对）
r2=cursor.fetchall()    # 取出后续所有内容
print(r2)

cursor.close()
conn.close()