import cv2
import numpy as np

img = cv2.imread('CCCC1.jpg')

small = cv2.resize(img, (1080,720)) 

cv2.imshow('image', small)

def click_event (event, x,y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:

       print (x , ',' , y)
       font= cv2.FONT_HERSHEY_SIMPLEX
       strXY = str(x) + ',' + str(y)
       cv2.putText(small, strXY, (x,y), font, .5, (0,255,0), 2)
       cv2.imshow('image',small)

    if event == cv2.EVENT_RBUTTONDOWN:

        blue = small[y, x, 0]
        green = small[y, x, 1]
        red = small[y, x, 2]
        font= cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue)+ ',' + str(green) + ',' + str(red)
        cv2.putText(small, strBGR, (x,y), font, .5, (255,255,0), 2)
        cv2.imshow('image',small)
        



cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()




