from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('PMS.db')
conn.execute("""CREATE TABLE IF NOT EXISTS PARKING (REG INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,HOSTEL CHAR(5) NOT NULL,SEX CHAR(8) NOT NULL,MOBILE CHAR(12) NOT NULL,EMAIL CHAR(50) NOT NULL,USERNAME CHAR(50) NOT NULL,PASSWORD CHAR(50) NOT NULL,VEHICLE CHAR(15),PARK CHAR(10), TYPE CHAR(12) ,P CHAR(2))""")
conn.commit()
conn.close()


def Base_Page():
    
    global root
    root=Tk()
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="LPU-Logo.png")
    logo=Label(root,image=icon)
    PMS=Label(root,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=2)
    
    icon1=PhotoImage(file="Login.png")
    Log=Label(root,image=icon1)
    Login_Button=Button(root,text="Login",font=("Times New Roman",32),bd=3,command=Login_Page)

    icon2=PhotoImage(file="NewUser.png")
    NUsr=Label(root,image=icon2)
    NewUser_Button=Button(root,text="New User",font=("Times New Roman",32),bd=3,command=BptoNu)
    icon3=PhotoImage(file="Availability.png")
    Avai=Label(root,image=icon3)
    Availability_Button=Button(root,text="Availability",font=("Times New Roman",32),bd=3,command=Availability)
    Log.grid(row=2)
    Login_Button.grid(row=3,column=0)
    NUsr.grid(row=2,column=1)
    NewUser_Button.grid(row=3,column=1)
    Avai.grid(row=2,column=2)
    Availability_Button.grid(row=3,column=2)
    root.mainloop()



def Login_Page():
    root.destroy()
    global Login_GUI
    Login_GUI=Tk()
    Login_GUI.title("Login Page")
    w,h=Login_GUI.winfo_screenwidth(),Login_GUI.winfo_screenheight()
    Login_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="LPU-Logo.png")
    logo=Label(Login_GUI,image=icon)
    PMS=Label(Login_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=4)
    
    lab1=Label(Login_GUI,text="User Name",padx=20,pady=5,font=("Times New Roman",28))
    lab2=Label(Login_GUI,text="Password",padx=20,pady=5,font=("Times New Roman",28))
    lab3=Label(Login_GUI,text="\n",font=("Times New Roman",28))
    global name
    global pswd
    name=Entry(Login_GUI,font=("Times New Roman",28))
    pswd=Entry(Login_GUI,show="*",font=("Times New Roman",28))
    
    Login_Button=Button(Login_GUI,text=" Login  ",command=validate,font=("Times New Roman",32))
    NewUser_Button=Button(Login_GUI,text="New User",command=LptoNu,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=1)
    lab2.grid(row=3,column=1)
    name.grid(row=2,column=2)
    pswd.grid(row=3,column=2)
    lab3.grid(row=4)
    Login_Button.grid(row=5,column=1)
    NewUser_Button.grid(row=5,column=2)
    Login_GUI.mainloop()

def LptoNu():
    Login_GUI.destroy()
    NewUser_Page()
    
def BptoNu():
    root.destroy()
    NewUser_Page()
    
def validate():
    c=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT USERNAME,PASSWORD FROM PARKING")
    if ((str(name.get())=="Admin" ) and (str(pswd.get())=="Admin")):
        messagebox.showinfo("Status", "Admin Login")
        SuperUser_Page()
    for row in cursor:
        if( (str(name.get())==row[0]) and (str(pswd.get())==row[1])):
            c=1
            break
        else:
            c=0
    if(c==1):
        messagebox.showinfo("Status", "Login Successful")
        User_Page()
    if(c==0):
        messagebox.showinfo("Status", "Login Failed.\nPlease Try Again")
    conn.commit()
        

