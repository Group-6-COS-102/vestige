import customtkinter as ctk
from PIL import Image


# ---------------- LAYOUT FUNCTION ---------------- #

def create_layout(app):

    # ---------------- LEFT SIDEBAR ---------------- #

    sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#1E1E2E"
    )

    sidebar.pack_propagate(False)
    sidebar.pack(side="left", fill="y")

    # ---------------- LOGO ---------------- #

    app_icon = ctk.CTkImage(
        Image.open("logo.png"),
        size=(20, 20)
    )

    logo_label = ctk.CTkLabel(
        sidebar,
        image=app_icon,
        text=" Vestige",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(20,10), padx=(5,40))

    app_icon2 = ctk.CTkImage(
        Image.open("ggg.PNG"),
        size=(50, 50))
    logo_label2 = ctk.CTkLabel(
        sidebar,
        image=app_icon2,
        text="  Profile" ,
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label2.pack(pady=(0), padx=(0,60))

    top_left = ctk.CTkFrame(sidebar, fg_color="transparent")
    top_left.pack(fill="x", side="top")

    bottom_left = ctk.CTkFrame(sidebar, fg_color="transparent")
    bottom_left.pack(fill="x", side="bottom", pady=10)


    # ---------------- NAV BUTTON FUNCTION ---------------- #

    def nav_button(text, image_path, parent):

        icon = ctk.CTkImage(
            parent,
            Image.open(image_path),
            size=(20, 20)
        )

        button = ctk.CTkButton(
            sidebar,
            image=icon,
            text=text,
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#0710B7",
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

    # --- TOP BAR (QUOTE & SEARCH) ---
    top_bar = ctk.CTkFrame(main_frame, fg_color="transparent")
    top_bar.pack(fill="x", padx=25, pady=(20, 10))

    quote = ctk.CTkLabel(
        top_bar, 
        text="\"Exploring how the past shapes the present\nand what we risk losing...\"", 
        font=("Poppins", 13, "italic"),
        text_color="#555555",
        justify="left"
    )
    quote.pack(side="left", anchor="w")

    search_bar = ctk.CTkEntry(
        top_bar, 
        placeholder_text="Search", 
        width=180, 
        height=28, 
        corner_radius=14,
        fg_color="#E0E0E0",
        border_width=0,
        text_color="black"
    )
    search_bar.pack(side="right", anchor="e", padx=10)

    # --- GREY CONTENT CONTAINER ---
    timeline_container = ctk.CTkFrame(main_frame, fg_color="#EBEBEB", corner_radius=20)
    timeline_container.pack(fill="both", expand=True, padx=25, pady=(10, 20))


    # ---------------- RIGHT SIDEBAR ---------------- #

    # Changed background color to match the deep blue style in the screenshot
    right_sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#2D5B94" 
    )

    right_sidebar.pack_propagate(False)
    right_sidebar.pack(side="right", fill="y")

    # --- SECTION 1: DID YOU KNOW ---
    dyk_title = ctk.CTkLabel(
        right_sidebar, 
        text="Did You Know...?", 
        font=("Poppins", 14, "bold"), 
        text_color="white"
    )
    dyk_title.pack(anchor="w", padx=15, pady=(15, 9))

    Third = ctk.CTkFrame(
        right_sidebar,
        width=170,
        height=170,
        corner_radius=10,
        fg_color="#FFFFFF",
    )
    Third.pack_propagate(False)
    Third.pack(fill="x", padx=15, pady=5)
    
    # Image placeholder inside Third frame
    
    dyk_img_file = ctk.CTkImage(Image.open("10.jpeg"), size=(150, 80)) 
    dyk_img = ctk.CTkLabel(Third, image=dyk_img_file, text="",)
    dyk_img.pack(pady=(10, 5))
    

    dyk_text = ctk.CTkLabel(
        Third, 
        text="☏Before smartphones,\ncommunication relied on letters\nand messengers (Town Criers).",
        font=("Exo", 10),
        text_color="black"
        
    )
    dyk_text.pack(pady=5)

    # --- SECTION 2: WHAT WE'RE LOSING ---
    losing_title = ctk.CTkLabel(
        right_sidebar, 
        text="What We're Losing", 
        font=("Poppins", 14, "bold"), 
        text_color="white"
    )
    losing_title.pack(anchor="w", padx=15, pady=(10, 0))

    # The texts for your 3 stacked cards
    losing_texts = [
        "Many indigenous languages are\ndisappearing",
        "Traditional clothing is now\nmostly worn at events",
        "The stories and customs that\nshaped us are slowly disappearing"
    ]
    

    for i in range(3):
        card = ctk.CTkFrame(
            right_sidebar,
            width=170,
            height=70,
            corner_radius=5,
            fg_color="white"
        )
        card.pack_propagate(False)
        card.pack(fill="x", padx=15, pady=5)
        
        losing_lbl = ctk.CTkLabel(
            card, 
            text=losing_texts[i], 
            font=("Poppins", 9, "bold"), 
            text_color="black",
            justify="center"
        )
        losing_lbl.pack(fill="both", expand=True, padx=10)
        
    # --- SECTION 3: SAVED ITEMS ---
    saved_title = ctk.CTkLabel(
        right_sidebar, 
        text="Saved Items", 
        font=("Poppins", 14 ), 
        text_color="white",
        
    )
    saved_title.pack(anchor="w", padx=15, pady=(10, 0))

    fourth = ctk.CTkFrame(
        right_sidebar,
        width=140,
        height=90,
        corner_radius=20,
        fg_color="#FFFFFF",
    )
    fourth.pack_propagate(False)
    fourth.pack(fill="x", padx=15, pady=5)

    saved_text = ctk.CTkLabel(
        fourth, 
        text="You haven't saved anything yet!", 
        font=("Poppins", 10, "bold"), 
        text_color="black",
        
    
    )
    saved_text.pack(fill="both", expand=True)
        
    return timeline_container


# ---------------- APP WINDOW ---------------- #

app = ctk.CTk()

app.geometry("1200x650")
app.title("Vestige")

# CREATE THE LAYOUT
content_area = create_layout(app)

# START APP
app.mainloop()