"""
tcp 客户端基础示例
"""
from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)

# 默认值就是创建tcp套接字
tcp_socket = socket()

# 发起链接
tcp_socket.connect(ADDR)

# 发送接受消息
msg = input(">>")
tcp_socket.send(msg.encode())
data = tcp_socket.recv(1024)
print("Server:",data.decode())

# 关闭
tcp_socket.close()