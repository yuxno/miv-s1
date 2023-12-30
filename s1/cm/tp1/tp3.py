import cv2 as cv
import numpy as np
from math import inf

point1, point2 = None, None
img1 = cv.imread('image072.png')
img2 = cv.imread('image092.png')

def get_coordinates(event, x, y, flags, params):
    global point1, point2

    if event == cv.EVENT_LBUTTONDOWN:
        point1 = (x, y)

    if event == cv.EVENT_RBUTTONDOWN:
        point2 = (x, y)

    if point1 is not None and point2 is not None:
        cv.rectangle(img1, point1, point2, (0, 0, 255), 2)

cv.namedWindow('Image')
cv.setMouseCallback('Image', get_coordinates)

while True:
    cv.imshow('Image', img1)

    key = cv.waitKey(1) & 0xFF

    if point1 is not None and point2 is not None:
        break

print(point1, point2)

x, y = point1[0], point1[1]
w, h = point2[0] - point1[0], point2[1] - point1[1]
k = 50

r1 = img1[y:y+h, x:x+w]
min_mse = inf
cords = None

for i in range(y - k, y + k + 1):
    for j in range(x - k, x + k + 1):
        if i >= 0 and j >= 0 and i + h < img2.shape[0] and j + w < img2.shape[1]:
            r2 = img2[i:i+h, j:j+w]
            mse = np.sum((r2 - r1) ** 2) / float(w * h)
            if min_mse > mse:
                min_mse = mse
                cords = (j, i)

print(cords, min_mse)

cropped_region = img2[cords[1]:cords[1]+h, cords[0]:cords[0]+w]
cv.imshow('Cropped Region', cropped_region)

cv.rectangle(img2, (cords[0] - k, cords[1] - k), (cords[0] + k + w, cords[1] + k + h), (0, 255, 0), 2)
cv.rectangle(img2, point1, point2, (0, 0, 255), 2)
cv.rectangle(img2, cords, (cords[0] + w, cords[1] + h), (255, 0, 0), 2)

cv.imshow('Image', img2)
cv.waitKey(0)
cv.destroyAllWindows()
