from datetime import datetime
from datetime import date
import csv

def markAttendance(name):
    f=open('attendance.csv','r+')
    #reader=csv.reader(f)
    #print(reader)zz
    Date = date.today()
    currentDate=str(Date)
    if name == "Unknown" :
        return
    namelist=[]
    curdate=[]
    
    for row in f:
        col=row.split(',')
        namelist.append(col[0])
        curdate.append(col[2])

    if (name in namelist) and (currentDate in curdate):
        return

    elif name not in namelist or currentDate not in curdate:
        now=datetime.now()
        dtString=now.strftime('%H:%M:%S')
        f.writelines(f'\n{name},{dtString},{currentDate}')
    f.close()