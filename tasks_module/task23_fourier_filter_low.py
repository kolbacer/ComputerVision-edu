import cv2 as cv
import numpy as np


def fourier_filter_low(img_path: str):
    img = cv.imread(img_path)

    dft = np.fft.fft2(img, axes=(0, 1))
    dft_shift = np.fft.fftshift(dft)
    radius = 64
    mask = np.zeros_like(img)
    mask = cv.GaussianBlur(mask, (19, 19), 0)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv.circle(mask, (cx, cy), radius, (255, 255, 255), -1)[0]
    dft_shift_masked = np.multiply(dft_shift, mask) / 255
    back_shift_masked = np.fft.ifftshift(dft_shift_masked)
    img_filtered = np.fft.ifft2(back_shift_masked, axes=(0, 1))
    result = np.abs(img_filtered).clip(0, 255).astype(np.uint8)

    cv.imshow("23_fourier_filter_low", result)
    cv.waitKey()
    return result
