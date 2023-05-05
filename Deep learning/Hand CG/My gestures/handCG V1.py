import cv2
import numpy as np
import mediapipe
import autopy

cam = cv2.VideoCapture(0)

initHand = mediapipe.solutions.hands

mainHand= initHand.Hands()

draw = mediapipe.solutions.drawing_utils

wScr , hScr = autopy.screen.size()

pX, pY = 0, 0

cX, cY = 0, 0

def handLandmarks(colorImg):

    landmarkList = []

    landmarkPositions = mainHand.process(colorImg)

    landmarkCheck = landmarkPositions.multi_hand_landmarks

    if landmarkCheck:
        for hand in landmarkCheck:
            for index, landmark in enumerate(hand.landmark):
                draw.draw_landmarks(img, hand, initHand.HAND_CONNECTIONS)
                h, w, c = img.shape
                centerX, centerY = int(landmark.x * w) , int(landmark.y * h)
                landmarkList.append([index, centerX, centerY])

    return landmarkList


def fingers(landmarks):
    fingerTips = []
    tipIds = [4, 8, 12, 16, 20] 

    if landmarks[tipIds[0]][1]> landmarks[tipIds[0] - 1][1] :
        fingerTips.append(1)
    else:
        fingerTips.append(0)
        #print(fingerTips)

    for id in range (1,5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)

    return fingerTips

while True:

    check, img = cam.read()        
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lmList = handLandmarks(imgRGB)
    print(lmList)


    if len (lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        finger = fingers(lmList)

        if finger[1] == 1 and finger[2] == 0:
            x3 = np.interp(x1, (0, 640), (0, wScr))
            y3 = np.interp(y1, (0, 480), (0, hScr))

            cX = pX + (x3 - pX) / 7
            cY = pY + (y3 - pY) / 7

            autopy.mouse.move(wScr-cX, cY)
            pX, pY = cX, cY

        if finger[1] == 1 and finger[0] == 0 :
            autopy.mouse.click()


    cv2.imshow('cam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()

