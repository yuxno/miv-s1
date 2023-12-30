import cv2
import numpy as np

image = cv2.imread('tp4\df.jpg', cv2.IMREAD_GRAYSCALE)

laplacian_image = cv2.Laplacian(image, cv2.CV_64F)

laplacian_image = cv2.normalize(laplacian_image, None, 0, 255, cv2.NORM_MINMAX)

laplacian_image = np.uint8(laplacian_image)

cv2.imshow('Image originale', image)
cv2.imshow('Laplacian Image', laplacian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
