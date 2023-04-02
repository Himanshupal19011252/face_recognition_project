from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
from time import strftime
from registerpage import register_page
from homepage import home_page
from datetime import datetime
import numpy as np


#----------------------------------login class-----------------------------------#


class login_page:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System/ Login")
        self.root.wm_iconbitmap("iconimg.ico")

        #backroun image
        bg_img=Image.open("images/lgbg.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        fst_lbl=Label(self.root,image=self.bg_photoimg)
        fst_lbl.place(x=0,y=0,width=1530,height=710)

        frame=Frame(self.root,bg="black")
        frame.place(x=550,y=155,width=300,height=375)

        #login image
        lg_img=Image.open("images/user_icon.jpg")
        lg_img=lg_img.resize((150,170),Image.ANTIALIAS)
        self.lg_photoimg=ImageTk.PhotoImage(lg_img)

        sec_lbl=Label(self.root,image=self.lg_photoimg)
        sec_lbl.place(x=650,y=160,width=100,height=100)


       # label username
        username=Label(frame,text="Username :",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=120)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=160,width=250)

         # label password
        password=Label(frame,text="Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=200)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=30,y=240,width=250)

        #image_icon1
        ui_img=Image.open("images/user_icon.jpg")
        ui_img=ui_img.resize((35,35),Image.ANTIALIAS)
        self.ui_photoimg=ImageTk.PhotoImage(ui_img)

        ui_lbl=Label(self.root,image=self.ui_photoimg)
        ui_lbl.place(x=580,y=275,width=25,height=25)

        #image_icon2
        ps_img=Image.open("images/lock.jpg")
        ps_img=ps_img.resize((40,40),Image.ANTIALIAS)
        self.ps_photoimg=ImageTk.PhotoImage(ps_img)

        ps_lbl=Label(self.root,image=self.ps_photoimg)
        ps_lbl.place(x=580,y=355,width=25,height=25)


        #loginbutton
        login_btn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=90,y=290,width=120,height=35)

        #registerbutton
        reg_btn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="red",bg="black",activeforeground="red",activebackground="black")
        reg_btn.place(x=30,y=340,width=120,height=30)

        #forgetpasword
        for_pass=Button(frame,text="Forget Password",command=self.forget_window,font=("times new roman",10,"bold"),borderwidth=0,fg="red",bg="black",activeforeground="red",activebackground="black")
        for_pass.place(x=150,y=340,width=120,height=30)


       
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register_page(self.new_window)
        

        

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please fill all required fields",parent=self.root)
        else:
            log_con=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
            log_cur=log_con.cursor()
            log_cur.execute(" select * from register where email=%s and password=%s",(

                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                    ))
            var=log_cur.fetchone()
            if var==None:
                messagebox.showerror("Invalid","Invalid username and password",parent=self.root)
            else:
                openn=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                if openn>0:
                    self.new_window2=Toplevel(self.root)
                    self.app=home_page(self.new_window2)
                else:
                   if not openn:
                    return
            log_con.commit()
            log_con.close()

    def reset_password(self):
        if self.combo_forsecurity_q.get()=="Select" and self.txtforsecans.get()=="" and self.txtforpassw.get()=="":
            messagebox.showerror("Error","Please fill all details",parent=self.root)
        elif self.combo_forsecurity_q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root)
        elif self.txtforsecans.get()=="":
            messagebox.showerror("Error","Please enter the Security answer",parent=self.root)
        elif self.txtforpassw.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root)
        else:
            res_con=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
            res_cur=res_con.cursor()
            queryreset=(" select * from register where email=%s and securityq=%s and securitya=%s")
            value=(self.txtuser.get(),self.combo_forsecurity_q.get(),self.txtforsecans.get(),)
            res_cur.execute(queryreset,value)
            resvar=res_cur.fetchone()
            if resvar==None:
                messagebox.showerror("Error","Please enter correct details",parent=self.root)
            else:
                resquery2=("update register set password=%s where email=%s")
                value=(self.txtforpassw.get(),self.txtuser.get())
                res_cur.execute(resquery2,value)
                res_con.commit()
                res_con.close()
                messagebox.showinfo("Info","Your password has been reset, now you can login with new password",parent=self.root)





    def forget_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter email",parent=self.root)
        else:
            for_con=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
            for_cur=for_con.cursor()
            query=(" select * from register where email=%s")
            value=(self.txtuser.get(),)
            for_cur.execute(query,value)
            forvar=for_cur.fetchone()
            if forvar==None:
                messagebox.showerror("Invalid","Email does not exits",parent=self.root)
            else:
                for_con.close()
                self.for_root=Toplevel()
                self.for_root.title("forget Password")
                self.for_root.geometry("340x400+530+150")
             
                forget=Label(self.for_root,text="Forget Password",font=("times new roman",15,"bold"),fg="orange",bg="white")
                forget.place(x=90,y=10)

                #security question
                forsecurityques=Label(self.for_root,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                forsecurityques.place(x=50,y=60)

                self.combo_forsecurity_q=ttk.Combobox(self.for_root,font=("times new roman",15,"bold"),state='readonly',justify=CENTER)
                self.combo_forsecurity_q["values"]=("Select","Your Home Town","Your Mother Name","Your Course Name")
                self.combo_forsecurity_q.place(x=50,y=110,width=250)
                self.combo_forsecurity_q.current(0)


                # csecurity answer
                forsec_ans=Label(self.for_root,text="Security Answer :",font=("times new roman",15,"bold"),fg="black",bg="white")
                forsec_ans.place(x=50,y=160)

                self.txtforsecans=ttk.Entry(self.for_root,font=("times new roman",15,"bold"))
                self.txtforsecans.place(x=50,y=210,width=250)


                # password
                forpassw=Label(self.for_root,text="New Password :",font=("times new roman",15,"bold"),fg="black",bg="white")
                forpassw.place(x=50,y=260)

                self.txtforpassw=ttk.Entry(self.for_root,font=("times new roman",15,"bold"))
                self.txtforpassw.place(x=50,y=310,width=250)

                fb=Button(self.for_root,text="Reset",command=self.reset_password,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="orange",activebackground="orange",activeforeground="white")
                fb.place(x=120,y=350,width=100)




if __name__ == "__main__":
    root=Tk()
    obj=login_page(root)
    root.mainloop()
    