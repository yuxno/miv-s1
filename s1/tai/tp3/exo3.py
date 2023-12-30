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

        return result_matrix



img=cv2.imread("TAI TP3/image2.png",cv2.IMREAD_GRAYSCALE)
img_matrix = np.array(img)



gaussian_k=np.array([
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
])

gaussian_non_2D=gaussian_k* [1/256]
result = convolution(img_matrix, gaussian_non_2D)

gaussian_y=np.array ([
    [1],
    [4],
    [6],
    [4],
    [1]
])

gaussian_x=np.array([1,4,6,4,1])

gaussian_y=(1/256)*gaussian_y

gaussian_2D=gaussian_x*gaussian_y

result2 = convolution(img_matrix, gaussian_2D)

# image_filter_2D=cv2.filter2D(img,-1,gaussian_2D)
# image_filter_non_2D=cv2.filter2D(img,-1,gaussian_non_2D)

cv2.imshow("og", img)
cv2.imshow("2d", result2)
cv2.imshow("not 2d", result)

cv2.waitKey()
cv2.destroyAllWindows()




# conv_img=convolu(gfdgfd)

# img_with_border = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_CONSTANT)
