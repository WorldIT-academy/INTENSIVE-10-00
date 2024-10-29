import customtkinter as ctk
from .main_screen import main_window_app

class UserWindow(ctk.CTkFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkFrame.__init__(
            self, 
            master= child_master, 
            width= 865,
            height= 530,
            border_width= 3,
            **kwargs
        )
        # self.grid(row= 0, column= 0, sticky= 'nsew')
        self.place(x= 20, y= 20)
        

window_user = UserWindow(child_master= main_window_app)