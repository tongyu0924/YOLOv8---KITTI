import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from PIL import Image

#convert data to yolo format

label_cols = [
    'label', 'truncated', 'occluded', 'alpha',
    'bbox_xmin', 'bbox_ymin', 'bbox_xmax',
    'bbox_ymax', 'dim_height', 'dim_width', 'dim_length',
    'loc_x', 'loc_y', 'loc_z', 'rotation_y'
]

classes = {'Car': 0,
 'Pedestrian': 1,
 'Van': 2,
 'Cyclist': 3,
 'Truck': 4,
 'Misc': 5,
 'Tram': 6,
 'Person_sitting': 7}

def convertToYoloBBox(bbox, size):
    # Yolo uses bounding bbox coordinates and size relative to the image size.
    # This is taken from https://pjreddie.com/media/files/voc_label.py .
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (bbox[4] + bbox[6]) / 2.0
    y = (bbox[5] + bbox[7]) / 2.0
    w = bbox[6] - bbox[4]
    h = bbox[7] - bbox[5]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (str(x),' ', str(y), ' ', str(w), ' ', str(h), '\n')

for idx in range(21):
    file = f"train/images/{idx:06d}.png"
    y = pd.read_csv(f'kitti_label/{idx:06d}.txt', sep=' ', header=None)
    y.columns = label_cols
    print(classes[y.iloc[0, :][0]])
    for j in range(y.shape[0]):
        print(y.shape)
        label = [str(classes[y.iloc[0, :][0]]), ' ']
        label += convertToYoloBBox(y.iloc[j, :], Image.open(file).size)
        print(label)

    path = f'train/labels/{idx:06d}.txt'
    f = open(path, 'w')
    f.writelines(label)
    f.close()