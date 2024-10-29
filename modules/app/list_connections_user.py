import customtkinter as ctk 
from  .main_screen import main_window_app

class ConnectionUsers(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self, 
            master= child_master,
            width= 353,
            height= 800, 
            **kwargs
        )
        self.place(x= 905, y= 20)

connection_user = ConnectionUsers(child_master= main_window_app)