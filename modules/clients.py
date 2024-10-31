import socket

with socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM) as client_socket:
    # Підключаємо клієнта  до локального IP та порту
    client_socket.connect(("WAN_IP_SERVER", 8080))
    # Відправляємо дані клієнта та кодує на сервер 
    client_socket.send("hello server!".encode())