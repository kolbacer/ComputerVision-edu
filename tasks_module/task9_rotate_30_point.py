import cv2 as cv


def rotate_30_point(img_path: str, point: (float, float) = (0, 0)):
    img = cv.imread(img_path)

    (h, w, d) = img.shape
    M = cv.getRotationMatrix2D(point, 30, 1.0)
    rotated = cv.warpAffine(img, M, (w, h))
    cv.circle(rotated, point, radius=3, color=(0, 0, 255), thickness=2)

    cv.imshow('9_rotate_30_point', rotated)
    cv.waitKey()
    return rotated
