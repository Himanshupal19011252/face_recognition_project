from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import os
from tkinter import messagebox 
import csv
from tkinter import filedialog

mydata=[]


class Attendance:

    def __init__(self,root):
        self.root_attendance=root
        self.root_attendance.geometry("1530x790+0+0")
        self.root_attendance.title("Face Attendance System/ attendance ")
        self.root_attendance.wm_iconbitmap("iconimg.ico")

        #-----------------variabls---------------3
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #backroun image short view1
        abg_img1=Image.open("images/erastudent1.jpg")
        abg_img1=abg_img1.resize((500,130),Image.ANTIALIAS)
        self.abg_photoimg1=ImageTk.PhotoImage(abg_img1)

        abgd_img1=Label(self.root_attendance,image=self.abg_photoimg1)
        abgd_img1.place(x=0,y=0,width=500,height=130)

        #backroun image short view2
        abg_img2=Image.open("images/att_hands.jpg")
        abg_img2=abg_img2.resize((400,130),Image.ANTIALIAS)
        self.sbg_photoimg2=ImageTk.PhotoImage(abg_img2)

        sbgd_img2=Label(self.root_attendance,image=self.sbg_photoimg2)
        sbgd_img2.place(x=500,y=0,width=400,height=130)

        #backroun image short view3
        abg_img3=Image.open("images/erastudent1.jpg")
        abg_img3=abg_img3.resize((500,130),Image.ANTIALIAS)
        self.abg_photoimg3=ImageTk.PhotoImage(abg_img3)

        abgd_img3=Label(self.root_attendance,image=self.abg_photoimg3)
        abgd_img3.place(x=900,y=0,width=500,height=130)

        #background image
        bg_img=Image.open("images/greenbg.png")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgd_img=Label(self.root_attendance,image=self.bg_photoimg)
        bgd_img.place(x=0,y=120,width=1530,height=710)

         #first frame
        fst_frame=Frame(bgd_img,bd=2)
        fst_frame.place(x=20,y=10,width=1320,height=560)

        #left frame
        left_frame=LabelFrame(fst_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=670,height=540)

        
        #right frame
        right_frame=LabelFrame(fst_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=690,y=10,width=620,height=540)

        #graphic era hill university
        era_img=Image.open("images/lera.jpg")
        era_img=era_img.resize((600,110),Image.ANTIALIAS)
        self.era_photoimg=ImageTk.PhotoImage(era_img)

        era_imgla=Label(left_frame,image=self.era_photoimg)
        era_imgla.place(x=20,y=0,width=600,height=120)

         #--------------------------attendance information----------------------#
        attendance_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        attendance_frame.place(x=10,y=140,width=650,height=350)


        #Labeland entry 
        
        attendance_id=Label(attendance_frame,text="Student id:",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_id.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        self.txtatt_id=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        self.txtatt_id.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #roll
        attendance_un_roll_no=Label(attendance_frame,text="un roll no :",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_un_roll_no.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        self.txtatt_un_roll_no=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        self.txtatt_un_roll_no.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #name
        attendance_name=Label(attendance_frame,text="Student Name:",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_name.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        self.txtatt_name=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        self.txtatt_name.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Department
        attendance_dep=Label(attendance_frame,text="Department :",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_dep.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        self.txtatt_dep=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        self.txtatt_dep.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #time
        attendance_time=Label(attendance_frame,text="Time:",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_time.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        self.txtatt_time=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        self.txtatt_time.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Date
        attendance_date=Label(attendance_frame,text="Date:",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_date.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        self.txtatt_date=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        self.txtatt_date.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Attendance status
        attendance_lbl=Label(attendance_frame,text="Attendance Status : ",font=("times new roman",12,"bold"),fg="black",bg="white")
        attendance_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        self.txtatt_date=ttk.Entry(attendance_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"))
        self.txtatt_date.grid(row=3,column=1,padx=10,pady=10,sticky=W)

       #-------------------------buttons-----------------#
        buttons_frame=LabelFrame(attendance_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        buttons_frame.place(x=50,y=310,width=480,height=35)

        #import csv
        btn_save=Button(buttons_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        btn_save.grid(row=0,column=0,sticky=W)

        # Export csv
        btn_Update=Button(buttons_frame,text="Export csv",width=17,command=self.exportCSV,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        btn_Update.grid(row=0,column=1,sticky=W)

        #Reset button
        btn_Reset=Button(buttons_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        btn_Reset.grid(row=0,column=3,sticky=W)


        #----------------table frame-----------------------------------#
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=14,y=15,width=590,height=480)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Attendance_table=ttk.Treeview(table_frame,column=("id","roll","name","Department","time","date","attendance status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Attendance_table.xview)
        scroll_y.config(command=self.Attendance_table.yview)

        self.Attendance_table.heading("id",text="student id")
        self.Attendance_table.heading("roll",text="Un roll no")
        self.Attendance_table.heading("name",text="student name")
        self.Attendance_table.heading("Department",text="Department")
        self.Attendance_table.heading("time",text="time")
        self.Attendance_table.heading("date",text="date")
        self.Attendance_table.heading("attendance status",text="Attendance status")

        
        self.Attendance_table["show"]="headings"


        self.Attendance_table.column("id",width=100)
        self.Attendance_table.column("roll",width=100)
        self.Attendance_table.column("name",width=100)
        self.Attendance_table.column("Department",width=100)
        self.Attendance_table.column("time",width=100)
        self.Attendance_table.column("date",width=100)
        self.Attendance_table.column("attendance status",width=100)

        self.Attendance_table.pack(fill=BOTH,expand=1)

        self.Attendance_table.bind("<ButtonRelease>",self.get_cursor)

    #------------fetch-------------------------#

    def fetchData(self,rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root_attendance)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
              messagebox.showerror("No Data","No Data found to export",parent=self.root_attendance)
              return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root_attendance)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data Export","Your data exported to "+os.path.basename(fln)+"successfully",parent=self.root_attendance)     
        except Exception as es:
                  messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root_attendance) 


    def get_cursor(self,event=""):
        cursor_row=self.Attendance_table.focus()
        content=self.Attendance_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
