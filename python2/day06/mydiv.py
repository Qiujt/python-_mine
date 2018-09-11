#try-except语句
#定义了进行异常监控的一段代码,并且提供了处理异常的机制


# try:                    #有可能发生的错误放到try里面
#     num=int(input('number:'))
#     result=100 / num
#     print(result)
#
# except ValueError:      ##异常处理代码
#     print('输入错误')
# except ZeroDivisionError:
#     print('输入错误')
# except KeyboardInterrupt:
#     print('Bye-bye')
# except  EOFError:
#     print('Bye-bye')
#
# print('Done')           ##提示报错后，程序不崩溃，执行Done


try:
    num=int(input('number:'))
    result=100 / num

except (ValueError,ZeroDivisionError):
    print('输入错误')

except (KeyboardInterrupt,EOFError):
    print('Bye-bye')

else:                   ##不发生异常才执行的代码
    print(result)

finally:                ##不管是否发生异常都要执行的代码
    print('Done')

##不是必须把所有的语句写全，常用的有try-except和try-finally组合