import matplotlib.pylab as plt
import histogram

def showhist(n):
    hist = histogram.load('Dataset/compare/'+str(n)+'.jpg.histogram')
    plt.plot(hist)
    plt.show()

for n in range(1,39):
    showhist(n)