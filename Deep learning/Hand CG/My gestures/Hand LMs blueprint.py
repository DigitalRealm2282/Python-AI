import cv2
import mediapipe
import time

result = cv2.VideoWriter('HandsLM.avi',cv2.VideoWriter_fourcc(*'XVID'), 30, (640, 480))

cam = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(static_image_mode=False)
mpDraw= mediapipe.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
     _, img = cam.read()
    
     RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
     result = hands.process(RGB)
     print(result.multi_hand_landmarks)
     
     if result.multi_hand_landmarks:
         for handLms in result.multi_hand_landmarks:
             for index, lm in enumerate(handLms.landmark):
                 print(index, lm)
                 h, w, c = img.shape
                 cx, cy = int(lm.x*w), int(lm.y*h)
                 print(index, cx, cy)
                 if index == 0:
                     cv2.circle(img, (cx, cy), 9, (150,245,55), cv2.FILLED)
                     print('index = '+str(index))
             
             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
     
     else:
        
        print('Hands not detected')
        
        
     cTime = time.time()
     FPS = 1/(cTime-pTime)
     pTime = cTime
     cv2.putText(img, str(int(FPS)), (15,60), cv2.FONT_HERSHEY_COMPLEX, 3, (0,255,0), 3)
     
     cv2.imshow('Hand LMS', img)
     
     key = cv2.waitKey(1)
     if key == 27:
         break
     
cv2.destroyAllWindows()
cam.release()