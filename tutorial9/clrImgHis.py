import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/cat2.jpg')
cv.imshow("cat", img)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r') 

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])  # Calculate histogram for each color channel
    plt.plot(hist, color=col)  # Plot the histogram for each channel
    plt.xlim([0, 256])  # Set x-axis limits
plt.show()  # Show the plot

cv.waitKey(0) 