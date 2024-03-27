#used to focus on the specific part of image that we want to focus on like a face using the given document 
import cv2 as cv
import numpy as np 
img=cv.imread("Photos/cats.jpg")
cv.imshow('Cat',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("Blank image ",blank)
mask=cv.circle(blank,(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
cv.imshow("Masked image",mask)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked image",masked)
cv.waitKey(0)
  