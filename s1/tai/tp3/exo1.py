import cv2
import numpy as np

def convolution(img_matrix, filter_kernel):
        result_matrix = np.zeros_like(img_matrix)
        filter_size = filter_kernel.shape[0]

        img_rows, img_cols = img_matrix.shape

        for i in range(img_rows - filter_size + 1):
                for j in range(img_cols - filter_size + 1):
                        img_patch = img_matrix[i:i+filter_size, j:j+filter_size]
                        result_matrix[i, j] = np.sum(img_patch * filter_kernel)

        return result_matrix

img = cv2.imread("TAI TP3\image1.png", cv2.IMREAD_GRAYSCALE)
img_matrix = np.array(img)

#the filters
filter_kernel1 = np.array([[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]])

filter_kernel2 = np.array([[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1]])

filter_kernel3 = np.array([[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 0],
                          [0, 1, 1, 1, 0],
                          [0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0]])

filter_kernel4 = np.array([[0, 0, 0, 0, 0],
                          [0, 0.5, 0.5, 0.5, 0],
                          [0, 0.5, 0.5, 0.5, 0],
                          [0, 0.5, 0.5, 0.5, 0],
                          [0, 0, 0, 0, 0]])

result1 = convolution(img_matrix, filter_kernel1)
result2 = convolution(img_matrix, filter_kernel2)
result3 = convolution(img_matrix, filter_kernel3)
result4 = convolution(img_matrix, filter_kernel4)


cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image 1", result1)
cv2.imshow("Filtered Image 2", result2)
cv2.imshow("Filtered Image 3", result3)
cv2.imshow("Filtered Image 4", result4)

cv2.waitKey(0)
cv2.destroyAllWindows()











# import cv2
# import numpy as np

# img = cv2.imread("TAI TP3\image1.png", cv2.IMREAD_GRAYSCALE)
# img_matrix = np.array(img)

# filter_kernel1 = np.array([[0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0],
#                           [0, 0, 1, 0, 0],
#                           [0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0]])

# filter_kernel2 = np.array([[0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 0],
#                           [0, 0, 0, 0, 1]])

# filter_kernel3 = np.array([[0, 0, 0, 0, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 0, 0, 0, 0]])

# filter_kernel4 = np.array([[0, 0, 0, 0, 0],
#                           [0, 0.5, 0.5, 0.5, 0],
#                           [0, 0.5, 0.5, 0.5, 0],
#                           [0, 0.5, 0.5, 0.5, 0],
#                           [0, 0, 0, 0, 0]])


# # Create an empty matrix for the result
# result_matrix = np.zeros_like(img_matrix)

# # Manually perform convolution
# img_rows, img_cols = img_matrix.shape
# filter_size = filter_kernel1.shape[0]

# for i in range(img_rows - filter_size + 1):
#         for j in range(img_cols - filter_size + 1):
#                 img_patch = img_matrix[i:i+filter_size, j:j+filter_size]
#                 result_matrix[i, j] = np.sum(img_patch * filter_kernel1)

# # Display the images
# cv2.imshow("Original Image", img)
# cv2.imshow("Filtered Image", result_matrix)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