def NewUser_Page():
    
    global NewUser_GUI
    NewUser_GUI=Tk()
    NewUser_GUI.title("Login Page")
    w,h=NewUser_GUI.winfo_screenwidth(),NewUser_GUI.winfo_screenheight()
    NewUser_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="LPU-Logo.png")
    logo=Label(NewUser_GUI,image=icon)
    PMS=Label(NewUser_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)
    
    lab1=Label(NewUser_GUI,text="Name",padx=20,pady=5,font=("Times New Roman",23))
    lab2=Label(NewUser_GUI,text="Reg. No.",padx=20,pady=5,font=("Times New Roman",23))
    lab3=Label(NewUser_GUI,text="Hostel",padx=20,pady=5,font=("Times New Roman",23))
    lab4=Label(NewUser_GUI,text="Gender",padx=20,pady=5,font=("Times New Roman",23))
    lab5=Label(NewUser_GUI,text="Mobile",padx=20,pady=5,font=("Times New Roman",23))
    lab6=Label(NewUser_GUI,text="Email ID",padx=20,pady=5,font=("Times New Roman",23))
    lab7=Label(NewUser_GUI,text="User Name",padx=20,pady=5,font=("Times New Roman",23))
    lab8=Label(NewUser_GUI,text="Password",padx=20,pady=5,font=("Times New Roman",23))
    global Name
    global Register
    global Hostel
    global Mobile
    global Email
    global UserName
    global Pass
    Name=Entry(NewUser_GUI,font=("Times New Roman",23))
    Register=Entry(NewUser_GUI,font=("Times New Roman",23))
    Hostel=Entry(NewUser_GUI,font=("Times New Roman",23))
    global Gender
    Gender = StringVar()
    G1 = Radiobutton(NewUser_GUI, text="Male", variable=Gender, value="Male",font=("Times New Roman",23))
    G2 = Radiobutton(NewUser_GUI, text="Female", variable=Gender, value="Female",font=("Times New Roman",23))
    Mobile=Entry(NewUser_GUI,font=("Times New Roman",23))
    Email=Entry(NewUser_GUI,font=("Times New Roman",23))
    UserName=Entry(NewUser_GUI,font=("Times New Roman",23))
    Pass=Entry(NewUser_GUI,font=("Times New Roman",23))
    lab1.grid(row=2,column=0)
    lab2.grid(row=3,column=0)
    lab3.grid(row=4,column=0)
    lab4.grid(row=5,column=0)
    lab5.grid(row=6,column=0)
    lab6.grid(row=7,column=0)
    lab7.grid(row=8,column=0)
    lab8.grid(row=9,column=0)
    Name.grid(row=2,column=1)
    Register.grid(row=3,column=1)
    Hostel.grid(row=4,column=1)
    G1.grid(row=5,column=1)
    G2.grid(row=5,column=2)
    Mobile.grid(row=6,column=1)
    Email.grid(row=7,column=1)
    UserName.grid(row=8,column=1)
    Pass.grid(row=9,column=1)

    lab10=Label(NewUser_GUI,text="",font=("Times New Roman",28))
    lab10.grid(row=10)
    Submit_Button=Button(NewUser_GUI,text="Submit",command=DB_Reg,font=("Times New Roman",25),bd=3)
    Submit_Button.grid(row=11,column=1)
    NewUser_GUI.mainloop()

def DB_Reg():

    dbReg=str(Register.get())
    dbName=str(Name.get())
    dbHostel=str(Hostel.get())
    dbMobile=str(Mobile.get())
    dbGender=str(Gender.get())
    dbEmail=str(Email.get())
    dbUserName=str(UserName.get())
    dbPass=str(Pass.get())
    
    conn = sqlite3.connect('PMS.db')
    cursor=conn.execute("INSERT INTO PARKING (REG,NAME,HOSTEL,SEX,MOBILE,EMAIL,USERNAME,PASSWORD) VALUES (?,?,?,?,?,?,?,?)",(dbReg,dbName,dbHostel,dbMobile,dbGender,dbEmail,dbUserName,dbPass))
    conn.commit()
    messagebox.showinfo("Status", "Successfully Registered\nUse the User Name & Password to Login")
    NewUser_GUI.destroy()
    Base_Page()

