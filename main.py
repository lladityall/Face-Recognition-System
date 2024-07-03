from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from Face_Recognition import face_recognition
from attendance import Attendance
from devloper import Developer
from Help import Helpsupport


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









if __name__=="__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()









  
