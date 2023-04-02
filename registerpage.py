from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class register_page:
    def __init__(self,root2):
        self.root2=root2
        self.root2.geometry("1530x790+0+0")
        self.root2.title("Face Attendance System/ Registration")
        self.root2.wm_iconbitmap("iconimg.ico")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_pass=StringVar()
        self.var_confirmpass=StringVar()
        self.var_checkk=IntVar()



        #backroun image
        bg_img=Image.open("images/rgbg.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        fst_lbl=Label(self.root2,image=self.bg_photoimg)
        fst_lbl.place(x=0,y=0,width=1530,height=710)


        # label register
        register=Label(self.root2,text="REGISTER HERE",font=("times new roman",15,"bold"),fg="orange",bg="white")
        register.place(x=30,y=30)


        # label first name
        frst_name=Label(self.root2,text="First Name :",font=("times new roman",15,"bold"),fg="black",bg="white")
        frst_name.place(x=30,y=120)

        self.txtfstname=ttk.Entry(self.root2,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtfstname.place(x=30,y=160,width=230)

         # label last name
        last_name=Label(self.root2,text="Last Name :",font=("times new roman",15,"bold"),fg="black",bg="white")
        last_name.place(x=300,y=120)

        self.txtlstname=ttk.Entry(self.root2,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtlstname.place(x=300,y=160,width=230)

         # email_id
        email_id=Label(self.root2,text="Email :",font=("times new roman",15,"bold"),fg="black",bg="white")
        email_id.place(x=30,y=210)

        self.txteid=ttk.Entry(self.root2,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txteid.place(x=30,y=250,width=230)

         # cotact number
        cont_no=Label(self.root2,text="Contact Number :",font=("times new roman",15,"bold"),fg="black",bg="white")
        cont_no.place(x=300,y=210)

        self.txtcontno=ttk.Entry(self.root2,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txtcontno.place(x=300,y=250,width=230)

        #security question
        securityques=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        securityques.place(x=30,y=300)

        self.combo_security_q=ttk.Combobox(self.root2,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state='readonly',justify=CENTER)
        self.combo_security_q["values"]=("Select","Your Home Town","Your Mother Name","Your Course Name")
        self.combo_security_q.place(x=30,y=340,width=230)
        self.combo_security_q.current(0)


        # csecurity answer
        sec_ans=Label(self.root2,text="Security Answer :",font=("times new roman",15,"bold"),fg="black",bg="white")
        sec_ans.place(x=300,y=300)

        self.txtsecans=ttk.Entry(self.root2,textvariable=self.var_securitya,font=("times new roman",15,"bold"))
        self.txtsecans.place(x=300,y=340,width=230)


         # password
        passw=Label(self.root2,text="Password :",font=("times new roman",15,"bold"),fg="black",bg="white")
        passw.place(x=30,y=390)

        self.txtpassw=ttk.Entry(self.root2,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txtpassw.place(x=30,y=430,width=230)

         # confirm password
        confm_passw=Label(self.root2,text="Confirm Password :",font=("times new roman",15,"bold"),fg="black",bg="white")
        confm_passw.place(x=300,y=390)

        self.txtconfpass=ttk.Entry(self.root2,textvariable=self.var_confirmpass,font=("times new roman",15,"bold"))
        self.txtconfpass.place(x=300,y=430,width=230)

        #checkbutton
        checkbutton=Checkbutton(self.root2,variable=self.var_checkk,text=" I Agree The Terms & Conditions",font=("times new roman", 12,"bold"),onvalue=1,offvalue=0)
        checkbutton.place(x=30,y=490)

       # register button
        rgimg=Image.open("images/register_button.jpg")
        rgimg=rgimg.resize((200,65),Image.ANTIALIAS)
        self.photoimager=ImageTk.PhotoImage(rgimg)

        rb=Button(self.root2,image=self.photoimager,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        rb.place(x=320,y=570,width=200)
        #print("3")


        
         #login button
        lgimg=Image.open("images/login_buttton.jpg")
        lgimg=lgimg.resize((220,75),Image.ANTIALIAS)
        self.photoimagel=ImageTk.PhotoImage(lgimg)

        lb=Button(self.root2,image=self.photoimagel,command=self.returnn_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        lb.place(x=40,y=560,width=220)

    def register_data(self):
        if self.var_fname.get()=="" or  self.var_email.get()=="" or self.var_securityq.get()=="Select" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_securitya.get()=="" or self.var_pass.get()=="" or self.var_confirmpass.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root2)
        elif self.var_email.get().endswith("@gmail.com")==False:
            messagebox.showerror("Error","Please check email format",parent=self.root2)
        elif self.var_fname.get().isalpha()==False:
            messagebox.showerror("Error","Please check check first name",parent=self.root2)
        elif self.var_lname.get().isalpha()==False:
            messagebox.showerror("Error","Please check check last name",parent=self.root2)
        elif len(self.var_email.get())<11:
            messagebox.showerror("Error","Please write complete email",parent=self.root2)
        elif len(self.var_contact.get())!=10:
            messagebox.showerror("Error","Please write correct contact Number",parent=self.root2)
        elif self.var_contact.get().isdigit()!=True:
            messagebox.showerror("Error","Contact number should contain only digits",parent=self.root2)
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","password & confirm password must be same",parent=self.root2)
        elif self.var_checkk.get()==0:
            messagebox.showerror("Error","Please agree our terms and codition",parent=self.root2)
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
                cur=con.cursor()
                queryre=("select * from register where email=%s")
                value=(self.var_email.get(),)
                cur.execute(queryre,value)
                row=cur.fetchone()
                if row!=None: 
                    messagebox.showerror("Error","user already exist,please try another email",parent=self.root2)
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_securityq.get(),
                                                                                        self.var_securitya.get(),
                                                                                        self.var_pass.get(),
                                                                                    
                                                                                    
                                                                                    
                                                                                    ))
                    messagebox.showinfo("Success","Register Successfuliy",parent=self.root2)
                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root2)

    def returnn_login(self):
        self.root2.destroy()
    






if __name__ == "__main__":
    root=Tk()
    obj=register_page(root)
    root.mainloop()