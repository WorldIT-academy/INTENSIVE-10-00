import customtkinter as ctk
from .main_screen import main_window_app

class WindowInfo(ctk.CTkTextbox):

    def __init__(self, child_master: object, **kwargs):
        ctk.CTkTextbox.__init__(
            self, 
            master = child_master,
            width = 420,
            height = 275, 
            **kwargs
        )
        self.place(x = 465, y = 560)

winfo = WindowInfo(child_master= main_window_app)