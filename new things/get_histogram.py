import cv2
import numpy as np
from matplotlib import pyplot as plt
from remove_noise import *
import histogram

hscale = 0

def onChange(x):
    global hscale

    hscale = x

def HSVmap():
    hsvmap = np.zeros((180, 256, 3), np.uint8)
    h, s = np.indices(hsvmap.shape[:2])

    hsvmap[:,:,0] = h
    hsvmap[:,:,1] = s
    hsvmap[:,:,2] = 255

    hsvmap = cv2.cvtColor(hsvmap, cv2.COLOR_HSV2BGR)

    return hsvmap
scale=1
def hist2D(filename):
    img = cv2.imread(filename)
    print("denoising...")
    img=denoise(img, 30)
    print("denoising...finished")
    hsvmap = HSVmap()

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv],[0],None,[180],[0,180])
    
    histogram.save(filename+'.histogram',hist)
    plt.plot(hist)
    plt.show()
    
k=input()
hist2D('../img/'+k)
