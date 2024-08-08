from tkinter import * ; 
from tkinter import Toplevel, messagebox ;
import time ;

root  = Tk(); 
root.title("Student Management System"); 

# Setting the background colour of the app
root.config(bg="orange"); 

# Setting the dimensions of the application
root.geometry("1397x745+79+35"); 

# Add Icons to the application
root.iconbitmap('student.ico'); 

# Restricting the access to change the size of the window
root.resizable(True,False); # => True - Can be changed , False => Cannot be changed


DataEntryFrame = Frame(root,bg="skyblue",relief=RIDGE,borderwidth=2); 
DataEntryFrame.place(x=10,y=110,width=500,height=600);

# **************************** ----------  Function for adding the details  ---------------- *************************************
def addStudent():
    def submitAdd():
        print("Added"); 
    
    addroot= Toplevel(master=DataEntryFrame);  
    addroot.grab_set(); 
    addroot.geometry("470x470+220+200"); 
    addroot.title("Student Management System"); 
    addroot.config(bg="skyblue"); 
    addroot.iconbitmap("Database-Cloud.ico"); 
    addroot.resizable(False,False); 

# ****************************  ---------  Type of data  ------- *************************************
    idLabel = Label(addroot,text="Identity No:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    idLabel.place(x=10,y=10); 
    
    nameLabel = Label(addroot,text="Student Name:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    nameLabel.place(x=10,y=70); 
    
    mobileLabel = Label(addroot,text="Mobile No:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    mobileLabel.place(x=10,y=130); 
    
    emailLabel = Label(addroot,text="Email-Id:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    emailLabel.place(x=10,y=190); 
    
    addressLabel = Label(addroot,text="Address:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    addressLabel.place(x=10,y=250); 
    
    genderLabel = Label(addroot,text="Gender:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    genderLabel.place(x=10,y=310); 
    
    dateOfBirth = Label(addroot,text="Date of Birth:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    dateOfBirth.place(x=10,y=370); 

# **************************** ------------  Adding data of students  -------------- *************************************
    idval = StringVar(); 
    nameval = StringVar(); 
    mobileval = StringVar(); 
    email_Id = StringVar(); 
    addressval = StringVar(); 
    genderval = StringVar(); 
    dateOfBirthVal = StringVar(); 

    idEntry = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= idval); 
    idEntry.place(x=213,y=13); 

    nameEntry = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= nameval); 
    nameEntry.place(x=213,y=73); 

    mobileEntry = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= mobileval); 
    mobileEntry.place(x=213,y=133); 

    email_IdEntry = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= email_Id); 
    email_IdEntry.place(x=213,y=193); 

    studentAddress = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= addressval); 
    studentAddress.place(x=213,y=253); 

    genderEntry = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= genderval); 
    genderEntry.place(x=213,y=313); 

    dateOfBirth_Entry = Entry(addroot,font=("times",18,"bold"),bd=3,textvariable= dateOfBirthVal); 
    dateOfBirth_Entry.place(x=213,y=373); 

    submitBtn = Button(addroot,text="SUBMIT",font=("Algerian",15,"bold"),width=15,bd=3,
                       background="orange",foreground="navyblue",activebackground="navyblue",
                       activeforeground="orange",command=submitAdd); 
    submitBtn.place(x=145,y=415); 

    addroot.mainloop(); 
