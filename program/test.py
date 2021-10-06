import histogram
import matplotlib.pyplot as plt

hit =  histogram.load('test.png.histogram')
plt.plot(hit)
plt.show()
