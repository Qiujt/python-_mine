# SMTP认证
# 如果本机没有SMTP功能,也可以使用第三方的邮件服务器
# 第三方邮件服务器往往需要认证

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP
import getpass

def send_msg(host, pwd, sender, receivers, subject, msg):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = SMTP(host)
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == '__main__':
    host = 'smtp.163.com'       ##SMTP服务器: smtp.163.com
    pwd = getpass.getpass()
    sender = 'kingjay0308@163.com'
    receivers = ['kingjay0308@163.com']
    subject = '邮件测试'
    msg = 'Python邮件测试\r\n'
    send_msg(host, pwd, sender, receivers, subject, msg)

##
# python3  /root/桌面/python/代码_mine/day13/inet_mail.py
# Password:   ##用从第三方登陆网易邮箱的密码（吾非登陆网易邮箱的密码）
