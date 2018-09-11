#time  模块
#datetime模块

import time

t1=time.localtime('[secs]')      #返回九元组，secs参数未提供,则以当前时间为准
# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=20, tm_hour=14, tm_min=53,
# tm_sec=2, tm_wday=0, tm_yday=232, tm_isdst=0)

time.gmtime()           #
time.time()
time.mktime(t1)         #把九元组转化为时间戳
time.sleep(1)
time.asctime()
time.ctime()
time.ctime(0)
time.asctime(t1)
time.strftime('%Y-%m-%d  %H-%M-%S')         #常用
time.strptime('2018-08-20', '%Y-%m-%d')     #转九元组



#datetime模块                 #了解，
from datetime  import datetime,timedelta
t1=datetime.now()
t1.year
t1.month
t2=datetime.today()         #类似datetime.now,只是参数不一样
datetime.strptime('2018-08-20', '%Y-%m-%d')     #返回datetime对象

dt=timedelta(days=100)      ##熟悉
t1-dt                       #100天前的时间戳
t1+dt                       #100天后的时间戳
