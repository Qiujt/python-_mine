# 案例2:检查标识符
# 1.  程序接受用户输入
# 2.  判断用户输入的标识符是否合法
# 3.  用户输入的标识符不能使用关键字
# 4.  有不合法字符,需要指明第几个字符不合法

from   string import  ascii_letters,digits          ##调用string的大小写字母
from   keyword import  iskeyword                ##关键字

first_chs=ascii_letters + '_'              #合法的第一个字符
other_chs=first_chs + digits

def check_id(idt):
    if iskeyword(idt):         #多个return，只会执行一个
        return '%s is keyword' % idt

    if idt[0] not in first_chs:
        return '\033[31;1m首\033[0m字符不合法'

    for ind,ch in enumerate(idt[1:]):   ##切片首字符，[(0,'字符1'),(1,'字符2'）]
        if ch not in other_chs:
            return  '第%个字符不合法'  % (ind+2)

    return  '%s是合法的'  % idt

if __name__ == '__main__':
    idt=input('待检查的表识符：')
    print(check_id(idt))

