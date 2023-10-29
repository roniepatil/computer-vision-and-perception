import cv2

import numpy as np


image = cv2.imread('Filtering/messi.png', 0)

# Define the coordinates for cropping (x, y, width, height)
x, y, w, h = 100, 100, 50, 50  # Adjust these values as needed

# Crop the portion of the image to use as template
template = image[y:y+h, x:x+w]

# Perform cross-correlation
# cv2.TM_CCOEFF_NORMED is the method used for matching. It stands for "Normalized Cross-Correlation Coefficient". 
# This method provides a score between -1 and 1, where 1 indicates a perfect match, -1 a perfect inverse match, and 0 no match.
# The result is stored in result, which is essentially a map of similarity scores. 
# Each pixel in result represents the score for the corresponding position of the template over the image.
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# You can also find the location of the best match
# min_val, max_val are the minimum and maximum similarity scores found in the result.
# min_loc, max_loc are the positions (coordinates) of the minimum and maximum values, respectively.
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# The top-left corner of the best match
top_left = max_loc
print(top_left)

# Optionally, you can draw a rectangle around the best match
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_right, 255, 2)  # 255 is the color (white), 2 is the thickness

# Show the result
cv2.imshow('Match', image)
cv2.waitKey(0)
cv2.destroyAllWindows()