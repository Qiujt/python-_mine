# 1.  Windows文本文件的行结束标志是\r\n
# 2.  类unix文本文件的行结束标志是\n
# 3.  编写程序,将unix文本文件格式转换为windows文本文件的格式

import sys
def unix2dos(fname):
    dst_fname=fname + '.txt'
    with open(fname,'rb') as src_fobj:

        with open(dst_fname,'w') as dst_fobj:
            for line in src_fobj:
                line=line.rstrip()  + '\r\n'        ##rstrip()删除空白字符\n ; (\r回车不换行)
                dst_fobj.write(line)

if __name__ == '__main__':
    unix2dos(sys.argv[1])


#验证
## [root@room9pc01 day06]# python3  unix2dos.py  login_dict.py


