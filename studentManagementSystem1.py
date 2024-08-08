from tkinter import * ;
from tkinter import Toplevel, messagebox ;
from tkinter.ttk import Treeview ;
from tkinter import ttk ;
import pymysql ; 
import datetime; 
import time ; 
import random ;


# **************************** ----------   Connect to Database  ---------------- *************************************
def connectDb():
    def submitDb():
        global conn,myCursor; 
        hostData = host_data.get();  
        userData = user_data.get(); 
        passwordData = password_data.get(); 
        try:
            conn = pymysql.connect(host=hostData,user=userData,password=passwordData); 
            myCursor = conn.cursor(); 
        except:
            messagebox.showerror("Notifications","Data is incorrect!! Please try again");
            return ; 
        try:
            str_query = "create database student_Management_System"; 
            myCursor.execute(str_query); 
            
            str_query = "Use student_Management_System"; 
            myCursor.execute(str_query); 
            
            str_query = "Create table studentData1(Id int, Name varchar(67), Mobile_No varchar(20), Email_Id varchar(100), Address varchar(255), gender varchar(10), D_O_B varchar(10),Date varchar(50), Time varchar(50))"; 
            myCursor.execute(str_query); 
        
            str_query = "Alter table studentData1 MODIFY COLUMN Id int NOT NULL"; 
            myCursor.execute(str_query); 
        
            str_query = "Alter table studentData1 MODIFY COLUMN Id int PRIMARY KEY "; 
            myCursor.execute(str_query); 
            messagebox.showinfo("Notifications","Database created!! Connection established............",parent=dbroot);  

        except:
            str_query = "use student_Management_System"; 
            myCursor.execute(str_query); 
            messagebox.showinfo("Notifications","Connection established............",parent=dbroot);  
            dbroot.destroy(); 
    
    dbroot = Toplevel(); 
    dbroot.grab_set(); 
    dbroot.geometry("589x290+779+357"); 
    dbroot.iconbitmap("Database-Cloud.ico"); 
    dbroot.resizable(True,False); 
    dbroot.config(bg="skyblue"); 

# **************************** ----------   Database labels  ---------------- *************************************
    hostLabel = Label(dbroot,text="Enter host:",bg="darkgray",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=13,anchor='w'); 
    hostLabel.place(x=10,y=10); 

    userLabel = Label(dbroot,text="Enter user:",bg="darkgray",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=13,anchor='w'); 
    userLabel.place(x=10,y=83); 

    passwordLabel = Label(dbroot,text="Enter password:",bg="darkgray",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=13,anchor='w'); 
    passwordLabel.place(x=10,y=155); 

# **************************** ----------   Database Entry Fields  ---------------- *************************************
    host_data = StringVar(); 
    user_data = StringVar(); 
    password_data= StringVar(); 
    
    hostEntry = Entry(dbroot,font=("Times",20,"bold"),bd=5,textvariable=host_data); 
    hostEntry.place(x=250,y=10); 

    userName = Entry(dbroot,font=("Times",20,"bold"),bd=5,textvariable=user_data); 
    userName.place(x=250,y=79); 

    password = Entry(dbroot,font=("Times",20,"bold"),bd=5,textvariable=password_data); 
    password.place(x=250,y=150); 

# **************************** ----------   Data submit button  ---------------- *************************************
    submitButton = Button(dbroot,text="SUBMIT",font=("Algerian",20,"bold"),width=11,background="orange",foreground="navyblue",
                          activebackground="navyblue",activeforeground="orange",command=submitDb); 
    submitButton.place(x=203,y=209); 

    dbroot.mainloop(); 


