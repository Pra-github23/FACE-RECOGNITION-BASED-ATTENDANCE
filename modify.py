import os
import csv

def modify():
    f=open("student_data.csv","r")
    f1=open("temp.csv","w",newline="")
    os.system('cls')
    id = input("Enter the ID:")
    there = 0
    for row in f:
        if id in row:
            there+=1
    if there == 1:
        os.system('cls')
        print("\t************************MODIFY************************")
        print('\n\n\n')
        print("[1] Edit Name.")
        print("[2] Delete Record.")
        print('\n\n\n')
        choice=int(input('Enter choice:'))
        if choice==1:
            a=[]
            reader=csv.reader(f)
            f.seek(0)
            for row in reader:
                if row[0]==id:
                   
                    print("Presious Name:{0}".format(row[1]))
                    name=input("Enter Name:")
                    row[1]=name
                a.append(row)
            writer=csv.writer(f1)
            for x in a:
                writer.writerow(x)    
            old='temp.csv'
            newf='student_data.csv'
            f.close()
            os.remove('student_data.csv')
            f1.close()
            os.rename(old,newf)
            k=input("Press Enter:")
                
        if choice==2:  
            for row in f:
                if id in row:
                    continue
                f1.writelines(row)            
            old='temp.csv'
            newf='student_data.csv'
            f.close()
            os.remove('student_data.csv')
            f1.close()
            os.rename(old,newf)
            k=input("Press Enter:")
    else:
        print("No Data Exist!....")
        k=input("Press Enter:")