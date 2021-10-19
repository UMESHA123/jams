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
import psycopg2

class ShowStudentResult():
    def __init__(self,root):
        self.root=root
        self.root.title(" Student Result")
        self.root.geometry('1055x440+213+145')
        self.root.resizable(False,False)
        self.root.configure(bg='white')
        top_label=tk.Label(self.root,text=' Student Result',font=('Bahnschrift',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)

        ####################################
        self.var_sem_select=StringVar()
        self.var_branch_select=StringVar()
        self.var_scheme_select=StringVar()

        self.var_usn_entry=StringVar()
        #######################################
        
        menu_frame=tk.LabelFrame(self.root,text='Menu',font=('times now roman',10,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=10,y=45,width=1035,height=55)

        self.sem_select=ttk.Combobox(menu_frame,width=20,textvariable=self.var_sem_select,state='readonly')
        self.sem_select.grid(row=0,column=0,padx=4,pady=3) 
        self.sem_select['values']=(
            '1st_Semister',
            '2nd_Semister',
            '3rd_Semister',
            '4th_Semister',
            '5th_Semister',
            '6th_Semister',
            '7th_Semister',
            '8th_Semister'
        )

        branch_select=ttk.Combobox(menu_frame,width=20,textvariable=self.var_branch_select,state='readonly')
        branch_select.grid(row=0,column=1,padx=4,pady=3)
        branch_select['values']=(
                                    'CHEMISTRY_cycle',
                                    'PHYSICS_cycle',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering'
        )
        scheme=ttk.Combobox(menu_frame,width=20,textvariable=self.var_scheme_select,state='readonly')
        scheme.grid(row=0,column=2,padx=4,pady=3)
        scheme['values']=(
            '2018',
            '2019'
        )
        button1=ttk.Button(menu_frame,text='Search',width=15,command=self.search).grid(row=0,column=3,padx=4,pady=3)
    def search(self):
        if self.var_branch_select.get()=='CHEMISTRY_cycle':
            if self.var_sem_select.get()=='1st_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from che_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_che_treeview.delete(*tree_che_treeview.get_children())
                                for row in rows:
                                    tree_che_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_che_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_che_treeview.xview)
                    scrolly.configure(command=tree_che_treeview.yview)

                    tree_che_treeview.heading('subject_code',text="Subject Code")
                    tree_che_treeview.heading('subjects',text="Subjects")
                    tree_che_treeview.heading('semister',text="Semister")
                    tree_che_treeview.heading('scheme',text="Scheme")
                    tree_che_treeview.heading('branch',text="Branch")
                    tree_che_treeview.heading('marks',text="Marks")
                    tree_che_treeview.heading('student_usn',text="Usn")
                    

                    tree_che_treeview.column('subject_code',width=200)
                    tree_che_treeview.column('subjects',width=200)
                    tree_che_treeview.column('semister',width=200)
                    tree_che_treeview.column('scheme',width=200)
                    tree_che_treeview.column('branch',width=200)
                    tree_che_treeview.column('marks',width=200)
                    tree_che_treeview.column('student_usn',width=200)

                    tree_che_treeview['show']='headings'
                    
                    tree_che_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='PHYSICS_cycle':
            if self.var_sem_select.get()=='2nd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from phy_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_phy_treeview.delete(*tree_phy_treeview.get_children())
                                for row in rows:
                                    tree_phy_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_phy_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_phy_treeview.xview)
                    scrolly.configure(command=tree_phy_treeview.yview)

                    
                    tree_phy_treeview.heading('subject_code',text="Subject Code")
                    tree_phy_treeview.heading('subjects',text="Subjects")
                    tree_phy_treeview.heading('semister',text="Semister")
                    tree_phy_treeview.heading('scheme',text="Scheme")
                    tree_phy_treeview.heading('branch',text="Branch")
                    tree_phy_treeview.heading('marks',text="Marks")
                    tree_phy_treeview.heading('student_usn',text="Usn")
                    

             
                    tree_phy_treeview.column('subject_code',width=200)
                    tree_phy_treeview.column('subjects',width=200)
                    tree_phy_treeview.column('semister',width=200)
                    tree_phy_treeview.column('scheme',width=200)
                    tree_phy_treeview.column('branch',width=200)
                    tree_phy_treeview.column('marks',width=200)
                    tree_phy_treeview.column('student_usn',width=200)

                    tree_phy_treeview['show']='headings'
                    
                    tree_phy_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Civil_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_3rd_treeview.delete(*tree_civil_3rd_treeview.get_children())
                                for row in rows:
                                    tree_civil_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_3rd_treeview.xview)
                    scrolly.configure(command=tree_civil_3rd_treeview.yview)

                    tree_civil_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_3rd_treeview.heading('subjects',text="Subjects")
                    tree_civil_3rd_treeview.heading('semister',text="Semister")
                    tree_civil_3rd_treeview.heading('scheme',text="Scheme")
                    tree_civil_3rd_treeview.heading('branch',text="Branch")
                    tree_civil_3rd_treeview.heading('marks',text="Marks")
                    tree_civil_3rd_treeview.heading('student_usn',text="Usn")
                    

                    tree_civil_3rd_treeview.column('subject_code',width=200)
                    tree_civil_3rd_treeview.column('subjects',width=200)
                    tree_civil_3rd_treeview.column('semister',width=200)
                    tree_civil_3rd_treeview.column('scheme',width=200)
                    tree_civil_3rd_treeview.column('branch',width=200)
                    tree_civil_3rd_treeview.column('marks',width=200)
                    tree_civil_3rd_treeview.column('student_usn',width=200)

                    tree_civil_3rd_treeview['show']='headings'
                    
                    tree_civil_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Civil_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_4th_treeview.delete(*tree_civil_4th_treeview.get_children())
                                for row in rows:
                                    tree_civil_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_4th_treeview.xview)
                    scrolly.configure(command=tree_civil_4th_treeview.yview)

            
                    tree_civil_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_4th_treeview.heading('subjects',text="Subjects")
                    tree_civil_4th_treeview.heading('semister',text="Semister")
                    tree_civil_4th_treeview.heading('scheme',text="Scheme")
                    tree_civil_4th_treeview.heading('branch',text="Branch")
                    tree_civil_4th_treeview.heading('marks',text="Marks")
                    tree_civil_4th_treeview.heading('student_usn',text="Usn")
                    

                    tree_civil_4th_treeview.column('subject_code',width=200)
                    tree_civil_4th_treeview.column('subjects',width=200)
                    tree_civil_4th_treeview.column('semister',width=200)
                    tree_civil_4th_treeview.column('scheme',width=200)
                    tree_civil_4th_treeview.column('branch',width=200)
                    tree_civil_4th_treeview.column('marks',width=200)
                    tree_civil_4th_treeview.column('student_usn',width=200)

                    tree_civil_4th_treeview['show']='headings'
                    
                    tree_civil_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Civil_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_5th_treeview.delete(*tree_civil_5th_treeview.get_children())
                                for row in rows:
                                    tree_civil_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_5th_treeview.xview)
                    scrolly.configure(command=tree_civil_5th_treeview.yview)

                    tree_civil_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_5th_treeview.heading('subjects',text="Subjects")
                    tree_civil_5th_treeview.heading('semister',text="Semister")
                    tree_civil_5th_treeview.heading('scheme',text="Scheme")
                    tree_civil_5th_treeview.heading('branch',text="Branch")
                    tree_civil_5th_treeview.heading('marks',text="Marks")
                    tree_civil_5th_treeview.heading('student_usn',text="Usn")
                    

                    tree_civil_5th_treeview.column('subject_code',width=200)
                    tree_civil_5th_treeview.column('subjects',width=200)
                    tree_civil_5th_treeview.column('semister',width=200)
                    tree_civil_5th_treeview.column('scheme',width=200)
                    tree_civil_5th_treeview.column('branch',width=200)
                    tree_civil_5th_treeview.column('marks',width=200)
                    tree_civil_5th_treeview.column('student_usn',width=200)

                    tree_civil_5th_treeview['show']='headings'
                    
                    tree_civil_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Civil_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_6th_treeview.delete(*tree_civil_6th_treeview.get_children())
                                for row in rows:
                                    tree_civil_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_6th_treeview.xview)
                    scrolly.configure(command=tree_civil_6th_treeview.yview)

                    tree_civil_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_6th_treeview.heading('subjects',text="Subjects")
                    tree_civil_6th_treeview.heading('semister',text="Semister")
                    tree_civil_6th_treeview.heading('scheme',text="Scheme")
                    tree_civil_6th_treeview.heading('branch',text="Branch")
                    tree_civil_6th_treeview.heading('marks',text="Marks")
                    tree_civil_6th_treeview.heading('student_usn',text="Usn")
                    

                    tree_civil_6th_treeview.column('subject_code',width=200)
                    tree_civil_6th_treeview.column('subjects',width=200)
                    tree_civil_6th_treeview.column('semister',width=200)
                    tree_civil_6th_treeview.column('scheme',width=200)
                    tree_civil_6th_treeview.column('branch',width=200)
                    tree_civil_6th_treeview.column('marks',width=200)
                    tree_civil_6th_treeview.column('student_usn',width=200)

                    tree_civil_6th_treeview['show']='headings'
                    
                    tree_civil_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Civil_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_7th_treeview.delete(*tree_civil_7th_treeview.get_children())
                                for row in rows:
                                    tree_civil_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_7th_treeview.xview)
                    scrolly.configure(command=tree_civil_7th_treeview.yview)

                    tree_civil_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_7th_treeview.heading('subjects',text="Subjects")
                    tree_civil_7th_treeview.heading('semister',text="Semister")
                    tree_civil_7th_treeview.heading('scheme',text="Scheme")
                    tree_civil_7th_treeview.heading('branch',text="Branch")
                    tree_civil_7th_treeview.heading('marks',text="Marks")
                    tree_civil_7th_treeview.heading('student_usn',text="Usn")
                    

                    tree_civil_7th_treeview.column('subject_code',width=200)
                    tree_civil_7th_treeview.column('subjects',width=200)
                    tree_civil_7th_treeview.column('semister',width=200)
                    tree_civil_7th_treeview.column('scheme',width=200)
                    tree_civil_7th_treeview.column('branch',width=200)
                    tree_civil_7th_treeview.column('marks',width=200)
                    tree_civil_7th_treeview.column('student_usn',width=200)

                    tree_civil_7th_treeview['show']='headings'
                    
                    tree_civil_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Civil_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_8th_treeview.delete(*tree_civil_8th_treeview.get_children())
                                for row in rows:
                                    tree_civil_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_8th_treeview.xview)
                    scrolly.configure(command=tree_civil_8th_treeview.yview)

                    tree_civil_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_8th_treeview.heading('subjects',text="Subjects")
                    tree_civil_8th_treeview.heading('semister',text="Semister")
                    tree_civil_8th_treeview.heading('scheme',text="Scheme")
                    tree_civil_8th_treeview.heading('branch',text="Branch")
                    tree_civil_8th_treeview.heading('marks',text="Marks")
                    tree_civil_8th_treeview.heading('student_usn',text="Usn")
          
                    tree_civil_8th_treeview.column('subject_code',width=200)
                    tree_civil_8th_treeview.column('subjects',width=200)
                    tree_civil_8th_treeview.column('semister',width=200)
                    tree_civil_8th_treeview.column('scheme',width=200)
                    tree_civil_8th_treeview.column('branch',width=200)
                    tree_civil_8th_treeview.column('marks',width=200)
                    tree_civil_8th_treeview.column('student_usn',width=200)

                    tree_civil_8th_treeview['show']='headings'
                    
                    tree_civil_8th_treeview.pack(fill=BOTH,expand=1)
        #####################################################################################
        ##############################################3##################################################################
        if self.var_branch_select.get()=='Mechanical_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from mech_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_mech_3rd_treeview.delete(*tree_mech_3rd_treeview.get_children())
                                for row in rows:
                                    tree_mech_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_mech_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_mech_3rd_treeview.xview)
                    scrolly.configure(command=tree_mech_3rd_treeview.yview)

               
                    tree_mech_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_mech_3rd_treeview.heading('subjects',text="Subjects")
                    tree_mech_3rd_treeview.heading('semister',text="Semister")
                    tree_mech_3rd_treeview.heading('scheme',text="Scheme")
                    tree_mech_3rd_treeview.heading('branch',text="Branch")
                    tree_mech_3rd_treeview.heading('marks',text="Marks")
                    tree_mech_3rd_treeview.heading('student_usn',text="Usn")
                    

                    tree_mech_3rd_treeview.column('subject_code',width=200)
                    tree_mech_3rd_treeview.column('subjects',width=200)
                    tree_mech_3rd_treeview.column('semister',width=200)
                    tree_mech_3rd_treeview.column('scheme',width=200)
                    tree_mech_3rd_treeview.column('branch',width=200)
                    tree_mech_3rd_treeview.column('marks',width=200)
                    tree_mech_3rd_treeview.column('student_usn',width=200)

                    tree_mech_3rd_treeview['show']='headings'
                    
                    tree_mech_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Mechanical_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from mech_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_mech_4th_treeview.delete(*tree_mech_4th_treeview.get_children())
                                for row in rows:
                                    tree_mech_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_mech_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_mech_4th_treeview.xview)
                    scrolly.configure(command=tree_mech_4th_treeview.yview)

                    tree_mech_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_mech_4th_treeview.heading('subjects',text="Subjects")
                    tree_mech_4th_treeview.heading('semister',text="Semister")
                    tree_mech_4th_treeview.heading('scheme',text="Scheme")
                    tree_mech_4th_treeview.heading('branch',text="Branch")
                    tree_mech_4th_treeview.heading('marks',text="Marks")
                    tree_mech_4th_treeview.heading('student_usn',text="Usn")
                    

                 
                    tree_mech_4th_treeview.column('subject_code',width=200)
                    tree_mech_4th_treeview.column('subjects',width=200)
                    tree_mech_4th_treeview.column('semister',width=200)
                    tree_mech_4th_treeview.column('scheme',width=200)
                    tree_mech_4th_treeview.column('branch',width=200)
                    tree_mech_4th_treeview.column('marks',width=200)
                    tree_mech_4th_treeview.column('student_usn',width=200)

                    tree_mech_4th_treeview['show']='headings'
                    
                    tree_mech_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Mechanical_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from mech_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_mech_5th_treeview.delete(*tree_mech_5th_treeview.get_children())
                                for row in rows:
                                    tree_mech_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_mech_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_mech_5th_treeview.xview)
                    scrolly.configure(command=tree_mech_5th_treeview.yview)

                    
                    tree_mech_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_mech_5th_treeview.heading('subjects',text="Subjects")
                    tree_mech_5th_treeview.heading('semister',text="Semister")
                    tree_mech_5th_treeview.heading('scheme',text="Scheme")
                    tree_mech_5th_treeview.heading('branch',text="Branch")
                    tree_mech_5th_treeview.heading('marks',text="Marks")
                    tree_mech_5th_treeview.heading('student_usn',text="Usn")
                    

                   
                    tree_mech_5th_treeview.column('subject_code',width=200)
                    tree_mech_5th_treeview.column('subjects',width=200)
                    tree_mech_5th_treeview.column('semister',width=200)
                    tree_mech_5th_treeview.column('scheme',width=200)
                    tree_mech_5th_treeview.column('branch',width=200)
                    tree_mech_5th_treeview.column('marks',width=200)
                    tree_mech_5th_treeview.column('student_usn',width=200)

                    tree_mech_5th_treeview['show']='headings'
                    
                    tree_mech_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Mechanical_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from mech_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_mech_6th_treeview.delete(*tree_mech_6th_treeview.get_children())
                                for row in rows:
                                    tree_mech_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_mech_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_mech_6th_treeview.xview)
                    scrolly.configure(command=tree_mech_6th_treeview.yview)

               
                    tree_mech_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_mech_6th_treeview.heading('subjects',text="Subjects")
                    tree_mech_6th_treeview.heading('semister',text="Semister")
                    tree_mech_6th_treeview.heading('scheme',text="Scheme")
                    tree_mech_6th_treeview.heading('branch',text="Branch")
                    tree_mech_6th_treeview.heading('marks',text="Marks")
                    tree_mech_6th_treeview.heading('student_usn',text="Usn")
                    

                    tree_mech_6th_treeview.column('subject_code',width=200)
                    tree_mech_6th_treeview.column('subjects',width=200)
                    tree_mech_6th_treeview.column('semister',width=200)
                    tree_mech_6th_treeview.column('scheme',width=200)
                    tree_mech_6th_treeview.column('branch',width=200)
                    tree_mech_6th_treeview.column('marks',width=200)
                    tree_mech_6th_treeview.column('student_usn',width=200)

                    tree_mech_6th_treeview['show']='headings'
                    
                    tree_mech_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Mechanical_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from mech_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_mech_7th_treeview.delete(*tree_mech_7th_treeview.get_children())
                                for row in rows:
                                    tree_mech_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_mech_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_mech_7th_treeview.xview)
                    scrolly.configure(command=tree_mech_7th_treeview.yview)

                
                    tree_mech_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_mech_7th_treeview.heading('subjects',text="Subjects")
                    tree_mech_7th_treeview.heading('semister',text="Semister")
                    tree_mech_7th_treeview.heading('scheme',text="Scheme")
                    tree_mech_7th_treeview.heading('branch',text="Branch")
                    tree_mech_7th_treeview.heading('marks',text="Marks")
                    tree_mech_7th_treeview.heading('student_usn',text="Usn")
   
                    tree_mech_7th_treeview.column('subject_code',width=200)
                    tree_mech_7th_treeview.column('subjects',width=200)
                    tree_mech_7th_treeview.column('semister',width=200)
                    tree_mech_7th_treeview.column('scheme',width=200)
                    tree_mech_7th_treeview.column('branch',width=200)
                    tree_mech_7th_treeview.column('marks',width=200)
                    tree_mech_7th_treeview.column('student_usn',width=200)

                    tree_mech_7th_treeview['show']='headings'
                    
                    tree_mech_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Mechanical_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from mech_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_mech_8th_treeview.delete(*tree_mech_8th_treeview.get_children())
                                for row in rows:
                                    tree_mech_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_mech_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_mech_8th_treeview.xview)
                    scrolly.configure(command=tree_mech_8th_treeview.yview)

     
                    tree_mech_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_mech_8th_treeview.heading('subjects',text="Subjects")
                    tree_mech_8th_treeview.heading('semister',text="Semister")
                    tree_mech_8th_treeview.heading('scheme',text="Scheme")
                    tree_mech_8th_treeview.heading('branch',text="Branch")
                    tree_mech_8th_treeview.heading('marks',text="Marks")
                    tree_mech_8th_treeview.heading('student_usn',text="Usn")
                    

                    tree_mech_8th_treeview.column('subject_code',width=200)
                    tree_mech_8th_treeview.column('subjects',width=200)
                    tree_mech_8th_treeview.column('semister',width=200)
                    tree_mech_8th_treeview.column('scheme',width=200)
                    tree_mech_8th_treeview.column('branch',width=200)
                    tree_mech_8th_treeview.column('marks',width=200)
                    tree_mech_8th_treeview.column('student_usn',width=200)

                    tree_mech_8th_treeview['show']='headings'
                    
                    tree_mech_8th_treeview.pack(fill=BOTH,expand=1)