# **************************** ----------  Function for adding the details  ---------------- *************************************
def addStudent():
    def submitAdd():
        id = idval.get(); 
        name = nameval.get(); 
        mobile = mobileval.get(); 
        email = email_Id.get(); 
        address = addressval.get(); 
        gender = genderval.get(); 
        dob = dateOfBirthVal.get(); 
        addedDate = time.strftime("%d/%m/%Y");  
        addedTime = time.strftime("%H:%M:%S"); 
        
        try:
            str_query = "DELETE FROM studentdata1 WHERE Name = ''"; 
            myCursor.execute(str_query); 
            
            str_query = "DELETE FROM studentdata1 WHERE Name is NULL"; 
            myCursor.execute(str_query); 
            
            # str_query = "DELETE FROM studentdata1 WHERE Id is Null"; 
            # myCursor.execute(str_query); 
            
            str_query = "Insert into studentData1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            myCursor.execute(str_query,(id,name,mobile,email,address,gender,dob,addedDate,addedTime)); 
            conn.commit(); 
            
            result = messagebox.askyesnocancel("Notifications","Id {} Name {} added successfully........ and want to clean the form".format(id,name),parent=addroot);
            if(result == True):
                idval.set(""); 
                nameval.set("");  
                mobileval.set("");  
                email_Id.set("");  
                addressval.set("");  
                genderval.set("");  
                dateOfBirthVal.set(""); 
        except:
            messagebox.showerror("Notifications","Id already exists!! try another id",parent=addroot); 
        
        str_query = "SELECT * FROM studentData1"; 
        myCursor.execute(str_query); 
        student_data = myCursor.fetchall(); 
        studentTable.delete(*studentTable.get_children()); 
        for i in student_data:
            listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
            studentTable.insert("",END,values=listOfData); 

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

# **************************** ------------  Adding data of student  -------------- *************************************
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

# **************************** ----------  Function for searching the details  ---------------- *************************************

