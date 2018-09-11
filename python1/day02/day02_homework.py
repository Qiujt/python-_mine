# print(1o11)
# print(0x11)
# print(0b11)
#
# a="pythonnsd1803"
# print(a[:-2])
# print(a[2:6:3])
# print('''(1)aa
# (2)vv
# (3)bb
# ''')
# # import random
# # b=input('1/2/3:')
# # print(b)
#
# print('this is a ' +'test' )
# print('this is   a   test')
# print('this','is','a','test',sep='***')
#
# print(a*2)
# alist=['tom','zhangsan','lisi']
# print(alist[0])
# alist2=[1,'tom',2,'zhangsan',3,'lisi']
# print(alist2[2])

# alist2=[1,'tom',2,'zhangsan',3,'lisi']
# print('tom' not  in alist2)
# print('lisi' in alist2)
# alist2.append('nidayede')
# print(alist2)

# alist3=(1,'tom',2,'zhangsan',3,'lisi')
# print('lisi' not in alist3)
# print(alist3[3])

# user_dict	=	{'name':'bob',	'age':23}
# print('bob' not  in user_dict)
# print('age'in user_dict)
# print(user_dict[0])         #报错,字典不支持下标操作

# if 0:                           #如果表达式的值非0或者为布尔值True,则代码组yes被执行
#     print('yes')
#
# else:
#     print('no')
# if '':                      ##空字符串、空列表、空元组,空字典的值均为False
#     print('yes')
# else:
#     print('no')
#
# if '  ':                    ##'有空格'
#     print('y')
# else:
#     print('n')

# import getpass
# user=input('you name:')
# password=getpass.getpass('you password')
# if user=='bob' and password=='123456':
#     print('\033[33;1mLogin successful\033[0m')
# else:
#     print('\033[32;1mLogin inorrect\033[0m')

# import  random
# number=random.randint(1,100)
# player=int(input('请输入一个数字:'))
#
# if  player>number:
#     print('大了')
# elif player<number:
#     print('小了')
# else:
#     print('对了')
# print(player)
#
# a=10
# b=20
# samller=a if a<b else b
# print( samller)

# socre=int(input('分数:'))
# if socre > 90:
#     print('优秀')
# elif socre >80:
#     print('好')
# elif socre >70:
#     print('良')
# elif socre >60:
#     print('及格')
# else:
#     print('要努力')

# #方法一:
# import random
# computer=random.choice(['石头','剪刀','布'])
# player=input(('石头/剪刀/布:'))
# print('你出了:%s,计算机出了:%s' %(player,computer))
#
# if player=='石头':
#     if computer=='石头':
#         print('平局')
#     elif computer=='剪刀':
#         print('\033[32;1myou win\033[0m')
#     else:
#         print('yum lose')
# elif player=='剪刀':
#     if computer=='石头':
#         print('you lose')
#     elif computer=='剪刀':
#         print('平局')
#     else:
#         print('yum win')
# else:
#     if computer=='石头':
#         print('you win')
#     elif computer=='剪刀':
#         print('you lose')
#     else:
#         print('平局')

# #方法二:
# import  random
# all_choice=['石头','剪刀','布']
# computer=random.choice(all_choice)                          #随机出一个##print(computer)
# win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]         ##player:computer
# #player=input('石头/剪刀/布:')
# ind='''(0)石头
# (1)剪刀
# (2)布
# 请选择:0/1/2:'''                      ##用户选择数字输入,更好的用户体验
# aa=int(input(ind))                  ##选择0/1/2赋值给aa
# player=all_choice[aa]
# print('你出了:%s,计算机出了:%s' %(player,computer))
#
# if computer==player:
#     print('平')
# elif [player,computer] in win_list:
#     print('you win')
# else:
#     print('you lose')

# #100内整数和
# summ=0
# counter=0
# while counter<101:
#     counter+=1                  ##位置错误
#     summ+=counter
# print(summ)
#
# #100内整数和
# summ=0
# counter=0
# while counter<101:
#     summ+=counter
#     counter+=1
# print(summ)

# #100内的偶数的和
# summ=0
# counter=0
#
# while counter < 101:
#     counter+=1
#     if counter % 2:              ##奇数时为False,无需counter%2==1
#         summ+=counter
# print(summ)


# import  random
# result=random.randint(1,10)
# answer=int(input("guess the number:"))
#
# if  answer > result:
#     print("猜大了！")
# elif answer < result:
#     print("猜小了！")
# else:
#     print("猜对了！")
#
# print(result)

#猜数:
# import  random
# computer=random.randint(1,100)
#
# while True:
#     answer=int(input('猜100内数:'))
#     if answer > computer:
#         print('大了')
#     elif answer < computer:
#         print('小了')
#     else:
#         print('猜对了')
#         break

# #优化:
# import  random
# computer=random.randint(1,100)
# running=True
#
# while running==True:
#     answer=int(input('猜100内数:'))
#     if answer > computer:
#         print('大了')
#     elif answer < computer:
#         print('小了')
#     else:
#         print('猜对了')
#         running=False













