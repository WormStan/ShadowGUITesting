from ultralytics import YOLO


model = YOLO('./runs/detect/train/weights/best.pt')
results = model.predict(source=r'<image path>')
for result in results:
    print(result)
