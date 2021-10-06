   
import cv2, numpy as np
import matplotlib.pylab as plt

def processHist(img):
    hsv1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv1],[0,1],None,[180,256],[0,180,0,256])
    return hist


def compareImg(img1,hist2):
    hist1 = processHist(img1)
    res = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return res


