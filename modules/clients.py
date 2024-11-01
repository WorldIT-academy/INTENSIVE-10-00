import socket
import pyautogui
import io
import time


with socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM) as client_socket:
    # Підключаємо клієнта  до локального IP та порту
    client_socket.connect(("WAN_IP_SERVER", 8081))
    while True:
        # Робимо скрiншот екрану
        data_screen = pyautogui.screenshot()
        # Створюємо об'єкт класу для байт коду зображення
        img_bytes = io.BytesIO()
        # Зберігаємо скріншот у змінну у вигляді байтiв
        data_screen.save(img_bytes, format="PNG")
        # Зберігаємо байти в змiнну
        data_bytes = img_bytes.getvalue()
        # Отримуемо довжину байтiв для серверу
        lenght = len(data_bytes)
        # Відправляємо дані клієнта на сервер 
        client_socket.sendall(str(lenght).encode() + data_bytes)
        time.sleep(0.2)