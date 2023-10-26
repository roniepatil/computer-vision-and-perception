import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'messi.png'
image = cv2.imread(image_path)

# Split the image into RGB channels
r_channel, g_channel, b_channel = cv2.split(image)

# Create meshgrid for 3D plotting
x = np.arange(image.shape[1])
y = np.arange(image.shape[0])
x, y = np.meshgrid(x, y)

# Plot the RGB channel intensities in 3D view
fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(x, y, r_channel, cmap='Reds')
ax1.set_title('Red Channel Intensity')

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x, y, g_channel, cmap='Greens')
ax2.set_title('Green Channel Intensity')

ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x, y, b_channel, cmap='Blues')
ax3.set_title('Blue Channel Intensity')

plt.tight_layout()
plt.show()
