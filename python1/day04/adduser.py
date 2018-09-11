# 案例3:创建用户
# 1.  编写一个程序,实现创建用户的功能
# 2.  提示用户输入用户名
# 3.  随机生成8位密码
# 4.  创建用户并设置密码
# 5.  将用户相关信息写入指定文件


import  subprocess                      #subprocess.call调用系统命令
import  sys
from randpass  import  randpass         ##之前写的randpass.py

def adduser(username,password,fname):
    user_info='''user information:
用户名：%s
密码：%s
'''% (username,password)
    subprocess.call('useradd %s' % username, shell=True )
    subprocess.call(
        'echo %s | passwd --stdin %s' %(password,username),shell=True )
    with   open(fname, 'a') as fobj:
        fobj.write(user_info)

if __name__ == '__main__':
    username=sys.argv[1]
    password=randpass()
    adduser(username,password,'/tmp/users.txt')


##效果
#[root@room9pc01 day04]# python3 adduser.py  user1
# [root@room9pc01 day04]# cat /tmp/users.txt
# user information:
# 用户名：user1
# 密码：OWRyeHbf

