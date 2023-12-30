import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
rectangle_coords = None

# Mouse callback function
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

    if key == 27:  # Press 'Esc' to exit
        break

if rectangle_coords is not None:
    x1, y1, x2, y2 = rectangle_coords

    # Load the other image
    img2 = cv2.imread("image092.png")

    # Draw the original rectangle on the other image
    cv2.rectangle(img2, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Calculate dimensions for the new rectangle in the other image
    new_x1 = x1 - 30
    new_y1 = y1 - 30
    new_x2 = x2 + 30
    new_y2 = y2 + 30

    # Draw the new rectangle on the other image
    cv2.rectangle(img2, (new_x1, new_y1), (new_x2, new_y2), (0, 255, 0), 2)

    # Loop through positions and calculate MSE
    min_mse = float('inf')
    best_position = None

    # Separate the loops for better clarity
    for y in range(new_y1, new_y2):
        # Loop 1: Extracting regions and calculating MSE
        for x in range(new_x1, new_x2):
            roi_img1 = img[y:y + (y2 - y1), x:x + (x2 - x1)]
            roi_img2 = img2[y:y + (y2 - y1), x:x + (x2 - x1)]
            
            mse = np.sum((roi_img1 - roi_img2) ** 2) / float(roi_img1.shape[0] * roi_img1.shape[1])

            if mse < min_mse:
                min_mse = mse
                best_position = (x, y)

    if best_position is not None:
        # Draw the rectangle with the lowest MSE in blue (same size as the original red rectangle)
        cv2.rectangle(img2, (best_position[0], best_position[1]),
                      (best_position[0] + (new_x2 - new_x1), best_position[1] + (new_y2 - new_y1)), (255, 0, 0), 2)

        print(f"Best Position: {best_position}, Minimum MSE: {min_mse}")

        # Display the image with the rectangles
        cv2.imshow("Other Image with Rectangles", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
