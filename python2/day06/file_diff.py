###对比url的出现频率，做缓存   #高效

#cp /etc/passwd  /tmp
#cp /etc/passwd  /tmp/mima
#修改第二个文件,差异

with open('/tmp/passwd') as  f1:
    with open('/tmp/mima')as f2:
        with open('/tmp/result','w')as f3:
            s1=set(f1)
            s2=set(f2)
            f3.writelines(s2-s1)

