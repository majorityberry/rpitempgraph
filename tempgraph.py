import sqlite3
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
        strTime = time.strftime("%Y-%m-%d\n%H:%M", timeArray)
        Time.append(strTime)

    fig,ax = plt.subplots()
    ax.plot(Time,Temp)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(500))
    #plt.plot(Time,Temp)
    plt.show()
    Conn.close()
main()