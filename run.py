import cv2
import numpy as np
img = cv2.imread('dog.png')

window = "Window"
# Create a named window
cv2.namedWindow(window)

# Move it to (40,30)
cv2.moveWindow(window, 40, 30)

# Percent of original size
scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Show image
cv2.imshow(window, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
