import sys
import os
import cx_Freeze 

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\hp\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\hp\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("face_attendance_system.py", base=base, icon="face_recognition.ico")]


cx_Freeze.setup(
    name = "Facial Recognition Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face_recognition.ico",'tcl86t.dll','tk86t.dll', 'images','data','database','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Attendace System | Developed By Himanshu pal",
    executables = executables
    )
