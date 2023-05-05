import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images.jpg')

#pixels size MUST BE ODD INT#

a = 3 

####filter_level####
g = 5 

m = 5

b1 = 9
b2= 75
#######

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

###noise_Reduction###
#averaging = cv2.blur(gray, (a, a)) #averaging_mean_img_pixels#

#gblur = cv2.GaussianBlur(gray, (g, g), 0) #filter_center_img# #0 = sigmaX# 

median = cv2.medianBlur(gray, m) #filter_salt_paper_img#

#bilateral = cv2.bilateralFilter(gray, b1, b2, b2) #filter_edges#

cv2.imshow('img you want',img)
#cv2.imshow('averaging', averaging)
#cv2.imshow('gblur', gblur)
cv2.imshow('median', median)
#cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()


