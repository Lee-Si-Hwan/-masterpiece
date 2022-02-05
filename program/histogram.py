import pickle
def save(filename,hist):
    print('saving ...')
    with open(filename,'wb') as file:
        pickle.dump(hist, file, pickle.HIGHEST_PROTOCOL)
    print("saved!")

def load(filename):
    hist=None
    with open(filename,'rb') as file:
        hist=pickle.load(file)
    return hist