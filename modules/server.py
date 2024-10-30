import socket

with socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM) as server_socket:
    # Для того щоб отримати lan ip потрiбно використати команду (WINDOWS: ipconfig,  LINUX/MACOS: ifconfig en0)
    server_socket.bind(('192.168.1.29', 8080))
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