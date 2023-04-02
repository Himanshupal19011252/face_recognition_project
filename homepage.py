
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from student import student_page
import os
from time import strftime
from datetime import datetime
from train import train_data_page
from face_recognition import face_recognition_page
from developer import developer_page
from help import help_page
from atendance import Attendance
import tkinter
import pytz



class home_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System/ Menu")
        self.root.wm_iconbitmap("iconimg.ico")


        # first Text
        l = Label(self.root, text = "FACE ATTENDANCE SYSTEM")
        l.place(x=0,y=0,width=1400,height=60)
        l.config(font =("Courier", 50,"bold"),background="dark cyan",foreground="white")

        #------------------time show-------------------#

        def time():
            home=pytz.timezone('Asia/kolkata')
            local_time=datetime.now(home)
            string=local_time.strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(l, font=('times new roman',14,'bold'),background='dark cyan',foreground='white')
        lbl.place(x=2,y=2,width=110,height=50)
        time()



        #backrounf image
        bg_img=Image.open("images/homebg.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        fst_lbl=Label(self.root,image=self.bg_photoimg)
        fst_lbl.place(x=0,y=70,width=1500,height=710)


        # add_student
        st_add_image=Image.open("images/student_add_logo.png")
        st_add_image=st_add_image.resize((120,120),Image.ANTIALIAS)
        self.st_add_photoimg=ImageTk.PhotoImage(st_add_image)


        B1=Button(self.root,image=self.st_add_photoimg,command=self.student_detail,cursor="hand2")
        B1.place(x=40,y=90,width=140,height=140)

        b1=Button(self.root,text="Add Students",command=self.student_detail,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b1.place(x=40,y=220,width=140,height=30)
      

        # face_recognition
        fr_img=Image.open("images/face_recognition.jpg")
        fr_img=fr_img.resize((145,145),Image.ANTIALIAS)
        self.fr_photoimg=ImageTk.PhotoImage(fr_img)


        B2=Button(self.root,image=self.fr_photoimg,command=self.face_recognize,cursor="hand2")
        B2.place(x=200,y=90,width=150,height=140)

        b2=Button(self.root,text="Face Recognition",command=self.face_recognize,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b2.place(x=200,y=220,width=150,height=30)
      

       # attendance
        att_img=Image.open("images/attendance_logo.png")
        att_img=att_img.resize((140,140),Image.ANTIALIAS)
        self.att_photoimg=ImageTk.PhotoImage(att_img)


        B3=Button(self.root,image=self.att_photoimg,command=self.attendance,cursor="hand2")
        B3.place(x=370,y=90,width=140,height=140)

        b3=Button(self.root,text="Attendance",command=self.attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b3.place(x=370,y=220,width=140,height=30)


         # help_desk
        hd_img=Image.open("images/helpdesk_logo.png")
        hd_img=hd_img.resize((120,120),Image.ANTIALIAS)
        self.hd_photoimg=ImageTk.PhotoImage(hd_img)


        B4=Button(self.root,image=self.hd_photoimg,cursor="hand2",command=self.help_detail)
        B4.place(x=530,y=90,width=140,height=140)

        b4=Button(self.root,text="Help",cursor="hand2",command=self.help_detail,font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b4.place(x=530,y=220,width=140,height=30)


         # trained_data
        td_img=Image.open("images/trained_data.png")
        td_img=td_img.resize((120,120),Image.ANTIALIAS)
        self.td_photoimg=ImageTk.PhotoImage(td_img)


        B5=Button(self.root,image=self.td_photoimg,command=self.train_detail,cursor="hand2")
        B5.place(x=40,y=300,width=140,height=140)

        b5=Button(self.root,text="Train Data",command=self.train_detail,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b5.place(x=40,y=420,width=140,height=30)


         # photos
        ph_img=Image.open("images/photos.png")
        ph_img=ph_img.resize((120,120),Image.ANTIALIAS)
        self.ph_photoimg=ImageTk.PhotoImage(ph_img)


        B6=Button(self.root,image=self.ph_photoimg,cursor="hand2",command=self.open_img)
        B6.place(x=200,y=300,width=150,height=140)

        b6=Button(self.root,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b6.place(x=200,y=420,width=150,height=30)


         # Developer
        dv_img=Image.open("images/developer_logo.jpg")
        dv_img=dv_img.resize((100,100),Image.ANTIALIAS)
        self.dv_photoimg=ImageTk.PhotoImage(dv_img)


        B7=Button(self.root,image=self.dv_photoimg,cursor="hand2",command=self.developer_detail)
        B7.place(x=370,y=300,width=140,height=140)

        b7=Button(self.root,text="Devloper",cursor="hand2",command=self.developer_detail,font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b7.place(x=370,y=420,width=140,height=30)
      

         # Exit
        ex_img=Image.open("images/exit_logo.png")
        ex_img=ex_img.resize((120,120),Image.ANTIALIAS)
        self.ex_photoimg=ImageTk.PhotoImage(ex_img)


        B8=Button(self.root,image=self.ex_photoimg,command=self.Exit,cursor="hand2")
        B8.place(x=530,y=300,width=140,height=140)

        b8=Button(self.root,text="Exit",cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="blue",fg="White",activeforeground="white",activebackground="blue")
        b8.place(x=530,y=420,width=140,height=30)
      

         # second Text
        l2 = Label(self.root, text = "press button according to your need")
        l2.place(x=40,y=550,width=630,height=50)
        l2.config(font =("Courier", 20,"bold"),background="white",foreground="blue")



        # last Text
        l3 = Label(self.root, text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE DEVELOPED BY HIMANSHU PAL")
        l3.place(x=0,y=680,width=1400,height=30)
        l3.config(font =("Courier", 20,"bold"),background="magenta",foreground="white")


    def open_img(self):
        os.startfile("data")

    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.detail=student_page(self.new_window)

    def train_detail(self):
        self.new_window=Toplevel(self.root)
        self.detail=train_data_page(self.new_window)
    
    def developer_detail(self):
        self.new_window=Toplevel(self.root)
        self.detail=developer_page(self.new_window)
    
    def help_detail(self):
        self.new_window=Toplevel(self.root)
        self.detail=help_page(self.new_window)

    def face_recognize(self):
        self.new_window=Toplevel(self.root)
        self.detail=face_recognition_page(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.detail=Attendance(self.new_window)

    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face Rcognition","Are you sure exit this project",parent=self.root)
        if self.Exit>0:
            self.root.destroy()
        else:
            return
      



if __name__ == "__main__":
    root=Tk()
    obj=home_page(root)
    root.mainloop()