
#tarfile模块          #压缩，解压
# •  tarfile模块允许创建、访问tar文件
# •  同时支持gzip、bzip2格式

import tarfile
import  os

#######压缩#########
#os.chdir('/etc')
tar=tarfile.open('/tmp/anquan.tar.gz', 'w:gz')         #压缩后放到/tmp
# tar.add('security')                 #add需要压缩的文件
# tar.add('hosts')
tar.add('/etc/security')
tar.add('/etc/hosts')
tar.close()

########解压#########
# os.chdir('/var/tmp')
# tar=tarfile.open('/tmp/anquan.tar.gz')
# tar.extractall()                    #解压所有
# tar.close()
