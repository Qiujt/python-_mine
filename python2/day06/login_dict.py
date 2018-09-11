# 1.  支持新用户注册,新用户名和密码注册到字典中
# 2.  支持老用户登陆,用户名和密码正确提示登陆成功
# 3.  主程序通过循环询问进行何种操作,根据用户的选择,执行注册或是登陆操作

from  getpass import  getpass
userdb={}
def login():                      #用户登陆
    username=input('username:')
    #password=input('password:')
    password=getpass('password:')
    #if username not in userdb or userdb[username] != password:
    if userdb.get(username) != password:        ##密码不对应时
        print('登陆失败')
    else:
        print('登陆成功')

def register():                 #注册
    username=input('username:')
    if username not in userdb:
        #password=input('password:')
        password=getpass('password:')
        userdb[username]=password
    else:
        print('%s已存在' %(username))

def show_menu():                ##交互选择操作
    cmds={'0':register,'1':login}
    prompt='''(0)  新用户注册
（1）登陆
（2）退出
pelase input your choines(0/1/2)'''
    while True:
        choice=input(prompt)
        if choice not in "012":
            print('无效输入，请重试！')
            continue

        if choice==2:
            break

        cmds[choice]()          #执行输入key的value   register  or login

if __name__ == '__main__':
    show_menu()

#[]命令行验证