   
import cv2, numpy as np
import matplotlib.pylab as plt
from remove_noise import *
import histogram

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
    if img is None:
        print("img load error : "+filename)
        return
    print('\tdenoising...')
    img=denoise(img, 30)
    print("\tdenoising finished")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv],[0],None,[180],[0,180])
    histogram.save('result/'+filename+'.histogram',hist)
    
try:

    for x in range(1,38):
        print(str(x)+' : processing started...')
        hist2D('data/'+str(x)+'.jpg')

        print('\tfinished processing '+str(x))
except:
    print("something is wierd.")
    input()