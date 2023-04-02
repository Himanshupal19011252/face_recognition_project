
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk


class developer_page:

    def __init__(self,rootdev):
        self.rootdev=rootdev
        self.rootdev.geometry("1530x790+0+0")
        self.rootdev.title("Face Attendance System/ About Developer")
        self.rootdev.wm_iconbitmap("iconimg.ico")

        #backroun image
        devbg_img=Image.open("images/dev_bg.jpg")
        devbg_img=devbg_img.resize((1530,710),Image.ANTIALIAS)
        self.devbg_photoimg=ImageTk.PhotoImage(devbg_img)

        fst_devlbl=Label(self.rootdev,image=self.devbg_photoimg)
        fst_devlbl.place(x=0,y=0,width=1530,height=710)

        dev_info=Label(self.rootdev,text="       DEVELOPER INFORMATION      ",font=("times new roman",40,"bold"),fg="white",bg="orange")
        dev_info.place(x=450,y=20)

        frame=Frame(self.rootdev,bg="white")
        frame.place(x=450,y=85,width=910,height=375)

        frame2=Frame(frame,bg="black")
        frame2.place(x=15,y=10,width=660,height=340)


       # label 
        dev_info1=Label(frame2,text="Hello I am Himanshu Pal",font=("times new roman",20,"bold"),fg="white",bg="black")
        dev_info1.place(x=10,y=20)

        dev_info2=Label(frame2,text="I am Student of Graphic era hill University, Dehradun",font=("times new roman",20,"bold"),fg="white",bg="black")
        dev_info2.place(x=10,y=70)

        dev_info3=Label(frame2,text="Now I am in 3rd Year from B.tech (CSE)",font=("times new roman",20,"bold"),fg="white",bg="black")
        dev_info3.place(x=10,y=130)

        dev_info4=Label(frame2,text="About : This project made by using tkinter,",font=("times new roman",20,"bold"),fg="white",bg="black")
        dev_info4.place(x=10,y=180)

        dev_info5=Label(frame2,text="Python and OpenCV",font=("times new roman",20,"bold"),fg="white",bg="black")
        dev_info5.place(x=10,y=230)

        dev_info6=Label(frame2,text="Graduation Year : 2019-2023",font=("times new roman",20,"bold"),fg="white",bg="black")
        dev_info6.place(x=10,y=280)


        #my image
        my_img=Image.open("images/myphoto.jpg")
        my_img=my_img.resize((200,465),Image.ANTIALIAS)
        self.my_photoimg=ImageTk.PhotoImage(my_img)

        my_lbl=Label(frame,image=self.my_photoimg)
        my_lbl.place(x=680,y=10,width=220,height=340)



   





if __name__ == "__main__":
    windev=Tk()
    appdev=developer_page(windev)
    windev.mainloop()
