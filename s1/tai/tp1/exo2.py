import cv2
import numpy as np
import os

# Define a function to process images
def process_image(image_path, all_highest_points,all_lowest_points):
    # Load and process the image
    img = cv2.imread(image_path, 0)
    white_pixel_coords = np.argwhere(img == 255)

    if white_pixel_coords.any():
        highest_point = tuple(white_pixel_coords[np.argmin(white_pixel_coords[:, 0])])
        lowest_point = tuple(white_pixel_coords[np.argmax(white_pixel_coords[:, 0])])

        # Append the highest point to the list of all highest points
        all_lowest_points.append(lowest_point)
        all_highest_points.append(highest_point)

        

    return all_highest_points

# Define a function to process images in a directory
def process_images_in_directory(directory_path):
    all_highest_points = []
    all_lowest_points=[]

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Adjust the file extensions as needed
                image_path = os.path.join(root, file)
                all_highest_points = process_image(image_path, all_highest_points,all_lowest_points)

    if len(all_highest_points) >= 2:
        # Calculate the center point of all highest points
        avg_highest_point = tuple(np.mean(all_highest_points, axis=0, dtype=int))
        avg_lowest_point = tuple(np.mean(all_lowest_points, axis=0, dtype=int))

        # Draw lines connecting all highest points
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Adjust the file extensions as needed
                    image_path = os.path.join(root, file)
                    img = cv2.imread(image_path, 0)
                    image_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                    for highest_point in all_highest_points:
                        cv2.line(image_color, (avg_highest_point[1], avg_highest_point[0]), (highest_point[1], highest_point[0]), (0, 0, 255), 1)  # Red line

                    for lowest_point in all_lowest_points:
                        cv2.line(image_color, (avg_lowest_point[1], avg_lowest_point[0]), (lowest_point[1], lowest_point[0]), (0, 0, 255), 1)  # Red line

                    # Display the image with circles and lines
                    cv2.imshow('Image with Circles and Lines', image_color)
                    cv2.waitKey(0)

# Specify the base directory where your folder structure is located
base_directory = "tp1/silhouette45/345"

# Call the function to process images in the directory and its subdirectories
process_images_in_directory(base_directory)
cv2.destroyAllWindows()
