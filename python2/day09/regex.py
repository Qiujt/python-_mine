import  re

re.match('f..','food')              #匹配到. 返回匹配对象
print(re.match('f..','seafood'))    #匹配不到，返回None
m=re.search('f..','seafood')        #从任意位置匹配，match从开头匹配
print(m.group())                    #返回匹配到的字符窜
re.findall('f..','seafood is food') #返回所有匹配到的字符窜类表
#得到['foo', 'foo']

#返回由匹配对象构成的迭代器，迭代器中的每个对象都有group方法
for m in re.finditer('f..','seafood is food'):
    print(m.group())
#得到
# foo
# foo

re.split('-|\.','hello-world.tar.gz')   #根据正则表达式中的分隔符把字符分割为一个列表

re.sub('X','zzg','hi X.How are you,X?') #把最后字符窜中的X，替换成zzg

patt=re.compile('f..')     #如果有大量匹配，对正则表达式模式进行编译（起个别名），可以提升效率
patt.search('seafood')      #编译后的对象也有search/match等方法
m = patt.search('seafood')
m.group()


#还有正则参考PPT



####################################################
# vim
# 192.168.4.1  dsfds454sfds
# 192.168.4.2  t65fdsf455fd
#
# :%s/\(\s...\)\(..\)\(..\)\(..\)\(..\)\(..\)/\1:\2:\3:\4:\5:\6/
# 192.168.4.1  ds:fd:s4:54:sf:ds
# 192.168.4.2  t6:5f:ds:f4:55:fd
