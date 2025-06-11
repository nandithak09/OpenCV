#Harris Corner Detection

import cv2
import numpy as np

image = cv2.imread('Assets/chessboard.png')
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)  # Apply Harris corner detection
# The parameters are:
# - gray: The input image in grayscale
# - 2: The block size, which is the size of the neighborhood considered for corner detection
# - 3: The aperture parameter for the Sobel operator
# - 0.04: The Harris detector free parameter
dst = cv2.dilate(dst, None)  # Dilate the result to enhance corner points

#Thshold for an optimal value, it may vary depending on the image.
image[dst > 0.01 * dst.max()] = [0, 0, 255]  # Mark corners in red
cv2.imshow('Harris Corners', image)  # Display the image with detected corners
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows