import cv2 
import numpy as np

image=cv2.imread("TP2/fig3.png")

size = image.shape  
m = size[0] #rows
n = size[1]  #column
label=np.ones([m,n])
for i in range(m):
    for j in range(n):
        if image[i,j]==[0]:#bg
            label[i,j]=0
            


