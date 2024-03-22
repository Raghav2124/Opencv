import cv2 as cv
img=cv.imread('Photos/cats.jpg')#used for reading the image
cv.imshow('Cat',img)
cv.waitKey(0)