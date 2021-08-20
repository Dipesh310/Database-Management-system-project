from tkinter import *
from tkinter import messagebox
import dbconnectionproject1 as db


def PropertyStaff():
    PID=property_id.get()
    PName=property_name.get()
    
    data=db.Finddata(PID,PName)
    Label(root,text="StaffID",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=1)
    Label(root,text="Designation",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=2)
    Label(root,text="Staff Salary",bg="light blue", fg="red", font=("Times New Roman",15,"bold")).grid(row=5,column=4)

    i=6
    for x in data:
        Label(root,text=x[0],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=i,column=1)
        Label(root,text=x[1],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=i,column=2)
        Label(root,text=x[2],bg="light blue", fg="black", font=("Times New Roman",12,"bold")).grid(row=i,column=4)
        i=i+1
    

    

    

root=Tk()
root.title("Staff And Property form")
root.geometry("900x550")
root.config(bg="light blue")

Label(root,text="Property and Staff information",bg="light blue",fg="red",font=("Courier new",18,"bold")).grid(row=0,columnspan=2)

Label(root,text="Property_ID",bg="light blue",fg="red",font=("Courier new",12,"bold")).grid(row=1,column=0)
property_id=Entry(root)
property_id.grid(row=1,column=1)

Label(root,text="Property_Name",bg="light blue",fg="red",font=("Courier new",12,"bold")).grid(row=2,column=0)
property_name=Entry(root)
property_name.grid(row=2,column=1)



Button(root,text="Check",command=PropertyStaff).grid(row=4,columnspan=1)

