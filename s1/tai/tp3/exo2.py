import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("TAI TP3/image2.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sigma_values = [10, 20, 70]

plt.figure(figsize=(10, 5))

for i, sigma in enumerate(sigma_values, 1):

    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), sigmaX=sigma)

    plt.subplot(1, len(sigma_values), i)
    plt.imshow(blurred_img, cmap='gray')
    plt.title(f'Sigma = {sigma}')

plt.show()
