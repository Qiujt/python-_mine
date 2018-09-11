import  sys
def copy(src_fname,dst_fname):
    src_fobj=open(src_fname,'rb')
    dst_fobj=open(dst_fname,'wb')

    while True:
        date=src_fobj.read(4096)
        if date==b'':
        #if len(data)==0:   #或者
        #if not data:       #或者
            break
        dst_fobj.write(date)
    src_fobj.close()
    dst_fobj.close()
copy(sys.argv[1],sys.argv[2])