import cv2
import numpy as np

img = cv2.imread('images.png',0)
cv2.imshow('img',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


Ath = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 111, 2)
Ath2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 2)
#cv2.createTrackbar('level', 'Ath', 0, 255, any)
#cv2.createTrackbar('level', 'Ath2', 0, 255, any)
#switch = '0 : OFF\ n 1 : ON'
#cv2.createTrackbar(switch,'image' , 0, 1, None )

cv2.imshow('img3',Ath)
cv2.imshow('img4',Ath2)
cv2.waitKey(0)
cv2.destroyAllWindows()