import os
from noiseRemover import denoise
import histogram
import model
from tqdm import tqdm

nowDir = os.path.dirname(__file__)

# make data
# 'histogram' : list() [hist_H, hist_S, hist_V]
# 'validrange' : list() [validRange_H, validRange_S, validRange_V]
def makeData(image):
    hist = model.make_histogram(image)
    validRange_H=list()
    validRange_S=list()
    validRange_V=list()
    for i in range(9):
        validRange_H.append(model.extractValidRange(hist[0][i]))
        validRange_S.append(model.extractValidRange(hist[1][i]))
        validRange_V.append(model.extractValidRange(hist[2][i]))
    return {'histogram':hist, 'validrange':[validRange_H, validRange_S, validRange_V]}

def preprocess():
    for num in tqdm(range(38),desc='preprocessing'):
        image = model.load_image(os.path.join(nowDir,'Dataset/data/'+str(num)+'.jpg'))
        image=denoise(image, 30)
        hist = makeData(image)
        histogram.save(os.path.join(nowDir,f'Dataset/compare/{num}.histogram'),hist)

preprocess()