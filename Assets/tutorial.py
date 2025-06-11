import cv2

# Read the image in grayscale

img = cv2.imread('Assets/Ganesh.jpg',-1)
# The second argument of cv2.imread() specifies the color type of the image
# Possible values for the second argument:

# -1 cv2.IMREAD_COLOR :  Loads a color image. Any transparency of image will be neglected. It is the default flag.
# 0 cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1 cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

#Resize the image to 400x400 pixels

# 1. img = cv2.resize(img, (400,400))

img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) # Resize the image to half its original size


#Rotate the image by 90 degrees clockwise

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg',img)# Save the modified image to a new file

# Display the image in a window named 'Ganesh'

cv2.imshow('Ganesh', img) 
cv2.waitKey(0) # Wait for a key press indefinitely 
# or for a specified amount of time (in milliseconds)
# If 0, it waits indefinitely until a key is pressed
# If a key is pressed, the program continues to the next line

cv2.destroyAllWindows() # Close all OpenCV windows