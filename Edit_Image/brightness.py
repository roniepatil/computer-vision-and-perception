import cv2
import numpy as np

# Load the image
image_path = "Edit_Image\messi.png"
image = cv2.imread(image_path)

# Convert image to float32 for processing
image_float = image.astype(np.float32)

# Scalar value
scalar_value = 1.5

# Multiply image with scalar
multiplied_image = image_float * scalar_value

# Clip values to stay in 0-255 range
multiplied_image = np.clip(multiplied_image, 0, 255)

# Convert back to uint8 data type
multiplied_image = multiplied_image.astype(np.uint8)

############## Another way to change brightness and constrast #############
# alpha is the contrast value. To lower the contrast, use 0 < alpha < 1. And for higher contrast use alpha > 1.
# beta is the brightness value. A good range for brightness value is [-127, 127]
# multiplied_image = cv2.convertScaleAbs(image, alpha=1, beta=127)
###########################################################################


# Save the multiplied image
# cv2.imwrite("multiplied_image.jpg", multiplied_image)

# Optionally, display the multiplied image
cv2.imshow("Multiplied Image", multiplied_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
