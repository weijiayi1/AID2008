"""
用tcp通讯读取文件写入服务器
"""
from socket import *
#创建套接字
tcp=socket()
#发起连接
tcp.connect(('127.0.0.1',8888))
while True:
#输入要发送的文件名
    fill_name =input("请输入要传送的文件名：")
    if not fill_name:
        break
    fill=open(fill_name)


