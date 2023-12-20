import cv2 as cv
import numpy as np


def dilation(img_path: str):
    img = cv.imread(img_path)

    kernel = np.ones((5, 5), 'uint8')
    result = cv.dilate(img, kernel, iterations=1)

    cv.imshow("25_dilation", result)
    cv.waitKey()
    return result
