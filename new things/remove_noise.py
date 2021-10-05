import cv2
import matplotlib.pyplot as plt

def denoising_img(img, h):
    rm_noise_img = cv2.fastNlMeansDenoisingColored(img, None, h,h,7,21)
    return rm_noise_img

def denoise(image,strength):
    dimg = denoising_img(image, strength)
    return dimg

