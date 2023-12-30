import cv2
import os
import numpy as np

# Define a function to find the highest point in an image
def find_highest_point(image_path):
    img = cv2.imread(image_path, 0)
    white_pixel_coords = np.argwhere(img == 255)
    
    if white_pixel_coords.any():
        sorted_white_pixel_coords = white_pixel_coords[np.lexsort((white_pixel_coords[:, 0],))]
        highest_point = tuple(sorted_white_pixel_coords[0])
    else:
        highest_point = None

    return highest_point

# Define a function to process images in a directory
def process_images(directory_path):
    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    highest_points = []

    for image in image_files:
        image_path = os.path.join(directory_path, image)
        highest_point = find_highest_point(image_path)

        if highest_point:
            highest_points.append(highest_point)

    if len(highest_points) >= 2:
        # Calculate the center point of all highest points
        avg_highest_point = tuple(np.mean(highest_points, axis=0, dtype=int))


        for image in image_files:
            image_path = os.path.join(directory_path, image)
            img = cv2.imread(image_path)

            # Draw lines to the center point
            cv2.line(img, (avg_highest_point[1], avg_highest_point[0]), (highest_point[1], highest_point[0]), (0, 0, 255), 2)  # Red line

            # Display each image with the lines
            cv2.imshow("Processed Image", img)
            cv2.waitKey(0)
            
    cv2.destroyAllWindows()

# Specify the directory containing your images
image_directory = "tp1/silhouette45"

# Call the function to process the images in the directory
process_images(image_directory)
