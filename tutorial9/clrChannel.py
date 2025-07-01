import cv2 as cv
import numpy as np

img = cv.imread('images/pic.jpg')
cv.imshow("Original Image", img)

b,g,r = cv.split(img)  # Split the image into its blue, green, and red channels
cv.imshow("Blue Channel", b)  # Show the blue channel
cv.imshow("Green Channel", g)  # Show the green channel
cv.imshow("Red Channel", r)  # Show the red channel

merged = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)  # Merge the channels back together and show the result

cv.waitKey(0)