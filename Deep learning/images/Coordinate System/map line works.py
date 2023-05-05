import cv2
import numpy as np

def EVENT(event, x, y, flags, param) :

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),13, (0,0,255), -1)

        points.append((x, y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (0, 255, 255))
        cv2.imshow('img', img)



img = np.zeros((512, 512, 3),np.uint8)

#cv2.imread('img.jpg', 0)

cv2.imshow('img', img)

points = []

cv2.setMouseCallback('img', EVENT)

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imread('', 0)

#cv2.resize('', 0, 0, 0)

#cv2.cvtColor('', cv2.COLOR_BGR2RGB)

#cv2.VideoCapture(0)

#cv2.cvtColor(cv2.VideoCapture, cv2.COLOR_BGR2RGB)



