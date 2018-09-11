import pymysql


conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = '123456',
    db = 'tedu',
    charset = 'utf8'        ##字段内容支持中文
)

# cursor =  conn.cursor()  #打开
# insert_dep1 = 'INSERT INTO  departments VALUES (%s,%s)'  #添加sql命令进行操作
# cursor.execute(insert_dep1,('1','人事部'))    #执行sql命令,添加('1','人事部')
# conn.commit()  #增删改查需要commit提交写入
# cursor.close()  #关闭
# conn.close()

#继续添加字段
cursor =  conn.cursor()  #打开
insert_dep1 = 'INSERT INTO  departments VALUES (%s,%s)'  #添加sql命令进行操作
insert_deps=[(2,'运维部'),(3,'开发部'),(4,'测试部')]
cursor.executemany(insert_dep1,insert_deps)
conn.commit()  #增删改查需要commit提交写入
cursor.close()  #关闭
conn.close()