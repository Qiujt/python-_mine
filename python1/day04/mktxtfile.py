
'''
1、思考一下，程序的运行场景
2、构思程序的结构，把每一个功能，写成一个函数
3、编写主程序代码，把这些函数串联起来
4、编写具体的函数代码部分
'''

# 案例1:创建文件
# 1.  编写一个程序,要求用户输入文件名
# 2.  如果文件已存在,要求用户重新输入
# 3.  提示用户输入数据,每行数据先写到列表中
# 4.  将列表数据写入到用户输入的文件名中

import os

def get_fname():
    while True:
        fname=input('filename:')
        if not os.path.exists(fname):
            break
        print('%s already exists , Try again ' % fname)

    return  fname


def get_content():
    content=[]
    print('请输入正文，end结束')
    while True:
        line=input('>')
        if line=='end':
            break
        content.append(line)

    return content


def wfile(fname,content):
    with   open(fname, 'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname=get_fname()
    content=get_content()
    content=['%s\n' % line for line in content]
    wfile(fname,content)
