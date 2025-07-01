import cv2 as cv

img = cv.imread('images/cat2.jpg')

#convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#(7,7) is the kernel size, it should be odd and positive
#cv.imshow('Blur',blur)

#edge cascade
canny = cv.Canny(img,125, 175)
#125 is the lower threshold and 175 is the upper threshold
#cv.imshow('Canny Edges',canny)

#dilating the image
dilated = cv.dilate(canny,(3,3), iterations =3)
#(3,3) is the kernel size, iterations =1 means that the dilation will be applied once
#cv.imshow('Dilated',dilated)

#resizing the image
resized = cv.resize(img, (400,400))
cv.imshow('Resized',resized)

#cropping the image
cropped = img[50:200, 200:400]  # y1:y2, x1:x2
cv.imshow('Cropped', cropped)

cv.waitKey(0)