import cv2 as cv
img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur) 

#cascade edge detection
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)
# ret,thresh=cv.threshold(gray,125,255,)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))



cv.waitKey(0)

