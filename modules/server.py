import socket
from threading import Thread
import PIL.Image
import io
import os
from .app.user_window import window_user

# Отримуємо повний шлях до картинки
IMAGE_PATH = os.path.abspath(__file__ + "/../../images/1.png")

def start_server():
    with socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM) as server_socket:
        # Для того щоб отримати lan ip потрiбно використати команду (WINDOWS: ipconfig,  LINUX/MACOS: ifconfig en0)
        server_socket.bind(('0.0.0.0', 8081))
        # Прослуховування користувачів, очікування підключення 
        server_socket.listen()

        print("Connecting ...")

        # Приймає підключення користувача
        # Зберігаємо налаштування клієнту його адресу
        client_socket, adress = server_socket.accept() # client_socket, adress = (socket, raddr)

        print("Connected user - ", adress)

        while True:
            # response_data - Зберігає поточнi дані вiд клiента 
            # download_data - Зберігає загальну суму поточних даних вiд клiента 
            # Отримуємо дані клієнту, розміром 1024 байти 
            # Отримуємо довжину байт коду
            lenght = client_socket.recv(6).decode()
            response_data = client_socket.recv(1024)
            download_data = response_data
            # Поки довжина отриманого байти коду менша за потрiбну отримуємо 
            while len(download_data) < int(lenght):
                # Отримуємо дані клієнту, розміром 1024 байти 
                response_data = client_socket.recv(1024)
                # Збираємо всі поточні дані разом
                download_data = download_data + response_data
            # є зображення
            if download_data:
                # Перетворимо дані, отримані з мережі в BytesIO
                download_data = io.BytesIO(download_data)
                # Створюємо картинку з отриманих байтів
                image = PIL.Image.open(download_data)
                # Зберігаємо картинку за вказаним шляхом
                image.save(IMAGE_PATH)
                # Змінюємо зображення в додатку window_user
                window_user.configure(image = window_user.load_image())

thread_server = Thread(target= start_server)
thread_server.start()

print("Create first thread")