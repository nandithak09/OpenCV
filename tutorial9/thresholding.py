#Thresholding is basically binarizing an image.
#Basically we compare each pixel value with a threshold value 
# and if the pixel value is greater than the threshold value, we set it to 255 (white) otherwise we set it to 0 (black).

import cv2 as cv

img = cv.imread('images/cat2.jpg')
#cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
#cv.imshow("Gray", gray)

# Simple Thresholding
threshold,thresh = cv.threshold(gray,120,255,cv.THRESH_BINARY)  # If pixel value > 120, set to 255 (white), else set to 0 (black)
cv.imshow("Thresholded", thresh)

threshold,thresh_inv = cv.threshold(gray,120,255,cv.THRESH_BINARY_INV)  # Inverse thresholding
cv.imshow("Inverse Thresholded", thresh_inv)

# Adaptive Thresholding
#In adaptive thresholding , the computer calculates the threshold for smaller regions of the image, 
# allowing for different thresholds in different areas.
a_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)  # Mean adaptive thresholding
cv.imshow("Adaptive Thresholding", a_thresh)

cv.waitKey(0)
