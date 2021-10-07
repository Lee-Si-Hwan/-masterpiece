   
import cv2, numpy as np
import matplotlib.pylab as plt
from noiseRemover import *
import histogram


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
    #histogram.save(''+filename+'.histogram',hist)

    plt.plot(hist)
    plt.show()
    
try:

    for x in range(1,1):
        print(str(x)+' : processing started...')
        hist2D('Dataset/data/'+str(x)+'.jpg')

        print('\tfinished processing '+str(x))
except:
    print("something is wierd.")
    input()