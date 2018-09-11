
#本机收发邮件

from  email.mime.text import  MIMEText
from  email.header import Header
from  smtplib import  SMTP          ##mtplib提供了一种很方便的途径发送电子邮件

message = MIMEText('this is a "mail_test"\r\n','plan','utf8')
message ['From'] = Header('zzg','utf8')
message ['To'] = Header('root','utf8')
message['Subject'] = Header('邮件测试','utf8')
smtp = SMTP('127.0.0.1')
smtp.send_message('zzg')