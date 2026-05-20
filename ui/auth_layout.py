import customtkinter as ctk
from ui.theme import BACKGROUND_GRAY, CARD_BLACK, PANEL_GRAY


def create_auth_layout(parent, panel_side="left"):

    page = ctk.CTkFrame(parent, fg_color=BACKGROUND_GRAY)

    card = ctk.CTkFrame(
        page,
        fg_color=CARD_BLACK,
        corner_radius=30,
        bg_color=BACKGROUND_GRAY
    )

    card.place(relx=0.5, rely=0.5, relwidth=0.75,
               relheight=0.75, anchor="center")

    # left and right sides
    left = ctk.CTkFrame(card, fg_color="transparent", corner_radius=0)
    right = ctk.CTkFrame(card, fg_color="transparent", corner_radius=0)

    left.place(relx=0.02, rely=0.02, relwidth=0.46, relheight=0.96)
    right.place(relx=0.52, rely=0.02, relwidth=0.46, relheight=0.96)

    panel = ctk.CTkFrame(
        card,
        fg_color=PANEL_GRAY,
        corner_radius=30
    )

    if panel_side == "left":
        panel.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.9)

    else:
        panel.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.9)

    return page, left, right, panel
