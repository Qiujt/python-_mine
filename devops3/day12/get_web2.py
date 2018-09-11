#模拟客户端  （爬取已设置反爬虫的网页）
#为了防止由于服务器限制，不能通过程序爬取页面，（可以设置一些Headers信息(User-Agent)），
     # 模拟使用firefox浏览

from  urllib import  request

url='http://127.0.0.1'
header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}     ##头部信息  （获取tail  -f /var/log/httpd/access_log）

r = request.Request(url, headers=header)
html = request.urlopen(r)
data = html.read()
print(data.decode('utf8'))

#验证：
#先开 tail  -f /var/log/httpd/access_log

##返回200响应





































































