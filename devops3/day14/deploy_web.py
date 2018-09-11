
# 案例7:发布应用
# •  编写应用发布程序
# –  根据分发服务器的版本,下载对应的应用
# –  校验应用程序
# –  发布指定程序

import requests
import  os
import hashlib
import tarfile
from urllib import request

def  get_webdata(url):              ##获得分发服务器（jenkins装了Apache）上的新版本代码
    r = requests.get(url)
    return  r.text

def download(url,fname):
    html = request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def  check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def  deploy(app):               ##各应用服务器展开，部署新版本
    os.chdir('/var/www/packages')  ##将从分发服务器（jenkins）得到的app代码解压
    tar = tarfile.open(app, 'r:gz')
    tar.extractall()
    tar.close()
    src = app.replace('.tar.gz', '')
    dst = '/var/www/html/mysite'    ##快捷方式（指向新版本，##亦可回滚到旧版本）
    if os.path.exists(dst):
        os.unlink(dst)          #删除旧的快捷方式
    os.symlink(src, dst)


if __name__ == '__main__':
    ver = get_webdata('http://192.168.122.236/deploy/live_version').strip()
                                                    ##得到需要的版本号
    app_name = 'mproject_%s.tar.gz' % ver
    app_url = 'http://192.168.122.236/deploy/packages/' + app_name
    app_path = os.path.join('/var/www/packages/' , app_name)  ##下载软件包到各应用服务器
    download(app_url,app_path)             ##下载软件包
    local_md5 = check_md5(app_path)       ##校验下载到的代码md5值
    remote_md5 = get_webdata(app_url + '.md5').strip()
    if  local_md5 == remote_md5:
        deploy(app_path)
