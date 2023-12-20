import cv2 as cv


def canny_edges(img_path: str):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

    edges = cv.Canny(img, 100, 200)

    cv.imshow('3_canny_edges', edges)
    cv.waitKey()
    return edges
