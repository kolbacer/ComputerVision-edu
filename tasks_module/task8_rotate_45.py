import cv2 as cv


def rotate_45(img_path: str):
    img = cv.imread(img_path)

    (h, w, d) = img.shape
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, 45, 1.0)
    img_rotated = cv.warpAffine(img, M, (w, h))

    cv.imshow('8_rotate_45', img_rotated)
    cv.waitKey()
    return img_rotated
