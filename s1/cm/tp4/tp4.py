import cv2
import numpy as np
import time

img1 = cv2.imread("Screenshot (44).png")
img2 = cv2.imread("Screenshot (45).png")

result_image = img2.copy()

# Convert frames to grayscale for simple subtraction
gray_frame1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_frame2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Calculate the residual frame by subtracting one frame from the other
residual_frame = cv2.subtract(gray_frame2, gray_frame1)
residual_frameRGB = cv2.subtract(img2, img1)

block_size = 16  # Define the block size for block matching
padding = 32
threshold = 10  # Set a threshold for matching within blocks

start = time.time()

# Identify blocks and perform block matching
for y_outer in range(block_size, residual_frame.shape[0] - block_size, block_size):
    for x_outer in range(block_size, residual_frame.shape[1] - block_size, block_size):
        # Extract a block from the residual frame
        block = residual_frame[
            y_outer : y_outer + block_size, x_outer : x_outer + block_size
        ]

        # Check the mean value of the block
        mean_value = np.mean(block)

        # If the mean value exceeds the threshold, consider it a match
        if mean_value > threshold:
            red_box = [x_outer, y_outer, x_outer + block_size, y_outer + block_size]

            green_box = [
                x_outer - padding,
                y_outer - padding,
                x_outer + 2 * padding,
                y_outer + 2 * padding,
            ]

            red_area = img1[red_box[1] : red_box[3], red_box[0] : red_box[2]]
            green_area = img2[green_box[1] : green_box[3], green_box[0] : green_box[2]]

            min_mse = float("inf")
            point = None

            for y in range(green_area.shape[0] - block_size):
                for x in range(green_area.shape[1] - block_size):
                    block = green_area[y : y + block_size, x : x + block_size]
                    mse = np.sum(
                        (red_area.astype("float") - block.astype("float")) ** 2
                    )
                    mse /= float(block_size * block_size)
                    if mse < min_mse:
                        min_mse = mse
                        point = (x + green_box[0], y + green_box[1])

            if point != None:
                cv2.rectangle(
                    img1,
                    (red_box[0], red_box[1]),
                    (red_box[2], red_box[3]),
                    (0, 0, 255),
                    2,
                )
                cv2.rectangle(
                    result_image,
                    point,
                    (point[0] + block_size, point[1] + block_size),
                    (255, 0, 0),
                    2,
                )

end = time.time() - start
print(end)

# Display the original image with highlighted matched blocks
cv2.imshow("Image", img1)
cv2.imshow("Image with Matched Blocks", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
