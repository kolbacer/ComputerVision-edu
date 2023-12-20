import cv2 as cv


def histogram_equalize(img_path: str):
    img = cv.imread(img_path)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_equalized = cv.equalizeHist(img_gray)

    cv.imshow("14_histogram_equalize", img_equalized)
    cv.waitKey()
    return img_equalized
