import customtkinter as ctk
from login_page import LoginPage
from dashboard import HomePage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the initial theme globally
        ctk.set_appearance_mode("dark")#Default theme

        self.title("Factory OCR")
        self.geometry("1000x600")

        self.login_page = LoginPage(self, self.show_home)
        self.login_page.pack(expand=True, fill="both")

    def show_home(self):
        self.login_page.pack_forget()
        self.home_page = HomePage(self)
        self.home_page.pack(expand=True, fill="both")

    def show_login(self):
        self.home_page.pack_forget()
        self.login_page = LoginPage(self, self.show_home)
        self.login_page.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = App()
    app.mainloop()
