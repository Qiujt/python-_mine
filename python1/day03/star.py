# #创建模块:
# # 每一个以.py作为结尾的python文件都是一个模块
# hi='Hello World!'
# def pstar(n=30):
#     print('*' * n)
#
#
# #调用模块
# #模块文件名字去掉后面的扩展名(.py)即为模块名
# import  star
# star.pstar()
# print(star.hi)
# star.pstar(50)


# #模块导入的特性
# hi='Hello World!'
# def pstar(n=30):
#     print('*' * n)
#
# if __name__ == '__main__': #当模块文件直接执行时,__name__的值为'__main__'
#                            #当模块被另一个文件导入时,__name__的值就是该模块的名字
#     pstar()
# else:
#     print('xx')
# # #命令行验证：
# # [root@room9pc01 day03]# python3  star.py
# # ******************************
# # [root@room9pc01 day03]# python3
# # >>> import star
# # xx

