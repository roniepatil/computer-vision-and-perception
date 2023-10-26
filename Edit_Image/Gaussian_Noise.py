import cv2
import numpy as np

# Gaussian noise is a statistical noise having a probability density function equal to that of the normal distribution 
# (also known as Gaussian distribution). Introducing Gaussian noise to an image can be useful for various purposes, 
# such as testing image processing algorithms.


def addGaussainNoise(image, mean=0, sigma=25):
    rows, cols, ch = image.shape
    gauss = np.random.normal(mean, sigma, (rows, cols, ch))
    gauss = gauss.reshape(rows, cols, ch)
    noisy = image + gauss
    return cv2.convertScaleAbs(noisy)


image = cv2.imread('Edit_Image/messi.png')


noisy_image = addGaussainNoise(image)

# Apply Gaussian filter
gaussian_filtered = cv2.GaussianBlur(noisy_image, (5, 5), 0)

# Apply Bilateral filter
bilateral_filtered = cv2.bilateralFilter(noisy_image, d=9, sigmaColor=75, sigmaSpace=75)

# Non-local Means Denoising
non_local_MD = cv2.fastNlMeansDenoisingColored(noisy_image, None, 10, 10, 7, 21)


cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Gaussian filter", gaussian_filtered)
cv2.imshow("Bilateral filter", bilateral_filtered)
cv2.imshow("Non-local Means Denoising", non_local_MD)
cv2.waitKey(0)
cv2.destroyAllWindows()