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
import smtplib
import random
from main_page import Jams

class ParentLogInPage():
    def __init__(self,root):
        self.root=root
        self.root.title("Goto LogIn Page")
        self.root.geometry('1280x658+0+0')
        #self.root.resizable(False,False)
        self.root.config(bg='#eef3f9')
        #############################################################################
        self.var_parent_mobile_number=StringVar()
        ################################################################################

        frame=Frame(self.root)
        frame.pack(fill=BOTH,expand=1)

        self.image=ImageTk.PhotoImage(file='All_Program_Photos/parent_log_in_page.png')
        label=Label(frame,image=self.image)
        label.pack(fill=BOTH,expand=1)

        parent_mobile_number=ttk.Entry(self.root,width=33,textvariable=self.var_parent_mobile_number)
        parent_mobile_number.place(x=569,y=269)


        login_button=Button(self.root,text='Log in.',bd=0,bg='#FFC312',fg='black',font=('times new roman',12,'bold'),width=20,command=self.sigin_confirm_data)
        login_button.place(x=570,y=320)
    
    def sigin_confirm_data(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        if self.var_parent_mobile_number.get()=='':
            messagebox.showerror('Error','EMAIL must be entered in the email etry box',parent=self.root)
        else:#########student_personal_database(table)  father_mobile_number
            cur.execute('select father_mobile_number from student_personal_database where father_mobile_number=?',(self.var_parent_mobile_number.get(),))
            parent_mobile_number=cur.fetchone()
            print(parent_mobile_number)
            if parent_mobile_number==None:
                messagebox.showerror('Error','The parent Number is not in our data base \nplease contact out facult member',parent=self.root)
            else:
                if parent_mobile_number[0]==self.var_parent_mobile_number.get():
                    messagebox.showinfo('Info','mobile number is currect \n "Log in Successful....."',parent=self.root)
                    ###########################################################################################################################
                    self.sigin_cinfirm=Toplevel(self.root)
                    self.ob1=Jams(self.sigin_cinfirm)
                    ###############################################################################################################################
                        
if __name__=='__main__':
    root=tk.Tk()
    ob1=ParentLogInPage(root)
    root.mainloop()