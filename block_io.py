"""

"""
from time import *
from socket import *



tcp = socket()
tcp.bind(('0.0.0.0', 8888))
tcp.listen(5)

tcp.setblocking(False)

while True:
    try:
        connfd, addr = tcp.accept()
        print('connect from', addr)
    except BlockingIOError as e:
        sleep(2)
    else:
        data = connfd.recv(1024).decode()
        print(data)
