import cv2
import numpy as np
from matplotlib import pyplot as plt
import histogram
import math
def getHist(title):
    hist = histogram.load(title)
    return hist

def makeHist(title):
    print(title)
    img_array = np.fromfile(title, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_LINEAR)
    # img = cv2.imread(title)
    #img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    if img is None:
        print("image not found")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    print(len(hsv[0]),len(hsv))
    width=len(hsv[0])
    height=len(hsv)
    hist=list()
    for i in range(1,4):
        for j in range(1,4):
            cutHsv = hsv[int((i-1)*height/3) : int(i*height/3) , int((j-1)*width/3) : int(j*width/3) ]
            
            hist.append(cv2.calcHist([cutHsv],[0],None,[180],[0,180]))
    print(len(hist))
    return hist

def getSumlist(hist):
    result = list()
    for i in hist:
        result.append(sum(i))
    return result

def drawHist(data, D, test):
    #data = cv2.normalize(data, None, 0, 180, cv2.NORM_INF)
    plt.plot(data)

    
    # for i in D:
    #     plt.scatter(i[0], i[1], c = "g")

    # for i in test:
    #     plt.scatter(i[0], i[1], c = "r")
    
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
    print(len(test_hist))
    test_data=list()
    for asdf in range(0,9):
        print(asdf)
        test_res = getSumlist(test_hist[asdf])

        test_data.append(findTop(test_res, 10, 4))

    result = list()
    i = 1
    for data in dataSet: #데이터 셋 중에서 한 명화 데이터
        sumAll=0
        j=0
        temp = 0
        for chunk in data:
            l = 0
            flag = [0,0,0,0]
            userChunk = test_data[j]
            for t in range(len(userChunk)): #내 그림의 한 대푯값
                for d in range(len(chunk)): #한 명화 데이터의 한 대푯값
                    if userChunk[t][0] > chunk[d][0] - 12 and userChunk[t][0] < chunk[d][0] + 12 and flag[t] == 0: #해당 명화의 한 대표값을 기준으로 +- 10 범위 안에 드는가
                        if userChunk[t][1] > chunk[d][1] - 12 and userChunk[t][1] < chunk[d][1]:
                            temp += 1
                            flag[t] = 1
                            l += (userChunk[t][1]- chunk[d][1])**2
            l = math.sqrt(l/(temp+1))
            sumAll+=l

            j+=1
        avgAll = sumAll/9
        result.append([temp, avgAll, i])
        print("temp:",temp)

        i+=1

    #print(result)
    return result
    

def findNearest(filepath):
    dataSet = list()
    for i in range(1, 39):
        data=list()
        for j in range(1,10):
            hist = getHist(f"Dataset/compare/{i}-{j}.histogram")
            res = getSumlist(hist)
            
            temp = findTop(res, 10, 4)
            data.append(temp)
        dataSet.append(data)
        #drawHist(res, temp)
    result = predictiveModel(filepath, dataSet)
    result = sorted(result, reverse = True, key = lambda x : (x[0], -x[1]))
    #print(result)
    
    
    try:
        for i in range(10):
            print("answer:")
            print(', ', result[i][2])

       
    except Exception as e:
        print(e)
    return (result)

def drawResult(data):
    fig = plt.figure()
    for i in range(9):
        img = cv2.imread(f"Dataset/data/{data[i][2]}.jpg")
        ax = fig.add_subplot(1, 9, i+1)
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_xticks([]), ax.set_yticks([])
    plt.show()
#################################
    
    # test_hist = makeHist("test7.png")
    # test_res = getSumlist(test_hist)
    # test_data = findTop(test_res, 6, 4)
    
    # hist = getHist("Dataset/compare/17.jpg.histogram")
    # res = getSumlist(hist)
    
    
    # drawHist(res, normalize(dataSet[16]), normalize(test_data))


