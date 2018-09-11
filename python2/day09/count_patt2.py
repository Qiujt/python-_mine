from collections import  Counter

c=Counter()
c.update(['1.1.1.1'])
c.update(['1.1.1.1'])
c.update(['1.1.1.1'])
print(c)
print(c.most_common(1))         ##得到前一项

# 案例1:分析apache访问日志
# •  编写一个apche日志分析脚本
# 1.  统计每个客户端访问apache服务器的次数
# 2.  将统计信息通过字典的方式显示出来
# 3.  分别统计客户端是Firefox和MSIE的访问次数
# 4.  分别使用函数式编程和面向对象编程的方式实现

#用OOP方式

import re
from collections import Counter

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        cpatt = re.compile(patt)
        patt_obj = Counter()
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    item = m.group()
                    patt_obj.update([item])
        return patt_obj

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    web_log = CountPatt(fname)
    a = web_log.count_patt(ip)
    print(a)
    print(a.most_common(3))
    b = web_log.count_patt('Firefox|MSIE|Chrome')
    print(b)
    print(b.most_common(5))
