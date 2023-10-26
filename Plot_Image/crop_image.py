import cv2

# Load the image
image_path = "messi.png"
image = cv2.imread(image_path)

# Define the coordinates of the region you want to crop
# Format: (startY:endY, startX:endX)
y1, y2, x1, x2 = 50, 250, 100, 300

# Crop the image
cropped_image = image[y1:y2, x1:x2]

# Extract the Red channel
# OpenCV represents images in BGR format (not RGB)
# Blue: blue_channel = image[:, :, 0]
# Green: green_channel = image[:, :, 1]
# Red: red_channel = image[:, :, 2]
red_channel = cropped_image[:, :, 2]

# If you want to visualize it as a red image (with green and blue channels set to zero)
red_colored_image = cropped_image.copy()
red_colored_image[:, :, 0] = 0  # Set blue channel to 0
red_colored_image[:, :, 1] = 0  # Set green channel to 0
red_colored_image[:, :, 2] = red_channel  # Set red channel


# Save the cropped image
# cv2.imwrite("cropped_image.jpg", cropped_image)

# Optionally, display the cropped image
cv2.imshow("Cropped Image", cropped_image)
cv2.imshow("Cropped Red Image", red_colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
