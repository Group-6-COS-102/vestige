import customtkinter as ctk


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(
            self,
            text="Welcome to the Home Page",
            font=("Konkhmer Sleokchher", 24, "bold")
        ).pack(pady=20, expand=True)
