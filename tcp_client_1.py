"""
tcp 客户端基础1
"""
from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)

# 默认值就是创建tcp套接字
tcp_socket = socket()

# 发起链接
tcp_socket.connect(ADDR)

while True:
# 发送接受消息
    msg = input(">>")
    #退出循环方案2
    if not msg:
        break
    tcp_socket.send(msg.encode())
    #输入quit退出 循环退出方案1
    #if msg =='quit':
    #    break
    data = tcp_socket.recv(1024)
    print("Server:",data.decode())

# 关闭
tcp_socket.close()