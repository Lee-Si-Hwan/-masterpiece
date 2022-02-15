import matplotlib.pyplot as plt
import histogram

def showHistogram(n):
     hist = histogram.load(f'program/Dataset/compare/{n}.histogram')
     for x in range(1,10):
          title=f'image {x}'
          plt.subplot(3,3,x)
          plt.title(title)
          plt.xticks([])
          plt.yticks([])
          plt.plot(hist['histogram'][0][x-1],color='r')
          plt.plot(hist['histogram'][1][x-1],color='g')
          plt.plot(hist['histogram'][2][x-1],color='b')
     plt.show()

# showHistogram(int(input('.histogram file number : ')))

import os
nowDir = os.path.dirname(__file__)
import numpy as np
import cv2
# Image Load

def load_image(title):
    img_array = np.fromfile(title, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#     img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_LINEAR)
    if img is None:
        print("Image not found")
        return None
    return img

def showDenoisedPicture():
     import model
     from noiseRemover import denoise
     pathname = os.path.join(nowDir,'Dataset/data/9.jpg')
     image = load_image(pathname)
     image=denoise(image, 30)
     cv2.imshow('yeah',  image)
     cv2.waitKey(0)

def showHSVHistogram():
     hist = histogram.load('program/Dataset/compare/2.histogram')

     #import model
     #image = model.load_image('program/testData/12.1.png')
     #H,S,V = model.make_histogram(image)

     plt.plot(hist['histogram'][0][5], label='H', color='r')
     plt.show()
     #plt.plot(hist['histogram'][1][1], label='S', color='g')
     #plt.show()
     #plt.plot(hist['histogram'][2][1], label='V', color='b')
     #plt.show()

showHSVHistogram()