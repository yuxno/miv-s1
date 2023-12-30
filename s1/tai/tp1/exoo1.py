import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

folder_path ='C:/Users/Z-REPAIR INFO/Downloads/silhouette45/nm-02/180'

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

count = 0
# Iterate directory
for path in os.listdir(folder_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(folder_path, path)):
        count += 1

lwlin=[]

for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(folder_path, image_file)

    # Load the binary image
    img = cv.imread(image_path, 0)

    high =(-1,-1)
    low=(-1,-1)
    #cv.imshow('fyc-90_3-001', img)
    y = img.shape[0]
    x = img.shape[1]

    for i in range(y):
        for j in range(x):
            if img[i,j]==255 :
                if high == (-1,-1):
                    high = (j,i)
                    lwlin.append(high)
                else: low= (j,i)


    print(high)
    print(low)

    image_color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    cv.circle(image_color,high, 2, (0, 0, 255), -1)
    cv.circle(image_color,low, 2, (0, 0, 255), -1)

   

    plt.imshow(image_color)
    plt.title('new')
    plt.show()


cv.waitKey(0)  ##basically wait infinitly till i click anything key to close the window
cv.destroyAllWindows()

