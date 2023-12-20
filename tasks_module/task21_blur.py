import cv2 as cv


def blur(img_path: str):
    img = cv.imread(img_path)

    result = cv.blur(img, ksize=(10, 10))

    cv.imshow("21_blur", result)
    cv.waitKey()
    return result