########################################################################################
####################################################################################
########################################################################################
#################################################################################333

        if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ece_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ece_3rd_treeview.delete(*tree_ece_3rd_treeview.get_children())
                                for row in rows:
                                    tree_ece_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ece_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ece_3rd_treeview.xview)
                    scrolly.configure(command=tree_ece_3rd_treeview.yview)

                  
                    tree_ece_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_ece_3rd_treeview.heading('subjects',text="Subjects")
                    tree_ece_3rd_treeview.heading('semister',text="Semister")
                    tree_ece_3rd_treeview.heading('scheme',text="Scheme")
                    tree_ece_3rd_treeview.heading('branch',text="Branch")
                    tree_ece_3rd_treeview.heading('marks',text="Marks")
                    tree_ece_3rd_treeview.heading('student_usn',text="Usn")
                    

                    
                    tree_ece_3rd_treeview.column('subject_code',width=200)
                    tree_ece_3rd_treeview.column('subjects',width=200)
                    tree_ece_3rd_treeview.column('semister',width=200)
                    tree_ece_3rd_treeview.column('scheme',width=200)
                    tree_ece_3rd_treeview.column('branch',width=200)
                    tree_ece_3rd_treeview.column('marks',width=200)
                    tree_ece_3rd_treeview.column('student_usn',width=200)

                    tree_ece_3rd_treeview['show']='headings'
                    
                    tree_ece_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ece_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ece_4th_treeview.delete(*tree_ece_4th_treeview.get_children())
                                for row in rows:
                                    tree_ece_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ece_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ece_4th_treeview.xview)
                    scrolly.configure(command=tree_ece_4th_treeview.yview)

                    tree_ece_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_ece_4th_treeview.heading('subjects',text="Subjects")
                    tree_ece_4th_treeview.heading('semister',text="Semister")
                    tree_ece_4th_treeview.heading('scheme',text="Scheme")
                    tree_ece_4th_treeview.heading('branch',text="Branch")
                    tree_ece_4th_treeview.heading('marks',text="Marks")
                    tree_ece_4th_treeview.heading('student_usn',text="Usn")
                    

            
                    tree_ece_4th_treeview.column('subject_code',width=200)
                    tree_ece_4th_treeview.column('subjects',width=200)
                    tree_ece_4th_treeview.column('semister',width=200)
                    tree_ece_4th_treeview.column('scheme',width=200)
                    tree_ece_4th_treeview.column('branch',width=200)
                    tree_ece_4th_treeview.column('marks',width=200)
                    tree_ece_4th_treeview.column('student_usn',width=200)

                    tree_ece_4th_treeview['show']='headings'
                    
                    tree_ece_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ece_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ece_5th_treeview.delete(*tree_ece_5th_treeview.get_children())
                                for row in rows:
                                    tree_ece_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ece_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ece_5th_treeview.xview)
                    scrolly.configure(command=tree_ece_5th_treeview.yview)

                    tree_ece_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_ece_5th_treeview.heading('subjects',text="Subjects")
                    tree_ece_5th_treeview.heading('semister',text="Semister")
                    tree_ece_5th_treeview.heading('scheme',text="Scheme")
                    tree_ece_5th_treeview.heading('branch',text="Branch")
                    tree_ece_5th_treeview.heading('marks',text="Marks")
                    tree_ece_5th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ece_5th_treeview.column('subject_code',width=200)
                    tree_ece_5th_treeview.column('subjects',width=200)
                    tree_ece_5th_treeview.column('semister',width=200)
                    tree_ece_5th_treeview.column('scheme',width=200)
                    tree_ece_5th_treeview.column('branch',width=200)
                    tree_ece_5th_treeview.column('marks',width=200)
                    tree_ece_5th_treeview.column('student_usn',width=200)

                    tree_ece_5th_treeview['show']='headings'
                    
                    tree_ece_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ece_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ece_6th_treeview.delete(*tree_ece_6th_treeview.get_children())
                                for row in rows:
                                    tree_ece_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ece_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ece_6th_treeview.xview)
                    scrolly.configure(command=tree_ece_6th_treeview.yview)

             
                    tree_ece_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_ece_6th_treeview.heading('subjects',text="Subjects")
                    tree_ece_6th_treeview.heading('semister',text="Semister")
                    tree_ece_6th_treeview.heading('scheme',text="Scheme")
                    tree_ece_6th_treeview.heading('branch',text="Branch")
                    tree_ece_6th_treeview.heading('marks',text="Marks")
                    tree_ece_6th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ece_6th_treeview.column('subject_code',width=200)
                    tree_ece_6th_treeview.column('subjects',width=200)
                    tree_ece_6th_treeview.column('semister',width=200)
                    tree_ece_6th_treeview.column('scheme',width=200)
                    tree_ece_6th_treeview.column('branch',width=200)
                    tree_ece_6th_treeview.column('marks',width=200)
                    tree_ece_6th_treeview.column('student_usn',width=200)

                    tree_ece_6th_treeview['show']='headings'
                    
                    tree_ece_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ece_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ece_7th_treeview.delete(*tree_ece_7th_treeview.get_children())
                                for row in rows:
                                    tree_ece_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ece_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ece_7th_treeview.xview)
                    scrolly.configure(command=tree_ece_7th_treeview.yview)

                    tree_ece_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_ece_7th_treeview.heading('subjects',text="Subjects")
                    tree_ece_7th_treeview.heading('semister',text="Semister")
                    tree_ece_7th_treeview.heading('scheme',text="Scheme")
                    tree_ece_7th_treeview.heading('branch',text="Branch")
                    tree_ece_7th_treeview.heading('marks',text="Marks")
                    tree_ece_7th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ece_7th_treeview.column('subject_code',width=200)
                    tree_ece_7th_treeview.column('subjects',width=200)
                    tree_ece_7th_treeview.column('semister',width=200)
                    tree_ece_7th_treeview.column('scheme',width=200)
                    tree_ece_7th_treeview.column('branch',width=200)
                    tree_ece_7th_treeview.column('marks',width=200)
                    tree_ece_7th_treeview.column('student_usn',width=200)

                    tree_ece_7th_treeview['show']='headings'
                    
                    tree_ece_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ece_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ece_8th_treeview.delete(*tree_ece_8th_treeview.get_children())
                                for row in rows:
                                    tree_ece_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ece_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ece_8th_treeview.xview)
                    scrolly.configure(command=tree_ece_8th_treeview.yview)

                    tree_ece_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_ece_8th_treeview.heading('subjects',text="Subjects")
                    tree_ece_8th_treeview.heading('semister',text="Semister")
                    tree_ece_8th_treeview.heading('scheme',text="Scheme")
                    tree_ece_8th_treeview.heading('branch',text="Branch")
                    tree_ece_8th_treeview.heading('marks',text="Marks")
                    tree_ece_8th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ece_8th_treeview.column('subject_code',width=200)
                    tree_ece_8th_treeview.column('subjects',width=200)
                    tree_ece_8th_treeview.column('semister',width=200)
                    tree_ece_8th_treeview.column('scheme',width=200)
                    tree_ece_8th_treeview.column('branch',width=200)
                    tree_ece_8th_treeview.column('marks',width=200)
                    tree_ece_8th_treeview.column('student_usn',width=200)

                    tree_ece_8th_treeview['show']='headings'
                    
                    tree_ece_8th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from eee_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_eee_3rd_treeview.delete(*tree_eee_3rd_treeview.get_children())
                                for row in rows:
                                    tree_eee_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_eee_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_eee_3rd_treeview.xview)
                    scrolly.configure(command=tree_eee_3rd_treeview.yview)

             
                    tree_eee_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_eee_3rd_treeview.heading('subjects',text="Subjects")
                    tree_eee_3rd_treeview.heading('semister',text="Semister")
                    tree_eee_3rd_treeview.heading('scheme',text="Scheme")
                    tree_eee_3rd_treeview.heading('branch',text="Branch")
                    tree_eee_3rd_treeview.heading('marks',text="Marks")
                    tree_eee_3rd_treeview.heading('student_usn',text="Usn")
                    

                 
                    tree_eee_3rd_treeview.column('subject_code',width=200)
                    tree_eee_3rd_treeview.column('subjects',width=200)
                    tree_eee_3rd_treeview.column('semister',width=200)
                    tree_eee_3rd_treeview.column('scheme',width=200)
                    tree_eee_3rd_treeview.column('branch',width=200)
                    tree_eee_3rd_treeview.column('marks',width=200)
                    tree_eee_3rd_treeview.column('student_usn',width=200)

                    tree_eee_3rd_treeview['show']='headings'
                    
                    tree_eee_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from eee_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_eee_4th_treeview.delete(*tree_eee_4th_treeview.get_children())
                                for row in rows:
                                    tree_eee_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_eee_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_eee_4th_treeview.xview)
                    scrolly.configure(command=tree_eee_4th_treeview.yview)

                  
                    tree_eee_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_eee_4th_treeview.heading('subjects',text="Subjects")
                    tree_eee_4th_treeview.heading('semister',text="Semister")
                    tree_eee_4th_treeview.heading('scheme',text="Scheme")
                    tree_eee_4th_treeview.heading('branch',text="Branch")
                    tree_eee_4th_treeview.heading('marks',text="Marks")
                    tree_eee_4th_treeview.heading('student_usn',text="Usn")
                    

                    tree_eee_4th_treeview.column('subject_code',width=200)
                    tree_eee_4th_treeview.column('subjects',width=200)
                    tree_eee_4th_treeview.column('semister',width=200)
                    tree_eee_4th_treeview.column('scheme',width=200)
                    tree_eee_4th_treeview.column('branch',width=200)
                    tree_eee_4th_treeview.column('marks',width=200)
                    tree_eee_4th_treeview.column('student_usn',width=200)

                    tree_eee_4th_treeview['show']='headings'
                    
                    tree_eee_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from eee_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_eee_5th_treeview.delete(*tree_eee_5th_treeview.get_children())
                                for row in rows:
                                    tree_eee_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_eee_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_eee_5th_treeview.xview)
                    scrolly.configure(command=tree_eee_5th_treeview.yview)

                    
                    tree_eee_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_eee_5th_treeview.heading('subjects',text="Subjects")
                    tree_eee_5th_treeview.heading('semister',text="Semister")
                    tree_eee_5th_treeview.heading('scheme',text="Scheme")
                    tree_eee_5th_treeview.heading('branch',text="Branch")
                    tree_eee_5th_treeview.heading('marks',text="Marks")
                    tree_eee_5th_treeview.heading('student_usn',text="Usn")
                    

                    tree_eee_5th_treeview.column('subject_code',width=200)
                    tree_eee_5th_treeview.column('subjects',width=200)
                    tree_eee_5th_treeview.column('semister',width=200)
                    tree_eee_5th_treeview.column('scheme',width=200)
                    tree_eee_5th_treeview.column('branch',width=200)
                    tree_eee_5th_treeview.column('marks',width=200)
                    tree_eee_5th_treeview.column('student_usn',width=200)

                    tree_eee_5th_treeview['show']='headings'
                    
                    tree_eee_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from eee_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_eee_6th_treeview.delete(*tree_eee_6th_treeview.get_children())
                                for row in rows:
                                    tree_eee_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_eee_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_eee_6th_treeview.xview)
                    scrolly.configure(command=tree_eee_6th_treeview.yview)

                   
                    tree_eee_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_eee_6th_treeview.heading('subjects',text="Subjects")
                    tree_eee_6th_treeview.heading('semister',text="Semister")
                    tree_eee_6th_treeview.heading('scheme',text="Scheme")
                    tree_eee_6th_treeview.heading('branch',text="Branch")
                    tree_eee_6th_treeview.heading('marks',text="Marks")
                    tree_eee_6th_treeview.heading('student_usn',text="Usn")
                    

                    tree_eee_6th_treeview.column('subject_code',width=200)
                    tree_eee_6th_treeview.column('subjects',width=200)
                    tree_eee_6th_treeview.column('semister',width=200)
                    tree_eee_6th_treeview.column('scheme',width=200)
                    tree_eee_6th_treeview.column('branch',width=200)
                    tree_eee_6th_treeview.column('marks',width=200)
                    tree_eee_6th_treeview.column('student_usn',width=200)

                    tree_eee_6th_treeview['show']='headings'
                    
                    tree_eee_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from eee_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_eee_7th_treeview.delete(*tree_eee_7th_treeview.get_children())
                                for row in rows:
                                    tree_eee_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_eee_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_eee_7th_treeview.xview)
                    scrolly.configure(command=tree_eee_7th_treeview.yview)

                
                    tree_eee_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_eee_7th_treeview.heading('subjects',text="Subjects")
                    tree_eee_7th_treeview.heading('semister',text="Semister")
                    tree_eee_7th_treeview.heading('scheme',text="Scheme")
                    tree_eee_7th_treeview.heading('branch',text="Branch")
                    tree_eee_7th_treeview.heading('marks',text="Marks")
                    tree_eee_7th_treeview.heading('student_usn',text="Usn")
                    

                    
                    tree_eee_7th_treeview.column('subject_code',width=200)
                    tree_eee_7th_treeview.column('subjects',width=200)
                    tree_eee_7th_treeview.column('semister',width=200)
                    tree_eee_7th_treeview.column('scheme',width=200)
                    tree_eee_7th_treeview.column('branch',width=200)
                    tree_eee_7th_treeview.column('marks',width=200)
                    tree_eee_7th_treeview.column('student_usn',width=200)

                    tree_eee_7th_treeview['show']='headings'
                    
                    tree_eee_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from eee_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_eee_8th_treeview.delete(*tree_eee_8th_treeview.get_children())
                                for row in rows:
                                    tree_eee_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_eee_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_eee_8th_treeview.xview)
                    scrolly.configure(command=tree_eee_8th_treeview.yview)

                   
                    tree_eee_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_eee_8th_treeview.heading('subjects',text="Subjects")
                    tree_eee_8th_treeview.heading('semister',text="Semister")
                    tree_eee_8th_treeview.heading('scheme',text="Scheme")
                    tree_eee_8th_treeview.heading('branch',text="Branch")
                    tree_eee_8th_treeview.heading('marks',text="Marks")
                    tree_eee_8th_treeview.heading('student_usn',text="Usn")
                    

           
                    tree_eee_8th_treeview.column('subject_code',width=200)
                    tree_eee_8th_treeview.column('subjects',width=200)
                    tree_eee_8th_treeview.column('semister',width=200)
                    tree_eee_8th_treeview.column('scheme',width=200)
                    tree_eee_8th_treeview.column('branch',width=200)
                    tree_eee_8th_treeview.column('marks',width=200)
                    tree_eee_8th_treeview.column('student_usn',width=200)

                    tree_eee_8th_treeview['show']='headings'
                    
                    tree_eee_8th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Computer_Science_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from cs_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_cs_3rd_treeview.delete(*tree_cs_3rd_treeview.get_children())
                                for row in rows:
                                    tree_cs_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_cs_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_cs_3rd_treeview.xview)
                    scrolly.configure(command=tree_cs_3rd_treeview.yview)

               
                    tree_cs_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_cs_3rd_treeview.heading('subjects',text="Subjects")
                    tree_cs_3rd_treeview.heading('semister',text="Semister")
                    tree_cs_3rd_treeview.heading('scheme',text="Scheme")
                    tree_cs_3rd_treeview.heading('branch',text="Branch")
                    tree_cs_3rd_treeview.heading('marks',text="Marks")
                    tree_cs_3rd_treeview.heading('student_usn',text="Usn")
                    

            
                    tree_cs_3rd_treeview.column('subject_code',width=200)
                    tree_cs_3rd_treeview.column('subjects',width=200)
                    tree_cs_3rd_treeview.column('semister',width=200)
                    tree_cs_3rd_treeview.column('scheme',width=200)
                    tree_cs_3rd_treeview.column('branch',width=200)
                    tree_cs_3rd_treeview.column('marks',width=200)
                    tree_cs_3rd_treeview.column('student_usn',width=200)

                    tree_cs_3rd_treeview['show']='headings'
                    
                    tree_cs_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Computer_Science_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from cs_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_cs_4th_treeview.delete(*tree_cs_4th_treeview.get_children())
                                for row in rows:
                                    tree_cs_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_cs_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_cs_4th_treeview.xview)
                    scrolly.configure(command=tree_cs_4th_treeview.yview)

                   
                    tree_cs_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_cs_4th_treeview.heading('subjects',text="Subjects")
                    tree_cs_4th_treeview.heading('semister',text="Semister")
                    tree_cs_4th_treeview.heading('scheme',text="Scheme")
                    tree_cs_4th_treeview.heading('branch',text="Branch")
                    tree_cs_4th_treeview.heading('marks',text="Marks")
                    tree_cs_4th_treeview.heading('student_usn',text="Usn")
                    

          
                    tree_cs_4th_treeview.column('subject_code',width=200)
                    tree_cs_4th_treeview.column('subjects',width=200)
                    tree_cs_4th_treeview.column('semister',width=200)
                    tree_cs_4th_treeview.column('scheme',width=200)
                    tree_cs_4th_treeview.column('branch',width=200)
                    tree_cs_4th_treeview.column('marks',width=200)
                    tree_cs_4th_treeview.column('student_usn',width=200)

                    tree_cs_4th_treeview['show']='headings'
                    
                    tree_cs_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Computer_Science_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from cs_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_cs_5th_treeview.delete(*tree_cs_5th_treeview.get_children())
                                for row in rows:
                                    tree_cs_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_cs_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_cs_5th_treeview.xview)
                    scrolly.configure(command=tree_cs_5th_treeview.yview)

               
                    tree_cs_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_cs_5th_treeview.heading('subjects',text="Subjects")
                    tree_cs_5th_treeview.heading('semister',text="Semister")
                    tree_cs_5th_treeview.heading('scheme',text="Scheme")
                    tree_cs_5th_treeview.heading('branch',text="Branch")
                    tree_cs_5th_treeview.heading('marks',text="Marks")
                    tree_cs_5th_treeview.heading('student_usn',text="Usn")
                    

                    tree_cs_5th_treeview.column('subject_code',width=200)
                    tree_cs_5th_treeview.column('subjects',width=200)
                    tree_cs_5th_treeview.column('semister',width=200)
                    tree_cs_5th_treeview.column('scheme',width=200)
                    tree_cs_5th_treeview.column('branch',width=200)
                    tree_cs_5th_treeview.column('marks',width=200)
                    tree_cs_5th_treeview.column('student_usn',width=200)

                    tree_cs_5th_treeview['show']='headings'
                    
                    tree_cs_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Computer_Science_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from cs_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_cs_6th_treeview.delete(*tree_cs_6th_treeview.get_children())
                                for row in rows:
                                    tree_cs_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_cs_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_cs_6th_treeview.xview)
                    scrolly.configure(command=tree_cs_6th_treeview.yview)

                    
                    tree_cs_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_cs_6th_treeview.heading('subjects',text="Subjects")
                    tree_cs_6th_treeview.heading('semister',text="Semister")
                    tree_cs_6th_treeview.heading('scheme',text="Scheme")
                    tree_cs_6th_treeview.heading('branch',text="Branch")
                    tree_cs_6th_treeview.heading('marks',text="Marks")
                    tree_cs_6th_treeview.heading('student_usn',text="Usn")
                    

              
                    tree_cs_6th_treeview.column('subject_code',width=200)
                    tree_cs_6th_treeview.column('subjects',width=200)
                    tree_cs_6th_treeview.column('semister',width=200)
                    tree_cs_6th_treeview.column('scheme',width=200)
                    tree_cs_6th_treeview.column('branch',width=200)
                    tree_cs_6th_treeview.column('marks',width=200)
                    tree_cs_6th_treeview.column('student_usn',width=200)

                    tree_cs_6th_treeview['show']='headings'
                    
                    tree_cs_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Computer_Science_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from cs_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_cs_7th_treeview.delete(*tree_cs_7th_treeview.get_children())
                                for row in rows:
                                    tree_cs_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_cs_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_cs_7th_treeview.xview)
                    scrolly.configure(command=tree_cs_7th_treeview.yview)

                    tree_cs_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_cs_7th_treeview.heading('subjects',text="Subjects")
                    tree_cs_7th_treeview.heading('semister',text="Semister")
                    tree_cs_7th_treeview.heading('scheme',text="Scheme")
                    tree_cs_7th_treeview.heading('branch',text="Branch")
                    tree_cs_7th_treeview.heading('marks',text="Marks")
                    tree_cs_7th_treeview.heading('student_usn',text="Usn")
                    

                    tree_cs_7th_treeview.column('subject_code',width=200)
                    tree_cs_7th_treeview.column('subjects',width=200)
                    tree_cs_7th_treeview.column('semister',width=200)
                    tree_cs_7th_treeview.column('scheme',width=200)
                    tree_cs_7th_treeview.column('branch',width=200)
                    tree_cs_7th_treeview.column('marks',width=200)
                    tree_cs_7th_treeview.column('student_usn',width=200)

                    tree_cs_7th_treeview['show']='headings'
                    
                    tree_cs_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Computer_Science_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from cs_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_cs_8th_treeview.delete(*tree_cs_8th_treeview.get_children())
                                for row in rows:
                                    tree_cs_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_cs_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_cs_8th_treeview.xview)
                    scrolly.configure(command=tree_cs_8th_treeview.yview)

      
                    tree_cs_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_cs_8th_treeview.heading('subjects',text="Subjects")
                    tree_cs_8th_treeview.heading('semister',text="Semister")
                    tree_cs_8th_treeview.heading('scheme',text="Scheme")
                    tree_cs_8th_treeview.heading('branch',text="Branch")
                    tree_cs_8th_treeview.heading('marks',text="Marks")
                    tree_cs_8th_treeview.heading('student_usn',text="Usn")
                    

                 
                    tree_cs_8th_treeview.column('subject_code',width=200)
                    tree_cs_8th_treeview.column('subjects',width=200)
                    tree_cs_8th_treeview.column('semister',width=200)
                    tree_cs_8th_treeview.column('scheme',width=200)
                    tree_cs_8th_treeview.column('branch',width=200)
                    tree_cs_8th_treeview.column('marks',width=200)
                    tree_cs_8th_treeview.column('student_usn',width=200)

                    tree_cs_8th_treeview['show']='headings'
                    
                    tree_cs_8th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Information_Science_and_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from civil_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_civil_3rd_treeview.delete(*tree_civil_3rd_treeview.get_children())
                                for row in rows:
                                    tree_civil_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_civil_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_civil_3rd_treeview.xview)
                    scrolly.configure(command=tree_civil_3rd_treeview.yview)

                    tree_civil_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_civil_3rd_treeview.heading('subjects',text="Subjects")
                    tree_civil_3rd_treeview.heading('semister',text="Semister")
                    tree_civil_3rd_treeview.heading('scheme',text="Scheme")
                    tree_civil_3rd_treeview.heading('branch',text="Branch")
                    tree_civil_3rd_treeview.heading('marks',text="Marks")
                    tree_civil_3rd_treeview.heading('student_usn',text="Usn")
              
                    tree_civil_3rd_treeview.column('subject_code',width=200)
                    tree_civil_3rd_treeview.column('subjects',width=200)
                    tree_civil_3rd_treeview.column('semister',width=200)
                    tree_civil_3rd_treeview.column('scheme',width=200)
                    tree_civil_3rd_treeview.column('branch',width=200)
                    tree_civil_3rd_treeview.column('marks',width=200)
                    tree_civil_3rd_treeview.column('student_usn',width=200)

                    tree_civil_3rd_treeview['show']='headings'
                    
                    tree_civil_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Information_Science_and_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ise_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ise_4th_treeview.delete(*tree_ise_4th_treeview.get_children())
                                for row in rows:
                                    tree_ise_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ise_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ise_4th_treeview.xview)
                    scrolly.configure(command=tree_ise_4th_treeview.yview)

               
                    tree_ise_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_ise_4th_treeview.heading('subjects',text="Subjects")
                    tree_ise_4th_treeview.heading('semister',text="Semister")
                    tree_ise_4th_treeview.heading('scheme',text="Scheme")
                    tree_ise_4th_treeview.heading('branch',text="Branch")
                    tree_ise_4th_treeview.heading('marks',text="Marks")
                    tree_ise_4th_treeview.heading('student_usn',text="Usn")
                    

                   
                    tree_ise_4th_treeview.column('subject_code',width=200)
                    tree_ise_4th_treeview.column('subjects',width=200)
                    tree_ise_4th_treeview.column('semister',width=200)
                    tree_ise_4th_treeview.column('scheme',width=200)
                    tree_ise_4th_treeview.column('branch',width=200)
                    tree_ise_4th_treeview.column('marks',width=200)
                    tree_ise_4th_treeview.column('student_usn',width=200)

                    tree_ise_4th_treeview['show']='headings'
                    
                    tree_ise_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Information_Science_and_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ise_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ise_5th_treeview.delete(*tree_ise_5th_treeview.get_children())
                                for row in rows:
                                    tree_ise_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ise_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ise_5th_treeview.xview)
                    scrolly.configure(command=tree_ise_5th_treeview.yview)

              
                    tree_ise_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_ise_5th_treeview.heading('subjects',text="Subjects")
                    tree_ise_5th_treeview.heading('semister',text="Semister")
                    tree_ise_5th_treeview.heading('scheme',text="Scheme")
                    tree_ise_5th_treeview.heading('branch',text="Branch")
                    tree_ise_5th_treeview.heading('marks',text="Marks")
                    tree_ise_5th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ise_5th_treeview.column('subject_code',width=200)
                    tree_ise_5th_treeview.column('subjects',width=200)
                    tree_ise_5th_treeview.column('semister',width=200)
                    tree_ise_5th_treeview.column('scheme',width=200)
                    tree_ise_5th_treeview.column('branch',width=200)
                    tree_ise_5th_treeview.column('marks',width=200)
                    tree_ise_5th_treeview.column('student_usn',width=200)

                    tree_ise_5th_treeview['show']='headings'
                    
                    tree_ise_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Information_Science_and_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ise_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ise_6th_treeview.delete(*tree_ise_6th_treeview.get_children())
                                for row in rows:
                                    tree_ise_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ise_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ise_6th_treeview.xview)
                    scrolly.configure(command=tree_ise_6th_treeview.yview)

                    tree_ise_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_ise_6th_treeview.heading('subjects',text="Subjects")
                    tree_ise_6th_treeview.heading('semister',text="Semister")
                    tree_ise_6th_treeview.heading('scheme',text="Scheme")
                    tree_ise_6th_treeview.heading('branch',text="Branch")
                    tree_ise_6th_treeview.heading('marks',text="Marks")
                    tree_ise_6th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ise_6th_treeview.column('subject_code',width=200)
                    tree_ise_6th_treeview.column('subjects',width=200)
                    tree_ise_6th_treeview.column('semister',width=200)
                    tree_ise_6th_treeview.column('scheme',width=200)
                    tree_ise_6th_treeview.column('branch',width=200)
                    tree_ise_6th_treeview.column('marks',width=200)
                    tree_ise_6th_treeview.column('student_usn',width=200)

                    tree_ise_6th_treeview['show']='headings'
                    
                    tree_ise_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Information_Science_and_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ise_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ise_7th_treeview.delete(*tree_ise_7th_treeview.get_children())
                                for row in rows:
                                    tree_ise_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ise_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ise_7th_treeview.xview)
                    scrolly.configure(command=tree_ise_7th_treeview.yview)

                 
                    tree_ise_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_ise_7th_treeview.heading('subjects',text="Subjects")
                    tree_ise_7th_treeview.heading('semister',text="Semister")
                    tree_ise_7th_treeview.heading('scheme',text="Scheme")
                    tree_ise_7th_treeview.heading('branch',text="Branch")
                    tree_ise_7th_treeview.heading('marks',text="Marks")
                    tree_ise_7th_treeview.heading('student_usn',text="Usn")
                    

                   
                    tree_ise_7th_treeview.column('subject_code',width=200)
                    tree_ise_7th_treeview.column('subjects',width=200)
                    tree_ise_7th_treeview.column('semister',width=200)
                    tree_ise_7th_treeview.column('scheme',width=200)
                    tree_ise_7th_treeview.column('branch',width=200)
                    tree_ise_7th_treeview.column('marks',width=200)
                    tree_ise_7th_treeview.column('student_usn',width=200)

                    tree_ise_7th_treeview['show']='headings'
                    
                    tree_ise_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Information_Science_and_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ise_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ise_8th_treeview.delete(*tree_ise_8th_treeview.get_children())
                                for row in rows:
                                    tree_ise_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ise_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ise_8th_treeview.xview)
                    scrolly.configure(command=tree_ise_8th_treeview.yview)

          
                    tree_ise_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_ise_8th_treeview.heading('subjects',text="Subjects")
                    tree_ise_8th_treeview.heading('semister',text="Semister")
                    tree_ise_8th_treeview.heading('scheme',text="Scheme")
                    tree_ise_8th_treeview.heading('branch',text="Branch")
                    tree_ise_8th_treeview.heading('marks',text="Marks")
                    tree_ise_8th_treeview.heading('student_usn',text="Usn")
                    

              
                    tree_ise_8th_treeview.column('subject_code',width=200)
                    tree_ise_8th_treeview.column('subjects',width=200)
                    tree_ise_8th_treeview.column('semister',width=200)
                    tree_ise_8th_treeview.column('scheme',width=200)
                    tree_ise_8th_treeview.column('branch',width=200)
                    tree_ise_8th_treeview.column('marks',width=200)
                    tree_ise_8th_treeview.column('student_usn',width=200)

                    tree_ise_8th_treeview['show']='headings'
                    
                    tree_ise_8th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
            if self.var_sem_select.get()=='3rd_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ete_3rd_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ete_3rd_treeview.delete(*tree_ete_3rd_treeview.get_children())
                                for row in rows:
                                    tree_ete_3rd_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ete_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ete_3rd_treeview.xview)
                    scrolly.configure(command=tree_ete_3rd_treeview.yview)

                  
                    tree_ete_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_ete_3rd_treeview.heading('subjects',text="Subjects")
                    tree_ete_3rd_treeview.heading('semister',text="Semister")
                    tree_ete_3rd_treeview.heading('scheme',text="Scheme")
                    tree_ete_3rd_treeview.heading('branch',text="Branch")
                    tree_ete_3rd_treeview.heading('marks',text="Marks")
                    tree_ete_3rd_treeview.heading('student_usn',text="Usn")
                    

                    tree_ete_3rd_treeview.column('subject_code',width=200)
                    tree_ete_3rd_treeview.column('subjects',width=200)
                    tree_ete_3rd_treeview.column('semister',width=200)
                    tree_ete_3rd_treeview.column('scheme',width=200)
                    tree_ete_3rd_treeview.column('branch',width=200)
                    tree_ete_3rd_treeview.column('marks',width=200)
                    tree_ete_3rd_treeview.column('student_usn',width=200)

                    tree_ete_3rd_treeview['show']='headings'
                    
                    tree_ete_3rd_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
            if self.var_sem_select.get()=='4th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ete_4th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ete_4th_treeview.delete(*tree_ete_4th_treeview.get_children())
                                for row in rows:
                                    tree_ete_4th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ete_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ete_4th_treeview.xview)
                    scrolly.configure(command=tree_ete_4th_treeview.yview)

                    tree_ete_4th_treeview.heading('subject_code',text="Subject Code")
                    tree_ete_4th_treeview.heading('subjects',text="Subjects")
                    tree_ete_4th_treeview.heading('semister',text="Semister")
                    tree_ete_4th_treeview.heading('scheme',text="Scheme")
                    tree_ete_4th_treeview.heading('branch',text="Branch")
                    tree_ete_4th_treeview.heading('marks',text="Marks")
                    tree_ete_4th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ete_4th_treeview.column('subject_code',width=200)
                    tree_ete_4th_treeview.column('subjects',width=200)
                    tree_ete_4th_treeview.column('semister',width=200)
                    tree_ete_4th_treeview.column('scheme',width=200)
                    tree_ete_4th_treeview.column('branch',width=200)
                    tree_ete_4th_treeview.column('marks',width=200)
                    tree_ete_4th_treeview.column('student_usn',width=200)

                    tree_ete_4th_treeview['show']='headings'
                    
                    tree_ete_4th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
            if self.var_sem_select.get()=='5th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ete_5th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ete_5th_treeview.delete(*tree_ete_5th_treeview.get_children())
                                for row in rows:
                                    tree_ete_5th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ete_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ete_5th_treeview.xview)
                    scrolly.configure(command=tree_ete_5th_treeview.yview)

             
                    tree_ete_5th_treeview.heading('subject_code',text="Subject Code")
                    tree_ete_5th_treeview.heading('subjects',text="Subjects")
                    tree_ete_5th_treeview.heading('semister',text="Semister")
                    tree_ete_5th_treeview.heading('scheme',text="Scheme")
                    tree_ete_5th_treeview.heading('branch',text="Branch")
                    tree_ete_5th_treeview.heading('marks',text="Marks")
                    tree_ete_5th_treeview.heading('student_usn',text="Usn")
                    

                    tree_ete_5th_treeview.column('subject_code',width=200)
                    tree_ete_5th_treeview.column('subjects',width=200)
                    tree_ete_5th_treeview.column('semister',width=200)
                    tree_ete_5th_treeview.column('scheme',width=200)
                    tree_ete_5th_treeview.column('branch',width=200)
                    tree_ete_5th_treeview.column('marks',width=200)
                    tree_ete_5th_treeview.column('student_usn',width=200)

                    tree_ete_5th_treeview['show']='headings'
                    
                    tree_ete_5th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
            if self.var_sem_select.get()=='6th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ete_6th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ete_6th_treeview.delete(*tree_ete_6th_treeview.get_children())
                                for row in rows:
                                    tree_ete_6th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ete_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ete_6th_treeview.xview)
                    scrolly.configure(command=tree_ete_6th_treeview.yview)

                  
                    tree_ete_6th_treeview.heading('subject_code',text="Subject Code")
                    tree_ete_6th_treeview.heading('subjects',text="Subjects")
                    tree_ete_6th_treeview.heading('semister',text="Semister")
                    tree_ete_6th_treeview.heading('scheme',text="Scheme")
                    tree_ete_6th_treeview.heading('branch',text="Branch")
                    tree_ete_6th_treeview.heading('marks',text="Marks")
                    tree_ete_6th_treeview.heading('student_usn',text="Usn")
                    

                   
                    tree_ete_6th_treeview.column('subject_code',width=200)
                    tree_ete_6th_treeview.column('subjects',width=200)
                    tree_ete_6th_treeview.column('semister',width=200)
                    tree_ete_6th_treeview.column('scheme',width=200)
                    tree_ete_6th_treeview.column('branch',width=200)
                    tree_ete_6th_treeview.column('marks',width=200)
                    tree_ete_6th_treeview.column('student_usn',width=200)

                    tree_ete_6th_treeview['show']='headings'
                    
                    tree_ete_6th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
            if self.var_sem_select.get()=='7th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ete_7th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ete_7th_treeview.delete(*tree_ete_7th_treeview.get_children())
                                for row in rows:
                                    tree_ete_7th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ete_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ete_7th_treeview.xview)
                    scrolly.configure(command=tree_ete_7th_treeview.yview)

                    tree_ete_7th_treeview.heading('subject_code',text="Subject Code")
                    tree_ete_7th_treeview.heading('subjects',text="Subjects")
                    tree_ete_7th_treeview.heading('semister',text="Semister")
                    tree_ete_7th_treeview.heading('scheme',text="Scheme")
                    tree_ete_7th_treeview.heading('branch',text="Branch")
                    tree_ete_7th_treeview.heading('marks',text="Marks")
                    tree_ete_7th_treeview.heading('student_usn',text="Usn")
  
                    tree_ete_7th_treeview.column('subject_code',width=200)
                    tree_ete_7th_treeview.column('subjects',width=200)
                    tree_ete_7th_treeview.column('semister',width=200)
                    tree_ete_7th_treeview.column('scheme',width=200)
                    tree_ete_7th_treeview.column('branch',width=200)
                    tree_ete_7th_treeview.column('marks',width=200)
                    tree_ete_7th_treeview.column('student_usn',width=200)

                    tree_ete_7th_treeview['show']='headings'
                    
                    tree_ete_7th_treeview.pack(fill=BOTH,expand=1)
        if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
            if self.var_sem_select.get()=='8th_Semister':
                if self.var_scheme_select.get()=='2018':
                    def search_result():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_usn_entry.get()=='':
                                messagebox.showerror('Error','The student USN Number must be required',parent=frame)
                            else:
                                cur.execute(f"select * from ete_8th_student_resultss where student_usn LIKE '%{self.var_usn_entry.get()}%' ")
                                rows=cur.fetchall()
                                tree_ete_8th_treeview.delete(*tree_ete_8th_treeview.get_children())
                                for row in rows:
                                    tree_ete_8th_treeview.insert('',END,values=row)
                        except Exception as ex:
                            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=frame)
