import cv2 as cv
import numpy as np


def change_brightness(img_path: str, brightness_offset: float = 0):
    img = cv.imread(img_path)

    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(img_hsv)
    v_new = v.astype(np.int16) + brightness_offset
    v_new = np.clip(v_new, 0, 255).astype(np.uint8)

    img_new = cv.merge((h, s, v_new))
    result = cv.cvtColor(img_new, cv.COLOR_HSV2BGR)

    cv.imshow("11_change_brightness", result)
    cv.waitKey()
    return result
