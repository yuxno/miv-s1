import cv2
import numpy as np
from math import inf


drawing = False
ix, iy = -1, -1
rectangle_coords = None

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rectangle_coords

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)
        rectangle_coords = (ix, iy, x, y)

img = cv2.imread("image072.png")
cv2.namedWindow("prof ymchi")
cv2.setMouseCallback("prof ymchi", draw_rectangle)

while True:
    cv2.imshow("prof ymchi", img)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  
        break

if rectangle_coords is not None:
    x1, y1, x2, y2 = rectangle_coords  # x1 y1 is top left coords and x2y2 bottom right

    img2 = cv2.imread("image092.png")

    cv2.rectangle(img2, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    new_x1 = x1 - 60
    new_y1 = y1 - 60
    new_x2 = x2 + 60
    new_y2 = y2 + 60

    cv2.rectangle(img2, (new_x1, new_y1), (new_x2, new_y2), (0, 255, 0), 2)

    min_mse = inf
    best_position = None

    for y in range(new_y1, new_y2+1):
        for x in range(new_x1, new_x2+1):
            # new red coords
            region_img1 = img2[y1:y2, x1:x2]  # red region

            neww_x1, neww_y1, neww_x2, neww_y2 = x, y , x +  region_img1.shape[1] , y + region_img1.shape[0]

            region_img2 = img2[new_y1:new_y2, new_x1:new_x2]  # green region

            print("red coords: ", neww_x1, neww_y1, neww_x2, neww_y2)
            print ("green coords: ", new_x1, new_y1, new_x2, new_y2)

            if  new_x1 <= neww_x1 <= new_x2 and new_y1 <= neww_y1 <= new_y2 and new_x1 <= neww_x2 <= new_x2 and new_y1 <= neww_y2 <= new_y2:
                
                region_img1_resized = cv2.resize(region_img1, (region_img2.shape[1], region_img2.shape[0]))

                mse = np.sum((region_img2 - region_img1_resized)**2) / float(region_img1.shape[0] * region_img1.shape[1])
            

                print(f"MSE: {mse}")

                if mse < min_mse:
                    min_mse = mse
                    best_position = (neww_x1, neww_y1, neww_x2, neww_y2)

    if best_position is not None:
        cv2.rectangle(img2, (best_position[0], best_position[1]), (best_position[2], best_position[3]), (255, 0, 0), 2)
        print(f"Best Position: {best_position}, Minimum MSE: {min_mse}")

    cv2.imshow("prof ymchi blazra9", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
