import mysql.connector as mysql
con=mysql.connect(host="localhost",user="root",password="",db="DBMSproject")



def Finddata(PID,PName):
    if(con):
        cursor=con.cursor()
        cursor.execute("Select Sid,SName,Ssalary from Staff,Property where Staff.Pid=Property.Pid and Staff.Pid=%s and Pname=%s",(PID,PName))
        data=cursor.fetchall()
        return data

def Customerdata(Rnum):
    if(con):
        cursor=con.cursor()
        query=f"Select C_name,check_in,check_out,C_phonenumber from Room join Customer on Room.room_number=Customer.room_number and Customer.room_number={Rnum}"
        cursor.execute(query)
        data=cursor.fetchone()
        return data

   
        
