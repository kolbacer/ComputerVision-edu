import cv2 as cv


def orb_features(img_path: str):
    img = cv.imread(img_path)

    orb = cv.ORB_create()
    kp, des = orb.detectAndCompute(img, None)
    res = cv.drawKeypoints(img, kp, None, flags=0)

    cv.imshow("1_orb_features", res)
    cv.waitKey()
    return res
