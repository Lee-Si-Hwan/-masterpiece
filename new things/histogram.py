def save(filename,hist):
    with open(filename,'wb') as file:
        file.write(bytes(hist))
def load(filename):
    hist=None
    with open(filename,'rb') as file:
        hist=file.read()
    return hist