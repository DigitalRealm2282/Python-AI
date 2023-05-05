import cv2
import HandTrackingModule as htm

cam = cv2.VideoCapture(0)

cam.set(3, 1080)

cam.set(4, 720)

detector =  htm.handDetector(detectionCon=0.7)

while True :
    success, img = cam.read()

    hands, img = detector.findHands(img)
    
    img1 = cv2.imread('images.jpg')
    
    if len(hands)==2:
        print("Zoom Gesture")
        print(detector.fingersup (hands[0]), detector.fingersup(hands[1]))
     
    img[10: 260 , 10: 260]= img1
    cv2.imshow('Hands', cam)
    cv2.waitKey(1)
    