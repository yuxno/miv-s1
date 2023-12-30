import cv2
import numpy as np

def divide_into_blocks(image, block_size):
    height, width = image.shape[:2]
    blocks = []

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image[i:i+block_size, j:j+block_size]
            blocks.append((i, j, block))  # Also store the starting coordinates

    return blocks

# Example usage
image_path1 = 'tp3\image072.png'  # Replace with the actual path to your first image
image_path2 = 'tp3\image092.png'  # Replace with the actual path to your second image

# Load images with error handling
image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

if image1 is None or image2 is None:
    print("Error: One or more images could not be loaded.")
else:
    # Ensure both images have the same dimensions
    min_height = min(image1.shape[0], image2.shape[0])
    min_width = min(image1.shape[1], image2.shape[1])

    image1 = image1[:min_height, :min_width]
    image2 = image2[:min_height, :min_width]

    block_size = 16
    blocks_image1 = divide_into_blocks(image1, block_size)

    # Calculate Absolute Difference for each block and reconstruct the image
    reconstructed_image = np.zeros_like(image1, dtype=np.uint8)

    for i, j, block in blocks_image1:
        # Get the corresponding block from the second image
        block_image2 = image2[i:i+block_size, j:j+block_size]

        # Calculate Absolute Difference between the two blocks
        abs_diff = cv2.absdiff(block, block_image2)

        # Update the reconstructed image using the residual
        reconstructed_image[i:i+block_size, j:j+block_size] = abs_diff

    # Display the original images, reconstructed image, and residual
    cv2.imshow('Original Image 1', image1)
    cv2.imshow('Original Image 2', image2)
    cv2.imshow('Reconstructed Image', reconstructed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
