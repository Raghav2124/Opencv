import cv2 as cv
import numpy as np 
blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)
#1 we will paint the image with a certain colour 
# blank[200:300,300:400]=0,255,0
# cv.imshow('Green',blank)
#Draw a rectangle 
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)

cv.imshow('Rectangle',blank)
#Draw a circle 
cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)
#write text in image
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

# img=cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)
cv.waitKey(0)
