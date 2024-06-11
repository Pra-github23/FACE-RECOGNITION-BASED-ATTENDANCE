import cv2

def newData():
    f=open("student_data.csv","a+")
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(1)

    id = input('Enter ID:')
    c=1
    for row in f:
        if id in row:
            print('Data Exist')
            c=0
            break
    sampleN=0        
    if c==1:                    
        name = input("Enter Name:")    
    while 1:

        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            sampleN=sampleN+1
cv2.imwrite("dataset/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h,        
                                                                                 x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('img',img)
            cv2.waitKey(1000)

        if sampleN==5:
            break

    f.writelines(f'\n{id},{name}')
    f.close()
    cap.release()

    cv2.destroyAllWindows()