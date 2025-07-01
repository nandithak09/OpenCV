#In open cv bitwise operations are used to perform pixel-wise operations on images.and between images and masks.
"""
bitwise_and : Performs a bitwise AND operation between two images or an image and a mask.
bitwise_or : Applies a logical OR operation between two images or an image and a mask.
bitwise_xor : Performs a bitwise XOR operation between two images or an image and a mask.
bitwise_not : Inverts the pixel values of an image or a mask.
"""
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")  # Create a blank image
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)  # Draw a filled rectangle
#(30,30) is the cordinates of rectangle
#(370,370) size of rectangle
circle = cv.circle (blank.copy(),(200,200),200,255,-1)
#(200,200) is the center of circle
#200 is the radius of circle
cv.imshow("Rectangle", rectangle)  # Show the rectangle
cv.imshow("Circle", circle)  # Show the circle

# Bitwise AND operation
bitwise_and = cv.bitwise_and(rectangle, circle)  
cv.imshow("Bitwise AND", bitwise_and) 
#took both the images and give out the intersection of both images
  
# Bitwise OR operation
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)
#took both the images and gave out the union of both images

# Bitwise XOR operation
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)
#took both the images and gave out the difference of both images

# Bitwise NOT operation
bitwise_not_rectangle = cv.bitwise_not(rectangle)
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT Rectangle", bitwise_not_rectangle)
cv.imshow("Bitwise NOT Circle", bitwise_not_circle)

cv.waitKey(0)