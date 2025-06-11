# Face and Eye Detection with OpenCV

import cv2
import numpy as np

cap = cv2.VideoCapture(0) 
# Load the pre-trained Haar Cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 

while True:
    ret, frame= cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  # Detect faces
    for(x,y,w,h) in faces: #x,y,w,h because detectMultiScale returns a list of rectangles
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5) # Draw rectangle around the face
        #x+w and y+h are used to get the bottom right corner of the rectangle
        #x and y are the top left corner of the rectangle
        #5 is the thickness of the rectangle

    #If we detect the face we can detect eyes in that region
    roi_gray = gray[y:y+w,x:x+w]#x+w = bottom right corner of the rectangle, y+w = bottom right corner of the rectangle
    roi_color = frame[y:y+h,x:x+w]  # Region of interest for color frame

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)


    cv2.imshow('Frame', frame)  # Display the captured frame
    if cv2.waitKey(1)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()