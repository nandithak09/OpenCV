import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # Detect corners using Shi-Tomasi corner detection method
# The parameters are:
# - gray: The input image in grayscale
# - 100: The maximum number of corners to return
# - 0.01: The quality level, which is a parameter for the corner detection algorithm
# - 10: The minimum distance between detected corners
corners = corners.astype(int)

#circle the corners and draw lines between them
for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
# Draw a circle at each corner with a radius of 5 pixels and color (255, 0, 0) (blue in BGR format)
# The -1 thickness means the circle is filled
# Draw lines between all pairs of corners

for i in range(len(corners)):
	for j in range(i + 1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()