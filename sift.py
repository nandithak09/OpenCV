import cv2 as cv
import numpy as np

img = cv.imread('Assets/cat2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()

#detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(gray, None)

#draw keypoints on the image
img_with_keypoints = cv.drawKeypoints(img, keypoints, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('SIFT Keypoints', img_with_keypoints)
cv.waitKey(0)
cv.destroyAllWindows()