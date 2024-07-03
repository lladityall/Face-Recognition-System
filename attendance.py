from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import csv 
from tkinter import filedialog


#Global variable for importCsv Function 
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x750+0+0")
        self.root.title("Attendance Pannel")

         #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_roll=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

# 1image
        img1=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\student.jpg")
        img1=img1.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img1)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=800,height=200)

        # 2 image 
        img2=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\clg.jpg")
        img2=img2.resize((800,200))
        self.photobg1=ImageTk.PhotoImage(img2)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=800,y=0,width=800,height=200)

        # Bacground image
        bg = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\bgimg.jpg")
        bg = bg.resize((1550,750))
        self.bg = ImageTk.PhotoImage(bg)

        bg_img = Label(self.root,image = self.bg)
        bg_img.place(x = 0,y=130,width=1550,height = 710)

          #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

         # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=20,y=55,width=1480,height=600)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=730,height=580)

        # right label frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=750,y=10,width=720,height=580)



        img_left = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\lol.jpeg")
        img_left = img_left.resize((720,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

# left side insie content
        left_inside_frame=Frame(left_frame,bd=2, relief=RIDGE, bg="white") 
        left_inside_frame.place(x=8,y=135,width=720,height=300)

        # Lables and inputs
        attendanceID_label = Label(left_inside_frame,text="Attendance_ID:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        attendanceID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,textvariable=self.var_id,width=15,font=("verdana",10,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        # Name
        Name_label = Label(left_inside_frame,text="Name.:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        Name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        Name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_name,width=15,font=("verdana",10,"bold"))
        Name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # Roll no.
        Rollno_label = Label(left_inside_frame,text="Department.:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        Rollno_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        Rollno_entry = ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=15,font=("verdana",10,"bold"))
        Rollno_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # Dep
        Department_label = Label(left_inside_frame,text="Roll no.:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        Department_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        Department_entry = ttk.Entry(left_inside_frame,textvariable=self.var_dep,width=15,font=("verdana",10,"bold"))
        Department_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)




        #Time  
        Time_label = Label(left_inside_frame,text="Time:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        Time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        Time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_time,width=15,font=("verdana",10,"bold"))
        Time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date 
        Date_label = Label(left_inside_frame,text="Date:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        Date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        Date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_date,width=15,font=("verdana",10,"bold"))
        Date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

# Attendance label
        attendancelabel = Label(left_inside_frame,text="Attendance-status:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        attendancelabel.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attend,width=20,font="verdana 10 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent") 
        self.atten_status.grid(row=4,column=1,pady=8,sticky=W)
        self.atten_status.current(0)



#Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=450,width=600,height=80)

        #import button
        import_btn=Button(btn_frame,command=self.importCsv,text="Import csv",width=10,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        import_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #export button
        export_btn=Button(btn_frame,command=self.exportCsv,text="Export csv",width=10,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        export_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #update button
        Update_btn=Button(btn_frame,text="Update",width=10,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        Update_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        # Reset
        Reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=10,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        Reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)


          # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=750,y=10,width=730,height=580)

          #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=710,height=455)

         #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL) 

        # create table
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Name","Department","Roll_no","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)


        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Roll_no",text="Roll_no")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Roll_no",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
       
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)

# fetch
    def fetchData(self,rows):
          self.attendanceReport.delete(*self.attendanceReport.get_children())
          for i in rows:
           self.attendanceReport.insert("",END,values=i)
        
# import
    def importCsv(self):
          global mydata
          mydata.clear()
          fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
          with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
              mydata.append(i)
            self.fetchData(mydata)

# export
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    


        



    def get_cursor(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attend.set(data[6])


    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("")
        





if __name__=="__main__":
     root = Tk()
     obj = Attendance(root)
     root.mainloop()
