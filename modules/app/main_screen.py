import customtkinter

WIDTH = 1300
HEIGTH = 852

main_window_app = customtkinter.CTk(fg_color= '#808080')

width_screen = main_window_app.winfo_screenwidth()
height_screen = main_window_app.winfo_screenheight()

x_coordinate = (width_screen // 2) - (WIDTH // 2)
y_coordinate = (height_screen // 2) - (HEIGTH // 2)

main_window_app.geometry(f"{WIDTH}x{HEIGTH}+{x_coordinate}+{y_coordinate}")