# ##08--16
# # 猜拳,三局两胜
# import  random
# all_choices=['石头','剪刀','布']
# win_lists=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# aa='''(0)石头
# （1）剪刀
# （2）布
# 请选择（0/1/2）：'''
# pwin=0
# cwin=0
#
# while pwin<2 and cwin<2:
#     computer=random.choice(all_choices)
#     bb=int(input(aa))
#     player=all_choices[bb]
#     print('你出了：%s,计算机出了:%s' % (player,computer))
#
#     if computer==player:
#         print('\033[32;1m平\033[0m')
#     elif [player,computer] in [win_lists]:
#         pwin+=1
#         print('\033[31;1myou win!!!\033[0m')
#     else:
#         cwin+=1
#         print('\033[33;1myou lose\033[0m')
#
# print("player赢次数:%d  computer赢次数:%d"    % (pwin,cwin) )
# ##%d用来输出十进制整数;%c,用来输出一个字符;%s,用来输出一个字符串;%f,用来输出实数（包括单，双精度），以小数形式输出
# if pwin>cwin:
#     print( '\033[41;1m最终你赢了 \033[0m' )
# else:
#     print('\033[41;1m最终你输了\033[0m')
#
