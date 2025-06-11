#Image Fundamentals and Manipulation

import cv2
import random

img=cv2.imread('Assets/Ganesh.jpg',-1)

print(img.shape) # Print the shape of the image (height, width, channels)
#channels = colorspace of image
#openCV uses BGR color space by default
# when we manipulate the image we modify the pixel values in the BGR color space

#changing pixel colors

'''for i in range(100):
    for j in range(img.shape[1]):
        img[i][j]= [ random.randint(0,255),random.randint(0,255),random.randint(0,255)]'''

# This code changes the color of the first 100 rows of the image to random colors
# The pixel values are set to random values between 0 and 255 for each channel (B, G, R)
'''cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#random.randint(low,high) generates a random number between low and high (inclusive)


#Copying and pasting specific parts of the image

tag = img[100:200,300:400] #Copy from row 500 to 700 and in that row from column 600 to 900
img[150:250,350:450] = tag #Paste the copied part to a new location in the image
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()