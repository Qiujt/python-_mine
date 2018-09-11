# SQLAlchemy
# 区别于PyMySQL：不依赖哪种数据库；不依赖sql命令   （不单适合mysql）

#连接mysql    ##通过create_engine实现数据库的连接

from  sqlalchemy import  create_engine
from  sqlalchemy.ext.declarative  import  declarative_base
from  sqlalchemy import  Column,Integer,String,ForeignKey,Date
from sqlalchemy.orm import sessionmaker


engine=create_engine(
    'mysql+pymysql://root:123456@localhost/tarena?charset=utf8',
    encoding='utf8',
    #echo=True
)
#echo=True表示将日志输出到终端屏幕,默认为False
##mysql+pymysql://用户名：密码@主机/库名
Base=declarative_base()         #创建ORM所需要的基类
Session = sessionmaker(bind=engine)

##部门表
class  Departments(Base):
    __tablename__='departments'    ##库中表名

    dep_id=Column(Integer,primary_key=True)   #dep_id是表中字段
    dep_name=Column(String(20),unique=True)   #dep_name是字段

    def __str__(self):
        return '[%s:%s]' % (self.dep_id,self.dep_name)

##员工表
class  Employees(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20),nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer,ForeignKey('departments.dep_id'))

    def __str__(self):
        return '[%s:%s]'% (self.emp_id,self.emp_name)

##工资表
class Salary(Base):
    __tablename__ = 'salary'

    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)    #没有时创建，有时不创建

#########   员工表结果分析  ##################
# MariaDB [tarena]> desc departments;
# +----------+-------------+------+-----+---------+----------------+
# | Field    | Type        | Null | Key | Default | Extra          |
# +----------+-------------+------+-----+---------+----------------+
# | dep_id   | int(11)     | NO   | PRI | NULL    | auto_increment |
# | dep_name | varchar(20) | YES  | UNI | NULL    |                |
# +----------+-------------+------+-----+---------+----------------+

# Integer                 ===>int
# String(20)              ===>varchar(20)
# primary_key=True        ===>PRI     auto_increment
# unique=True             ===>’部门‘名字不能重名