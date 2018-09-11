#创建字典
# •  通过{ }操作符创建字典
# •  通过dict()工厂方法创建字典
# •  通过fromkeys()创建具有相同值的默认字典
# adict={'name':'bob'}
# print(adict)
# ##{'name': 'bob'}

# bdict=dict(['ab','cd',('name','bob')])
# print(bdict)
# ##{'a': 'b', 'c': 'd', 'name': 'bob'}

cdict={}.fromkeys(['bob','tom','lily'],7)
# print(cdict)
# ##{'bob': 7, 'tom': 7, 'lily': 7}
# for key in cdict:
#     print('%s: %s'  %(key,cdict[key]))

#print('%(bob)s'  % cdict)       ##将bob对应的值打印

#更新字典
# cdict['tom']=8              #tom存在，跟新值8
# cdict['jerry']=8            #jerry不存在，向字典中添加新值
# print(cdict)

#删除字典

#字典操作符

#作用于字典的函数

#字典内建方法
dict.copy()             #返回字典(深复制)的一个副本
ddict=cdict.copy()      #将cdict的内容赋值给ddict,ddict使用全新的内存空间
cdict.get('bob')        #返回bob对应的value,如果没有bob，返回None(可以自定义（'bob','not found'）)
cdict.setdefault('bob',8)   #bob已经是字典的key,返回value;如果key不存在，向字典中写入
cdict.keys()        #返回一个包含字典中键的列表
cdict.values()        #返回一个包含字典中所有值的列表
cdict.items()       #返回一个包含字典中(键,值)对元组的列表
cdict.update({'aaa':1,'bbb':2})     #合并字典(键-值对添加到字典dict)
print(cdict)