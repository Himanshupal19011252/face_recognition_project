from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk


class help_page:

    def __init__(self,roothelp):
        self.roothelp=roothelp
        self.roothelp.geometry("1530x790+0+0")
        self.roothelp.title("Face Attendance System/ Help")
        self.roothelp.wm_iconbitmap("iconimg.ico")

        #backroun image
        helpbg_img=Image.open("images/help4.jpg")
        helpbg_img=helpbg_img.resize((1530,710),Image.ANTIALIAS)
        self.helpbg_photoimg=ImageTk.PhotoImage(helpbg_img)

        fst_helplbl=Label(self.roothelp,image=self.helpbg_photoimg)
        fst_helplbl.place(x=0,y=0,width=1530,height=710)

        help_info1=Label(self.roothelp,text="Help Desk",font=("times new roman",50,"bold"),fg="green",bg="light gray")
        help_info1.place(x=590,y=50,height=70)
        
        help_info2=Label(self.roothelp,text="Support: himaaanshupal03@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_info2.place(x=520,y=205,height=50)
        

if __name__ == "__main__":
    winhelp=Tk()
    apphelp=help_page(winhelp)
    winhelp.mainloop()
