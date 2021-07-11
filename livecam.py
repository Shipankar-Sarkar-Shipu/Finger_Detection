import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)#width id is 3
cap.set(4,480)#height id is 4
# cap(10,100)# brightness id  is 10

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # cv2.imshow('Video', frame)
    imgGrey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    # cv2.imshow('Video_Grey', imgGrey)
    imgBlur=cv2.GaussianBlur(frame,(65,65),0)
    # cv2.imshow('Video_Blur', imgBlur)
    # imgCanny=cv2.Canny(frame,150,150)
    # cv2.imshow('Video', imgCanny)
    imgHor=np.hstack((frame,imgBlur))
    cv2.imshow("Horizontal",imgHor)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()