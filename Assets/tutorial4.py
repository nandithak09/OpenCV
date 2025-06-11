import cv2
import numpy as np



cap = cv2.VideoCapture(0)  # Open the default camera (0 is usually the default camera index)

while True:
    ret,frame = cap.read()  # Read a frame from the camera
    width=int(cap.get(3))
    height=int(cap.get(4))

    img= cv2.line(frame,(0,0),(width,height),(255,0,0),5)# Draw a blue line from the top-left corner to the bottom-right corner
    img= cv2.line(img,(0,height),(width,0),(0,255,0),5)
    img = cv2.rectangle(img,(100,100),(200,200),(128,128,128),5) #100,100 = center position, 200,200 = radius
    img = cv2.circle(img,(300,300),60,(0,0,255),-1) # Draw a filled red circle at the center of the frame with a radius of 60 pixels
    #300,300 = center position, 60 = radius, (0,0,255) = color in BGR format, -1 = filled circle

    #Draw text on the frame
    font= cv2.FONT_HERSHEY_SIMPLEX  # Define the font type
    img = cv2.putText(img,'I am Great!',(10,height-10),font,2,(0,0,0),5,cv2.LINE_AA)  # Draw text at the bottom of the frame
    #200,height-10 = position of the text, font = font type,4= font scale (0,0,0) = color in BGR format, 5 = line thickness, cv2.LINE_AA = line type

    cv2.imshow('Webcam Feed', img)  # Display the frame in a window named 'Webcam Feed'
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()  # Release the camera when done
cv2.destroyAllWindows()  # Close all OpenCV windows

