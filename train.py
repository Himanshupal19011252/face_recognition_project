from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from tkinter import messagebox


class train_data_page:

    def __init__(self,root):
        self.root_train=root
        self.root_train.geometry("1530x790+0+0")
        self.root_train.title("Face Attendance System/ Train Data ")
        self.root_train.wm_iconbitmap("iconimg.ico")

        #backroun image
        trainbg_img=Image.open("images/trainedimage.jpg")
        trainbg_img=trainbg_img.resize((1530,710),Image.ANTIALIAS)
        self.trainbg_photoimg=ImageTk.PhotoImage(trainbg_img)

        fst_trainlbl=Label(self.root_train,image=self.trainbg_photoimg)
        fst_trainlbl.place(x=0,y=0,width=1530,height=710)

        #trainbutton
        train_btn=Button(self.root_train,text="Train Data",command=self.train_classifier,font=("times new roman",25,"bold"),bd=3,relief=RIDGE,fg="white",bg="orange",activeforeground="white",activebackground="orange")
        train_btn.place(x=520,y=610,width=465,height=90)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Grays cale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #--------------Train the classifier And save--------------------#
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainnig datasets completed!",parent=self.root_train)
        





if __name__ =="__main__":
    root=Tk()
    obj=train_data_page(root)
    root.mainloop()