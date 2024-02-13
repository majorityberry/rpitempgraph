import sqlite3
import time
import sys

def main():
    Conn = sqlite3.connect(str(sys.argv[1]))
    Cur = Conn.cursor()
    Temp_File=open("/sys/class/thermal/thermal_zone0/temp")

    Cur.execute("CREATE TABLE IF NOT EXISTS TEMP (ID INT PRIMARY KEY NOT NULL,TEMP INT NOT NULL,TIME INT NOT NULL);")#添加表

    Cur.execute("SELECT ID FROM TEMP ORDER BY ID DESC LIMIT 0,1;")
    Id=Cur.fetchone()
    if Id == None:
        Next_Id = 0
    else:
        Next_Id = int(Id[0])+1
    Temp = int(Temp_File.read())
    Time = time.time()
    
    Cur.execute("INSERT INTO TEMP (ID,TEMP,TIME) VALUES (?,?,?)",(Next_Id,Temp,Time) )#主要操作

    Conn.commit()#收尾工作
    Conn.close()
    Temp_File.close()
main()
