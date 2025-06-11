# Displaying video capture from a webcam using OpenCV

import cv2
import numpy as np
cap = cv2.VideoCapture(0) # Open the default camera (0 is usually the default camera index)
while True:
    ret, frame = cap.read() # Read a frame from the camera
    #ret is a boolean indicating if the frame was read successfully
    cv2.imshow('Webcam Feed', frame) # Display the frame in a window named 'Webcam Feed'
    if cv2.waitKey(1)==ord('q'):
        break
cap.release() # Release the camera when done
cv2.destroyAllWindows() # Close all OpenCV windows