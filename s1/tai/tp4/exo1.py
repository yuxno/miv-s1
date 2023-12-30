import cv2
import numpy as np

image = cv2.imread('tp4\df.jpg', cv2.IMREAD_GRAYSCALE)

gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

magnitude_gradient = np.sqrt(gradient_x**2 + gradient_y**2)

# Calculer l'orientation du gradient (en degrés)
gradient_orientation = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)

cv2.imshow('Image originale', image)
cv2.imshow('Magnitude du gradient', cv2.normalize(magnitude_gradient, None, 0, 255, cv2.NORM_MINMAX))
cv2.imshow('Orientation du gradient', cv2.normalize(gradient_orientation, None, 0, 255, cv2.NORM_MINMAX))
cv2.waitKey(0)
cv2.destroyAllWindows()


















# filter_x=np.array([[-1,1]],dtype=int)
# filter_y=np.array([[-1],[1]],dtype=int)
# gradient_x=convolution(image,filter_x)
# gradient_y=convolution(image,filter_y)