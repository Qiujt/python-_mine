#模块的导入
                    #需要一个叫做“路径搜索”的过程
                    #  >>>	import	sys
                    # >>>	print(sys.path)	   #查看模块允许放到的地方
#导入自己的模块可以把模块（习惯）放到： /usr/local/lib/python3.6/site-packages下
#还可以设置环境变量PTYHONPATH，指向自己所写模块的路径
#export  PYTHONPATH='/root/python3.6/day04'

# 如果模块文件在一个目录中，可以把目录当作包
# mkdir rrr
# cp railway rrr/
# python3
# >>> import rrr.railway
# md5值：一种hash哈希算法，单向加密，相同的数据生成相同的乱码，不同的数据，生成
# 的乱码一定不同，不能通过乱码反推回原始数据

###################################
import os
for path,folders,files in os.walk('/tmp/security'):     #假如路径、目录、文件
    for each_file  in files:
        print(os.path.join(path,each_file))             #路径、文件拼接


