#Template Matching and Object Detection

import cv2
import numpy as np
# Load the main image and the template image
img = cv2.imread('Assets/soccer_practice.jpg',0)
template = cv2.imread('Assets/ball.PNG',0)
h,w = template.shape

#Methods for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2= img.copy()

    result = cv2.matchTemplate(img2, template, method)  # Perform template matching
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # Get the minimum and maximum values and their locations
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)  # Calculate the bottom-right corner of the rectangle
    cv2.rectangle(img2, location, bottom_right, 255, 5)  # Draw a rectangle around the detected template
    cv2.imshow('Detected', img2)  # Display the image with the detected template
    cv2.waitKey(0)  # Wait for a key press to continue to the next method
cv2.destroyAllWindows()  # Close all OpenCV windows

