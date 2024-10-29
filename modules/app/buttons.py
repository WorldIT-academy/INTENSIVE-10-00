import customtkinter as ctk
from .main_screen import main_window_app

class Buttons(ctk.CTkButton):
    def __init__(self, child_master: object, title: str, command: object | None = None, **kwargs):
        ctk.CTkButton.__init__(
            self,
            master = child_master,
            width = 165,
            height = 48,
            border_width = 2,
            command = command,
            text = title
        )
        self.place(x = 20, y = 560)

start_server = Buttons(child_master = main_window_app, title = "START")
        