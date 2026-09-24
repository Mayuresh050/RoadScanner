from ultralytics import YOLO

model = YOLO(r"runs\detect\train-3\weights\best.pt")

results = model(r"Test\test_1.jpg")

results[0].show()