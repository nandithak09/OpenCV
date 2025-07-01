import cv2 as cv

img = cv.imread('images/cat2.jpg')
cv.imshow("cat", img)


#Averaging
#Surrounding pixels avregaed is put in the center pixel

average = cv.blur(img,(3,3))
cv.imshow("Average Blurring", average)

#Gaussian Blurring
gaussian = cv.GaussianBlur(img, (3, 3), 0)  # The last parameter is the standard deviation in X and Y direction
cv.imshow("Gaussian Blurring", gaussian)

#Median Blurring
median = cv.medianBlur(img, 3)  # The kernel size must be odd
cv.imshow("Median Blurring", median)

#Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 35, 25)  # The first parameter is the diameter of the pixel neighborhood, 
#the second is the sigma in color space, and the third is the sigma in coordinate space
cv.imshow("Bilateral Blurring", bilateral)
cv.waitKey(0)