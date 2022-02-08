import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import histogram

nowDir = os.path.dirname(__file__)

# return masterpieces histograms as list
def get_masterpieces():
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
def extractValidRange(histogram, ratio = 0.9, error = 0.01):
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
    plt.plot(histogram)
    plt.plot([cutline for x in range(len(histogram)) if True])
    plt.show()
    return cutline

            
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
    similarity = intersection / len(histogram) * 100
    return similarity


# ensemble all similarity
# a,b,c = list
def ensemble(a, b, c):
    return (sum(a)+sum(b)+sum(c))/3

# compare with histogram
# return rank list
def predict(hist_H, hist_S, hist_V):

    rank = list()
    for index, masterpiece in enumerate(get_masterpieces()):
        similarity_H=list()
        similarity_S=list()
        similarity_V=list()
        for i in range(9):
            validRange_H = extractValidRange(hist_H[i])
            validRange_S = extractValidRange(hist_S[i])
            validRange_V = extractValidRange(hist_V[i])


            similarity_H.append(calculate_similarity(hist_H[i], validRange_H, masterpiece['histogram'][0][i], masterpiece['validrange'][0][i]))
            similarity_S.append(calculate_similarity(hist_S[i], validRange_S, masterpiece['histogram'][1][i], masterpiece['validrange'][1][i]))
            similarity_V.append(calculate_similarity(hist_V[i], validRange_V, masterpiece['histogram'][2][i], masterpiece['validrange'][2][i]))
        similarity = ensemble(similarity_H, similarity_S, similarity_V)
        rank.append([index, similarity])
    rank.sort(key=lambda x:x[1], reverse=True)
    return rank

def use_model(title):
    image = load_image(title)
    hist_H, hist_S, hist_V = make_histogram(image)
    return predict(hist_H, hist_S, hist_V)