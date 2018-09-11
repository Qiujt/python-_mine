import getpass              ##模块，密码不显示在屏幕
user=input("username:")
#print(user)

passed=getpass.getpass("password:")
#print(passed)

if user=='bob' and passed=='123456':
    print('\033[32;1mLogin successful\033[0m')
else:
    print('\033[31;1mLogin inorrect\033[0m')