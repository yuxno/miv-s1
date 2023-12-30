import cv2 
import numpy as np
from matplotlib import pyplot as plt
import os

color=0
image = cv2.imread('C:/Users/Z-REPAIR INFO/Downloads/silhouette45/nm-02/180/001-nm-02-180-106.png' , color)

##cv2.imshow('img', image) 
white_pixel_coords = np.argwhere(image == 255)

sorted_white_pixel_coords = white_pixel_coords[np.lexsort((white_pixel_coords[:, 0],))]
highest_point = tuple(sorted_white_pixel_coords[0])
lowest_point = tuple(sorted_white_pixel_coords[-1])


image_color=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cv2.circle(image_color, (highest_point[1],highest_point[0]), 2 ,(0,0,255), -1)
cv2.circle(image_color, (lowest_point[1], lowest_point[0]), 2 ,(0,0,255), -1)

cv2.imshow('Image with Circles', image_color)

print("Highest Point:", highest_point)
print("Lowest Point:", lowest_point)

##plt.imshow(image_color)
##plt.show()

cv2.waitKey(0)  ##basically wait infinitly till i click anything key to close the window
cv2.destroyAllWindows()
