#集合也用{}表示，就像是一个无值的字典
s1=set('abc')
s2=set('bcd')
len(s2)
for ch in s2:
    print(ch)

'a'in s1            #支持用in和not in
s1 | s2             #取并集
s1 & s2             #交集
s1 -s2              #差补
s1.add(10)          #添加成员
s1.update(['hello','world'])        #批量添加成员
s1.remove(10)                       #移除成员
s1.issubset(s2)     #判断s1是否s2的子集；是就返回True
s1.issuperset(s2)  #如果s2是s1的超集,则返回True,否则返回False
s1.union(s2)        #s1 | s2
s1.intersection(s2) #s1 & s2
s1.difference(s2)   #s1 -s2