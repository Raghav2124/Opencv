import cv2 as cv 
img=cv.imread("license.jpeg")
cv.imshow('Lady',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
haer_=cv.CascadeClassifier('haer_faces.xml')
faces_rect=haer_.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
print(f'Number of faces found={len(faces_rect)}')


for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)