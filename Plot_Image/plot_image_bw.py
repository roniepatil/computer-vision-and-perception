import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'Plot_Image/messi.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# image = cv2.GaussianBlur(image, (15,15), 20)
# Convert the image to black and white
# _, bw_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('Black and White Image', image)
# cv2.imwrite('BW.messi.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot the intensities in 3D view
x = np.arange(image.shape[1])
y = np.arange(image.shape[0])

x, y = np.meshgrid(x, y)
z = image

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='gray')

plt.show()


