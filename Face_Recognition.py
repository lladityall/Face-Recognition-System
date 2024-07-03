from tkinter import*
from sys import path
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
import numpy as np
import cv2
import os



class face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x750+0+0")
        self.root.title("face_recogntion")



#Title
        title_lbl=Label(self.root,text = "Welcome to Face Recognition Pannel",font=("Roboto",35,"bold"),bg="Grey",fg="Black")
        title_lbl.place(x=0,y=0,width=1540,height=45)

# Left image
        img_top = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\face_detector1.jpg")
        img_top = img_top.resize((650,700))
        self.img_top = ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image = self.img_top)
        first_lbl.place(x = 0,y=45,width=650,height = 700)

# Right Image
        img_bottom = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\face_detector2.jpg")
        img_bottom = img_bottom.resize((950,700))
        self.img_bottom = ImageTk.PhotoImage(img_bottom)

        first_lbl = Label(self.root,image = self.img_bottom)
        first_lbl.place(x = 650,y=45,width=950,height = 700)

# Button
        b2_1= Button(first_lbl,command=self.face_recog  ,text = "Face Recognition",cursor="hand2",font=("Roboto",15,"bold"),bg="cyan",fg="white")
        b2_1.place(x=375,y=590,width=200,height=40)

            #=====================Attendance===================

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n},{d}, {dtString}, {d1}, Present")

 #================face recognition==================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))



                conn = mysql.connector.connect(username='root', password='Aditya@136',host='localhost',database='facerecognition',port=3306)
                cursor = conn.cursor()

                

                cursor.execute("select Name from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Department from student where Student_ID="+str(id))
                d=cursor.fetchone()
                d="+".join(d)

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=cursor.fetchone()
                i="+".join(i)



                


                if confidence > 80:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


 


# Recognization
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1)==13:
                break
        videoCap.release()
        cv2.destroyAllWindows()
            





if __name__=="__main__":
     root = Tk()
     obj = face_recognition(root)
     root.mainloop()