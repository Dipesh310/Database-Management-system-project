from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import dbconnectionproject1 as db

    
def RoomCustomer():
    Rnum=room_num.get()
    
    Label(root,text="customer name",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=1)
    Label(root,text="checkIN",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=2)
    Label(root,text="checkOUT",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=4)
    Label(root,text="Phone-no",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=5)
    
    data=db.Customerdata(Rnum)
                            

    Label(root,text=data[0],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=6,column=1)
    Label(root,text=data[1],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=6,column=2)
    Label(root,text=data[2],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=6,column=4)
    Label(root,text=data[3],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=6,column=5)
    
    



    


  
root=Tk()
root.title("Customer details form")
root.geometry("900x550")
root.config(bg="light blue")
  
Label(root,text="Custromer Information",bg="light blue",fg="red",font=("Courier new",18,"bold")).grid(row=0,columnspan=2)

Label(root,text="RoomNumber",bg="light blue",fg="red",font=("Courier new",12,"bold")).grid(row=1,column=0)
room_num=Entry(root)
room_num.grid(row=1,column=1)

Button(root,text="Check",command=RoomCustomer).grid(row=4,columnspan=1)




