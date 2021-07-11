import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
   
    ret, frame = cap.read()
    imgGrey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGrey,1.1,4)
    #Hand masking
    hsvim = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype = "uint8")
    upper = np.array([20, 255, 255], dtype = "uint8")
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(skinRegionHSV, (2,2))
    ret,thresh = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY)
    cv2.imshow("thresh", thresh)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,1),2)
    cv2.imshow("Horizontal",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()