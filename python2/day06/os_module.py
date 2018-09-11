
#os模块
#该模块是python访问操作系统功能的主要接口

import  os

os.getcwd()     #pwd
os.listdir()    #ls
os.listdir('/tmp/mydemo')   #ls /tmp/mydemo
os.mkdir('/tmp/mydemo')
os.chdir('/tmp/mydemo')
os.mknod('test')                  #touch test
os.symlink('/etc/hosts','zhuji')       #ln -s /etc/hosts   zhuji
os.path.isfile('zhuji')             #是文件？  此返回False
os.path.isdir('/tmp')
os.path.exists('/abc')
os.path.abspath('zhuji')
os.path.basename('/tmp/abc/aa/cc')      #'cc'
os.path.dirname('/tmp/abc/aa/cc')       #'/tmp/abc/aa'
os.path.split('/tmp/abc/aa/cc')         #('/tmp/abc/aa', 'cc')
os.path.splitext('/tmp/abc/aa/cc')      #('/tmp/abc/aa/cc', '')
os.path.join('/tmp','abc')              #'/tmp/abc'     #合并
os.rmdir('/tmp/abc/aa/cc')              #删除空目录cc
os.chmod('aa',0o777)                    #改权限（八进制）

import  string