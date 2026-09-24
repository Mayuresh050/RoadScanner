from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")

    model.train(
        data=r"C:\Users\Gadget Care\Prime_Batch\RoadScanner\dataset_merged\data.yaml",
        epochs=30,
        imgsz=640,
        workers=0
    )