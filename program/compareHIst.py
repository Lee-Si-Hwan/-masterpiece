   
import cv2, numpy as np
import matplotlib.pylab as plt

def compareImg(hist1,hist2):
    res = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return res
