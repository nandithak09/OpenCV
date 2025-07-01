import cv2 as cv
import matplotlib.pyplot as plt     

img = cv.imread('images/cat2.jpg')
cv.imshow("cat", img)

#plt.imshow(img)  # Display the image using matplotlib
#plt.show()
#gives the image in RGB format, but OpenCV uses BGR format by default

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

#hsv to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)

cv.waitKey(0)