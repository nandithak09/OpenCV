import cv2 as cv

img = cv.imread('images/cat2.jpg')
cv.imshow("cat", img)

resized = cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC)  # Resize the image to 300x300 pixels using cubic interpolation
#cv.imshow('Resized', resized)

#flipping
flip = cv.flip(img,-1) # Flip the image vertically (0 for vertical, 1 for horizontal, -1 for both)
#cv.imshow('Flipped', flip)  # Show the flipped image

# Cropping
crop = img[50:200, 100:300]  # Crop the image from y=50 to y=200 and x=100 to x=300
cv.imshow('Cropped', crop)  # Show the cropped image

cv.waitKey(0)