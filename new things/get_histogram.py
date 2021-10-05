import cv2
import numpy as np
from matplotlib import pyplot as plt
from remove_noise import *

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

    hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
    hist = np.clip(hist*0.005*scale,0,1)
    hist = hsvmap*hist[:,:,np.newaxis] / 255.0

    cv2.imshow('hist2D',hist)
    cv2.waitKey(0)
    
k=input()
hist2D('../img/'+k)
