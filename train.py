from ultralytics import YOLO

# reference : https://docs.ultralytics.com/zh/datasets/detect/#usage
# Load a model
model = YOLO("yolov8n.pt") # load a pretrained model

# Train the model
results = model.train(data='data.yaml', epochs=100, imgsz=640)

# Validate the model
results = model.val(data="data.yaml")

