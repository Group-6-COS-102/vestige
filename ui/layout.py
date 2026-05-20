import customtkinter as ctk
from PIL import Image


# ---------------- LAYOUT FUNCTION ---------------- #

def create_layout(app):

    # ---------------- LEFT SIDEBAR ---------------- #

    left_sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#1E1E2E"
    )

    left_sidebar.pack_propagate(False)
    left_sidebar.pack(side="left", fill="y")

    # ---------------- LOGO ---------------- #

    app_icon = ctk.CTkImage(
        Image.open("assets/icons/logo.PNG"),
        size=(20, 20)
    )

    logo_label = ctk.CTkLabel(
        left_sidebar,
        image=app_icon,
        text=" Vestige",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(20, 10), padx=(5, 40))

    app_icon = ctk.CTkImage(
        Image.open("assets/pictures/profile.PNG"),
        size=(30, 30))
    logo_label = ctk.CTkLabel(
        left_sidebar,
        image=app_icon,
        text="  Profile",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(0), padx=(0, 60))

    top_left = ctk.CTkFrame(left_sidebar, fg_color="transparent")
    top_left.pack(fill="x", side="top")

    bottom_left = ctk.CTkFrame(left_sidebar, fg_color="transparent")
    bottom_left.pack(fill="x", side="bottom", pady=10)

    # ---------------- NAV BUTTON FUNCTION ---------------- #

    def nav_button(text, image_path, parent):

        icon = ctk.CTkImage(
            Image.open(image_path),
            size=(20, 20)
        )

        button = ctk.CTkButton(
            parent,
            image=icon,
            text=text,
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#313244",
            anchor="w"
        )

        button.pack(fill="x", padx=10, pady=10)

        return button

    # ---------------- BUTTONS ---------------- #

    nav_button("Home", "assets/icons/home.png", top_left)
    nav_button("Then Vs Now", "assets/icons/tvn.png", top_left)
    nav_button("Timelines", "assets/icons/time.png", top_left)
    nav_button("Lost Traditions", "assets/icons/lost.png", top_left)
    nav_button("Gallery", "assets/icons/gallery.png", top_left)
    nav_button("About", "assets/icons/about.png", top_left)
    nav_button("Settings", "assets/icons/setting.png", bottom_left)
    nav_button("Log out", "assets/icons/logout.png", bottom_left)

    # ---------------- MAIN AREA ---------------- #

    main_frame = ctk.CTkFrame(
        app,
        fg_color="#F5F5F5"
    )

    main_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    # SAMPLE CONTENT
    title = ctk.CTkLabel(
        main_frame,
        text="Main Content Area",
        font=("Poppins", 35, "bold"),
        text_color="black"
    )

    title.pack(pady=50)

    # ---------------- RIGHT SIDEBAR ---------------- #

    right_sidebar = ctk.CTkFrame(
        app,
        width=300,
        corner_radius=0,
        fg_color="#525258"
    )

    right_sidebar.pack_propagate(False)
    right_sidebar.pack(side="right", fill="y")

    top_right = ctk.CTkFrame(right_sidebar, fg_color="transparent")
    top_right.pack(fill="x", side="top")

    bottom_right = ctk.CTkFrame(right_sidebar, fg_color="transparent")
    bottom_right.pack(fill="x", side="bottom", pady=10)

    Third = ctk.CTkFrame(
        top_right,
        width=240,
        height=170,
        corner_radius=10,
        fg_color="#FFFFFF",
    )

    Third.pack(fill="y", pady=(40, 40))
    # SAMPLE CARDS
    for i in range(3):

        card = ctk.CTkFrame(
            top_right,
            width=240,
            height=70,
            corner_radius=10,
            fg_color="white"
        )

        card.pack(pady=8)

    fourth = ctk.CTkFrame(
        bottom_right,
        width=240,
        height=90,

        corner_radius=10,
        fg_color="#FFFFFF",

    )

    fourth.pack(fill="y", pady=(10))

    return main_frame, left_sidebar, right_sidebar, Third, fourth
