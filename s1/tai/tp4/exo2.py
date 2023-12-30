import cv2
import numpy as np

def laplacian_pixel(img, x, y):
    laplacian_mask = np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])

    # extrating 3x3 parts bech nhsbo
    region = img[x-1:x+2, y-1:y+2]

    laplacian_value = np.sum(region * laplacian_mask)

    return laplacian_value

image = cv2.imread('tp4/df.jpg', cv2.IMREAD_GRAYSCALE)

laplacian_image = np.zeros_like(image, dtype=np.float32)

for x in range(1, image.shape[0]-1):
    for y in range(1, image.shape[1]-1):
        laplacian_image[x, y] = laplacian_pixel(image, x, y)

# to fit the vamlues between 0 and 255 TO MAKE THEM VISIVLE
laplacian_image = cv2.normalize(laplacian_image, None, 0, 255, cv2.NORM_MINMAX)

laplacian_image = np.uint8(laplacian_image)

cv2.imshow('Image originale', image)
cv2.imshow('Laplacian Image', laplacian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
