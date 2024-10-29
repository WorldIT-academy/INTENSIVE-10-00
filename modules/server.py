import socket

server_socket = socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 8080))