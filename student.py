from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os



class student_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System/student Management")
        self.root.wm_iconbitmap("iconimg.ico")



        #-------------------variable----------------#
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_unroll_no=StringVar()
        self.var_classroll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phoneno=StringVar()
        self.var_father=StringVar()
        self.var_teacher=StringVar()

        
        

        #backroun image short view1
        sbg_img1=Image.open("images/erastudent1.jpg")
        sbg_img1=sbg_img1.resize((500,130),Image.ANTIALIAS)
        self.sbg_photoimg1=ImageTk.PhotoImage(sbg_img1)

        sbgd_img1=Label(self.root,image=self.sbg_photoimg1)
        sbgd_img1.place(x=0,y=0,width=500,height=130)

        #backroun image short view2
        sbg_img2=Image.open("images/lera.jpg")
        sbg_img2=sbg_img2.resize((400,130),Image.ANTIALIAS)
        self.sbg_photoimg2=ImageTk.PhotoImage(sbg_img2)

        sbgd_img2=Label(self.root,image=self.sbg_photoimg2)
        sbgd_img2.place(x=500,y=0,width=400,height=130)

        #backroun image short view3
        sbg_img3=Image.open("images/erastudent1.jpg")
        sbg_img3=sbg_img3.resize((500,130),Image.ANTIALIAS)
        self.sbg_photoimg3=ImageTk.PhotoImage(sbg_img3)

        sbgd_img3=Label(self.root,image=self.sbg_photoimg3)
        sbgd_img3.place(x=900,y=0,width=500,height=130)

        #backroun image
        bg_img=Image.open("images/o1.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        bgd_img=Label(self.root,image=self.bg_photoimg)
        bgd_img.place(x=0,y=120,width=1530,height=710)


        #first frame
        fst_frame=Frame(bgd_img,bd=2)
        fst_frame.place(x=20,y=10,width=1320,height=560)

        #left frame
        left_frame=LabelFrame(fst_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=640,height=540)

        
        #right frame
        right_frame=LabelFrame(fst_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=660,y=10,width=640,height=540)

        #graphic era hill university
        era_img=Image.open("images/searchimgly.jpg")
        era_img=era_img.resize((600,130),Image.ANTIALIAS)
        self.era_photoimg=ImageTk.PhotoImage(era_img)

        era_imgla=Label(right_frame,image=self.era_photoimg)
        era_imgla.place(x=20,y=0,width=600,height=120)

        #--------------------------current course information----------------------#
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=10,width=615,height=100)
        
        #department
        department_lbl=Label(current_course_frame,text="Department ",font=("times new roman",10,"bold"),fg="black",bg="white")
        department_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        department_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state='readonly',justify=CENTER)
        department_combo["values"]=("Select","Computer science","Machanical","Civil","IT","ART","Management","Medical")
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=15,pady=5,sticky=W)


        #course
        course_lbl=Label(current_course_frame,text="Course ",font=("times new roman",10,"bold"),fg="black",bg="white")
        course_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state='readonly',justify=CENTER)
        course_combo["values"]=("Select","B.tech","B.pharma","BSC","M.tech","GNM","MSC","PHD")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=15,pady=5,sticky=W)
        

        #year
        year_lbl=Label(current_course_frame,text="Year ",font=("times new roman",10,"bold"),fg="black",bg="white")
        year_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state='readonly',justify=CENTER)
        year_combo["values"]=("Select","2021-2022","2022-2023","2023-2024","2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=15,pady=5,sticky=W)


        #semester
        sem_lbl=Label(current_course_frame,text="Semester ",font=("times new roman",10,"bold"),fg="black",bg="white")
        sem_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",10,"bold"),state='readonly',justify=CENTER)
        sem_combo["values"]=("Select","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=15,pady=5,sticky=W)


        # ------------------class student information ------------------------------#
        classstudent_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        classstudent_frame.place(x=10,y=130,width=615,height=370)

        
        # label student id
        st_id=Label(classstudent_frame,text="Student id:",font=("times new roman",12,"bold"),fg="black",bg="white")
        st_id.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        self.txtst_id=ttk.Entry(classstudent_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        self.txtst_id.grid(row=0,column=1,padx=10,pady=10,sticky=W)

         # label student Name
        st_name=Label(classstudent_frame,text="Student Name:",font=("times new roman",12,"bold"),fg="black",bg="white")
        st_name.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        self.txtst_name=ttk.Entry(classstudent_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        self.txtst_name.grid(row=0,column=3,padx=10,pady=10,sticky=W)


        # label student University Roll_no
        st_unirollno=Label(classstudent_frame,text="Un roll_no:",font=("times new roman",12,"bold"),fg="black",bg="white")
        st_unirollno.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        self.txtst_unirollno=ttk.Entry(classstudent_frame,textvariable=self.var_unroll_no,width=20,font=("times new roman",12,"bold"))
        self.txtst_unirollno.grid(row=1,column=1,padx=10,pady=10,sticky=W)

         # label student class roll no
        cl_roll_no=Label(classstudent_frame,text="Class Roll No:",font=("times new roman",12,"bold"),fg="black",bg="white")
        cl_roll_no.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        self.txtcl_roll_no=ttk.Entry(classstudent_frame,textvariable=self.var_classroll_no,width=20,font=("times new roman",12,"bold"))
        self.txtcl_roll_no.grid(row=1,column=3,padx=10,pady=10,sticky=W)


        # label student gender
        gender_lbl=Label(classstudent_frame,text="Gender: ",font=("times new roman",12,"bold"),fg="black",bg="white")
        gender_lbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state='readonly',justify=CENTER)
        gender_combo["values"]=("Select","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

         # Date of birth
        dob=Label(classstudent_frame,text="DOB :",font=("times new roman",12,"bold"),fg="black",bg="white")
        dob.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        self.txtdob=ttk.Entry(classstudent_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        self.txtdob.grid(row=2,column=3,padx=10,pady=10,sticky=W)


        # label email
        st_email=Label(classstudent_frame,text="Email:",font=("times new roman",12,"bold"),fg="black",bg="white")
        st_email.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        self.txtst_email=ttk.Entry(classstudent_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        self.txtst_email.grid(row=3,column=1,padx=10,pady=10,sticky=W)

         # lable phone no
        phone_no=Label(classstudent_frame,text="Phone No. :",font=("times new roman",12,"bold"),fg="black",bg="white")
        phone_no.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        self.txtphone_no=ttk.Entry(classstudent_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",12,"bold"))
        self.txtphone_no.grid(row=3,column=3,padx=10,pady=10,sticky=W)


        # label father
        st_father=Label(classstudent_frame,text="Father :",font=("times new roman",12,"bold"),fg="black",bg="white")
        st_father.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        self.txtst_father=ttk.Entry(classstudent_frame,textvariable=self.var_father,width=20,font=("times new roman",12,"bold"))
        self.txtst_father.grid(row=4,column=1,padx=10,pady=10,sticky=W)

         # lable teacher name
        phone_no=Label(classstudent_frame,text="Teacher Name :",font=("times new roman",12,"bold"),fg="black",bg="white")
        phone_no.grid(row=4,column=2,padx=10,pady=10,sticky=W)

        self.txtphone_no=ttk.Entry(classstudent_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        self.txtphone_no.grid(row=4,column=3,padx=10,pady=10,sticky=W)

        #radio Buttons photo sample
        photo_sample=Label(classstudent_frame,text="Photo Sample",font=("times new roman",10,"bold"),fg="black",bg="white")
        photo_sample.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        self.var_radio=StringVar()

        radiobtn1=ttk.Radiobutton(classstudent_frame,variable=self.var_radio,text="Yes",value="Yes")
        radiobtn1.grid(row=5,column=1,sticky=W)
      

        radiobtn2=ttk.Radiobutton(classstudent_frame,variable=self.var_radio,text="No",value="No")
        radiobtn2.grid(row=5,column=2,sticky=W)

        #----------buttons frame--------------#
        buttons_frame=LabelFrame(classstudent_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        buttons_frame.place(x=15,y=270,width=580,height=35)

        #save button
        btn_save=Button(buttons_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_save.grid(row=0,column=0,sticky=W)

        #Update button
        btn_Update=Button(buttons_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_Update.grid(row=0,column=1,sticky=W)

        #Delete button
        btn_Delete=Button(buttons_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_Delete.grid(row=0,column=2,sticky=W)

        #Reset button
        btn_Reset=Button(buttons_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_Reset.grid(row=0,column=3,sticky=W)

        #-------------------------button second frame----------------------------#
        buttons_frame2=LabelFrame(classstudent_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        buttons_frame2.place(x=15,y=305,width=580,height=35)

        #Take Photo Sample button
        btn_Take_Photo_Sample=Button(buttons_frame2,command=self.generate_dataset,text="Take Photo Sample",width=63,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_Take_Photo_Sample.grid(row=1,column=0,sticky=W)

        #-------------------------search frame----------------------------#
        search_frame=LabelFrame(right_frame,bd=2,bg="white",text="Search Records",relief=RIDGE,font=("times new roman",12,"bold"))
        search_frame.place(x=20,y=130,width=600,height=100)

        search=Label(search_frame,text="Search by : \tStudent Id ",font=("times new roman",10,"bold"),fg="black",bg="white")
        search.grid(row=0,column=0,padx=20,pady=5,sticky=W)
        self.var_search_std_id=StringVar()
        
         # type here
        typehere=Label(search_frame,text="Type Here :",font=("times new roman",10,"bold"),fg="black",bg="white")
        typehere.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        self.txttypehere=ttk.Entry(search_frame,textvariable=self.var_search_std_id,width=20,font=("times new roman",10,"bold"))
        self.txttypehere.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #search an dshow all btn frame
        searchbtn_frame=LabelFrame(search_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        searchbtn_frame.place(x=20,y=40,width=520,height=35)

        #search button
        btn_search=Button(searchbtn_frame,text="Search",width=28,command=self.search_data,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_search.grid(row=1,column=0)

        #show all button
        btn_showall=Button(searchbtn_frame,text="Show All",width=27,command=self.fetch_data,font=("times new roman",12,"bold"),bg="orange",fg="white",activebackground="orange",activeforeground="white")
        btn_showall.grid(row=1,column=2)
  

        #----------------table frame-----------------------------------#
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=17,y=235,width=605,height=280)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","Un roll no","class roll no","gender","DOB","email","phone no","Father","Teacher Name","Photo Sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student id")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("Un roll no",text="Un roll no")
        self.student_table.heading("class roll no",text="Class roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email id")
        self.student_table.heading("phone no",text="Phone No")
        self.student_table.heading("Father",text="Father Name")
        self.student_table.heading("Teacher Name",text="Teacher Name")
        self.student_table.heading("Photo Sample",text="Photo Sample")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("Un roll no",width=100)
        self.student_table.column("class roll no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone no",width=100)
        self.student_table.column("Father",width=100)
        self.student_table.column("Teacher Name",width=100)
        self.student_table.column("Photo Sample",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

        #-------function declaration-----------------#

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year"  or self.var_sem.get()=="Select Semester"  or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_unroll_no.get()=="" or self.var_classroll_no.get()=="" or self.var_gender.get()==""  or self.var_dob.get()==""  or self.var_email.get()=="" or self.var_phoneno.get()==""  or self.var_father.get()=="" or self.var_teacher.get()=="" or self.var_radio.get()=="" :
            messagebox.showerror("Error","All field are required",parent=self.root)
        elif self.var_email.get().endswith("@gmail.com")==False:
            messagebox.showerror("Error","Please check email format",parent=self.root)
        elif len(self.var_email.get())<11:
            messagebox.showerror("Error","Please write complete email",parent=self.root)
        elif len(self.var_phoneno.get())!=10:
            messagebox.showerror("Error","Please write correct contact Number",parent=self.root)
        elif self.var_phoneno.get().isdigit()!=True:
            messagebox.showerror("Error","Contact number should contain only digits",parent=self.root)
        elif self.var_std_name.get().replace(' ','').isalpha()==False:
            messagebox.showerror("Error","Please type correct student name",parent=self.root)
        elif self.var_father.get().replace(' ','').isalpha()==False:
            messagebox.showerror("Error","Please type correct father name",parent=self.root)
        elif self.var_teacher.get().replace(' ','').isalpha()==False:
            messagebox.showerror("Error","Please type correct teacher name",parent=self.root)
        elif self.var_unroll_no.get().isdigit()!=True:
           messagebox.showerror("Error","university roll no should contain only digits",parent=self.root)
        elif self.var_classroll_no.get().isdigit()!=True:
           messagebox.showerror("Error","class roll no should contain only digits",parent=self.root)
        elif self.var_std_id.get().isdigit()!=True:
           messagebox.showerror("Error","student id should contain only digits",parent=self.root)
        else:
            try:
                scon=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
                scur=scon.cursor()
                scur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_unroll_no.get(),
                self.var_classroll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phoneno.get(),
                self.var_father.get(),
                self.var_teacher.get(),
                self.var_radio.get()
                 ))
    
                scon.commit()
                self.fetch_data()
                scon.close()
                messagebox.showinfo("Success","Register Successfuliy",parent=self.root)
            except Exception as ess:
                messagebox.showerror("Error",f"Error due to: {str(ess)}",parent=self.root)
    

    #----------------fetch data-------------------#
    def fetch_data(self):
        #fcon=cx_Oracle.connect('system/dbms@localhost/xe')
        fcon=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
        fcur=fcon.cursor()
        fcur.execute("select * from student")
        data=fcur.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            fcon.commit()
        fcon.close()
        
    #-----------------get cursor--------------#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_unroll_no.set(data[6]),
        self.var_classroll_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phoneno.set(data[11]),
        self.var_father.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])

    #---------search data-----------------#
    def search_data(self):
        if self.var_search_std_id.get()=="":
            messagebox.showerror("Error","Please type Student id",parent=self.root)
        else:
            try:
                scon=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
                scur=scon.cursor()
                scur.execute("select * from student where std_id='"+self.var_search_std_id.get()+"'")
                rows=scur.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                    scon.commit()
                else:
                    messagebox.showerror("Error","Student id does not exist",parent=self.root)
                scon.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #--------update-------------#
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="" or self.var_year.get()==""  or self.var_sem.get()==""  or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_unroll_no.get()=="" or self.var_classroll_no.get()=="" or self.var_gender.get()==""  or self.var_dob.get()==""  or self.var_email.get()=="" or self.var_phoneno.get()==""  or self.var_father.get()=="" or self.var_teacher.get()=="" or self.var_dep.get()=="" :
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)  
                if Update>0:
                    upcon=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
                    upcur=upcon.cursor()
                    upcur.execute("update student set dep=%s,course=%s,year=%s,sem=%s,std_name=%s,un_roll_no=%s,class_roll_no=%s,gender=%s,dob=%s,email=%s,phone_no=%s,father=%s,teacher=%s,photo_sample=%s where std_id=%s",(
                                                                                                                                                                  self.var_dep.get(),
                                                                                                                                                                  self.var_course.get(),
                                                                                                                                                                  self.var_year.get(),
                                                                                                                                                                  self.var_sem.get(),
                                                                                                                                                                  self.var_std_name.get(),
                                                                                                                                                                  self.var_unroll_no.get(),
                                                                                                                                                                  self.var_classroll_no.get(),
                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                  self.var_dob.get(),
                                                                                                                                                                  self.var_email.get(),
                                                                                                                                                                  self.var_phoneno.get(),
                                                                                                                                                                  self.var_father.get(),
                                                                                                                                                                  self.var_teacher.get(),
                                                                                                                                                                  self.var_radio.get(),
                                                                                                                                                                  self.var_std_id.get()
                                                                                                                                                                  ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","student details successfully update completed",parent=self.root)
                upcon.commit()
                self.fetch_data()
                upcon.close()
            except Exception as up:
                messagebox.showerror("Error",f"Error due to: {str(up)}",parent=self.root)

    #-------------delete-----------------#
    def delete_data(self):
        if self.var_std_id=="":
            messagebox.showerror("Error","Student is must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    delcon=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
                    delcur=delcon.cursor()
                    delquery= "delete from student where std_id=%s"
                    val=(self.var_std_id.get(),)
                    delcur.execute(delquery,val)
                else:
                    if not delete:
                        return
                delcon.commit()
                self.fetch_data()
                delcon.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as dele:
                messagebox.showerror("Error",f"Error due to: {str(dele)}",parent=self.root)

    #--------------reset-----------------#
    def reset_data(self):
        self.var_dep.set("Select")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_sem.set("Select")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_unroll_no.set("")
        self.var_classroll_no.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_father.set("")
        self.var_teacher.set("")
        self.var_radio.set("")


#-------------------------------generate data set or Take photo Sample------------------------------#

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="" or self.var_year.get()==""  or self.var_sem.get()==""  or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_unroll_no.get()=="" or self.var_classroll_no.get()=="" or self.var_gender.get()==""  or self.var_dob.get()==""  or self.var_email.get()=="" or self.var_phoneno.get()==""  or self.var_father.get()=="" or self.var_teacher.get()=="" or self.var_dep.get()=="" :
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                pcon=mysql.connector.connect(host="localhost",user="root",password="8171@dbms",database="hpdb1")
                pcur=pcon.cursor()
                pcur.execute("select * from student")
                myresult=pcur.fetchall()
                id=0
                for x in myresult:
                    id+=1
                pcur.execute("update student set dep=%s,course=%s,year=%s,sem=%s,std_name=%s,un_roll_no=%s,class_roll_no=%s,gender=%s,dob=%s,email=%s,phone_no=%s,father=%s,teacher=%s,photo_sample=%s where std_id=%s",(
                                                                                                                                                                  self.var_dep.get(),
                                                                                                                                                                  self.var_course.get(),
                                                                                                                                                                  self.var_year.get(),
                                                                                                                                                                  self.var_sem.get(),
                                                                                                                                                                  self.var_std_name.get(),
                                                                                                                                                                  self.var_unroll_no.get(),
                                                                                                                                                                  self.var_classroll_no.get(),
                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                  self.var_dob.get(),
                                                                                                                                                                  self.var_email.get(),
                                                                                                                                                                  self.var_phoneno.get(),
                                                                                                                                                                  self.var_father.get(),
                                                                                                                                                                  self.var_teacher.get(),
                                                                                                                                                                  self.var_radio.get(),
                                                                                                                                                                  self.var_std_id.get()==id+1
                                                                                                                                                             ))
                pcon.commit()
                self.fetch_data()
                self.reset_data()
 

                #======================Load predefined data on face frontals from openCv---------------------------#
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
            
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
        
                messagebox.showinfo("Result","Generating data sets compled!!!!",parent=self.root)
            except Exception as up:
                    messagebox.showerror("Error",f"Error due to: {str(up)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=student_page(root)
    root.mainloop()