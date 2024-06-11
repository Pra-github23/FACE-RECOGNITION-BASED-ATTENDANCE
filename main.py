from face_read import newData
from train import trainImages
from modify import modify
from recogniser import recogniser
from show_attendance import showAttendance
import os

os.system('cls')   
while True:
            
    print()
    print("\t*****************************************************")
    print("\t**********************FACEDANCE**********************")
    print("\t*****************************************************")
    print("[1] New Entry.")
    print("[2] Train Images.")
    print("[3] Recogniser.")
    print("[4] Show Attendance..")
    print("[5] Modify.")
    print("[6] Exit.")
    print()
    
    choice = int(input("Select your choice:"))
    if choice==1:
        newData()
    
    elif choice==2:
        trainImages()

    elif choice==3:
        recogniser()

    elif choice==4:
        showAttendance()

    elif choice==5:
        modify()

    elif choice==6:
        break

    else:
        print("Envalid entry!......")