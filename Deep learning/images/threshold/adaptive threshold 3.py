import cv2
import numpy as np

level_M= 100

level_G= 90

img = cv2.imread('images1.jpg',0)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)

cv2.imshow('Original',img)

Ath = cv2.adaptiveThreshold(img, level_M, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
Ath2 = cv2.adaptiveThreshold(img, level_G, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#cv2.createTrackbar('level', 'Ath', 0, 255, any)
#cv2.createTrackbar('level', 'Ath2', 0, 255, any)
#switch = '0 : OFF\ n 1 : ON'
#cv2.createTrackbar(switch,'image' , 0, 1, None )

#resized=cv2.resize(img, (450,450))    ####resizing img####
#cv2.imshow('MTH1',resized)

cv2.imshow('MTH',Ath)
cv2.imshow('GTH',Ath2)
cv2.waitKey(0)
cv2.destroyAllWindows()