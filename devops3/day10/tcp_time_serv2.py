# forking服务器,解决需要同时响应多个客户端；
# 父进程负责接受客户端的连接请求
# 子进程负责处理客户端的请求


# 案例5:创建多线程时间戳服务器
# •  编写一个TCP服务器
# 1.  服务器监听在0.0.0.0的12345端口上
# 2.  收到客户端数据后,将其加上时间戳后回送给客户端
# 3.  如果客户端发过来的字符全是空白字符,则终止与客户端的连接
# 4.  要求能够同时处理多个客户端的请求
# 5.  要求使用多线程的方式进行编写


import socket
import os
from time import strftime

class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def handle_child(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = data.decode('utf8')
            sdata = '[%s] %s' % (strftime('%H:%M:%S'), data)
            cli_sock.send(sdata.encode('utf8'))
        cli_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            pid = os.fork()  # 创建子进程
            if pid:
                while True:
                    # 通过循环，处理所有的子进程，waitpid会优先处理僵尸进程
                    # 正在运行的子进程返回(0,0)，则中断循环
                    result = os.waitpid(-1, 1) ##1父进程不挂起，可以同时为多个客户端服务
                    # print(result)
                    if result[0] == 0:
                        break
                cli_sock.close()  # 父进程只负责响应客户端，不用和客户通信
            else:
                self.serv.close()  # 子进程只负责与客户通信，不负责建立连接
                self.handle_child(cli_sock)
                exit()  # 子进程通信完后，要退出，不要再进入循环
        self.serv.close()
##################################################################
# if result[0] == 0:
#     break
# 父进程回到外层循环，等待下一个客户端连接
# 内层循环处理僵尸进程（客户端telnet  127.0.0.1  12345 再quit后，产生僵尸进程）；
##################################################################

if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()
