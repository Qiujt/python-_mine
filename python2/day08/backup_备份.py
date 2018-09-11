# 案例1:备份程序
# 1.  需要支持完全和增量备份
# 2.  周一执行完全备份
# 3.  其他时间执行增量备份
# 4.  备份文件需要打包为tar文件并使用gzip格式压缩


import  tarfile
import  os
import  hashlib
import  pickle as p
from  time import  strftime

def  check_md5(fname):
    m=hashlib.md5()

    with  open(fname,'rb')  as fobj:
        while True:
            data=fobj.read(4096)        ##校验大文件，分块读出()
            if not data:
                break
            m.update(data)

    return  m.hexdigest()

def full_backup(src_dir,dst_dir,md5file):
    #定义文件名,例如：security_full_20180822.tar.gz
    #路径加文件名
    #压缩文件
    #记住每天md5值，保留到md5file
    fname=('%s_full_%s.tar.gz' %\
         (os.path.basename(src_dir.rstrip('/')),strftime('%Y%m%d')))
    #security_full_20180822.tar.gz      ##文件命名

    #basename截取目录最右边
    #import  os
    #>>> print(os.path.basename('/etc/security/'))  ##rstrip('/')去除目录文件后面的/
    #>>>security

    fname=os.path.join(dst_dir,fname)     #拼接目标目录与增量文件名
    tar=tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    md5_dict={}
    for path,folders,files  in  os.walk(src_dir):
        for each_file in files:
            key=os.path.join(path,each_file)
            md5_dict[key]=check_md5(key)
#>>>import  pprint
#>>>pprint.pprint(list(os.walk('/tmp/security')))
#排序得到/tmp/security, 目录，  文件....



    with open(md5file,'wb')as fobj:
        p.dump(md5_dict,fobj)

def incr_backup(src_dir, dst_dir, md5file):
    #定义文件名
    #路径加文件名
    #压缩文件
    #读出旧的md5值
    #新旧对比，判断是否执行增量备份
    fname = "%s_incr_%s.tar.gz" % \
            (os.path.basename(src_dir.rstrip('/')), strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    new_md5 = {}
    with open(md5file, 'rb') as fobj:
        old_md5 = p.load(fobj)

    for path, folders, files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path, each_file)
            new_md5[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        p.dump(new_md5, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in new_md5:
        if old_md5.get(key) != new_md5[key]:
            tar.add(key)
    tar.close()


if __name__ == '__main__':
    #cp  -r /etc/security  /tmp
    #mkdir  /tmp/backu
    src_dir='/etc/security'             #源目录
    dst_dir='/tmp/backup'               #目标目录
    md5file='/tmp/backup/md5.data'      #存放每天文件的md5值

    if strftime('%a')=='Mon':
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)

#第一次运行脚本时，注意先改if 的日期为当下，执行第一次完全备份，再者执行第一次增量备份
#tar  tvzf  .tar.gz         ##查看压缩包下有什么文件

