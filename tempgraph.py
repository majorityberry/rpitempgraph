import sqlite3
import time
import matplotlib.pyplot as plt
import sys

def main():
    Conn = sqlite3.connect(str(sys.argv[1]))
    Cur = Conn.cursor()
    Cur.execute("SELECT TEMP,TIME FROM TEMP;")

    Data=Cur.fetchall()
    Temp=[]
    Time=[]
    for row in Data:
        Temp.append(row[0]/1000)
        timeArray = time.localtime(row[1])
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        Time.append(strTime)

    plt.plot(Time,Temp)
    plt.show()
    Conn.close()
main()