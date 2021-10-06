import cv2
import numpy as np
from matplotlib import pyplot as plt
from noiseRemover import *
import histogram
import compareHist

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
    print("PROCESSING  "+filename)
    img = cv2.imread(filename)
    print("denoising...")
    img=denoise(img, 30)
    print("denoising...finished")
    cv2.imshow("denoised image",img)
    hsvmap = HSVmap()

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv],[0],None,[180],[0,180])
    
    #histogram.save(filename+'.histogram',hist)
    return hist
    


def compareWith(masterpieceName,userHist):
    hist=histogram.load(masterpieceName+'.histogram')
    return compareHist.compareImg(hist,userHist)


def findNearestImg(fileName):
    hist=hist2D(fileName)
    max=0
    maxIndex=0
    for x in range(1,38):
        tmp = compareWith('data/'+x+'.jpg',hist)
        if (tmp>max):
            max=tmp
            maxIndex=x
    return maxIndex

