import cv2


detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():

    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detect.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces :

        cv2.rectangle(img, (x, y), (x+w , y+h), (0, 0, 255), 3)

        cv2.imshow('img', img)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

cap.release()
cv2.destroyAllWindows()
        

