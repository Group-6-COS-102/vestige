import customtkinter as ctk
from PIL import Image
from ui.layout import create_layout


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        main_frame, left_sidebar, right_sidebar, Third, fourth = create_layout(
            self)
        main_frame.pack(fill="both", expand=True)
