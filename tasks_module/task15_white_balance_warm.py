import cv2 as cv
import numpy as np


def white_balance_warm(img_path: str, warmth: float = 20):
    img = cv.imread(img_path)

    b, g, r = cv.split(img)
    result = cv.merge((
        np.clip((b.astype(np.int16) - warmth), 0, 255).astype(np.uint8),
        g,
        np.clip((r.astype(np.int16) + warmth), 0, 255).astype(np.uint8)
    ))

    cv.imshow("15_white_balance_warm", result)
    cv.waitKey()
    return result
