# 案例1:分析apache访问日志
# •  编写一个apche日志分析脚本
# 1.  统计每个客户端访问apache服务器的次数
# 2.  将统计信息通过字典的方式显示出来
# 3.  分别统计客户端是Firefox和MSIE的访问次数
# 4.  分别使用函数式编程和面向对象编程的方式实现

import  re

def count_patt(fname,patt):
    patt_dict={}                    #预想最终结果存为字典，key为各IP，值为每个IP访问次数
    cpatt=re.compile(patt)          #ip='^(\d+\.){3}\d+'##个人理解，此正则动作起个别名cpatt

    with open(fname) as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                key=m.group()
                # if key  not in patt_dict:
                #     patt_dict[key] =1
                # else:
                #     patt_dict[key] +=1
                patt_dict[key]=patt_dict.get(key,0) + 1     ##优化上面四行


    return  patt_dict


if __name__ == '__main__':
    fname='access_log'          #文件在脚本同级目录下
    ip='^(\d+\.){3}\d+'
#正则，^(\d+\.)数字（\d）；+\.前面出现的正则表达式一次或多次；
#{3}前面出现的正则表达式（^(\d+\.)）3次
#\d+，匹配任意数字,与[0-9]同义，匹配前面出现的正则表达式一次或多次
    print(count_patt(fname,ip))
    br='Firefox|MSIE|Chrome'
    print(count_patt(fname,br))
    #也可以统计文件
    shell = 'bash$|nologin$'
    print(count_patt('/etc/passwd', shell))

#得到数据
# ips={'172.40.58.150': 10, '172.40.58.124': 6, '172.40.58.101': 10, '127.0.0.1': 121, '192.168.4.254': 103,
#  '192.168.2.254': 110, '201.1.1.254': 173, '201.1.2.254': 119, '172.40.0.54': 391, '172.40.50.116': 244}
# {'Chrome': 24, 'Firefox': 870, 'MSIE': 391}
# {'bash': 4, 'nologin': 37}

#字典无序，转化为列表再排序
#print(ips.items())              ##每一项的健值放到元组里面成为两项
#dict_items([('172.40.58.150', 10), ('172.40.58.124', 6), ('172.40.58.101', 10),
#('127.0.0.1', 121), ('192.168.4.254', 103), ('192.168.2.254', 110), ('201.1.1.254', 173),
#  ('201.1.2.254', 119), ('172.40.0.54', 391), ('172.40.50.116', 244)])

#list(ips.items())
#再运用快速排序         ##或者from collections import  Counter




##shell密令分析apache访问日志           ##没有筛选出客户端用什么搜索引擎
#awk '{print $1}' access_log | sort | uniq -c | sort -nr
                              #ip排序
                                    #去除重复，-c统计IP出现次数
                                                #r降序
