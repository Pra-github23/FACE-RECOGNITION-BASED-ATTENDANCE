import os

def showAttendance():
    os.system('cls')
    total=int(input("Enter Total Working days till today:"))
    f=open("attendance.csv", "r")
    f1=open("student_data.csv","r")
    id=input("Enter the ID:")
    there = 0
    for row in f1:
        if id in row:
            there+=1
    if there==1:

        count=0
        for row in f:
            col=row.split(',')
            if col[0]==id:
                count+=1
        percentage = (count/total)*100 
            
        print("ID:",id)
        print("Total working days:",total)
        print("No. of days present:",count)
        print("Attendance percentage:{:.2f}".format(percentage))
        k=input("Press Enter:")
    else :
        print("No Data Exists!....")
        k=input("Press Enter:")