"""
Created on Sun May 31 15:12:58 2020
@author: Jamal Ali
Email : jamalabdu213@gmail.com

you need to install OpenCV by using this command in the terminal:
pip install opencv-python
"""
import cv2

###########################
frameWidth = 640
frameHeight = 480
nPlateCascade= cv2.CascadeClassifier("Res/haarcascade_russian_plate_number.xml")
minArea = 500
Color = (255,0,255)
count = 0
###########################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,Color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("Roi",imgRoi)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Res/Scan/NoPlate"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count += 1
        
