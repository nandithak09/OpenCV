#Mirroring Video multiple times
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    width = int(cap.get(3)) #cap.get(3) returns the width of the frame
    height= int(cap.get(4)) #cap.get(4) returns the height of the frame
    # Create a black image with the same size as the frame
    black_image = np.zeros(frame.shape, np.uint8)
    smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5) # Resize the frame to half its original size
    black_image[:height//2,:width//2]= cv2.rotate(smaller_frame,cv2.ROTATE_180)# Place the smaller frame in the top-left corner of the black image
    black_image[height//2:,:width//2]=smaller_frame # Place the smaller frame in the bottom-left corner of the black image
    black_image[:height//2,width//2:]= cv2.rotate(smaller_frame,cv2.ROTATE_180) # Place the smaller frame in the top-right corner of the black image
    black_image[height//2:,width//2:]=smaller_frame # Place the smaller frame in the bottom-right corner of the black image

    cv2.imshow('frame', black_image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()