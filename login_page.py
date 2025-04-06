import customtkinter as ctk
from PIL import Image

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, login_callback):
        super().__init__(master)
        self.master = master
        self.login_callback = login_callback
        self.configure(fg_color="#2a2d38")  # Dark theme background
        self.create_widgets()

    def create_widgets(self):
        # Title with modern font
        ctk.CTkLabel(self, text="Factory OCR Login", font=("Poppins", 24, "bold"), text_color="white").pack(pady=40)

        # Username Entry
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", font=("Poppins", 14), width=280)
        self.username_entry.pack(pady=10)

        # Password Entry
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", font=("Poppins", 14), width=280)
        self.password_entry.pack(pady=10)

        # Load the login icon
        login_icon = ctk.CTkImage(light_image=Image.open("icons/login_icon.png"), size=(20, 20))  # Adjust icon size

        # Login Button with icon inside
        login_button = ctk.CTkButton(self, text="Login", command=self.try_login, corner_radius=15, width=280, height=40, 
                                     fg_color="#4C5C68", hover_color="#3A4B59", text_color="white", font=("Poppins", 14),
                                     image=login_icon, compound="left")  # Display icon on the left of the text
        login_button.pack(pady=20)

        # Error Message Label (initially invisible)
        self.error_label = ctk.CTkLabel(self, text="Invalid credentials", text_color="red", font=("Poppins", 16,"bold"))
        self.error_label.pack(pady=10)
        self.error_label.pack_forget()  # Hide error message initially

    def try_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin":
            self.login_callback()
        else:
            self.error_label.pack()  # Show error message if credentials are invalid
