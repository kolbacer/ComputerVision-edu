import cv2 as cv


def hsv(img_path: str):
    img = cv.imread(img_path)

    img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

    cv.imshow('5_hsv', img_hsv)
    cv.waitKey()
    return img_hsv
