from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import numpy as np
import cv2
import os



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1600x750+0+0")
        self.root.title("Train")


 #Title
        title_lbl=Label(self.root,text = "TRAIN DATASET",font=("Roboto",35,"bold"),bg="blue",fg="White")
        title_lbl.place(x=0,y=0,width=1540,height=45)

# Top Image
        img_top = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\facialrecognition.png")
        img_top = img_top.resize((1550,330))
        self.img_top = ImageTk.PhotoImage(img_top)


        first_lbl = Label(self.root,image = self.img_top)
        first_lbl.place(x = 0,y=45,width=1550,height = 325)

# Bottom Image
        img_bottom = Image.open(r"C:\Users\Aditya\Downloads\face_recognition_system-20230221T135317Z-001\face_recognition_system\college_images\people.jpg")
        img_bottom = img_bottom.resize((1550,330))
        self.img_bottom = ImageTk.PhotoImage(img_bottom)


        first_lbl = Label(self.root,image = self.img_bottom)
        first_lbl.place(x = 0,y=440,width=1550,height = 325)



# Button
        b2_1= Button(self.root,text = "TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Roboto",15,"bold"),bg="black",fg="white")
        b2_1.place(x=0,y=360,width=1560,height=80)





# training dataset

    def train_classifier(self):
        data_dir=("dataimg")
        path=[ os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
    
        #Train Classifier
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)











if __name__=="__main__":
     root = Tk()
     obj = Train(root)
     root.mainloop()

