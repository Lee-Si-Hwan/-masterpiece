import matplotlib.pyplot as plt
import histogram

def showHistogram(n):
     hist = histogram.load(f'program/Dataset/compare/{n}.histogram')
     for x in range(1,10):
          title=f'image {x}'
          plt.subplot(3,3,x)
          plt.title(title)
          plt.xticks([])
          plt.yticks([])
          plt.plot(hist[x-1])
     plt.show()

showHistogram(int(input('.histogram file number : ')))