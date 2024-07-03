from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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
       


        



if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()