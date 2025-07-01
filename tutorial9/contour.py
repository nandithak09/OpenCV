import cv2 as cv
import numpy as np

img = cv.imread('Assets/cat2.jpg')
#cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert the image to grayscale
#cv.imshow("gray", gray)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)  # Create a blank image with the same dimensions as the input image

#blur = cv.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur to the grayscale image


#canny = cv.Canny(img, 125,175)#125 = lower threshold, 175 = upper threshold
#cv.imshow("canny",canny)


ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)  # Apply binary thresholding to the grayscale image
#If the intensity of a pixel is greater than 125, it will be set to 255 (white), otherwise it will be set to 0 (black)
cv.imshow("thresh", thresh)  # Show the thresholded image

contours, heirarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)  # Find contours in the image
#cv.RETR_LIST retrieves all contours, cv.CHAIN_APPROX_NONE stores all points of the contour
print(f"Number of contours found: {len(contours)}")  # Print the number of contours found

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contours", blank)  # Draw the contours on the blank image and display it

cv.waitKey(0)