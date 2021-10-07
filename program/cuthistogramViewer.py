import matplotlib.pyplot as plt
import histogram

for x in range(1,10):
     title=f'image {x}'
     plt.subplot(3,3,x)
     plt.title(title)
     plt.xticks([])
     plt.yticks([])
     hist = histogram.load(f'Dataset/compare/2-{x}.histogram')
     plt.plot(hist)

# hist = histogram.load(f'Dataset/compare/3-3.histogram')
# plt.plot(hist)
plt.show()