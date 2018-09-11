import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tedu',
    charset = 'utf8'
)

cursor =  conn.cursor()  #打开

##改
insert_dep1='UPDATE departments SET dep_name=%s WHERE dep_name=%s'
cursor.execute(insert_dep1, ('人力资源部','人事部'))

##删
delete1='delete from departments  where dep_name=%s'
cursor.execute(delete1,('测试部',))

conn.commit()         #增删改查需要commit提交写入
cursor.close()
conn.close()