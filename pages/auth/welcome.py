import customtkinter as ctk
from PIL import Image

from pages.auth.login import LoginPage
from ui.auth_layout import create_auth_layout
from ui.theme import PRIMARY_BLUE, TEXT_WHITE


class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # shared layout
        page, left, right, panel = create_auth_layout(self, panel_side="left")
        page.pack(fill="both", expand=True)

        # large logo placeholder
        ctk.CTkLabel(
            panel,
            text="Logo",
            font=("Konkhmer Sleokchher", 40, "bold"),
            text_color="white"
        ).place(relx=0.5, rely=0.40, anchor="center")

        # small logo placeholder
        ctk.CTkLabel(
            right,
            text="LOGO",
            font=("Konkhmer Sleokchher", 20, "bold"),
            text_color="white"
        ).place(relx=0.5, rely=0.15, anchor="center")

        ctk.CTkLabel(
            right,
            text="Vestige",
            font=("Konkhmer Sleokchher", 50, "bold"),
            text_color="white"
        ).place(relx=0.5, rely=0.30, anchor="center")

        # motto
        ctk.CTkLabel(
            right,
            text="Preserving Yesterday...",
            font=("Konkhmer Sleokchher", 25, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        # get started button
        ctk.CTkButton(
            right,
            text="Get Started",
            fg_color=PRIMARY_BLUE,
            text_color=TEXT_WHITE,
            corner_radius=15,
            width=180,
            height=50,
            font=("Khonkhmer Sleokchher", 18, "bold"),
            command=lambda: self.controller.show_page(LoginPage)
        ).place(relx=0.50, rely=0.68, anchor="center")
