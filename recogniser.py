import numpy as np
import cv2
from mark_attendance import markAttendance


def recogniser():
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read("face_train/trainingdata.yml")
    id="Unknown"
    #cap.set()
    #font=cv2.FONT_HERSHEY_SIMPLEX,5,1,0,4
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,confidence=rec.predict(gray[y:y+h,x:x+w])
            if (confidence < 65):
                id = str(id)
                #confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "Unknown"
                #confidence = "  {0}%".format(round(100 - confidence))
            
            #cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)
        cv2.imshow('img',img)
        markAttendance(id)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()