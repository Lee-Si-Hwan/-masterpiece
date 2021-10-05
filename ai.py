import numpy as np
import matplotlib.pyplot as plt
import random
import math

masterPieces = {"귀에 붕대를 감은 자화상":[[358, 456], [605, 456], [526, 516], [526, 616]],
                "진주 귀걸이를 한 소녀": [[375, 477], [495, 477], [437, 519], [435, 619]],
                "젊은 여인의 초상":[[386, 333], [279, 333], [346, 376], [343, 476]],
                "원숭이와 함께 한 자화상": [[402, 412], [281, 412], [353, 435], [351, 535]]}

def resizeCoordinates(data):
    eye1,eye2,nose,mouth=data
    asdf=length(nose,mouth)
    asdf=100/asdf
    for x in range(4):
        for y in range(2):
            data[x][y]*=asdf
            data[x][y]=int(data[x][y])
    
    return data


def length(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def lengthSquare(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


def make(dot):
    x = dot[2][0]
    y = dot[2][1]
    for i in range(len(dot)):
        dot[i][0] -= x
        dot[i][1] -= y
    return dot

def score(data):
    data=resizeCoordinates(data)
    print("[눈1,눈2,코,입]:",data)
    num = list()
    for dots in masterPieces.values():
        temp = 0
        for i in range(len(data)):
            temp += lengthSquare(dots[i], data[i])
        temp=math.sqrt(temp)
        num.append(temp)

    num.sort()
    for i in range(len(num)):
        print(list(masterPieces.keys())[num.index(num[i])])
    result=(list(masterPieces.keys())[num.index(num[0])]) #예측 결과 출력
    print("yeah yeeyeah")
    print(result)
    
    '''
    for i in masterPieces.values():
        make(i)
        colors = [random.random(), random.random(), random.random(), 1]
        for j in i:
            x, y = j[0], j[1]
            plt.scatter(x, y, color = colors, marker = "x")
    make(data)

    for j in data:
        x, y = j[0], j[1]
        plt.scatter(x, y, color = [0,0,0], marker = "^")
    plt.xlim([-256, 256])      # X축의 범위: [xmin, xmax]
    plt.ylim([-256, 256])     # Y축의 범위: [ymin, ymax]
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()'''
    return result
    
