import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions import hands

cap= cv2.VideoCapture(0) 

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpdraw =  mp.solutions.drawing_utils # To draw the landmarks

cTime=0
pTime=0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)# Hands() function only takes rgb images
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        counter=0
        for handlms in results.multi_hand_landmarks:
            
            cy0,cy1,cy2,cy3,cy4,cy5,cy6,cy7,cy8,cy9,cy10,cy11,cy12,cy13,cy14,cy15,cy16,cy17,cy18,cy19,cy20=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            for id, lm in enumerate(handlms.landmark):
                # print(id, lm)# it is fractional value, where we need pixel value. They are giving ratio of the image
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                # print(id,cx,cy)
                
                exec(f'cy{id}=cy')
            if cy1>cy2>cy3>cy4 and cy4<cy5:
                counter+=1
            if cy5>cy6>cy7>cy8:
                counter+=1
            if cy9>cy10>cy11>cy12:
                counter+=1
            if cy13>cy14>cy15>cy16:
                counter+=1
            if cy17>cy18>cy19>cy20:
                counter+=1
            
        

            



            mpdraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS) # as we are showing img and not imgRGB
        cv2.putText(img, f"Count: {counter}",(320,68),cv2.FONT_ITALIC,1,(255,0,255),2)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    
    cv2.putText(img, str(int(fps)),(20,68),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)

    cv2.imshow("Image",img)

    cv2.waitKey(1)