import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(title):
    img_array = np.fromfile(title, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_LINEAR)
    if img is None:
        print("image not found")
        return None
    return img
 
def make_histogram(image):
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    width=len(hsv[0])
    height=len(hsv)
    hist = list()
    for i in range(1,4):
        for j in range(1,4):
            cutHsv = hsv[int((i-1)*height/3) : int(i*height/3) , int((j-1)*width/3) : int(j*width/3) ]
            hist.append(cv2.calcHist([cutHsv],[0,1],None,[180,256],[0,180,0,256]))
    return hist

plt.plot( make_histogram(load_image('program/Dataset/data/1.jpg'))[1])
plt.show()