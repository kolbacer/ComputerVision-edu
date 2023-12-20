import cv2 as cv
import numpy as np


def fourier_filter_high(img_path: str):
    img = cv.imread(img_path)

    dft = np.fft.fft2(img, axes=(0, 1))
    dft_shift = np.fft.fftshift(dft)
    radius = 16
    mask = np.zeros_like(img)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv.circle(mask, (cx, cy), radius, (255, 255, 255), -1)[0]
    mask = 255 - mask
    mask = cv.GaussianBlur(mask, (19, 19), 0)
    dft_shift_masked = np.multiply(dft_shift, mask) / 255
    back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
    img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0, 1))
    result = np.abs(3 * img_filtered).clip(0, 255).astype(np.uint8)

    cv.imshow("22_fourier_filter_high", result)
    cv.waitKey()
    return result
