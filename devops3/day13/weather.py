# 案例3:天气预报查询
# 1.  运行程序时,屏幕将出现你所在城市各区县名字
# 2.  用户指定查询某区县,屏幕上将出现该区县当前的气温、湿度、风向、风速等

from urllib import request
import json

weather = request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
info = request.urlopen('http://www.weather.com.cn/data/cityinfo/101010100.html')
zhishu = request.urlopen('http://www.weather.com.cn/data/zs/101010100.html')
weather_data = weather.read()
info_data = info.read()
zs_data = zhishu.read()
print(json.loads(weather_data))
print('*' * 50)
print(json.loads(info_data))
print('*' * 50)
print(json.loads(zs_data))


# JSON概述
# •  JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式

# dumps方法               ##编码
# loads方法               ##进行decode解码,得到原始数据
# >>>	import	json
# >>>	number	=	json.dumps(100)
# >>>	json.loads(number)
# 100           #得到原始数据
# >>> n
# '100'
# >>>	m=json.dumps([1,	2,	3])
# >>>m
# '[1,	2,	3]'
# >>>m.json.loads()
# [1,	2,	3]      #得到原始数据


# 天气预报查询
# •  搜索“中国天气网 城市代码查询”,查找城市代码
# •  城市天气情况接口
#
# –  实况天气获取:http://www.weather.com.cn/data/sk/城市代码.html
# –  城市信息获取:http://www.weather.com.cn/data/cityinfo/城市代码.html
# –  详细指数获取:http://www.weather.com.cn/data/zs/城市代码.html
