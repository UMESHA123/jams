import tkinter as tk
from tkcalendar import *
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import sqlite3
from tkinter import messagebox
from tkinter import colorchooser
from stpf_log_in_page import StaffLogInPage
from faculty_ligin_page import FacultyLogInPage
from student_login_page import StudentLogInPage
from nes_login_page import NesLogInPage
from parent_log_in_page import ParentLogInPage
from developer_login_page import DevelopLogInPage


class GotoLoginPage():
    def __init__(self,root):
        self.root=root
        self.root.title("Goto LogIn Page")
        self.root.geometry('1280x658+0+0')
        #self.root.resizable(False,False)
        self.root.config(bg='#eef3f9')
        
        self.bg=ImageTk.PhotoImage(file='All_Program_Photos/main_all_login_page.png')
        frame=Frame(self.root,width=1280,height=704,bg='black')
        frame.pack(side=TOP)
        label=Label(frame,width=1284,height=704,image=self.bg,bg='black')
        label.pack(fill=BOTH)


        faculty_log_in_button=Button(self.root,text='Faculty Log in.',font=('times new roman',13,'bold'),bg='#FFC312',fg='black',activebackground='#FFC312',bd=0,width=18,height=2,command=self.FacultyLogInPage)
        faculty_log_in_button.place(x=300,y=280)

        staff_log_in_button=Button(self.root,text='Staff Log in.',font=('times new roman',13,'bold'),bg='#FFC312',fg='black',activebackground='#FFC312',bd=0,width=18,height=2,command=self.StaffLogInPage)
        staff_log_in_button.place(x=540,y=280)

        student_log_in_button=Button(self.root,text='Student Log in.',font=('times new roman',13,'bold'),bg='#FFC312',fg='black',activebackground='#FFC312',bd=0,width=18,height=2,command=self.StudentLogInPage)
        student_log_in_button.place(x=770,y=280)

        parent_log_in_button=Button(self.root,text='Parent Log in.',font=('times new roman',13,'bold'),bg='#FFC312',fg='black',activebackground='#FFC312',bd=0,width=18,height=2,command=self.ParentLogInPage)
        parent_log_in_button.place(x=300,y=350)

        nes_log_in_button=Button(self.root,text='Nes Log in.',font=('times new roman',13,'bold'),bg='#FFC312',fg='black',activebackground='#FFC312',bd=0,width=18,height=2,command=self.NesLogInPage)
        nes_log_in_button.place(x=540,y=350)

        developer_log_in_button=Button(self.root,text='Developer Log in.',font=('times new roman',13,'bold'),bg='#FFC312',fg='black',activebackground='#FFC312',bd=0,width=18,height=2,command=self.DevelopLogInPage)
        developer_log_in_button.place(x=770,y=350)

    def FacultyLogInPage(self):
        self.gotoFacultyLogInPage=Toplevel(self.root)
        self.ob1=FacultyLogInPage(self.gotoFacultyLogInPage)
    def StaffLogInPage(self):
        self.gotoStaffLogInPage=Toplevel(self.root)
        self.ob1=StaffLogInPage(self.gotoStaffLogInPage)
    def StudentLogInPage(self):
        self.gotoStudentLogInPage=Toplevel(self.root)
        self.ob1=StudentLogInPage(self.gotoStudentLogInPage)
    def ParentLogInPage(self):
        self.gotoParentLogInPage=Toplevel(self.root)
        self.on1=ParentLogInPage(self.gotoParentLogInPage)
    def NesLogInPage(self):
        self.gotoNesLogInPage=Toplevel(self.root)
        self.ob1=NesLogInPage(self.gotoNesLogInPage)
    def DevelopLogInPage(self):
        self.gotoDevelopLogInPage=Toplevel(self.root)
        self.ob1=DevelopLogInPage(self.gotoDevelopLogInPage)

    
         
        
if __name__=='__main__':
    root=tk.Tk()
    ob1=GotoLoginPage(root)
    root.mainloop()