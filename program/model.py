from re import L
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import histogram
import math

nowDir = os.path.dirname(__file__)

# return masterpieces histograms as list
def get_masterpieces():
    masterpiece_num = 131
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
def extractValidRange(histogram, ratio = 0.8, error = 0.01):
    area = 0
    standard = sum(histogram)*ratio
    cutline = max(histogram)//2
    temp = max(histogram)//2

    #binary search
    while abs(area-standard) > standard * error:
        area = 0
        temp = temp//2
        for i in histogram:
            if i > cutline:
                area += i-cutline
            else:
                    continue
        if area > standard:
            cutline += temp
        else:
            cutline -= temp
        if temp == 0:
            break
    # plt.plot(histogram)
    # plt.plot([cutline for x in range(len(histogram)) if True])
    # plt.show()
    validRange = list()
    for index, y in enumerate(histogram):
        if y > cutline:
            validRange.append(index)
    return validRange

            
# return as similarity percent
# histogram : np.array(), valid_range: list(), to_compare: np.array(), to_compare_valid_range: list()
def calculate_similarity(histogram, valid_range, to_compare, to_compare_valid_range):
    if len(histogram)!=len(to_compare):
        print("histogram length is not same")
        return 0
    
    intersection = 0
    for value in valid_range:
        if value in to_compare_valid_range:
            intersection += 1
    similarity = intersection / len(valid_range) * 100
    return similarity


# ensemble all similarity
# a,b,c = list
def ensemble(h, s, v):
    return math.sqrt(h*s*v)
    # return (h+s+v) /3

def arithMean(list):
    return sum(list)/len(list)

def geoMean(list):
    temp = 1
    for i in list:
        if i == 0:
            continue
        else:
            temp *= i
    return (temp)**(1/len(list))


# compare with histogram
# return rank list
def predict(hist_H, hist_S, hist_V,ratio=0.8,error=0.01, ensemble_func = geoMean, ensemble_func2 = geoMean):
    rank = list()

    validRange_H = list()
    validRange_S = list()
    validRange_V = list()
    for chunk in range(9):
        validRange_H.append(extractValidRange(hist_H[chunk],ratio,error))
        validRange_S.append(extractValidRange(hist_S[chunk],ratio,error))
        validRange_V.append(extractValidRange(hist_V[chunk],ratio,error))
        
    for index, masterpiece in enumerate(get_masterpieces()):
        similarity_H=list()
        similarity_S=list()
        similarity_V=list()
        for chunk in range(9):
            similarity_H.append(calculate_similarity(hist_H[chunk], validRange_H[chunk], masterpiece['histogram'][0][chunk], masterpiece['validrange'][0][chunk]))
            similarity_S.append(calculate_similarity(hist_S[chunk], validRange_S[chunk], masterpiece['histogram'][1][chunk], masterpiece['validrange'][1][chunk]))
            similarity_V.append(calculate_similarity(hist_V[chunk], validRange_V[chunk], masterpiece['histogram'][2][chunk], masterpiece['validrange'][2][chunk]))

        avg_H = ensemble_func2(similarity_H)
        avg_S = ensemble_func2(similarity_S)
        avg_V = ensemble_func2(similarity_V)
        similarity = ensemble_func([avg_H, avg_S, avg_V])
        rank.append([index, similarity, avg_H, avg_S, avg_V])
    rank.sort(key=lambda x:x[1], reverse=True)
    return rank

def use_model(title):
    image = load_image(title)
    hist_H, hist_S, hist_V = make_histogram(image)
    return predict(hist_H, hist_S, hist_V)