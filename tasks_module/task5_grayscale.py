import cv2 as cv


def grayscale(img_path: str):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    cv.imshow('4_grayscale', img)
    cv.waitKey()
    return img
