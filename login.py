from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import face_recognition_system
import mysql.connector
from attendance import Attendance
from devloper import Developer
from Help import Helpsupport
from student import Student
from train import Train
from Face_Recognition import face_recognition


def main():
    win=Tk()
    app=login_Window(win)
    win.mainloop()   

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")

# bg img
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\loginbg.png")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=00,y=00, relwidth=1,relheight=1)

# frame
        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=600,y=200,width=340,height=450)

# Logo immg
        img1=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\logo.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=720,y=205, width=100,height=100)


        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=130,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)

         #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.register_window,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)




    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            conn = mysql.connector.connect(username='root', password='Aditya@136',host='localhost',database='facerecognition',port=3306)
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
            if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=face_recognition_system(self.new_window)
            else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()







# --------class register import
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Panel")
        self.root.geometry("1600x900+0+0")


# Varriablels


        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securtiyQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()



        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\un.jpg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)
        
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\facialrecognition (1).png")
        left_lbl=Label(self.root, image=self.bg1) 
        left_lbl.place(x=50,y=100, width=478, height=550)

        frame=Frame(self.root,bg="white") 
        frame.place(x=520,y=100, width=800,height=550)


        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=320,y=50)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=100)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=125,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=170)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=195,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=430,y=100)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txtuser.place(x=433,y=125,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=430,y=170)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=433,y=195,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=250)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_securtiyQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=275,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=320)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=345,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=430,y=250)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txtuser.place(x=433,y=275,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=430,y=320)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=433,y=345,width=270)

        # Checkbutton
        self.var_check=IntVar()
        self.checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        self.checkbtn.place(x=100,y=380,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.register,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=410,width=270,height=35)

        # Creating Button Login
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=433,y=410,width=270,height=35)


    def register(self):
        if (self.var_fname.get()=="" or self.var_email.get()=="" or  self.var_securtiyQ.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pass.get() != self.var_confpass.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
            # messagebox.showinfo("Successfully","Successfully Register!")
        try:
           conn = mysql.connector.connect(username='root', password='Aditya@136',host='localhost',database='facerecognition',port=3306)
           my_cursor = conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
           else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securtiyQ.get(),
                self.var_securityA.get(),
                self.var_pass.get()
                                                                                 ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
       


# main project imoort

class face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x750+0+0")
        self.root.title("E-Studency")


# Inserting the images
# 1 img
        img = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\BestFacialRecognition.jpg")
        img = img.resize((550,130))
        self.photoimg = ImageTk.PhotoImage(img)


        first_lbl = Label(self.root,image = self.photoimg)
        first_lbl.place(x = 0,y=0,width=500,height = 130)

# 2 img
        img1 = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\facialrecognition.png")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        first_lbl = Label(self.root,image = self.photoimg1)
        first_lbl.place(x = 500,y=0,width=500,height = 130)

# 3 img
        img2 = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\images.jpg")
        img2 = img2.resize((800,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)


        first_lbl = Label(self.root,image = self.photoimg2)
        first_lbl.place(x = 1000,y=0,width=600,height = 130)


        # Backgrond img
        bg = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\bgimg.jpg")
        bg = bg.resize((1550,750))
        self.bg = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root,image = self.bg)
        bg_img.place(x = 0,y=130,width=1550,height = 710)



        # Title
        title_lbl=Label(bg_img,text = "E-Studency",font=("Roboto",35,"bold"),bg="white",fg="black")

        title_lbl.place(x=0,y=0,width=1530,height=45)


# student buttons
        stud = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\student.jpg")
        stud = stud.resize((225,225))
        self.stud = ImageTk.PhotoImage(stud)

        b2 = Button(bg_img,image=self.stud , command=self.student_details,cursor="hand2")
        b2.place(x=200,y=100,width=220,height=220)

        b2_1= Button(bg_img,text = "Student Details",command=self.student_details,cursor="hand2",font=("Roboto",15,"bold"),bg="black",fg="white")
        b2_1.place(x=200,y=300,width=220,height=40)


# Detect Face button    
        dect = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\face_detector1.jpg")
        dect = dect.resize((225,225))
        self.dect = ImageTk.PhotoImage(dect)

        b2 = Button(bg_img,image=self.dect,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1= Button(bg_img,text = "Face Detector",cursor="hand2",command=self.face_data,font=("Roboto",15,"bold"),bg="black",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)
       

# attendance button
        attd = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\attendance.jpg")
        attd = attd.resize((225,225))
        self.attd = ImageTk.PhotoImage(attd)

        b3 = Button(bg_img,image=self.attd,cursor="hand2",command=self.attendance_data  )
        b3.place(x=800,y=100,width=220,height=220)

        b3_1= Button(bg_img,text = "Attendance",cursor="hand2",command=self.attendance_data     ,font=("Roboto",15,"bold"),bg="black",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


# Help button        
        hlp = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\help.jpg")
        hlp = hlp.resize((225,225))
        self.hlp = ImageTk.PhotoImage(hlp)

        b4 = Button(bg_img,command=self.help_data,image=self.hlp,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1= Button(bg_img,command=self.help_data,text = "Help desk",cursor="hand2",font=("Roboto",15,"bold"),bg="black",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

# Train face button
        trn = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\train.jpg")
        trn = trn.resize((225,225))
        self.trn = ImageTk.PhotoImage(trn)

        b5 = Button(bg_img,image=self.trn,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1= Button(bg_img,text = "Train Data",command=self.train_data,cursor="hand2",font=("Roboto",15,"bold"),bg="black",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)

# Photos face button
        pic = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\people.jpg")
        pic = pic.resize((225,225))
        self.pic = ImageTk.PhotoImage(pic)

        b6 = Button(bg_img,image=self.pic,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1= Button(bg_img,text = "Photos",cursor="hand2",command=self.open_img,font=("Roboto",15,"bold"),bg="black",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)

# Developers
        dev = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\dev.jpg")
        dev = dev.resize((225,225))
        self.dev = ImageTk.PhotoImage(dev)

        b7 = Button(bg_img,command=self.Developer_data,image=self.dev,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)

        b7_1= Button(bg_img,command=self.Developer_data,text = "Developers",cursor="hand2",font=("Roboto",15,"bold"),bg="black",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)

# Exit buttton
        ex = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\exit.jpg")
        ex = ex.resize((225,225))
        self.ex = ImageTk.PhotoImage(ex)

        b8 = Button(bg_img,command=self.Close,image=self.ex,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1= Button(bg_img,command=self.Close,text = "Exit",cursor="hand2",font=("Roboto",15,"bold"),bg="black",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)



    def open_img(self):
        os.startfile("dataimg")

    




# Function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()