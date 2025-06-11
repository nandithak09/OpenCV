#Colors and Color Detection

#Convert BGR to HSV

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  # Convert BGR to HSV color space
    lower_blue=np.array([90,50,50])
    upper_blue=np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)  # Apply the mask to the original frame



    #mask= part of an image.It tells us which part of the image we want to work with, It tells which part of an image is ther in the range of lowerbound and upper bound
    #we compare pixel by pixel and mask tells this particular pixel is blue and we keep it if its not then we make it black.

    cv2.imshow('frame',result)
    cv2.imshow('mask',mask)  # Display the mask

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()  # Close all OpenCV windows
