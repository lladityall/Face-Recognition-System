from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
# from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x750+0+0")
        self.root.title("Face_Recogonition_System")



# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\facial_recognition_action.jpg")
        img=img.resize((1553,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=80,y=20,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\images.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=80,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\face_detector1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=350,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Suyash Labde",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=350,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\face_detector1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=580,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Kartik patel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=580,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\aditya13.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=810,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Aditya patil",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=810,y=380,width=180,height=45)

        


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()