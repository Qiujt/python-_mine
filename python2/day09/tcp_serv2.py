import  socket

host=''             #表示监听在0.0.0.0
port=12345          #端口号，应该>1024
addr=(host,port)
s=socket.socket()

#如果没有以下一行设置，当程序结束后，系统默认保留该套接字60秒，无法立即再运行
#加上以下设置，程序可以立即重新启动
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:                             ##
    cli_sock,cli_addr=s.accept()
    print('Client connected from：',cli_addr)
    while True:
        data=cli_sock.recv(1024)
        if data.strip() ==b'quit':
            break
        print(data.decode('utf8'))
        sdata=input('>')
        sdata='%s\r\n' % sdata
        cli_sock.send(sdata.encode('utf8'))

    cli_sock.close()
s.close()                       ##实际没有执行这一行，上面死循环
#客户端访问telent  127.0.0.1  12345