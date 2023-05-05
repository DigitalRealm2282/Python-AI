import cv2
import numpy as np

cap = cv2.VideoCapture('vtestavi.mp4')

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # *'XVID'

out= cv2.VideoWriter('output2.avi',fourcc,30,(1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    diff = cv2.absdiff(frame1,frame2)

    gray=cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),0)

    _,thresh=cv2.threshold(blur, 60,255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=10)
    
    contours,_=cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900 :
            continue

        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame1,"status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

image= cv2.resize(frame1,(1280,720))

out.write(image)

cv2.imshow("detect", frame1)

frame1=frame2
ret, frame2 = cap.read() 
       
if cv2.waitKey(60) == 27:
  cv2.destroyAllWindows()
  cap.release()
  out.release()