#########################################################################
                    frame=Frame(self.root,bg='white')
                    frame.place(x=0,y=100,width=1040,height=325)

                    usn_entry=ttk.Entry(frame,textvariable=self.var_usn_entry,width=40)
                    usn_entry.place(x=300,y=20)

                    result_search_button=ttk.Button(frame,text='Serach Result.',command=search_result)
                    result_search_button.place(x=550,y=18)
#########################################################3
                    label_frame3=LabelFrame(frame)
                    label_frame3.place(x=10,y=85,width=1030,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ete_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ete_8th_treeview.xview)
                    scrolly.configure(command=tree_ete_8th_treeview.yview)

              
                    tree_ete_8th_treeview.heading('subject_code',text="Subject Code")
                    tree_ete_8th_treeview.heading('subjects',text="Subjects")
                    tree_ete_8th_treeview.heading('semister',text="Semister")
                    tree_ete_8th_treeview.heading('scheme',text="Scheme")
                    tree_ete_8th_treeview.heading('branch',text="Branch")
                    tree_ete_8th_treeview.heading('marks',text="Marks")
                    tree_ete_8th_treeview.heading('student_usn',text="Usn")
           
                    tree_ete_8th_treeview.column('subject_code',width=200)
                    tree_ete_8th_treeview.column('subjects',width=200)
                    tree_ete_8th_treeview.column('semister',width=200)
                    tree_ete_8th_treeview.column('scheme',width=200)
                    tree_ete_8th_treeview.column('branch',width=200)
                    tree_ete_8th_treeview.column('marks',width=200)
                    tree_ete_8th_treeview.column('student_usn',width=200)

                    tree_ete_8th_treeview['show']='headings'
                    
                    tree_ete_8th_treeview.pack(fill=BOTH,expand=1)
        
         
if __name__=='__main__':
    root=tk.Tk()
    ob1=ShowStudentResult(root)
    root.mainloop()