import cv2 as cv


def sift_features(img_path: str):
    img = cv.imread(img_path)

    sift = cv.SIFT_create()
    kp = sift.detect(img, None)
    res = cv.drawKeypoints(img, kp, img)

    cv.imshow("2_sift_features", res)
    cv.waitKey()
    return res
