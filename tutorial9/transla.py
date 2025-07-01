import cv2 as cv
import numpy as np

img = cv.imread('images/cat2.jpg')
cv.imshow("cat", img)

#Translation 
# It is the process of shifting an image in the x and y direction.
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # Create a translation matrix
    dimensions = (img.shape[1], img.shape[0])  # Get the dimensions of the image
    return cv.warpAffine(img, transMat, dimensions)  # Apply the translation
translated = translate(img, 100, 100)  # Translate the image by 100 pixels in both x and y direction
#-x = left
#-y = up
#x = right
#y = down
cv.imshow('Translated', translated)
cv.waitKey(0)