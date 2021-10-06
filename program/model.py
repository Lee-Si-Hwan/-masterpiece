import cv2
import numpy as np
from matplotlib import pyplot as plt
import histogram
import math

def getHist(title):
    hist = histogram.load(title)
    return hist

def makeHist(title):
    img = cv2.imread(title)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    hist = cv2.calcHist([img], [0,1], None, [180, 256], [0, 180, 0, 256])

    return hist

def getSumlist(hist):
    result = list()
    for i in hist:
        result.append(sum(i))
    return result

def drawHist(data, D, test):
    #data = cv2.normalize(data, None, 0, 180, cv2.NORM_INF)
    #plt.plot(data)

    
    for i in D:
        plt.scatter(i[0], i[1], c = "g")

    for i in test:
        plt.scatter(i[0], i[1], c = "r")
    
    plt.show()
    
    
def findTop(data, length, num): #사진의 대푯값 찾기
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

def normalize(data): #정규화 함수
    nomz = list()
    for j in range(len(data)): 
        nomz.append(data[j][1])
    k = max(nomz)

    for j in range(len(data)): #D 정규화
        data[j][1] /= k

    return data

def predictiveModel(testTitle, dataSet):
    test_hist = makeHist(testTitle)
    
    test_res = getSumlist(test_hist)

    test_data = findTop(test_res, 10, 4)
    
    result = list()
    i = 1
    for data in dataSet: #데이터 셋 중에서 한 명화 데이터
        temp = 0
        l = 0
        flag = [0,0,0,0]
        for t in range(len(test_data)): #내 그림의 한 대푯값
            for d in range(len(data)): #한 명화 데이터의 한 대푯값
                if test_data[t][0] > data[d][0] - 12 and test_data[t][0] < data[d][0] + 12 and flag[t] == 0: #해당 명화의 한 대표값을 기준으로 +- 10 범위 안에 드는가
                    temp += 1
                    flag[t] = 1
                    l += (test_data[t][1]- data[d][1])**2
        l = math.sqrt(l/(temp+1))
        result.append([temp, l, i])
        i+=1

    #print(result)
    return result
    

if __name__ == "__main__":
    dataSet = list()
    for i in range(1, 38):
        hist = getHist(f"Dataset/compare/{i}.jpg.histogram")
        res = getSumlist(hist)
        
        temp = findTop(res, 10, 4)
        
        print(temp)
        dataSet.append(temp)
        #drawHist(res, temp)
    result = predictiveModel("test7.png", dataSet)
    result = sorted(result, reverse = True)
    print(result)

    top = result[0][0] #3
    real_res = list()
    i = 0
    while result[i][0] == top:
        real_res.append(result[i])
        i+=1
    print("답:",real_res[len(real_res)-1][2], real_res[len(real_res)-2][2], real_res[len(real_res)-3][2])

#################################3
    
    test_hist = makeHist("test7.png")
    test_res = getSumlist(test_hist)
    test_data = findTop(test_res, 6, 4)
    
    hist = getHist("Dataset/compare/17.jpg.histogram")
    res = getSumlist(hist)
    
    
    drawHist(res, normalize(dataSet[16]), normalize(test_data))


