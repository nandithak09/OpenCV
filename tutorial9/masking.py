#Masking = focus on specific parts of data while ignoring others

import cv2 as cv
import numpy as np

img = cv.imread('images/cat2.jpg') 
#cv.imshow("cat", img)  

blank = np.zeros(img.shape[:2], dtype = "uint8")
#cv.imshow("blank", blank) 

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)  # Create a circular mask
#cv.imshow("Mask", mask)  

masked = cv.bitwise_and(img, img, mask=mask)  # Apply the mask to the image
cv.imshow("Masked Image", masked)  

cv.waitKey(0)