def User_Page():
    Login_GUI.destroy()
    global User_GUI
    User_GUI=Tk()
    w,h=User_GUI.winfo_screenwidth(),User_GUI.winfo_screenheight()
    User_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="LPU-Logo.png")
    logo=Label(User_GUI,image=icon)
    PMS=Label(User_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)

    icon1=PhotoImage(file="Book.png")
    Book=Label(User_GUI,image=icon1)
    BookParking_Button=Button(User_GUI,text="Book Parking",font=("Times New Roman",32),bd=3,command=Book_Page)

    icon2=PhotoImage(file="Policy.png")
    Policy=Label(User_GUI,image=icon2)
    Policy_Button=Button(User_GUI,text="Parking Policy",font=("Times New Roman",32),bd=3,command=ParkingPolicy)

    icon3=PhotoImage(file="Logout.png")
    Logout=Label(User_GUI,image=icon3)
    Logout_Button=Button(User_GUI,text="Logout",font=("Times New Roman",32),bd=3,command=UptoBp)

    icon4=PhotoImage(file="Parking.png")
    Y=Label(User_GUI,text="Registration No.",font=("Times New Roman",28),padx=20,pady=5)
    global Z
    Z=Entry(User_GUI,font=("Times New Roman",28))
    Details=Label(User_GUI,image=icon4)
    Details_Button=Button(User_GUI,text="Details",font=("Times New Roman",32),bd=3,command=De)
    
    Book.grid(row=2)
    BookParking_Button.grid(row=3,column=0)
    Policy.grid(row=2,column=1)
    Policy_Button.grid(row=3,column=1)
    Logout.grid(row=2,column=2)
    Logout_Button.grid(row=3,column=2)
    Details.grid(row=2,column=3)
    Y.grid(row=3,column=3)
    Z.grid(row=4,column=3)
    Details_Button.grid(row=5,column=3)
    User_GUI.mainloop()
    User_GUI.mainloop()
    
def De():
    zz=int(Z.get())
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT REG,NAME,HOSTEL,SEX,MOBILE,EMAIL,VEHICLE,PARK,TYPE  FROM PARKING")
    for row in cursor:
        if(row[0]==zz):
            S="PARKING DETAILS : \nREG. NO. = "+str(row[0])+"\nNAME = "+row[1]+"\nHOSTEL = "+row[2]+"\nGENDER = "+row[4]+"\nMOBILE = "+row[3]+"\nEMAIL = "+row[5]+"\nVEHICLE = "+row[6]+"\nPARKING = "+row[7]+"\nCATEGORY = "+row[8]+"\n\n"
            messagebox.showinfo("Details",S)
    conn.commit()
    
def ParkingPolicy():
     messagebox.showinfo("Parking Policy", "NOTE : \nAll students wishing to use parking facilities operated by the University Parking Office on the University Park campus, or any property owned or leased by The Lovely Professional University, must register their vehicle with the Parking Office and, while parked, properly display an authorized parking permit.\n\nParking permits must be properly displayed while parked:\n\nMOTORCYCLES: Permit (sticker) must be clearly visible from the front or rear of the motorcycle.\nAUTOMOBILES: Hang permit from rearview mirror, facing forward. Permit must be clearly visible. If windshield tint strip prevents clear display, permit hangers are available from the Parking Office.\n\nExceptions must be approved by the Parking Office in advance.")

def UptoBp():
    messagebox.showinfo("Status","Successfully Logged Off")
    User_GUI.destroy()
    Base_Page()

