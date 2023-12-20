import cv2 as cv


def binarization_contours(img_path: str):
    img = cv.imread(img_path)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, img_bin = cv.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(img_bin.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 0, 255), 2, cv.LINE_AA, hierarchy, 1)

    cv.imshow("19_binarization_contours", img)
    cv.waitKey()
    return img
