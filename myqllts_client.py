"""
群聊聊天室客户端
"""
from socket import *

id=('127.0.0.1',7777)
# 创建udp套接字
udp =socket(AF_INET,SOCK_DGRAM)
#发送接收
while True:
    name=input('请输入你的用户名')
    udp.sendto(name.encode(),id)
    data,sid =udp.recvfrom(1024)
    if data!=b'n':
        print(data.decode())
        while True:
            neirong =input()
            udp.sendto(neirong.encode(), id)
            da, sid = udp.recvfrom(1024)
            print(da.decode())