def Book_Page():
    
    User_GUI.destroy()
    global Book_GUI
    Book_GUI=Tk()
    Book_GUI.title("Book Parking")
    w, h = Book_GUI.winfo_screenwidth(),Book_GUI.winfo_screenheight()
    Book_GUI.geometry("%dx%d+0+0" % (w, h))
    icon=PhotoImage(file="LPU-Logo.png")
    logo=Label(Book_GUI,image=icon)
    PMS=Label(Book_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)

    lab1=Label(Book_GUI,text="Reg. No.",padx=20,pady=5,font=("Times New Roman",32))
    lab2=Label(Book_GUI,text="Vehicle. No.",padx=20,pady=5,font=("Times New Roman",32))
    lab3=Label(Book_GUI,text="Parking",padx=20,pady=5,font=("Times New Roman",32))
    lab4=Label(Book_GUI,text="Category",padx=20,pady=5,font=("Times New Roman",32))
    lab5=Label(Book_GUI,text="Price",padx=20,pady=5,font=("Times New Roman",32))
    global Reg
    global Veh
    Reg=Entry(Book_GUI,font=("Times New Roman",32))
    Veh=Entry(Book_GUI,font=("Times New Roman",32))
    global var
    var = StringVar()
    R1 = Radiobutton(Book_GUI, text="29 Block", variable=var, value="29 Block",font=("Times New Roman",32))
    R2 = Radiobutton(Book_GUI, text="34 Block", variable=var, value="34 Block",font=("Times New Roman",32))
    global VehTyp
    VehTyp = StringVar()
    R3 = Radiobutton(Book_GUI, text="Two Wheeler", variable=VehTyp, value="2 Wheeler",command=CalPrice2,font=("Times New Roman",32))
    R4 = Radiobutton(Book_GUI, text="Four Wheeler", variable=VehTyp, value="4 Wheeer",command=CalPrice4,font=("Times New Roman",32))
    
    
    Book_Button=Button(Book_GUI,text="Book Now",command=Park,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=0)
    Reg.grid(row=2,column=1)

    lab2.grid(row=3,column=0)
    Veh.grid(row=3,column=1)

    lab3.grid(row=4,column=0)
    R1.grid(row=4,column=1)
    R2.grid(row=4,column=2)

    lab4.grid(row=5,column=0)
    R3.grid(row=5,column=1)
    R4.grid(row=5,column=2)

    lab5.grid(row=6,column=0)
    global amt
    amt = Label(Book_GUI,font=("Times New Roman",32))
    amt.grid(row=6,column=1)
    
    Book_Button.grid(row=7,columnspan=2)
    
    Book_GUI.mainloop()


def CalPrice2():
        amt.config(text="1000")
def CalPrice4():
        amt.config(text="1500")
    

def Park():
    dbR=str(Reg.get())
    dbV=str(Veh.get())
    dbA=str(var.get())
    dbT=str(VehTyp.get())
    conn = sqlite3.connect('PMS.db')
    conn.execute("UPDATE PARKING SET VEHICLE=?,PARK=?,TYPE=?,P=1 WHERE REG=?", (dbV,dbA,dbT,dbR))
    conn.commit()
    conn.close()
    messagebox.showinfo("Status","Successfully Booked Parking")
    Book_GUI.destroy()
    Base_Page()

def Availability():
    Tot34=20
    Tot29=45
    C34=0
    C29=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT PARK FROM PARKING")
    for row in cursor:
        if(row[0]=="34 Block"):
            C34=C34+1
        if(row[0]=="29 Block"):
            C29=C29+1
    conn.commit()
    Av34=str(Tot34-C34)
    Av29=str(Tot29-C29)
    messagebox.showinfo("Status","Available Parking Slots\n\nBLOCK 29 ---- "+Av29+"\n\nBLOCK 34 ----  "+Av34)
    
def SuperUser_Page():
    Login_GUI.destroy()
    global SuperUser_GUI
    SuperUser_GUI=Tk()
    w,h=SuperUser_GUI.winfo_screenwidth(),SuperUser_GUI.winfo_screenheight()
    SuperUser_GUI.geometry("%dx%d+0+0" % (w,h))

# Empty Laber at Column 1

    Emp=Label(SuperUser_GUI,text="                     ",font=("Times New Roman",17),padx=17,pady=5)
    Emp.grid(row=1,column=0)

# LPU Logo & Heading
    
    icon=PhotoImage(file="LPU-LogoDetails.png")
    logo=Label(SuperUser_GUI,image=icon)
    PMS=Label(SuperUser_GUI,text="Parking Management System",font=("Helvetica", 48))
    logo.grid(row=1,column=1)
    PMS.grid(row=1,column=2,columnspan=4)

# Parking Details

    icon1=PhotoImage(file="ParkingDetails.png")
    Details=Label(SuperUser_GUI,image=icon1)
    Y=Label(SuperUser_GUI,text="Registration No.",font=("Times New Roman",17),padx=17,pady=3)
    global Z
    Z=Entry(SuperUser_GUI,font=("Times New Roman",17))
    Y1=Label(SuperUser_GUI,text="Vehicle No.",font=("Times New Roman",17),padx=17,pady=3)
    global Z1
    Z1=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    Details_Button=Button(SuperUser_GUI,text="Fetch Details",font=("Times New Roman",15),bd=3,width=12)

    

    Details.grid(row=2,column=1)
    Y.grid(row=3,column=1)
    Z.grid(row=4,column=1)
    Y1.grid(row=5,column=1)
    Z1.grid(row=6,column=1)
    
    Details_Button.grid(row=7,column=1,pady=4,rowspan=2)
   
    

