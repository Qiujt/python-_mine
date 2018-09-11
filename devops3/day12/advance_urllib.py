'''
数据编码
URL标准中只会允许一部分ASCII字符,比如数字、字母、部分符号等
标准的URL字符中不能包括汉字、一些标点符号等。为了能表示这些字符，需要编解码
'''

from urllib import  request

r=request.quote('hello 达内')    # 编码成浏览器可读字符
print(r)

ur=request.unquote(r)
print(ur)

####  结果 ###
#  hello%20%E8%BE%BE%E5%86%85
#   hello 达内

#验证：
#