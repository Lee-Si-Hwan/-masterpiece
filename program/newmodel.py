import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import histogram

nowDir = os.path.dirname(__file__)

# return masterpieces histograms as list
def get_masterpieces_histogram():
    masterpiece_num = 38
    masterpieces = list()
    for x in range(masterpiece_num):
        masterpieces.append(histogram.load(os.path.join(nowDir, f'Dataset/compare/{x}.histogram')))
    return masterpieces

# Image Load
def load_image(title):
    img_array = np.fromfile(title, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_LINEAR)
    if img is None:
        print("Image not found")
        return None
    return img


# Cut and Make Histogram
def make_histogram(image):
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    print(hsv)
    width=len(hsv[0])
    height=len(hsv)
    hist_H = list()
    hist_S = list()
    hist_V = list()
    for i in range(1,4):
        for j in range(1,4):
            cutHsv = hsv[int((i-1)*height/3) : int(i*height/3) , int((j-1)*width/3) : int(j*width/3) ]
            hist_H.append(cv2.calcHist([cutHsv],[0],None,[180],[0,180]))
            hist_S.append(cv2.calcHist([cutHsv],[1],None,[256],[0,256]))
            hist_V.append(cv2.calcHist([cutHsv],[2],None,[256],[0,256]))
    return hist_H, hist_S, hist_V


# return as list
# histogram : np.array()
def extractValidRange(histogram):
    
    pass

# return as similarity percent
# histogram : np.array(), valid_range: list(), to_compare: np.array() as valid range
def calculate_similarity(histogram, valid_range, to_compare):

    pass


# ensemble all similarity
def ensemble(a, b, c):
    return (a+b+c)/3

# compare with histogram
def predict(hist_H, hist_S, hist_V):
    validRange_H = extractValidRange(hist_H)
    validRange_S = extractValidRange(hist_S)
    validRange_V = extractValidRange(hist_V)

    highest_similarity_index=0
    highest_similarity=0
    for index, masterpiece in enumerate(get_masterpieces_histogram()):
        masterpiece
        similarity_H = calculate_similarity(hist_H, validRange_H, masterpiece[0])
        similarity_S = calculate_similarity(hist_S, validRange_S, masterpiece[1])
        similarity_V = calculate_similarity(hist_V, validRange_V, masterpiece[2])
        similarity = ensemble(similarity_H, similarity_S, similarity_V)
        if similarity > highest_similarity:
            highest_similarity = similarity
            highest_similarity_index = index
    return highest_similarity_index

