import cv2 as cv 
img=cv.imread("Photos/lady.jpg")
cv.imshow('Lady',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
cv.waitKey(0)