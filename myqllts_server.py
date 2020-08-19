"""
群聊聊天室服务端
"""
from socket import *

# 创建udp套接字
udp = socket(AF_INET, SOCK_DGRAM)
# 绑定端口和地址
udp.bind(('0.0.0.0', 7777))
print('等待中...')
user = {}
uport = []
id_prot = []
# 获取用户名并存起来
while True:
    data, id = udp.recvfrom(1024)
    port = id[1]#获取端口号
    print('连接',id,data.decode())
    while True:
        if id not in id_prot:
            try:#user字典为空时用0代替报错
                name = user[port]
            except KeyError:
                name = 0
                print(name)
                print(data.decode())
            if name != data.decode():#不等则没有重名
                user[port] = data.decode()#以端口为键存用户名
                uport.append(id[1])
                id_prot.append(id)
                for d in id_prot:
                    if not d:
                        pass
                    else:
                        udp.sendto('欢迎'.encode() + user[port].encode(), d)
                        break
            else:
                udp.sendto(b'n', id)
        else:
            if not data:
                uport.remove(id[0])
                user.pop(user[port])
                id_prot.remove(id)
            for d in id_prot:
                if not d:
                   pass
                else:
                    udp.sendto(user[port].encode() + ':'.encode() + data, d)
            break
