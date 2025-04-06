import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import threading
from model import predict_image  

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color="#2a2d38")  # Dark theme background
        self.selected_image_path = None
        self.setup_sidebar()
        self.setup_main_area()

    def setup_sidebar(self):
        sidebar = ctk.CTkFrame(self, width=250, fg_color="#1f222b", corner_radius=15)  # Rounded corners
        sidebar.pack(side="left", fill="y", padx=15, pady=15)

        # Title with modern font
        ctk.CTkLabel(sidebar, text="Factory OCR", text_color="white", font=("Poppins", 22, "bold")).pack(pady=30)

        # Menu buttons with rounded style and hover effect
        self.add_menu_button(sidebar, "Import Photo", self.import_photo, "icons/upload_icon.png")
        self.add_menu_button(sidebar, "Take Photo", self.capture_photo, "icons/camera_icon.png")
        self.add_menu_button(sidebar, "Predict", self.run_prediction, "icons/predict_icon.png")
        self.add_menu_button(sidebar, "Logout", self.logout, "icons/logout_icon.png")

        
    def add_menu_button(self, parent, text, command, icon_path):
        icon_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(20, 20))  # Load icon image
        btn = ctk.CTkButton(parent, text=text, command=command, corner_radius=15, width=200, height=40,
                            fg_color="#4C5C68", hover_color="#3A4B59", text_color="white", font=("Poppins", 14),
                            image=icon_image)  # Add icon to button
        btn.pack(pady=10)

    def setup_main_area(self):
        self.main_area = ctk.CTkFrame(self, fg_color="#222734")
        self.main_area.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        # Card-like frame for image + prediction
        self.image_card = ctk.CTkFrame(self.main_area, fg_color="#2b303b", corner_radius=12)
        self.image_card.pack(pady=40, padx=30)

        # Image preview
        self.image_label = ctk.CTkLabel(self.image_card, text="Upload or take a photo", font=("Poppins", 18), text_color="white")
        self.image_label.pack(pady=20, padx=20)

        # Prediction output
        self.prediction_label = ctk.CTkLabel(self.image_card, text="", font=("Poppins", 16), text_color="lightgray")
        self.prediction_label.pack(pady=(0, 20))

        # Spinner (invisible by default)
        self.spinner_label = ctk.CTkLabel(self.image_card, text="Predicting...", font=("Poppins", 14), text_color="lightgray")
        self.spinner_label.pack()
        self.spinner_label.pack_forget()  # Hide it initially

    def import_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.jpeg")])
        if file_path:
            self.selected_image_path = file_path
            self.display_image(file_path)

    def capture_photo(self):
        os.makedirs("captured", exist_ok=True)
        response = messagebox.askyesno("Camera Permission", "This app needs access to your camera. Allow?")
        if not response:
            messagebox.showinfo("Permission Denied", "Camera access was not granted.")
            return

    # Open camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to access the camera.")
            return

    # Create camera popup window
        self.camera_window = ctk.CTkToplevel(self)
        self.camera_window.title("Live Camera")
        self.camera_window.geometry("640x500")
        self.camera_window.resizable(False, False)
        self.camera_window.protocol("WM_DELETE_WINDOW", self.close_camera)

    # Live camera frame
        self.video_label = ctk.CTkLabel(self.camera_window, text="")
        self.video_label.pack(pady=10)

    # Capture Button
        capture_btn = ctk.CTkButton(self.camera_window, text="📸 Capture Photo", command=self.capture_image, 
                                    fg_color="#4C5C68", hover_color="#3A4B59", font=("Poppins", 14))
        capture_btn.pack(pady=10)

    # Start live feed in a thread
        self.running = True
        self.update_frame()

    def update_frame(self):
        if self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
            # Convert to ImageTk for display
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)

                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)

            self.after(10, self.update_frame)

    def capture_image(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                save_path = os.path.join("captured", "capture.jpg")
                cv2.imwrite(save_path, frame)
                self.selected_image_path = save_path
                self.display_image(save_path)
                self.close_camera()

    def close_camera(self):
        self.running = False
        if hasattr(self, "cap") and self.cap.isOpened():
            self.cap.release()
        if hasattr(self, "camera_window"):
            self.camera_window.destroy()


    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)

        # Show image
        self.image_label.configure(image=img, text="")
        self.image_label.image = img

    def run_prediction(self):
        if not self.selected_image_path:
            self.image_label.configure(text="Please select or capture an image first.")
            return

        # Show spinner
        self.spinner_label.pack()
        self.prediction_label.configure(text="")

        # Run prediction after a slight delay to allow image rendering
        self.after(100, self.run_prediction_delayed, self.selected_image_path)

    def run_prediction_delayed(self, image_path):
        prediction = predict_image(image_path)
        self.prediction_label.configure(text=f"Prediction: {prediction}")
        self.spinner_label.pack_forget()

    def logout(self):
        self.master.show_login()
