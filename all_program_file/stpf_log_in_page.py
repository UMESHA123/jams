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
import time


class StaffLogInPage():
    def __init__(self,root):
        self.root=root
        self.root.title("Goto LogIn Page")
        self.root.geometry('1280x658+0+0')
        #self.root.resizable(False,False)
        self.root.config(bg='#eef3f9')

        #############################################################################
        self.var_user_email=StringVar()
        self.var_pass_word=StringVar()
        self.var_user_confirm_password=StringVar()
        self.var_user_email_sing_up=StringVar()
        self.var_user_email_otp_sing_up=StringVar()
        self.var_user_password_sing_up=StringVar()
        self.var_otp=StringVar()
        ################################################################################

        frame=Frame(self.root)
        frame.pack(fill=BOTH,expand=1)

        self.image=ImageTk.PhotoImage(file='All_Program_Photos/staff_log_in_page.png')
        label=Label(frame,image=self.image)
        label.pack(fill=BOTH,expand=1)

        user_email=ttk.Entry(self.root,width=34,textvariable=self.var_user_email)
        user_email.place(x=570,y=267)

        password_entry=ttk.Entry(self.root,width=34,textvariabl=self.var_pass_word)
        password_entry.place(x=570,y=369)

        otp_entry=ttk.Entry(self.root,width=34,textvariabl=self.var_otp)
        otp_entry.place(x=570,y=319)

        
        forget_button=Button(self.root,text='Forget your password.',font=('Bookman Old Style',10),bd=0,bg='#1E1818',fg='red',width=20,command=self.forget_your_password)
        forget_button.place(x=520,y=455)

        login_button=Button(self.root,text='Log in.',bd=0,bg='#FFC312',fg='black',font=('times new roman',12,'bold'),width=20,command=self.sigin_confirm_data)
        login_button.place(x=570,y=410)

        otp_button=Button(self.root,text='Send OTP.',font=('Bookman Old Style',10),bd=0,bg='#1E1818',fg='red',width=10,command=self.singin_send_otp)
        otp_button.place(x=700,y=455)
    
    def singin_send_otp(self):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        if self.var_user_email.get()=="":
            messagebox.showerror('Error','User Email must be required.',parent=self.root)
        else:
            to_=self.var_user_email.get()
            #email_='uumesharameshahugger@gmail.com'
            #pass_='wkrzqhxpotskxhmy'
            email_='uumesharameshahugger@gmail.com'
            pass_='wkrzqhxpotskxhmy'

            s.login(email_,pass_)
            self.otp=str(time.strftime('%H%M%S'))
            print(self.otp)
            
            
            subj='Log in Password.'
            msg=f'Your log in password is : {str(self.otp)}\nThis email is auto genereted email dont replay is.\nthenaks for connecting me'
            msg='Subject:{}\n\n{}'.format(subj,msg)
            s.sendmail(email_,to_,msg)
            
            chk=s.ehlo()
            if chk[0]==250:
                messagebox.showinfo('Info','Email.is send to your email.\n plese check it.',parent=self.root)
    
    def forget_your_password(self):
        self.forget_password=Toplevel(self.root)
        self.forget_password.geometry('1280x658+0+0')

        frame1=Frame(self.forget_password)
        frame1.pack(fill=BOTH,expand=1)

        self.image1=ImageTk.PhotoImage(file='All_Program_Photos/student_sing_up_page.png')
        label1=Label(frame1,image=self.image1)
        label1.pack(fill=BOTH,expand=1)

        user_email1=ttk.Entry(frame1,width=31,textvariable=self.var_user_email_sing_up)
        user_email1.place(x=569,y=260)

        otp_email1=ttk.Entry(frame1,width=31,textvariable=self.var_user_email_otp_sing_up)
        otp_email1.place(x=569,y=310)

        password=ttk.Entry(frame1,width=31,textvariable=self.var_user_password_sing_up)
        password.place(x=569,y=359)

        confirm=ttk.Entry(frame1,width=31,textvariable=self.var_user_confirm_password)
        confirm.place(x=569,y=410)

        singup_button=Button(frame1,text='Sing up.',bd=0,bg='#FFC312',fg='black',font=('times new roman',12,'bold'),width=10,command=self.singup_data)
        singup_button.place(x=570,y=460)

        singup_otp_button=Button(frame1,text='Send otp.',bd=0,bg='#FFC312',fg='black',font=('times new roman',12,'bold'),width=8,command=self.singup_send_otp)
        singup_otp_button.place(x=680,y=460)

        #singup_button=Button(frame1,text='send OTP.',bd=0,bg='#FFC312',fg='black',font=('times new roman',12,'bold'),width=10,command=self.send_email)
        #singup_button.place(x=750,y=390)
    def singup_send_otp(self):
        ss=smtplib.SMTP('smtp.gmail.com',587)
        ss.starttls()
        if self.var_user_email_sing_up.get()=="":
            messagebox.showerror('Error','User Email must be required.',parent=self.root)
        else:
            to_=self.var_user_email_sing_up.get()
            #email_='uumesharameshahugger@gmail.com'
            #pass_='wkrzqhxpotskxhmy'
            email_='uumesharameshahugger@gmail.com'
            pass_='wkrzqhxpotskxhmy'

            ss.login(email_,pass_)
            self.sing_upotp=str(time.strftime('%H%M%S'))
            print(self.sing_upotp)
            
            
            subj='Log in Password.'
            msg=f'Your log in password is : {str(self.sing_upotp)}\nThis email is auto genereted email dont replay is.\nthenaks for connecting me'
            msg='Subject:{}\n\n{}'.format(subj,msg)
            ss.sendmail(email_,to_,msg)
            
            chk=ss.ehlo()
            if chk[0]==250:
                messagebox.showinfo('Info','Email.is send to your email.\n plese check it.',parent=self.root)

    def singup_data(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        if self.var_user_email_sing_up.get()=='':
            messagebox.showerror('Error','The email staff email must be required',parent=self.forget_password)
        else:
            if self.var_user_email_otp_sing_up.get()=='':
                messagebox.showerror('Error','Enter the OTP.',parent=self.forget_password)
            else:
                if self.var_user_password_sing_up.get()=='':
                    messagebox.showerror('Error','Enter the password \n-->password must be required',parent=self.forget_password)
                else:
                    if self.var_user_confirm_password.get()=='':
                        messagebox.showerror('Error','password must be required',parent=self.forget_password)
                    else:
                        if self.var_user_password_sing_up.get()!=self.var_user_confirm_password.get():
                            messagebox.showerror('Error','New password is not equal to the confirm password',parent=self.forget_password)
                        else:
                            if self.sing_upotp!=self.var_user_email_otp_sing_up.get():
                                messagebox.showerror('Error','Entered otp is not currrect please check it\n the otp is send to your email address')
                            else:
                                cur.execute('insert into sing_up_data (user_email,otp,user_password,user_confirm_password) values(?,?,?,?)',(
                                    self.var_user_email_sing_up.get(),
                                    self.var_user_email_otp_sing_up.get(),
                                    self.var_user_password_sing_up.get(),
                                    self.var_user_confirm_password.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The Sing Up successfuly.....',parent=self.forget_password)
                                con.close()
    def sigin_confirm_data(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        if self.var_user_email.get()=='':
            messagebox.showerror('Error','EMAIL must be entered in the email etry box',parent=self.root)
        else:
            if self.var_pass_word.get()=='':
                messagebox.showerror('Error','PASSWORD must be entered in the password entry box',parent=self.root)
            else:
                if self.var_otp.get()=='':
                    messagebox.showerror('Error','OTP must be entered\n your otp is send to your mail please check it',parent=self.root)
                else:
                    cur.execute('select user_password from sing_up_data where user_email=?',(self.var_user_email.get(),))
                    login_user_password=cur.fetchone()
                    print(login_user_password)
                    if login_user_password==None:
                        messagebox.showerror('Error','Sing up firt then login to jams.',parent=self.root)
                    else:
                        if login_user_password[0]!=self.var_pass_word.get():
                            messagebox.showerror('Error','password is incurrect',parent=self.root)
                        else:
                            messagebox.showinfo('Info','Your password is correct')
                            if self.otp==self.var_otp.get():
                                messagebox.showinfo('Info','password and otp is currect',parent=self.root)
                                    
                                self.sigin_cinfirm=Toplevel(self.root)
                                self.ob1=Jams(self.sigin_cinfirm)
                                
                            else:
                                messagebox.showinfo('Error','chech you email and password',parent=self.root)

if __name__=='__main__':
    root=tk.Tk()
    ob1=StaffLogInPage(root)
    root.mainloop()