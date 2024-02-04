# YOLOv8---KITTI
### Test
    model = YOLO("runs/detect/train/weights/last.pt")

    test = Image.open("C:/Users/user/Downloads/000001.png")
    results = model(test)

    for r in results:
        im_array = r.plot()  # 绘制预测结果的BGR numpy数组
        im = Image.fromarray(im_array[..., ::-1])  # 转换为RGB PIL图像
        img = cv2.cvtColor(im_array[..., ::-1], cv2.COLOR_BGR2RGB) # Open-CV将图像读取为BGR，我们将其转换为RGB
        cv2.imshow("result", img)  # 显示图像
        cv2.waitKey(0) 