# CheckIN

    icon2=PhotoImage(file="CheckIN.png")
    ChIN=Label(SuperUser_GUI,image=icon2)
    
    A=Label(SuperUser_GUI,text="Registration No.",font=("Times New Roman",17),padx=17,pady=3)
    global B
    B=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    A1=Label(SuperUser_GUI,text="Vehicle No.",font=("Times New Roman",17),padx=17,pady=3)
    global B1
    B1=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    A2=Label(SuperUser_GUI,text="Slot Number",font=("Times New Roman",17),padx=17,pady=3)
    global B2
    B2=Entry(SuperUser_GUI,font=("Times New Roman",17))

    R=Label(SuperUser_GUI,text="Block",font=("Times New Roman",25),padx=17,pady=3)
    global pd
    pd = StringVar()
    R1 = Radiobutton(SuperUser_GUI, text="29 Block", variable=pd, value="29 Block",font=("Times New Roman",17))
    R2 = Radiobutton(SuperUser_GUI, text="34 Block", variable=pd, value="34 Block",font=("Times New Roman",17))
    
    CheckIN_Button=Button(SuperUser_GUI,text="Check IN",font=("Times New Roman",17),bd=3,width=12)

    ChIN.grid(row=2,column=2,columnspan=2)
    A.grid(row=3,column=2,columnspan=2)
    B.grid(row=4,column=2,columnspan=2)
    A1.grid(row=5,column=2,columnspan=2)
    B1.grid(row=6,column=2,columnspan=2)
    A2.grid(row=7,column=2,columnspan=2)
    B2.grid(row=8,column=2,columnspan=2)
    R.grid(row=9,column=2,columnspan=2)
    R1.grid(row=10,column=2)
    R2.grid(row=10,column=3)
    CheckIN_Button.grid(row=11,column=2,columnspan=2)

# CheckOUT

    icon3=PhotoImage(file="CheckOUT.png")
    ChOUT=Label(SuperUser_GUI,image=icon3)
    
    C=Label(SuperUser_GUI,text="Registration No.",font=("Times New Roman",17),padx=17,pady=5)
    global D
    D=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    C1=Label(SuperUser_GUI,text="Vehicle No.",font=("Times New Roman",17),padx=17,pady=5)
    global D1
    D1=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    C2=Label(SuperUser_GUI,text="Slot Number",font=("Times New Roman",17),padx=17,pady=5)
    global D2
    D2=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    CheckOUT_Button=Button(SuperUser_GUI,text="Check OUT",font=("Times New Roman",17),bd=3,width=12)

    ChOUT.grid(row=2,column=4)
    C.grid(row=3,column=4)
    D.grid(row=4,column=4)
    C1.grid(row=5,column=4)
    D1.grid(row=6,column=4)
    C2.grid(row=7,column=4)
    D2.grid(row=8,column=4)
    
    CheckOUT_Button.grid(row=10,column=4,rowspan=1)


# Other Features
    icon4=PhotoImage(file="Features.png")
    Feat=Label(SuperUser_GUI,image=icon4)
    OverView_Button=Button(SuperUser_GUI,text="Overview",font=("Times New Roman",17),bd=3,width=12)
    History_Button=Button(SuperUser_GUI,text="History",font=("Times New Roman",17),bd=3,width=12)
    Slots_Button=Button(SuperUser_GUI,text="Available Slots",font=("Times New Roman",17),bd=3,width=12)
    Logout_Button=Button(SuperUser_GUI,text="Logout",font=("Times New Roman",17),bd=3,width=12)

    Feat.grid(row=2,column=5)
    OverView_Button.grid(row=4,column=5,pady=4)
    History_Button.grid(row=6,column=5,pady=4)
    Slots_Button.grid(row=8,column=5,pady=4)
    Logout_Button.grid(row=10,column=5)

    SuperUser_GUI.mainloop()







 
Base_Page()

