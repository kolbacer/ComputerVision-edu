import cv2 as cv


def flip_right(img_path: str):
    img = cv.imread(img_path)

    img_flipped = cv.flip(img, 1)

    cv.imshow('6_flip_right', img_flipped)
    cv.waitKey()
    return img_flipped
