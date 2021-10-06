import cv2
import numpy as np
from matplotlib import pyplot as plt

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

def hist2D():
    img = cv2.imread('copyPearl.png')
    hsvmap = HSVmap()

    cv2.namedWindow("hist2D", 0)
    cv2.createTrackbar("scale", "hist2D", hscale, 32, onChange)

    while True:
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
        '''
        print(type(hist), hist.shape)
        f = open("lists.txt", "w")
        for i in hist:
            f.write(str(i))
        f.close()
        break
        '''
        
        hist = np.clip(hist*0.005*hscale,0,1)
        hist = hsvmap*hist[:,:,np.newaxis] / 255.0
 
        cv2.imshow('hist2D',hist)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindow()
    

hist2D() 
