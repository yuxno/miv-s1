import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("TAI TP3/image2.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sigma = 120
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), sigmaX=sigma)

cv2.imshow("og", gray_img)
cv2.imshow("gaussian", blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()








# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(gray_img, cmap='gray')
# plt.title('Original Image')

# plt.subplot(1, 2, 2)
# plt.imshow(blurred_img, cmap='gray')
# plt.title(f'Blurred Image (Sigma = {sigma})')

# plt.show()
