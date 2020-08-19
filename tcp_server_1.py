"""
tcp服务端循环流程1
特点：每次只处理一个客户端，一个完成后才能进行下一个
重点代码！！！
"""
from socket import*
#创建tcp套接字 使用默认值就是tcp套接字
tcp_socket=socket(AF_INET,SOCK_STREAM)
#绑定地址
tcp_socket.bind(('0.0.0.0',8888))
#设置监听 将tcp套接字可以被连接
tcp_socket.listen(5)
#处理客户端连接
while True:
   print("等待连接..")
   connfd,addr =tcp_socket.accept()
   print("连接：",addr)#客户端地址

   while True:
#先收后发
       data =connfd.recv(1024)#recv是阻塞函数
    #退出方案2
       if not data:
           connfd.close()#客户端退出连接套接字就没用了
           break

    #输入quit退出方案1
    #if data.decode()=='quit':
    #    break
       print('接收到',data.decode())
#发
       connfd.send(b'thanks')

#关闭
tcp_socket.close()

