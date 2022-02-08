import cv2, numpy as np
import matplotlib.pylab as plt
from noiseRemover import *
import histogram
import os
import newmodel
import tqdm

nowDir = os.path.dirname(__file__)

scale=1
def normalizePicture(image):
    return cv2.resize(image,dsize=(1000,1000),interpolation=cv2.INTER_LINEAR)

def hist2D(filenamea):
    filename=os.path.join(nowDir,'Dataset/data/'+str(filenamea)+'.jpg')
    img = cv2.imread(filename)
    if img is None:
        print("img load error : "+filename)
        return
    print('\tdenoising...')
    img=normalizePicture(img)
    
    img=denoise(img, 30)
    print("\tdenoising finished")


    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    
def preprocess():
    for num in tqdm(range(38),desc='preprocessing'):
        print(str(num)+' : processing started...')
        image = newmodel.load_image(os.path.join(nowDir,'Dataset/data/'+str(num)+'.jpg'))
        newmodel.make_histogram()
        histogram.save(os.path.join(nowDir,f'Dataset/compare/{num}.histogram'),hist)

        print('\tfinished processing '+str(num))