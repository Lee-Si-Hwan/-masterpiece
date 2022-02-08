from model import load_image, make_histogram, extractValidRange, calculate_similarity, ensemble, predict

image = load_image("program/Dataset/data/8.jpg")
h, s, v = make_histogram(image)
print(h)
print(extractValidRange(h[0]))
print(predict(h, s, v))