import cv2 as cv
import numpy as np


def erosion(img_path: str):
    img = cv.imread(img_path)

    kernel = np.ones((5, 5), 'uint8')
    result = cv.erode(img, kernel, iterations=1)

    cv.imshow("24_erosion", result)
    cv.waitKey()
    return result
