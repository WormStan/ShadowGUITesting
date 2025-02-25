import os
from ultralytics import YOLO


def train_yolo(data_yaml, model_path, epochs=16, img_size=640, batch_size=16):
    """
    Train YOLOv8 model with the specified parameters.
    :param data_yaml: Path to the dataset configuration file (dataset.yaml).
    :param model_path: Path to the pre-trained YOLO model.
    :param epochs: Number of training epochs (default is 8).
    :param img_size: Size of the input images (default is 320).
    :param batch_size: Batch size for training (default is 16).
    """

    yolo_model = YOLO(model_path)
    yolo_model.train(data=data_yaml, epochs=epochs,
                     imgsz=img_size, batch=batch_size)


data_yaml = r"./dataset.yaml"
model_path = r"./yolo_modules/yolov8n.pt"
train_yolo(data_yaml=data_yaml, model_path=model_path)
