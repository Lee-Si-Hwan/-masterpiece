import numpy as np
import matplotlib.pyplot as plt
import random
import math

masterPieces = {"1": [[100,100], [150, 100], [120, 150], [120, 210]],
       "2": [[130,100], [170, 130], [125, 160], [112, 190]]}

def length(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1]))

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
    print("[눈1,눈2,코,입]:",data)
    num = list()
    for dots in masterPieces.values():
        temp = 0
        for i in range(len(data)):
            temp += length(dots[i], data[i])
        num.append(temp)

    print(num.index(min(num)))
    
    
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
    plt.show()


    
