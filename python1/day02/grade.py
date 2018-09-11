grade=int(input("分数:"))
if grade > 90:              ##匹配即停止，亦可写区间判断，麻烦
    print('优秀')
elif 80 < grade:
    print('好')
elif 70 < grade:
    print('良')
elif 60 < grade:
    print('及格')
else:
    print('你要努力了')



