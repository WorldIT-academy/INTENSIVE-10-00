import socket
from threading import Thread

def start_server():
    with socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM) as server_socket:
        # Для того щоб отримати lan ip потрiбно використати команду (WINDOWS: ipconfig,  LINUX/MACOS: ifconfig en0)
        server_socket.bind(('0.0.0.0', 8080))
        # Прослуховування користувачів, очікування підключення 
        server_socket.listen()

        print("Connecting ...")

        # Приймає підключення користувача
        # Зберігаємо налаштування клієнту його адресу
        client_socket, adress = server_socket.accept() # client_socket, adress = (socket, raddr)

        print("Connected user - ", adress)

        # Отримуємо дані клієнту, розміром 1024 байти і декодуємо їх
        data = client_socket.recv(1024).decode()
        
        print(data)

thread_server = Thread(target= start_server)
thread_server.start()

print("Create first thread")