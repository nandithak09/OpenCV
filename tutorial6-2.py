#Harris Corner Detection

import cv2
import numpy as np

image = cv2.imread('Assets/chessboard.png')
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)


# Step 1: Compute gradients using Sobel operator
Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in X
Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in Y

# Step 2: Compute products of gradients
Ixx = Ix * Ix  # Gradient product in X
Ixy = Ix * Iy  # Gradient product in X and Y
Iyy = Iy * Iy  # Gradient product in Y

# Step 3: Apply Gaussian filter to smooth the squared gradients
Ixx = cv2.GaussianBlur(Ixx, (3, 3), sigmaX=1)
Iyy = cv2.GaussianBlur(Iyy, (3, 3), sigmaX=1)
Ixy = cv2.GaussianBlur(Ixy, (3, 3), sigmaX=1)

# Step 4: Compute the Harris corner response R
k = 0.04  # Harris detector free parameter
detM = (Ixx * Iyy) - (Ixy ** 2)
traceM = Ixx + Iyy
R = detM - k * (traceM ** 2)

# Step 5: Thresholding and marking corners
R = cv2.dilate(R, None)  # For better visualization
threshold = 0.01 * R.max()
image[R > threshold] = [0, 0, 255]  # Mark corners in red

#dst = cv2.cornerHarris(gray, 2, 3, 0.04)  # Apply Harris corner detection
# The parameters are:
# - gray: The input image in grayscale
# - 2: The block size, which is the size of the neighborhood considered for corner detection
# - 3: The aperture parameter for the Sobel operator
# - 0.04: The Harris detector free parameter
#dst = cv2.dilate(dst, None)  # Dilate the result to enhance corner points

#Threshold for an optimal value, it may vary depending on the image.
#image[R > 0.01 * R.max()] = [0, 0, 255]  # Mark corners in red
cv2.imshow('Harris Corners', image)  # Display the image with detected corners
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows