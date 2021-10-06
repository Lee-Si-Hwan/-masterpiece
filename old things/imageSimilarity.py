import cv2
import matplotlib.pyplot as plt

colors = ['b','g','r']
def createHist(image):
    bgr=cv2.split(image)
    for (data,color) in zip(bgr, colors):
        hist = cv2.calcHist([data],[0],None,[256],[0,255])
        plt.plot(hist, color=color)

    plt.show()
a=input()
b = cv2.imread(a)
createHist(b)
