"""
创建套接字
"""

import socket

udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM
                           )
udp_socket.bind(("127.0.0.1",8888))
udp_socket.bind(("0.0.0.0",8888))