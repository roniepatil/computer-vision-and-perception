import cv2
import numpy as np


image = cv2.imread('Filtering/messi.png')

# Define a kernel for convolution (e.g., a simple blur kernel)
kernel = np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]], dtype=np.float32)

kernel /= 9 # Normalize the kernel

# Perform convolution
# Second Argument (-1): This specifies the desired depth of the destination image. By setting it to -1, 
# you're indicating that the output image (after convolution) should have the same depth as the source image. 
# In other words, if the input image is 8-bit, the output will also be 8-bit.
convolved_image = cv2.filter2D(image, -1, kernel)

# Show the result
cv2.imshow('Convolved image', convolved_image)
cv2.waitKey(0)
cv2.destroyAllWindows()