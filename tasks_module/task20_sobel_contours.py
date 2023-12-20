import cv2 as cv
import numpy as np


def sobel_contours(img_path: str):
    img = cv.imread(img_path)

    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    result = cv.filter2D(img, -1, kernel)

    cv.imshow("20_sobel_contours", result)
    cv.waitKey()
    return result
