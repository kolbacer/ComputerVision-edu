import tasks_module as task

img_path = "./images/cat.jpg"

task.orb_features(img_path)
task.sift_features(img_path)
task.canny_edges(img_path)
task.hsv(img_path)
task.grayscale(img_path)
task.flip_right(img_path)
task.flip_bottom(img_path)
task.rotate_45(img_path)
task.rotate_30_point(img_path, (100, 300))
task.move_right_10(img_path)
task.change_brightness(img_path, 100)
task.change_contrast(img_path, 3)
task.gamma_correction(img_path, 2.5)
task.histogram_equalize(img_path)
task.white_balance_warm(img_path, 20)
task.white_balance_cold(img_path, 40)
task.change_palette(img_path, (30, 50, -40))
task.binarization(img_path)
task.binarization_contours(img_path)
task.sobel_contours(img_path)
task.blur(img_path)
task.fourier_filter_high(img_path)
task.fourier_filter_low(img_path)
task.erosion(img_path)
task.dilation(img_path)
