import cv2 as cv
import numpy as np


def move_right_10(img_path: str):
    img = cv.imread(img_path)

    (h, w, d) = img.shape
    M = np.float32([[1, 0, 10], [0, 1, 0]])
    img_moved = cv.warpAffine(img, M, (w, h))

    cv.imshow('10_move_right_10', img_moved)
    cv.waitKey(0)
    return img_moved
