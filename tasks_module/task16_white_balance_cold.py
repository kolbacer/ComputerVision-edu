import cv2 as cv
import numpy as np


def white_balance_cold(img_path: str, coldness: float = 20):
    img = cv.imread(img_path)

    b, g, r = cv.split(img)
    result = cv.merge((
        np.clip((b.astype(np.int16) + coldness), 0, 255).astype(np.uint8),
        g,
        np.clip((r.astype(np.int16) - coldness), 0, 255).astype(np.uint8)
    ))

    cv.imshow("16_white_balance_cold", result)
    cv.waitKey()
    return result
