from model import load_image, make_histogram, extractValidRange, calculate_similarity, ensemble, predict
from noiseRemover import denoise
from os import walk
import os
import math
nowDir = os.path.dirname(__file__)
filenames = next(walk(os.path.join(nowDir,'testData')), (None, None, []))[2]
print(filenames)

result = list()

def arithMean(list):
    return sum(list)/len(list)

def geoMean(list):
    temp = 1
    for i in list:
        temp *= i
    return math.sqrt(temp)

def RMS(list):
    temp = 0
    for i in list:
        temp += i**2
    return math.sqrt(temp/len(list))

from tqdm import tqdm
with tqdm(total = 170) as pbar:
    ratio = 0.1
    while ratio <= 0.9:
        error = 0.001
        while(error <= 0.01):
            #print(f"{ratio} {error}")
            ranklist = list() #전체 테스트 파일에 대한 랭크 리스트
            sumrank = 0 #해당 파라미터에 대한 정확도 평균

            for filename in filenames:
                # print('\t'+filename)
                filepath = os.path.join(nowDir,'testData',filename)
                image = load_image(filepath)
                h, s, v = make_histogram(image)
                real_answer = int(filename.split('.')[0])
                answer = predict(h, s, v,ratio,error,geoMean,RMS) #파라미터 여기서 조절

                rank = None
                for index, i in enumerate(answer):
                    if i[0]==real_answer:
                        rank = index
                        break
                if rank is not None:
                    ranklist.append([filename,rank])
                    sumrank += rank
            sumrank /= len(filenames)
            result.append([sumrank, ratio, error,ranklist])
            error += 0.001
            pbar.update(1)
        ratio += 0.05
    print(result)
    with open('temp2.txt', 'w') as f:
        f.write(str(result))
    input()