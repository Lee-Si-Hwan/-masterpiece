from model import load_image, make_histogram, extractValidRange, calculate_similarity, ensemble, predict
from noiseRemover import denoise

image = load_image("program/Dataset/data/8.jpg")
image=denoise(image, 30)
h, s, v = make_histogram(image)
print(h)
print(extractValidRange(h[0]))
print(predict(h, s, v))