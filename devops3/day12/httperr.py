
# urllib中包括了四个模块
# –  urllib.request可以用来发送request和获取request的结果
# –  urllib.error包含了urllib.request产生的异常
# –  urllib.parse用来解析和处理URL
# –  urllib.robotparse用来解析页面的robots.txt文件

#HTTP异常处理
#捕获异常需要导入urllib.error模块


from urllib import request, error

try:
    html = request.urlopen('http://127.0.0.1/xxx.html/')  # xxx.html不存在
except error.HTTPError as e:  # 把报错信息保存到变量e中
    print(e)

try:
    html = request.urlopen('http://127.0.0.1/aaa.html')  # aaa.html无访问权限
except error.HTTPError as e:
    print(e)

####   结果   #######
# HTTP Error 404: Not Found
# HTTP Error 403: Forbidden