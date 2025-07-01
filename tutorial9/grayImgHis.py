#Histogram basicaly allows you to visualize the distribution of pixel intensities in an image.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/cat2.jpg')
cv.imshow("cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")  

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
cv.imshow("Gray", gray)

circle = cv.circle(blank,(img.shape[1]//2 , img.shape[0]//2),100,255,-1)

mask = cv.bitwise_and(gray, gray, mask=circle)  
cv.imshow("Mask", mask)  

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])  # Calculate histogram for the grayscale image
#[gray] is the source image, [0] is the channel index (0 for grayscale), 
# None is the mask, [256] is the number of bins, and [0, 256] is the range of pixel values
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)  # Plot the histogram
plt.xlim([0, 256])  # Set x-axis limits
plt.show()  # Show the plot
