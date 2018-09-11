#下载网络资源
##下载图片。 day13的wget更加优秀

# 读取内容常见的有3种方式:
# –  read()读取文件的全部内容,与readlines()不同的是,read()会把读取到的内容赋给一个字符串变量。
# –  readlines()读取文件的全部内容,readlines()会把读取到的内容赋值给一个列表变量。
# –  readline()读取文件的一行内容

# 爬取图片
# 1.  将http://www.tedu.cn所有的图片下载到本地
# 2.  本地的目录为/tmp/images
# 3.  图片名与网站上图片名保持一致


import re
import os
from urllib import request

def download(url, fname):
    html = request.urlopen(url)         ##打开并爬取一个网页
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def search_url(fname, patt):
    patt_list = []
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                item = m.group()
                patt_list.append(item)

    return patt_list

if __name__ == '__main__':
    img_dirs = '/tmp/imgs'
    if not os.path.exists(img_dirs):
        os.mkdir(img_dirs)
    download('http://www.baidu.com/', '/tmp/baidu.html')
    img_patt = 'http://[\w./-]+\.(jpg|jpeg|gif|png)'
    img_list = search_url('/tmp/baidu.html', img_patt)
    for url in img_list:
        fname = url.split('/')[-1]
        fname = os.path.join(img_dirs, fname)
        try:                                                   #异常处理
            download(url, fname)
        except:
            pass



