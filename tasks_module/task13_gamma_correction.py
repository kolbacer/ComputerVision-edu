import cv2 as cv
import numpy as np


def gamma_correction(img_path: str, gamma: float = 2.5):
    img = cv.imread(img_path)

    table = [((i / 255) ** (1 / gamma)) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    result = cv.LUT(img, table)

    cv.imshow("13_gamma_correction", result)
    cv.waitKey()
    return result
