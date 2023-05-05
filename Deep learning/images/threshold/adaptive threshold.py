import cv2
import numpy as np

img = cv2.imread('download.jpg',0)

Ath = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)
Ath2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)

cv2.imshow('original', img)
cv2.imshow('MTH',Ath)
cv2.imshow('GTH',Ath2)
cv2.waitKey(0)
cv2.destroyAllWindows()