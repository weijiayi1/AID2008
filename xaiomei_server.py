"""
tcp 服务端循环流程 2
特点：发一次消息要连接一次断开一次
重点代码!!!
"""

from socket import *

# 创建tcp套接字 其实使用默认值就是tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听,让tcp套接字可以被链接
tcp_socket.listen(5)

# 处理客户端连接
while True:
    print("等待客户端消息....")
    connfd,addr = tcp_socket.accept()
    data = connfd.recv(1024)
    d=str()
    if data.decode()=='你多大了':
        d='2岁啦'
    elif data.decode()=='你是男生女生':
        d='我是机器人'
    elif data.decode()=='你漂亮吗':
        d='我天生丽质'
    elif data.decode()=='你叫什么':
        d='我叫小美'
    else:
        d='我还小,听不懂'
    connfd.send(d.encode())

    connfd.close()

# 关闭
tcp_socket.close()




