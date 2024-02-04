# YOLOv8---KITTI
### Test
```
model = YOLO("runs/detect/train/weights/last.pt")
test = Image.open("C:/Users/user/Downloads/000001.png")
results = model(test)

for r in results:
    im_array = r.plot()  # 繪製預測结果的BGR numpy數組
    im = Image.fromarray(im_array[..., ::-1])  # 轉換為RGB PIL圖像
    img = cv2.cvtColor(im_array[..., ::-1], cv2.COLOR_BGR2RGB) # 圖像讀取為BGR，將其轉換為RGB
    cv2.imshow("result", img) 
    cv2.waitKey(0)
```
