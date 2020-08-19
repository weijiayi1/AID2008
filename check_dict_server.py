"""
用服务器的方式查询字典
"""
from socket import *
import pymysql
#创建套接字,绑定ip和端口
udp =socket(AF_INET,SOCK_DGRAM)
udp.bind(("0.0.0.0",8888))
#2.连接数据库
while True:
    db =pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "dict",
                     charset = "utf8")
#udp接收查询信息
    print('空闲等待...')
    data,ip=udp.recvfrom(1024)
    if data.decode()=='q':
        n = udp.sendto(str('服务器已关闭').encode(), ip)
        db.close()
        udp.close()
        break
    print('查询',ip,'的',data.decode())
#创建游标
    cur =db.cursor()
#查询解析
    sql ="select mean from words where word=%s;"
    cur.execute(sql,data.decode())
    db.commit()
#获取解析内容
    jx=cur.fetchone()#此语句返回的是元组
    try:
       for jxx in jx:
          pass
    except TypeError:
        jxx='没有相对应的解析'
        cur.close()
        db.close()
#通过udp发送解析
    n=udp.sendto(jxx.encode(),ip)
    cur.close()
db.close()
udp.close()