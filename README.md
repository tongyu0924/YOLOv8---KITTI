# YOLOv8---KITTI
Reference : 

https://github.com/ultralytics/ultralytics/tree/main

https://github.com/shreydan/yolo-object-detection-kitti/tree/main

Dataset : 

https://www.kaggle.com/datasets/klemenko/kitti-dataset

### Prepare data
convert data to yolo format

yolo format : [class, x_center, y_center, width, height]  (x, y, w, h need to be 0 ~ 1)
```
python generate_dataset.py
```

### Train
```
python train.py
```

### Test
```
model = YOLO("runs/detect/train/weights/last.pt")
test = Image.open("test.png")
results = model(test)

for r in results:
    im_array = r.plot()  # 繪製預測结果的BGR numpy數組
    im = Image.fromarray(im_array[..., ::-1])  # 轉換為RGB PIL圖像
    img = cv2.cvtColor(im_array[..., ::-1], cv2.COLOR_BGR2RGB) # 圖像讀取為BGR，將其轉換為RGB
    cv2.imshow("result", img) 
    cv2.waitKey(0)
```

result :

![image](https://github.com/tongyu0924/YOLOv8---KITTI/assets/119610311/fd012d2f-0b92-40da-91b6-fda705829912)


