# #hashlib模块


# •  hashlib用来替换md5和sha模块,并使他们的API一致,专门提供hash算法
# •  包括md5、sha1、sha224、sha256、sha384、sha512,使用非常简单、方便
                                #/etc/shadow用户密码$6$为sha512加密，$1$为md5加密
# >>>	import	hashlib
# >>>	m=hashlib.md5()
#>>>	m.update('hello	world!')	    #md5校验
# >>>	m.hexdigest()                   #得到md5值
# 'fc3ff98e8c6a0d3087d515c0473f8677'

import  sys
import   hashlib

def  check_md5(fname):
    m=hashlib.md5()

    with  open(fname,'rb')  as fobj:
        while True:
            data=fobj.read(4096)        ##校验大文件，分块读出
            if not data:
                break
            m.update(data)

    return  m.hexdigest()



if __name__ == '__main__':
    print(check_md5(sys.argv[1]))