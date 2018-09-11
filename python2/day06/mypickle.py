
#没有用pickle模块时，数据写入文件，只能把字符串对象写入；其他数据需先转换成字符串再写入文件 。

#pickle模块
#pickle存储器可以将任意的数据类型写入文件，还可以无损取出

import  pickle as p

shop_file='/tmp/shop.txt'
# shop_list=['apple','eggs','banana']
# with open(shop_file,'wb') as fobj:
#     p.dump(shop_list,fobj)              #将列表写入文件

with open(shop_file,'rb')as fobj:
    mylist=p.load(fobj)                     #取出仍然时列表

print(mylist[1])
