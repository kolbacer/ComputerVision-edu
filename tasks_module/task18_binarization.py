import cv2 as cv


def binarization(img_path: str):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

    ret, result = cv.threshold(img, 127, 255, 0)

    cv.imshow("18_binarization", result)
    cv.waitKey()
    return result
