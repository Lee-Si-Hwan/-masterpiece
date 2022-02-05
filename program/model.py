import cv2
import numpy as np
from matplotlib import pyplot as plt
import histogram
import math
import os

nowDir = os.path.dirname(__file__)
datasetDir = os.path.join(nowDir,'Dataset')

def makeHist(title):
    img_array = np.fromfile(title, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img = cv2.resize(img,(1000,1000),interpolation=cv2.INTER_LINEAR)
    if img is None:
        print("image not found")
        return None
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    print(len(hsv[0]),len(hsv))
    width=len(hsv[0])
    height=len(hsv)
    hist=list()
    for i in range(1,4):
        for j in range(1,4):
            cutHsv = hsv[int((i-1)*height/3) : int(i*height/3) , int((j-1)*width/3) : int(j*width/3) ]
            #cv2.imshow(f'{i},{j} Image',cutHsv)
            hist.append(cv2.calcHist([cutHsv],[0],None,[180],[0,180]))

    print(len(hist))
    return hist

def makeComparingHist(data,to_compare):
    fig = plt.figure()
    
    hist = histogram.load(os.path.join(nowDir,f'Dataset/compare/{to_compare}.histogram'))
    for x in range(1,10):
        subplot = fig.add_subplot(3,3,x)
        # remove legend of subplot
        subplot.legend_ = None
        subplot.plot(hist[x-1],color="g", label="masterpiece")
        subplot.plot(data[x-1],color="b", label="user")
    return fig

def getSumlist(hist):
    result = list()
    for i in hist:
        result.append(sum(i))
    return result


def findTop(data, length, num): #사진의 대푯값 찾기
    top = sorted(data, reverse = True)
    D = list()
    i = 0
    while len(D)< num:
        what = True
        t = data.index(top[i])
        
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
    test_data=list()
    for asdf in range(0,9):
        test_res = getSumlist(test_hist[asdf])
        test_data.append(findTop(test_res, 10, 4))

    result = list()
    i = 1
    for data in dataSet: #데이터 셋 중에서 한 명화 데이터
        sumAll=0
        j=0
        temp = 0
        chunk_len = 0 #한 명화 데이터의 대푯값 총 개수
        for chunk in data:
            l = 0
            flag = [0,0,0,0]
            userChunk = test_data[j]
            for t in range(len(userChunk)): #내 그림의 한 대푯값
                for d in range(len(chunk)): #한 명화 데이터의 한 대푯값
                    chunk_len += 1#대푯값 개수 더하기
                    if userChunk[t][0] > chunk[d][0] - 10 and userChunk[t][0] < chunk[d][0] + 10 and flag[t] == 0: #해당 명화의 한 대표값을 기준으로 +- 10 범위 안에 드는가
                        if userChunk[t][1] > chunk[d][1] - 10000 and userChunk[t][1] < chunk[d][1] + 10000:
                            temp += 1
                            flag[t] = 1
                            l += (userChunk[t][1]- chunk[d][1])**2
            l = math.sqrt(l/(temp+1))
            sumAll+=l

            j+=1
        avgAll = sumAll/9
        result.append([temp/chunk_len, avgAll, i])######333

        i+=1

    return result, test_hist
    

def findNearest(filepath):
    dataSet = list()
    for i in range(1, 38):
        data=list()
        hist = histogram.load(os.path.join(datasetDir,f"compare/{i}.histogram"))
        for j in range(9):
            res = getSumlist(hist[j])
            
            temp = findTop(res, 10, 4)
            data.append(temp)
        dataSet.append(data)
    result, test_hist = predictiveModel(filepath, dataSet)
    result = sorted(result, reverse = True, key = lambda x : (x[0], -x[1]))
    
    try:
        to_print="Answer : "
        for i in range(10):
            to_print+=str(result[i][2])+', '
    except Exception as e:
        print(e)
    return result, test_hist

def drawResult(data):
    fig = plt.figure()
    for i in range(9):
        img = cv2.imread(os.path.join(datasetDir,f"data/{data[i][2]}.jpg"))
        ax = fig.add_subplot(1, 9, i+1)
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_xticks([]), ax.set_yticks([])
    return fig
