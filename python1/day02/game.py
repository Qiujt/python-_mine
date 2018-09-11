# #方法一：
# import random
# computer=random.choice(['石头','剪刀','布'])
# player=input('石头/剪刀/布：')
# #print('你出了:player, 计算机出了:computer')
# print('你出了:%s, 计算机出了:%s' %(player,computer))        ##简写
#
# if player=='石头':
#     if computer=='石头':
#         print('平')
#     elif computer=='剪刀':
#         print('you win!!!')
#     else:
#         print('you lose!!!')
# elif player=='剪刀':
#     if computer=='石头':
#         print('you lose!!!')
#     elif computer=='剪刀':
#         print('平')
#     else:
#         print('you win!!!')
# else:
#     if computer=='石头':
#         print('you win')
#     elif computer=='剪刀':
#         print('you lose!!!')
#     else:
#         print('平!!!')


#方法二：               #简写
import  random
all_choices=['石头','剪刀','布']
win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]       #组合可能赋予变量
prompt='''(0)石头
(1)剪刀
(2)布
请选择0/1/2:'''
computer=random.choice(all_choices)
ind=int(input(prompt))
player=all_choices[ind]

print('你出了:%s, 计算机出了:%s' %(player,computer))
if player==computer:
    print('\033[32;1m平局\033[0m')
elif [player,computer]  in win_list:
    print('\033[33;1myou win!!!\033[0m')
else:
    print('\033[31;1myou lose!!!\033[0m')


