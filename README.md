# 🏭 Factory OCR App

A modern desktop application for factory environments to **capture, upload, and predict cast numbers** on tires using a pre-trained machine learning model.

Built with **Python**, **CustomTkinter**, and **OpenCV**.

---

## ✨ Features

- 🔒 Beautiful modern **login interface**
- 🎨 Dark/light **theme switcher** with icons
- 📸 Capture photo from webcam with **live preview**
- 🖼️ Upload image from your device
- 🔍 Predict tire cast numbers using an integrated model
- 🧠 Built-in support for **custom-trained ML models**
- ⚡ Smooth transitions and clean UI animations

---

## 📷 Screenshot

![App Preview](https://via.placeholder.com/800x400.png?text=Factory+OCR+Preview)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hydr64/factory-ocr-app.git
cd factory-ocr-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Or manually install:

```bash
pip install customtkinter opencv-python pillow
```

### 3. Run the App

```bash
python main.py
```

---

### 4. Login to the app

```username = admin
password= admin
```

## 🧠 Model Integration

- You can customize the model by editing `model.py`.
- The `predict_image(image_path)` function should return the prediction string.

---

## 📁 Project Structure

```
📂 CCRapp/
├── dashboard.py       # Home page with sidebar & prediction logic
├── login_page.py      # Login UI logic
├── main.py            # App entry point
├── model.py           # Prediction logic using ML model
├── assets/            # Icons/images
└── README.md          # This file
```

---

## 🛠️ Tech Stack

- 🐍 Python 3.12
- 🎨 [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- 🎥 OpenCV
- 🧠 PIL (Pillow)

---

## 👨‍💻 Authors

- Hayder Hmidi
- Aymen Ayouni
  > École Supérieure d'Ingénieur Privée Gafsa – [CITIC Dicastal Competition]

---

## 📜 License

This project is licensed under the MIT License.
