#1、list=['电脑'，‘显示器’，‘笔记本’，‘机械硬盘’]
#2、是否闰年

import  random
import  sys
list = ['电脑', '显示器', '笔记本', '机械硬盘']
choice_list='''(1)输出商品信息
（2）可以添加商品
'''
num=int(input('请选择1/2:'))
if num==1:
    print(list)
    choice=int(input('请选择对应商品1/2/3/4:'))
    shop=list[num-1]
    print(shop)
else:
    print('你可以添加商品')
    list_add=input('商品名：')
    list.append(list_add)
    print(list)


add_year=int(input('年份：'))
if add_year%4==0 and add_year%100!=0 or add_year%400==0:
    print('%s''为闰年' %(add_year))
else:
    print('%s''非闰年' %(add_year))

