import PIL.Image
import customtkinter as ctk
from .main_screen import main_window_app
import os, PIL

class UserWindow(ctk.CTkLabel):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkLabel.__init__(
            self, 
            master= child_master, 
            width= 865,
            height= 530,
            # border_width= 3,
            text= "",
            image=self.load_image(),
            **kwargs
        )
        # self.grid(row= 0, column= 0, sticky= 'nsew')
        self.place(x= 20, y= 20)
        
    def load_image(self):
        image_path = os.path.abspath(__file__ + "/../../../images/1.png")
        image = PIL.Image.open(image_path)
        return ctk.CTkImage(light_image = image, size = (865, 530))

window_user = UserWindow(child_master= main_window_app)