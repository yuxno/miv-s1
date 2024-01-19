import cv2
import numpy as np
import time

def mean_squared_error(block1, block2):
    numerator = np.sum((block1.astype("float") - block2.astype("float")) ** 2)
    denominator = float(block1.size)

    # Check for division by zero
    if denominator == 0:
        return 0  # or any other suitable value

    return numerator / denominator

def logarithmic_search(frame1, frame2, search_parameter, center):
    height, width = frame1.shape

    while search_parameter >= 1:
        positions = center + np.array([(0, 0), (search_parameter, 0), (0, search_parameter),
                                        (-search_parameter, 0), (0, -search_parameter),
                                        (search_parameter // 2, search_parameter // 2),
                                        (-search_parameter // 2, search_parameter // 2),
                                        (-search_parameter // 2, -search_parameter // 2),
                                        (search_parameter // 2, -search_parameter // 2)])

        valid_positions = np.logical_and(positions >= 0, positions < np.array([height, width])).all(axis=1)

        evaluations = []
        for position in positions[valid_positions]:
            block1 = frame1[center[0] - search_parameter // 2:center[0] + search_parameter // 2,
                            center[1] - search_parameter // 2:center[1] + search_parameter // 2]
            block2 = frame2[position[0] - search_parameter // 2:position[0] + search_parameter // 2,
                            position[1] - search_parameter // 2:position[1] + search_parameter // 2]

            # Ensure both blocks have the same size
            block1, block2 = match_block_sizes(block1, block2)

            error = mean_squared_error(block1, block2)
            evaluations.append((position, error))

        # Find the position with the minimum error
        best_match = min(evaluations, key=lambda x: x[1])
        center = best_match[0]

        # Reduce the search parameter
        search_parameter //= 2

    return tuple(center)

def match_block_sizes(block1, block2):
    # Ensure both blocks have the same size
    if block1.shape[0] < block2.shape[0]:
        block2 = block2[:block1.shape[0], :]
    elif block1.shape[0] > block2.shape[0]:
        block2 = np.pad(block2, ((0, block1.shape[0] - block2.shape[0]), (0, 0)), mode='constant')

    if block1.shape[1] < block2.shape[1]:
        block2 = block2[:, :block1.shape[1]]
    elif block1.shape[1] > block2.shape[1]:
        block2 = np.pad(block2, ((0, 0), (0, block1.shape[1] - block2.shape[1])), mode='constant')

    return block1, block2

img1 = cv2.imread("image072.png")
img2 = cv2.imread("image092.png")

result_image = img2.copy()

gray_frame1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_frame2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Calculate the residual frame by subtracting one frame from the other
residual_frame = cv2.subtract(gray_frame2, gray_frame1)

block_size = 16  # Define the block size for block matching
k=32
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
            center = (y_outer + block_size // 2, x_outer + block_size // 2)
            best_match = logarithmic_search(residual_frame, gray_frame2, k, center)

            red_box = [x_outer, y_outer, x_outer + block_size, y_outer + block_size]
            green_box = [best_match[1] - block_size // 2, best_match[0] - block_size // 2,
                         best_match[1] + block_size // 2, best_match[0] + block_size // 2]

            red_area = img1[red_box[1] : red_box[3], red_box[0] : red_box[2]]
            green_area = img2[green_box[1] : green_box[3], green_box[0] : green_box[2]]

            min_mse = float("inf")
            point = None

            for y in range(green_area.shape[0] - block_size + 1):
                for x in range(green_area.shape[1] - block_size + 1):
                    block = green_area[y : y + block_size, x : x + block_size]
                    mse = np.sum(
                        (red_area.astype("float") - block.astype("float")) ** 2
                    )
                    mse /= float(block_size * block_size)
                    if mse < min_mse:
                        min_mse = mse
                        point = (x + green_box[0], y + green_box[1])

            if point is not None:
                cv2.rectangle(
                    img1,
                    (red_box[0], red_box[1]),
                    (red_box[2], red_box[3]),
                    (0, 0, 255),
                    2,
                )
                cv2.rectangle(
                    result_image,
                    (point[0], point[1]),
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
