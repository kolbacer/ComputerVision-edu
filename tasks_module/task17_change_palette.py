import cv2 as cv
import numpy as np


def change_palette(img_path: str, palette_diff: (float, float, float) = (0, 0, 0)):
    img = cv.imread(img_path)

    b, g, r = cv.split(img)
    result = cv.merge((
        np.clip((b.astype(np.int16) + palette_diff[2]), 0, 255).astype(np.uint8),
        np.clip((g.astype(np.int16) + palette_diff[1]), 0, 255).astype(np.uint8),
        np.clip((r.astype(np.int16) + palette_diff[0]), 0, 255).astype(np.uint8)
    ))

    cv.imshow("17_change_palette", result)
    cv.waitKey()
    return result
