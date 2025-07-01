import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3),dtype = 'uint8')
#cv.imshow('image',blank)
#Paint the image in certain color
#blank[:] = 0,255,0
#blank[200:300,300:400] = 0,0,255
#blank[:] = Select all pixels in the image
#cv.imshow('green',blank)

#cv.rectangle(blank,(0,0),(250,250),(255,0,0), thickness =2)
#cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,0,0), thickness=cv.FILLED)
#cv.imshow('rectangle',blank)

#Draw a circle
#cv.circle(blank,(250,250),40,(0,255,0),thickness=3)
#cv.imshow('circle',blank)

#Draw a line
#cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness = 3)
#cv.imshow('line',blank)

#Write text on the image
cv.putText(blank,'Hello World',(225,225),cv.FONT_HERSHEY_TRIPLEX,1,(255,255,255),thickness=2)
#1 is the font scale
#(225,225) is the position of the text
cv.imshow('text',blank)


cv.waitKey(0)