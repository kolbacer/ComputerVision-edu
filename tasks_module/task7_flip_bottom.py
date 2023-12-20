import cv2 as cv


def flip_bottom(img_path: str):
    img = cv.imread(img_path)

    img_flipped = cv.flip(img, 0)

    cv.imshow('7_flip_bottom', img_flipped)
    cv.waitKey()
    return img_flipped
