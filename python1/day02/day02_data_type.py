# print(0o11)
# print(0x11)
# print(0b11)

import os
#os.chmod('day02_data_type.py',755)          #错误，因为权限是八进制
os.chmod('day02_data_type.py',0o755)

print('tom\'s pet is  cat')
print("tom's pet is cat")

#names=zhangsan\n lisi\n dacui\n
#print(names)
names2='''zhangsan
lisi
dacui
'''
print(names2)


a='python'
print(len(a))
print(a[::-1])
print(a[::-2])