   
import cv2, numpy as np
import matplotlib.pylab as plt
from noiseRemover import *
import histogram


scale=1
def normalizePicture(image):
    return cv2.resize(image,dsize=(1000,1000),interpolation=cv2.INTER_LINEAR)

def hist2D(filenamea):
    filename='Dataset/data/'+str(filenamea)+'.jpg'
    img = cv2.imread(filename)
    if img is None:
        print("img load error : "+filename)
        return
    print('\tdenoising...')
    img=normalizePicture(img)
    
    img=denoise(img, 30)
    print("\tdenoising finished")


    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    print(len(hsv[0]),len(hsv))
    width=len(hsv[0])
    height=len(hsv)

    for i in range(1,4):
        for j in range(1,4):
            cutHsv = hsv[int((i-1)*height/3) : int(i*height/3) , int((j-1)*width/3) : int(j*width/3) ]
            
            hist = cv2.calcHist([cutHsv],[0],None,[180],[0,180])
            # plt.plot(hist)
            # plt.title(f'Dataset/compare/{filenamea}-{i*3+j-3}.histogram')
            # plt.show()
            histogram.save(f'Dataset/compare/{filenamea}-{i*3+j-3}.histogram',hist)
            

    #plt.plot(hist)
    #plt.show()
    
try:

    for x in range(1,39):
        print(str(x)+' : processing started...')
        hist2D(x)

        print('\tfinished processing '+str(x))
except Exception as e:
    print("something is wierd.")
    print(e)
    input()
input()