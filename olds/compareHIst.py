   
import cv2, numpy as np
import matplotlib.pylab as plt



def getHist(img, myimg):
    img1 = cv2.imread(img)
    img2 = cv2.imread(myimg)
    hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    hist1 = cv2.calcHist([hsv1],[0,1],None,[180,256],[0,180,0,256])

    hsv2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
    hist2 = cv2.calcHist([hsv2],[0,1],None,[180,256],[0,180,0,256])

    return hist1, hist2


def compareImg():
    hist1, hist2 = getHist("noisehat1.png", "copyPearl.png")
    res = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    print(res)

compareImg()
