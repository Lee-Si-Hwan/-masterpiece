from noiseRemover import *
import histogram
import os
import newmodel as model
from tqdm import tqdm

nowDir = os.path.dirname(__file__)

# make data
# 'histogram' : list() [hist_H, hist_S, hist_V]
# 'validrange' : list() [validRange_H, validRange_S, validRange_V]
def makeData(image):
    hist = model.make_histogram(image)
    validRange_H = model.extractValidRange(hist[0])
    validRange_S = model.extractValidRange(hist[1])
    validRange_V = model.extractValidRange(hist[2])
    return {'histogram':hist, 'validrange':[validRange_H, validRange_S, validRange_V]}

def preprocess():
    for num in tqdm(range(38),desc='preprocessing'):
        image = model.load_image(os.path.join(nowDir,'Dataset/data/'+str(num)+'.jpg'))
        image=denoise(image, 30)
        hist = makeData(image)
        histogram.save(os.path.join(nowDir,f'Dataset/compare/{num}.histogram'),hist)

preprocess()