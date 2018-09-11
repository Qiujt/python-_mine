print('Hello	World!')
print('Hello   '+'World!')
print('Hello',	'World!')
print('Hello',	'World!',	sep='***')
print('Hello',	'World!',	sep='***',	end='')
print('123','321',sep='***' )

user = input('username:')
print(user)

a = input('number:')    #input读入的数据都是字符类型
# a + 5                  #错误，不能把数字和字符进行加法运算
print(int(a) + 5)       #将字符转换成数字，再和5进行加法运算
print(a + str(5))       #将数字5转换成字符，再和字符串拼接
