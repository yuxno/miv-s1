import cv2
import numpy as np

image_path = "image072.png"
image2_path = "image092.png"
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
img2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)

box_coordinates = []
padding = 50


def draw_rect(event, x, y, flags, param):
    global box_coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        box_coordinates = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        box_coordinates.append((x, y))
        cv2.rectangle(
            img,
            (box_coordinates[0][0], box_coordinates[0][1]),
            (box_coordinates[1][0], box_coordinates[1][1]),
            (0, 0, 255),
            2,
        )
        cv2.rectangle(
            img,
            (box_coordinates[0][0] - padding, box_coordinates[0][1] - padding),
            (box_coordinates[1][0] + padding, box_coordinates[1][1] + padding),
            (0, 255, 0),
            2,
        )

        # Extract red area
        red_box = [
            box_coordinates[0][0],
            box_coordinates[0][1],
            box_coordinates[1][0],
            box_coordinates[1][1],
        ]

        green_box = [
            box_coordinates[0][0] - padding,
            box_coordinates[0][1] - padding,
            box_coordinates[1][0] + padding,
            box_coordinates[1][1] + padding,
        ]

        w_red = red_box[2] - red_box[0]
        h_red = red_box[3] - red_box[1]

        w_green = w_red + 2 * padding
        h_green = h_red + 2 * padding

        print(red_box)
        print((w_red, h_red))
        print(green_box)
        print((w_green, h_green))

        red_area = img[red_box[1] : red_box[3], red_box[0] : red_box[2]]
        green_area = img2[green_box[1] : green_box[3], green_box[0] : green_box[2]]

        min_mse = float("inf")

        for y in range(green_area.shape[0] - h_red):
            for x in range(green_area.shape[1] - w_red):
                block = green_area[y : y + h_red, x : x + w_red]
                mse = np.sum((red_area.astype("float") - block.astype("float")) ** 2)
                mse /= float(w_red * h_red)
                if mse < min_mse:
                    min_mse = mse
                    point = (x + green_box[0], y + green_box[1])

        cv2.rectangle(
            img2,
            point,
            (point[0] + w_red, point[1] + h_red),
            (0, 0, 255),
            2,
        )
        cv2.imshow("image2", img2)


cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_rect)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
