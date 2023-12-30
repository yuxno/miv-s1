import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("TP2/grayscale.png",0)

histogram=np.zeros(256,dtype=int)  #return n array of 256 case of zeros

height, width=img.shape
for y in range(height):
    for x in range(width):
        freq=img[y,x]
        histogram[freq]+=1

plt.bar(range(256), histogram, color='b', alpha=0.7)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Histogram')
seuil = 128  # Change this value to your desired threshold

# Apply thresholding
thresholded_image = (img > seuil).astype(np.uint8) * 255

# Display the thresholded image
plt.figure()
plt.imshow(thresholded_image, cmap='gray')
plt.title(f'Thresholded Image (Seuil={seuil})')
plt.show()