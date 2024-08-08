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

# **************************** ----------  Function for searching the details  ---------------- *************************************

def searchStudent():
    def submitSearch():
        print(); 
    searchRoot = Toplevel(master=DataEntryFrame);  
    searchRoot.grab_set(); 
    searchRoot.geometry("529x529+220+200"); 
    searchRoot.title("Student Management System"); 
    searchRoot.config(bg="skyblue"); 
    searchRoot.iconbitmap("Database-Cloud.ico"); 
    searchRoot.resizable(False,False); 

# ****************************  --------- Type of data   ------- *************************************
    idLabel = Label(searchRoot,text="Identity No:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    idLabel.place(x=10,y=10); 
    
    nameLabel = Label(searchRoot,text="Student Name:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    nameLabel.place(x=10,y=70); 
    
    mobileLabel = Label(searchRoot,text="Mobile No:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    mobileLabel.place(x=10,y=130); 
    
    emailLabel = Label(searchRoot,text="Email-Id:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    emailLabel.place(x=10,y=190); 
    
    addressLabel = Label(searchRoot,text="Address:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    addressLabel.place(x=10,y=250); 
    
    genderLabel = Label(searchRoot,text="Gender:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    genderLabel.place(x=10,y=310); 
    
    dateOfBirth = Label(searchRoot,text="Date of Birth:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    dateOfBirth.place(x=10,y=370); 

    date_Entry = Label(searchRoot,text="Enter date:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    date_Entry.place(x=10,y=430);

# **************************** ------------  Searching data of students  -------------- *************************************
    idval = StringVar(); 
    nameval = StringVar(); 
    mobileval = StringVar(); 
    email_Id = StringVar(); 
    addressval = StringVar(); 
    genderval = StringVar(); 
    dateOfBirthVal = StringVar(); 
    dateVal = StringVar();  

    idEntry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= idval); 
    idEntry.place(x=213,y=13); 

    nameEntry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= nameval); 
    nameEntry.place(x=213,y=73); 

    mobileEntry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= mobileval); 
    mobileEntry.place(x=213,y=133); 

    email_IdEntry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= email_Id); 
    email_IdEntry.place(x=213,y=193); 

    studentAddress = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= addressval); 
    studentAddress.place(x=213,y=253); 

    genderEntry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= genderval); 
    genderEntry.place(x=213,y=313); 

    dateOfBirth_Entry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= dateOfBirthVal); 
    dateOfBirth_Entry.place(x=213,y=373); 

    dateEntry = Entry(searchRoot,font=("times",18,"bold"),bd=3,textvariable= dateVal); 
    dateEntry.place(x=213,y=433); 

    submitBtn = Button(searchRoot,text="SUBMIT",font=("Algerian",15,"bold"),width=15,bd=3,
                       background="orange",foreground="navyblue",activebackground="navyblue",
                       activeforeground="orange",command=submitSearch); 
    submitBtn.place(x=145,y=485);  

    searchRoot.mainloop(); 
