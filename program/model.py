import cv2
import numpy as np
from matplotlib import pyplot as plt
import histogram

def getHist(title):
    hist = histogram.load(title)
    return hist

def getSumlist(hist):
    result = list()
    for i in hist:
        result.append(sum(i))
    return result

def drawHist(data, D):
    x = list(range(1, 181))
    plt.plot(data)
    for i in D:
        plt.scatter(i[0], i[1], c = "g")
    plt.show()
    
    
def findTop(data, length, num):
    top = sorted(data, reverse = True) #정렬
    D = list()
    i = 0
    while len(D)< num:
        what = True
        t = data.index(top[i])
        #print(t)
        
        for j in range(1, length):
            if t+j < 180:
                if data[t] < data[t+j]:
                    what = False
                    break
            if t-j >=0:
                if data[t] < data[t-j]:
                    what = False
                    break
        if what:
            D.append([t, top[i]])
        if i < 179:
            i += 1
        else:
            break
    return D



if __name__ == "__main__":
    dataSet = list()
    for i in range(1, 38):
        hist = getHist(f"Dataset/compare/{i}.jpg.histogram")
        res = getSumlist(hist)
        temp = findTop(res, 10, 4)
        
        print(temp)
        dataSet.append(temp)
        drawHist(res, temp)
    


