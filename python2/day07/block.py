#生成器

def block():
    content=[]
    counter=0
    for line in fobj:
        content.append(line)
        counter+=1
        if counter ==10:        #每读取十行,返回值
            yield  content
            content=[]
            counter=0

    if content:                 #不满十行
        yield  content


if __name__ == '__main__':
    with    open('/etc/passwd') as fobj:
        for lines in block(fobj):
            print(lines)
            print()
