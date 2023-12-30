import cv2
import numpy as np

def region_growing(binary_img, seed_point, threshold):
    stack = []
    segment = []

    # Convert the seed_point to a tuple, as cv2.imread returns a NumPy array
    seed_point = tuple(seed_point)
    
    stack.append(seed_point)
    segment.append(seed_point)

    while stack:
        current_pixel = stack.pop()
        neighbors = get_neighbors(current_pixel, binary_img.shape)

        for neighbor in neighbors:
            if is_valid(neighbor, segment) and should_add_to_segment(neighbor, binary_img, threshold, seed_point):
                stack.append(neighbor)
                segment.append(neighbor)

    return segment

def get_neighbors(current_pixel, shape):
    neighbors = []
    x, y = current_pixel

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < shape[0] and 0 <= new_y < shape[1]:
                neighbors.append((new_x, new_y))

    return neighbors

def is_valid(neighbor, segment):
    if neighbor not in segment:
        return True
    return False

def should_add_to_segment(neighbor, binary_img, threshold, seed_point):
    x, y = neighbor
    seed_value = binary_img[x, y]
    return np.abs(seed_value - binary_img[seed_point]) <= threshold


def main():
    binary_img = cv2.imread('TP2/fig1.png', cv2.IMREAD_GRAYSCALE)
    
    # Define the seed point and threshold
    seed_point = (0, 0)  # Replace with the coordinates of your seed point
    threshold = 10  # Adjust the threshold value as needed

    # Perform region growing
    segment = region_growing(binary_img, seed_point, threshold)
    print("Segment size:", len(segment))

if __name__ == "__main__":
    main()
