import cv2 as cv

img = cv.imread('images/cat2.jpg')
cv.imshow("cat",img)

def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width , height)
    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)
# frame = img that we want to resize.
# dimensions = specify the new size of the img and it should be a tuple.
# interpolation = specifies the interpolation method use to resize the image
# interpolation method determines how the pixel value is calculated when the image is resized.

resized_image = rescaleframe(img)
cv.imshow('resized cat',resized_image)
cv.waitKey(0)
"""
capture = cv.VideoCapture('videos/video1.mp4')
while True:
    isTrue , frame = capture.read()

    frame_resized = rescaleframe(frame, scale=.20)

    cv.imshow('video',frame)
    cv.imshow('video resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()    
"""