def searchStudent():
    def submitSearch():
        id = idval.get(); 
        name = nameval.get(); 
        mobile = mobileval.get(); 
        email = email_Id.get(); 
        address = addressval.get(); 
        gender = genderval.get(); 
        dob = dateOfBirthVal.get(); 
        addedDate = time.strftime("%d/%m/%Y"); 

        if(id != ''):
            str_query = 'SELECT * FROM studentData1 WHERE Id=%s'; 
            myCursor.execute(str_query,(id)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(name != ''):
            str_query = 'SELECT * FROM studentData1 WHERE Name=%s'; 
            myCursor.execute(str_query,(name)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(mobile != ''):
            str_query = 'SELECT * FROM studentData1 WHERE Mobile_No=%s'; 
            myCursor.execute(str_query,(mobile)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(email != ''):
            str_query = 'SELECT * FROM studentData1 WHERE Email_Id=%s'; 
            myCursor.execute(str_query,(email)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(address != ''):
            str_query = 'SELECT * FROM studentData1 WHERE Address=%s'; 
            myCursor.execute(str_query,(address)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(gender != ''):
            str_query = 'SELECT * FROM studentData1 WHERE gender=%s'; 
            myCursor.execute(str_query,(gender)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(dob != ''):
            str_query = 'SELECT * FROM studentData1 WHERE D_O_B=%s'; 
            myCursor.execute(str_query,(dob)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
        elif(addedDate != ''):
            str_query = 'SELECT * FROM studentData1 WHERE Date=%s'; 
            myCursor.execute(str_query,(addedDate)); 
            student_data = myCursor.fetchall();  
            studentTable.delete(*studentTable.get_children()); 
            for i in student_data:
                listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
                studentTable.insert('',END,values=listOfData);  
         
    
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

# **************************** ----------  Function for delete the details  ---------------- *************************************

def deleteStudent():
    focusOn = studentTable.focus(); 
    content = studentTable.item(focusOn); 
    particularElement = content["values"][0]; 
    str_query = "DELETE FROM studentData1 where Id = %s"; 
    myCursor.execute(str_query,(particularElement)); 
    conn.commit(); 
    messagebox.showinfo("Notifications","Id {} delete successfully.......".format(particularElement)); 

    str_query = "SELECT * FROM studentData1"; 
    myCursor.execute(str_query);

    student_data = myCursor.fetchall(); 
    studentTable.delete(*studentTable.get_children()); 
 
    for i in student_data:
        listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
        studentTable.insert("",END,values=listOfData);  

# **************************** ----------  Function for updating the details  ---------------- *************************************

def updateStudent():
    def updateData():
        id = idval.get(); 
        name = nameval.get(); 
        mobile = mobileval.get(); 
        email = email_Id.get(); 
        address = addressval.get(); 
        gender = genderval.get(); 
        dob = dateOfBirthVal.get(); 
        addedDate = dateVal.get();   
        addedTime = timeVal.get(); 

        str_query = "UPDATE studentData1 set Name=%s,Mobile_No=%s,Email_Id=%s,Address=%s,gender=%s,D_O_B=%s,Date=%s,Time=%s WHERE Id=%s"; 
        myCursor.execute(str_query,(name,mobile,email,address,gender,dob,addedDate,addedTime,id)); 
        conn.commit(); 

        messagebox.showinfo("Notifications","Id {} updated Successfully.........".format(id),parent=updateRoot);  
        str_query = 'SELECT * FROM studentData1'; 
        myCursor.execute(str_query); 
        student_data = myCursor.fetchall();  
        studentTable.delete(*studentTable.get_children()); 
        for i in student_data:
            listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
            studentTable.insert('',END,values=listOfData); 


    updateRoot = Toplevel(master=DataEntryFrame);  
    updateRoot.grab_set(); 
    updateRoot.geometry("579x579+200+150"); 
    updateRoot.title("Student Management System"); 
    updateRoot.config(bg="skyblue"); 
    updateRoot.iconbitmap("Database-Cloud.ico"); 
    updateRoot.resizable(False,False); 

# ****************************  --------- Type of data   ------- *************************************
    idLabel = Label(updateRoot,text="Identity No:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    idLabel.place(x=10,y=10); 
    
    nameLabel = Label(updateRoot,text="Student Name:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    nameLabel.place(x=10,y=70); 
    
    mobileLabel = Label(updateRoot,text="Mobile No:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    mobileLabel.place(x=10,y=130); 
    
    emailLabel = Label(updateRoot,text="Email-Id:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    emailLabel.place(x=10,y=190); 
    
    addressLabel = Label(updateRoot,text="Address:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    addressLabel.place(x=10,y=250); 
    
    genderLabel = Label(updateRoot,text="Gender:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    genderLabel.place(x=10,y=310); 
    
    dateOfBirth = Label(updateRoot,text="Date of Birth:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w'); 
    dateOfBirth.place(x=10,y=370); 

    date_Entry = Label(updateRoot,text="Enter date:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    date_Entry.place(x=10,y=430); 

    timeEntry = Label(updateRoot,text="Enter time:",bg="darkgray",fg="darkblue",font=("Times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timeEntry.place(x=10,y=490); 

# **************************** ------------  Updating data of students -------------- *************************************
    idval = StringVar(); 
    nameval = StringVar(); 
    mobileval = StringVar(); 
    email_Id = StringVar(); 
    addressval = StringVar(); 
    genderval = StringVar(); 
    dateOfBirthVal = StringVar(); 
    dateVal = StringVar();  
    timeVal =StringVar();  

    idEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= idval); 
    idEntry.place(x=213,y=13); 

    nameEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= nameval); 
    nameEntry.place(x=213,y=73); 

    mobileEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= mobileval); 
    mobileEntry.place(x=213,y=133); 

    email_IdEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= email_Id); 
    email_IdEntry.place(x=213,y=193); 

    studentAddress = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= addressval); 
    studentAddress.place(x=213,y=253); 

    genderEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= genderval); 
    genderEntry.place(x=213,y=313); 

    dateOfBirth_Entry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= dateOfBirthVal); 
    dateOfBirth_Entry.place(x=213,y=373); 

    dateEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= dateVal); 
    dateEntry.place(x=213,y=433); 

    timeEntry = Entry(updateRoot,font=("times",18,"bold"),bd=3,textvariable= timeVal); 
    timeEntry.place(x=213,y=493); 

    submitBtn = Button(updateRoot,text="SUBMIT",font=("Algerian",15,"bold"),width=15,bd=3,
                       background="orange",foreground="navyblue",activebackground="navyblue",
                       activeforeground="orange",command=updateData); 
    submitBtn.place(x=145,y=537);  
    
    focusOn = studentTable.focus(); 
    content = studentTable.item(focusOn); 
    elements = content["values"]; 
    print(elements); 
    print(len(elements)); 

    if(len(elements) != 0):
        idval.set(elements[0]);  
        nameval .set(elements[1]); 
        mobileval .set(elements[2]); 
        email_Id .set(elements[3]); 
        addressval .set(elements[4]); 
        genderval .set(elements[5]); 
        dateOfBirthVal .set(elements[6]); 
        dateVal .set(elements[7]); 
        timeVal .set(elements[8]); 

    updateRoot.mainloop();  

# **************************** ----------  Function for showing all the details  ---------------- *************************************

def showAllData():
    str_query = 'SELECT * FROM studentData1'; 
    myCursor.execute(str_query); 
    student_data = myCursor.fetchall();  
    studentTable.delete(*studentTable.get_children()); 
    for i in student_data:
        listOfData = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]; 
        studentTable.insert('',END,values=listOfData);

# **************************** ----------  Function for exporting the details  ---------------- *************************************

def exportData():
    print(""); 

# **************************** ----------  Function for exiting the app  ---------------- *************************************

def exitApp():
    result = messagebox.askyesnocancel("Notification","Do you want to exit?");
    if(result == True):
        root.destroy(); 
         

# **************************** ----------  Colours  ---------------- *************************************
colors = ["red","orange","yellow","blue","gold","silver"]; 

# **************************** ----------  Clock => Function  ---------------- *************************************
def clockColor():
    foregroundColor = random.choice(colors); 
    clock.config(fg=foregroundColor); 
    clock.after(300,clockColor); 
def displayTime():
    timeString = time.strftime('%H:%M:%S'); 
    dateString = time.strftime('%d/%m/%Y'); 
    clock.config(text = "Date:"+ dateString + "\n" + "Time:" + timeString); 
    clock.after(200,displayTime); 

# **************************** ----------  Label => Function  ---------------- *************************************
def introLabelColorChoice():
    foregroundColor = random.choice(colors); 
    SliderLabel.config(fg=foregroundColor); 
    SliderLabel.after(100,introLabelColorChoice); 
def IntroLabelTick():
    global count, text; 
    if(count >= len(title)):
        count = 0; 
        text = ''; 
        SliderLabel.config(text=text); 
    else:
        text = text + title[count]; 
        SliderLabel.config(text=text);
        count += 1;
    SliderLabel.after(179,IntroLabelTick);     

# **************************** ------------------------- *************************************
 
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

# **************************** ----------   Frames  ---------------- *************************************
DataEntryFrame = Frame(root,bg="skyblue",relief=RIDGE,borderwidth=2); 
DataEntryFrame.place(x=10,y=110,width=500,height=600); 

ShowDataFrame = Frame(root,bg="skyblue",relief=GROOVE,borderwidth=2); 
ShowDataFrame.place(x=530,y=110,width=797,height=600); 

# **************************** ----------   Label  ---------------- *************************************
title = "Student Database Management System" ; 
count = 0 ; 
text = ''; 
SliderLabel = Label(root,text=title,font=("Sans-serif",30,'italic bold'),relief=RIDGE,borderwidth=2,width=35,bg="navyblue"); 
SliderLabel.place(x=265,y=5); 

# Calling the label function
IntroLabelTick(); 
introLabelColorChoice(); 

# **************************** ----------   Clock  ---------------- *************************************
clock = Label(root,font=("Arial",15,'bold'),relief=GROOVE,borderwidth=2,width=20,bg="navyblue"); 
clock.place(x=2,y=5); 

# Calling the time function
displayTime(); 
clockColor(); 

# **************************** ----------   Connect to database  ---------------- *************************************
connectButton = Button(root,text = "Connect to Database",width=16,font=("Arial",18,"bold"),relief=GROOVE,borderwidth=2,bg="navyblue",fg="orange",
                       activebackground="orange",activeforeground="navyblue",command=connectDb); 
connectButton.place(x=1130,y=5); 

# **************************** ---------- Data entry frame (Line => 92) Student data fields  ---------------- *************************************
front_label = Label(DataEntryFrame,text="****************** Welcome *****************",width=25,
                   font=("Arial",22,"italic bold"),bg="skyblue",fg="darkblue"); 
front_label.pack(side=TOP,expand=True); 

# **************************** ---------- addBtn ---------------- *************************************

addbtn = Button(DataEntryFrame,text='1: Add Student',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=addStudent); 
addbtn.pack(side=TOP,expand=600); 

# **************************** ---------- search button  ---------------- *************************************

searchButton = Button(DataEntryFrame,text='2: Search student',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=searchStudent); 
searchButton.pack(side=TOP,expand=600); 

# **************************** ---------- delete button  ---------------- *************************************

deleteBtn = Button(DataEntryFrame,text='3: Delete student',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=deleteStudent); 
deleteBtn.pack(side=TOP,expand=600); 

# **************************** ---------- update button  ---------------- *************************************

updateBtn = Button(DataEntryFrame,text='4: Update student',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=updateStudent); 
updateBtn.pack(side=TOP,expand=600); 

# **************************** ---------- show all button  ---------------- *************************************

showAllButton = Button(DataEntryFrame,text='5: Show all',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=showAllData); 
showAllButton.pack(side=TOP,expand=600); 

# **************************** ---------- export button ---------------- *************************************

exportBtn = Button(DataEntryFrame,text='6: Export',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=exportData); 
exportBtn.pack(side=TOP,expand=600); 

# **************************** ---------- exit button  ---------------- *************************************

exitButton = Button(DataEntryFrame,text='7: Exit',width=20,font=("Arial",15,"bold"),bd=2,bg="darkgray",fg="navyblue",
                activebackground="darkblue",activeforeground="orange",command=exitApp); 
exitButton.pack(side=TOP,expand=600); 


# **************************** ---------- Show data frame ---------------- *************************************
style = ttk.Style(); 
style.configure("Treeview.Heading",font=("Times",20,"bold"),foreground="navyblue"); 
style.configure("Treeview",font=("Times",15,"bold"),background="orange",foreground="navyblue"); 

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL); 
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL); 

studentTable = Treeview(ShowDataFrame,columns=("Id","Student Name","Mobile No","Email_Id","Address","Gender","D.O.B","Added Date","Added Time"),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set) ; 
scroll_x.pack(side=BOTTOM,fill=X); 
scroll_x.config(command=studentTable.xview); 

scroll_y.pack(side=RIGHT,fill=Y); 
scroll_y.config(command=studentTable.yview); 

studentTable.heading("Id",text="Id"); 
studentTable.heading("Student Name",text="Student Name"); 
studentTable.heading("Mobile No",text="Mobile No"); 
studentTable.heading("Email_Id",text="Email_Id"); 
studentTable.heading("Address",text="Address"); 
studentTable.heading("Gender",text="Gender"); 
studentTable.heading("D.O.B",text="D.O.B"); 
studentTable.heading("Added Date",text="Added Date"); 
studentTable.heading("Added Time",text="Added Time"); 

studentTable["show"] = "headings"; 

studentTable.column("Id",width=137); 
studentTable.column("Student Name",width=379); 
studentTable.column("Mobile No",width=250); 
studentTable.column("Email_Id",width=389); 
studentTable.column("Address",width=500); 
studentTable.column("Gender",width=150); 
studentTable.column("D.O.B",width=200); 
studentTable.column("Added Date",width=200); 
studentTable.column("Added Time",width=200); 

studentTable.pack(fill=BOTH,expand=1); 

root.mainloop(); 


