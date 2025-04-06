# model.py
from ultralytics import YOLO
import cv2

model = YOLO("best.pt")  # make sure path is correct

def predict_image(image_path):
    results = model(image_path)
    names = model.names  # map class index to label name

    if results and results[0].boxes is not None:
        predictions = results[0].boxes.cls.tolist()
        labels = [names[int(cls)] for cls in predictions]
        return ", ".join(labels) if labels else "No number detected"
    else:
        return "No number detected"
