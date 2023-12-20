import cv2 as cv


def change_contrast(img_path: str, alpha: float = 1):
    img = cv.imread(img_path)

    result = cv.convertScaleAbs(img, alpha=alpha)

    cv.imshow("12_change_contrast", result)
    cv.waitKey()
    return result
