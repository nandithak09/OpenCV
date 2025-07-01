import cv2
import numpy as np

img = cv2.imread('Assets/edgeflower.jpg',0)


##########################################
# Prewitt Edge Detector
prewitt_kernel_x = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
prewitt_kernel_y = np.array([[1, 1, 1],[0, 0, 0],[-1, -1, -1]])

prewitt_x = cv2.filter2D(img, -1, prewitt_kernel_x)
prewitt_y = cv2.filter2D(img, -1, prewitt_kernel_y)
prewitt = prewitt_x + prewitt_y


##########################################
# Roberts Edge Detector
roberts_kernel_x = np.array([[1, 0],[0, -1]])
roberts_kernel_y = np.array([[0, 1],[-1, 0]])

roberts_x = cv2.filter2D(img, -1, roberts_kernel_x)
roberts_y = cv2.filter2D(img, -1, roberts_kernel_y)
roberts = roberts_x + roberts_y


##########################################
# Sobel Edge Detector
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(sobel_x + sobel_y) 


##########################################
# Canny Edge Detector
canny = cv2.Canny(img, 100, 200)
# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Prewitt Edge Detector', prewitt)
cv2.imshow('Roberts Edge Detector', roberts)
cv2.imshow('Sobel Edge Detector', sobel)
cv2.imshow('Canny Edge Detector', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()




