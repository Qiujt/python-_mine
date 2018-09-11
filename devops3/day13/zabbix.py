
#利用好帮助文档
## https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/

#一、获取zabbix版本信息
        #https://...apiinfo/version
#二、取得令牌后,访问其他数据只要出示该令牌即可,不需要再进行身份验证（使用 user.login）
        #https://...user/login
#三、检索主机（使用 host.get 方法所有已配置主机的ID,主机名和接口。）
        #https://...host/get
#四、检索主机所在的组
        #https://.../host.get
# 五、检索zabbix所有组
        ##https://.../hostgroup.get
#六、检索模板
         #https://...template.get
#七、创建主机
         #https://...host.create



import  requests
import  json

url = 'http://192.168.4.254/api_jsonrpc.php'
headers	= {'Content-Type':'application/json-rpc'}
data = {
    'jsonrpc':'2.0',	            #jsonrpc协议的版本号，固定的
    'method':'apiinfo.version',	    #API方法;在zabbix手册上查到的，查询zabbix版本
    'id':	1,	                    #本次请求的标识符(随便写个数字)
    'auth':	None,	                #不需要身份验证
    'params': {},	                #没有额外参数
}
#zabbix要求提交的数据是json格式
r =	requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())	                    #zabbix返回的数据都是json格式

#### 1、 运行获取到 Zabbix API 版本。   #################
{'jsonrpc': '2.0', 'result': '3.4.4', 'id': 1} #使用JSON-RPC 2.0协议


######################################################3
#获取Admin的身份验证令牌
url = 'http://192.168.4.254/api_jsonrpc.php'
headers	= {'Content-Type':'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}
#zabbix要求提交的数据是json格式
r =	requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())	                    #zabbix返回的数据都是json格式

###### 使用 user.login 方法登录并获取到身份验证令牌  #####################
{'jsonrpc': '2.0', 'result': '41e89b6fd0d2ffe1450cee67f8abed40', 'id': 1}
# 又包含以下属性:
# –  jsonrpc - JSON-RPC协议的版本
# –  result - 方法返回的数据
# –  id - 相应请求的标识符


#######################################################3
#四、检索所有的主机
url = 'http://192.168.4.254/api_jsonrpc.php'
headers	= {'Content-Type':'application/json-rpc'}
data ={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "host": [
        #         "Zabbix server",  #可以指定已经添加的被监控的主机
        #         "Linux server"
        #     ]
        # }
    },
    "auth": "41e89b6fd0d2ffe1450cee67f8abed40",     #身份验证令牌
    "id": 1
}
r =	requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())

################################
#检索主机Zabbix server所在的组
url = 'http://192.168.4.254/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectGroups": "extend",
        "filter": {
            "host": [
                "Zabbix server"
            ]
        }
    },
    "auth": "41e89b6fd0d2ffe1450cee67f8abed40",
    "id": 2
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

###################################
# 五、检索zabbix所有组
url = 'http://192.168.4.254/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "name": [
        #         "Zabbix servers",
        #         "Linux servers"
        #     ]
        # }
    },
    "auth": "41e89b6fd0d2ffe1450cee67f8abed40",
    "id": 1
}
r = requests.post(url, headers=headers, data=json.dumps(data))
ginfo = r.json()
print(ginfo['result'])
for item in ginfo['result']:
    print(item['groupid'], item['name'])

#############################################
#六、检索模板
url = 'http://192.168.4.254/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "template.get",
    "params": {
        "output": "extend",
        # "filter": {
        #     "host": [
        #         "Template OS Linux",
        #         "Template OS Windows"
        #     ]
        # }
    },
    "auth": "41e89b6fd0d2ffe1450cee67f8abed40",
    "id": 1
}
r = requests.post(url, headers=headers, data=json.dumps(data))
tinfo = r.json()
# print(tinfo)
for item in tinfo['result']:
    print(item['templateid'], item['host'])


#############################################
# 七、创建主机，主机名为mylinux，加入到Linux Servers组，应用Template os Linux模板
url = 'http://192.168.4.254/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "mylinux",
        "interfaces": [
            {
                "type": 1,  # 1 agent; 2 SNMP; 3 IPMI; 4 JMX
                "main": 1,  # 该接口是否在主机上用作默认接口。1 默认
                "useip": 1,  # 是否应通过IP进行连接
                "ip": "192.168.4.3",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "1"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
    },
    "auth": "41e89b6fd0d2ffe1450cee67f8abed40",
    "id": 1
}





