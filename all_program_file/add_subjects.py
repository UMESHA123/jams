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

class AddSubjects():
    def __init__(self,root):
        self.root=root
        self.root.title("Add subjects")
        self.root.geometry('1055x440+213+145')
        self.root.resizable(False,False)
        self.root.configure(bg='white')
        ################################################
        self.var_sem_select=StringVar()
        self.var_branch_select=StringVar()

        self.var_che_subject=StringVar()
        self.var_che_subject_serach=StringVar()

        self.var_phy_subject=StringVar()
        self.var_phy_subject_serach=StringVar()

        self.var_civil_3rd_subject=StringVar()
        self.var_civil_3rd_subject_serach=StringVar()

        self.var_civil_4th_subject=StringVar()
        self.var_civil_4th_subject_serach=StringVar()

        self.var_civil_5th_subject=StringVar()
        self.var_civil_5th_subject_serach=StringVar()

        self.var_civil_6th_subject=StringVar()
        self.var_civil_6th_subject_serach=StringVar()

        self.var_civil_7th_subject=StringVar()
        self.var_civil_7th_subject_serach=StringVar()

        self.var_civil_8th_subject=StringVar()
        self.var_civil_8th_subject_serach=StringVar()

        self.var_ece_3rd_subject=StringVar()
        self.var_ece_3rd_subject_serach=StringVar()

        self.var_ece_4th_subject=StringVar()
        self.var_ece_4th_subject_serach=StringVar()

        self.var_ece_5th_subject=StringVar()
        self.var_ece_5th_subject_serach=StringVar()

        self.var_ece_6th_subject=StringVar()
        self.var_ece_6th_subject_serach=StringVar()

        self.var_ece_7th_subject=StringVar()
        self.var_ece_7th_subject_serach=StringVar()

        self.var_ece_8th_subject=StringVar()
        self.var_ece_8th_subject_serach=StringVar()

        self.var_mech_3rd_subject=StringVar()
        self.var_mech_3rd_subject_serach=StringVar()

        self.var_mech_4th_subject=StringVar()
        self.var_mech_4th_subject_serach=StringVar()

        self.var_mech_5th_subject=StringVar()
        self.var_mech_5th_subject_serach=StringVar()

        self.var_mech_6th_subject=StringVar()
        self.var_mech_6th_subject_serach=StringVar()

        self.var_mech_7th_subject=StringVar()
        self.var_mech_7th_subject_serach=StringVar()

        self.var_mech_8th_subject=StringVar()
        self.var_mech_8th_subject_serach=StringVar()

        self.var_eee_3rd_subject=StringVar()
        self.var_eee_3rd_subject_serach=StringVar()

        self.var_eee_4th_subject=StringVar()
        self.var_eee_4th_subject_serach=StringVar()

        self.var_eee_5th_subject=StringVar()
        self.var_eee_5th_subject_serach=StringVar()

        self.var_eee_6th_subject=StringVar()
        self.var_eee_6th_subject_serach=StringVar()

        self.var_eee_7th_subject=StringVar()
        self.var_eee_7th_subject_serach=StringVar()

        self.var_eee_8th_subject=StringVar()
        self.var_eee_8th_subject_serach=StringVar()

        self.var_cs_3rd_subject=StringVar()
        self.var_cs_3rd_subject_serach=StringVar()

        self.var_cs_4th_subject=StringVar()
        self.var_cs_4th_subject_serach=StringVar()

        self.var_cs_5th_subject=StringVar()
        self.var_cs_5th_subject_serach=StringVar()

        self.var_cs_6th_subject=StringVar()
        self.var_cs_6th_subject_serach=StringVar()

        self.var_cs_7th_subject=StringVar()
        self.var_cs_7th_subject_serach=StringVar()

        self.var_cs_8th_subject=StringVar()
        self.var_cs_8th_subject_serach=StringVar()

        self.var_ete_3rd_subject=StringVar()
        self.var_ete_3rd_subject_serach=StringVar()

        self.var_ete_4th_subject=StringVar()
        self.var_ete_4th_subject_serach=StringVar()

        self.var_ete_5th_subject=StringVar()
        self.var_ete_5th_subject_serach=StringVar()

        self.var_ete_6th_subject=StringVar()
        self.var_ete_6th_subject_serach=StringVar()

        self.var_ete_7th_subject=StringVar()
        self.var_ete_7th_subject_serach=StringVar()

        self.var_ete_8th_subject=StringVar()
        self.var_ete_8th_subject_serach=StringVar()

        self.var_ise_3rd_subject=StringVar()
        self.var_ise_3rd_subject_serach=StringVar()

        self.var_ise_4th_subject=StringVar()
        self.var_ise_4th_subject_serach=StringVar()

        self.var_ise_5th_subject=StringVar()
        self.var_ise_5th_subject_serach=StringVar()

        self.var_ise_6th_subject=StringVar()
        self.var_ise_6th_subject_serach=StringVar()

        self.var_ise_7th_subject=StringVar()
        self.var_ise_7th_subject_serach=StringVar()

        self.var_ise_8th_subject=StringVar()
        self.var_ise_8th_subject_serach=StringVar()
        ################################################

        top_label=tk.Label(self.root,text='Add Faculty',font=('Bahnschrift',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)

        menu_frame=tk.LabelFrame(self.root,text='Menu',font=('times now roman',10,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=10,y=45,width=1035,height=55)

        self.sem_select=ttk.Combobox(menu_frame,width=30,textvariable=self.var_sem_select,state='readonly')
        self.sem_select.grid(row=0,column=0,padx=4,pady=3) 
        self.sem_select['values']=(
            'CHEMISTRY_cycle',
            'PHYSICS_cycle',
            '3rd_Semister',
            '4th_Semister',
            '5th_Semister',
            '6th_Semister',
            '7th_Semister',
            '8th_Semister'
        )

        branch_select=ttk.Combobox(menu_frame,width=30,textvariable=self.var_branch_select,state='readonly')
        branch_select.grid(row=0,column=1,padx=4,pady=3)
        branch_select['values']=(
                                    '1st_semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering'
                                    

        )
        button1=ttk.Button(menu_frame,text='Search',width=15,command=self.search).grid(row=0,column=2,padx=4,pady=3)
        button2=ttk.Button(menu_frame,text='Add to Data Base',width=20).grid(row=0,column=3,padx=4,pady=3)
        button3=ttk.Button(menu_frame,text='Update',width=15).grid(row=0,column=4,padx=4,pady=3)
        button4=ttk.Button(menu_frame,text='Delete',width=15).grid(row=0,column=5,padx=4,pady=3)
        button4=ttk.Button(menu_frame,text='Clear',width=15).grid(row=0,column=6,padx=4,pady=3)
    def search(self):
        ################################# chemistry cycle
        if self.var_sem_select.get()=='CHEMISTRY_cycle':
            if self.var_branch_select.get()=='1st_semister':
    
                def add_che_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_che_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_che_subjects (semister,branch,che_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_che_subject.get()
                        ))
                        con.commit()
                        fetch_che_subjects()
                        con.close()
                def fetch_che_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_che_subjects')
                        rows=cur.fetchall()
                        self.student_che_subjects_table.delete(*self.student_che_subjects_table.get_children())

                        for row in rows:
                            self.student_che_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_che_data(ev):
                    read=self.student_che_subjects_table.focus()
                    content=self.student_che_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_che_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_che_data():
                    fetch_che_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_che_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_che_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_che_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_che_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_che_subjects_table.focus()
                                        content=self.student_che_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_che_subjects set che_subjects=%s where cid=%s',(
                                        self.var_che_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_che_subjects()
                                    clear_che_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_che_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_che_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_che_subjects where che_subjects=%s ',(self.var_che_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_che_data()
                                    fetch_che_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def che_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_che_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_che_subjects where che_subjects LIKE '%{self.var_che_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_che_subjects_table.delete(*self.student_che_subjects_table.get_children())
                            for row in rows:
                                self.student_che_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                chemistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                chemistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_che_subject)
                chemistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_che_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=che_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_che_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_che_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_che_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_che_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_che_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','che_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_che_subjects_table.xview)
                newscrolly.config(command=self.student_che_subjects_table.yview)

                
                self.student_che_subjects_table.heading('semister',text='Semister')
                self.student_che_subjects_table.heading('branch',text='Branch')
                self.student_che_subjects_table.heading('che_subjects',text='Subjects')

                
                
                self.student_che_subjects_table.column('semister',width=100)
                self.student_che_subjects_table.column('branch',width=200)
                self.student_che_subjects_table.column('che_subjects',width=200)

                self.student_che_subjects_table['show']='headings'

                self.student_che_subjects_table.pack(fill=BOTH,expand=1)
                fetch_che_subjects()
                self.student_che_subjects_table.bind('<ButtonRelease-1>',get_che_data)
                



        
        ############################################## physics cycle
        if self.var_sem_select.get()=='PHYSICS_cycle':
            if self.var_branch_select.get()=='2nd_semister':
                def add_phy_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_phy_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_phy_subjects (semister,branch,phy_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_phy_subject.get()
                        ))
                        con.commit()
                        fetch_phy_subjects()
                        con.close()
                def fetch_phy_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_phy_subjects')
                        rows=cur.fetchall()
                        self.student_phy_subjects_table.delete(*self.student_phy_subjects_table.get_children())

                        for row in rows:
                            self.student_phy_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_phy_data(ev):
                    read=self.student_phy_subjects_table.focus()
                    content=self.student_phy_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[2])
                    self.var_phy_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_phy_data():
                    fetch_phy_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_phy_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_phy_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_phy_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_phy_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_phy_subjects_table.focus()
                                        content=self.student_phy_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_phy_subjects set phy_subjects=%s where cid=%s',(
                                        self.var_phy_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_phy_subjects()
                                    clear_phy_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_phy_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_phy_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_phy_subjects where phy_subjects=%s ',(self.var_phy_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_phy_data()
                                    fetch_phy_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def phy_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_phy_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_phy_subjects where phy_subjects LIKE '%{self.var_phy_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_phy_subjects_table.delete(*self.student_phy_subjects_table.get_children())
                            for row in rows:
                                self.student_phy_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                phymistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                phymistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_phy_subject)
                phymistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_phy_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=phy_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_phy_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_phy_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_phy_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_phy_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_phy_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','phy_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_phy_subjects_table.xview)
                newscrolly.config(command=self.student_phy_subjects_table.yview)

                
                self.student_phy_subjects_table.heading('semister',text='Semister')
                self.student_phy_subjects_table.heading('branch',text='Branch')
                self.student_phy_subjects_table.heading('phy_subjects',text='Subjects')

                self.student_phy_subjects_table.column('semister',width=100)
                self.student_phy_subjects_table.column('branch',width=200)
                self.student_phy_subjects_table.column('phy_subjects',width=200)

                self.student_phy_subjects_table['show']='headings'

                self.student_phy_subjects_table.pack(fill=BOTH,expand=1)
                fetch_phy_subjects()
                self.student_phy_subjects_table.bind('<ButtonRelease-1>',get_phy_data)
        ############################################################ civil
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                def add_civil_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_civil_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_civil_3rd_subjects (semister,branch,civil_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_civil_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_civil_3rd_subjects()
                        con.close()
                def fetch_civil_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_civil_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_civil_3rd_subjects_table.delete(*self.student_civil_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_civil_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_civil_3rd_data(ev):
                    read=self.student_civil_3rd_subjects_table.focus()
                    content=self.student_civil_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_civil_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_civil_3rd_data():
                    fetch_civil_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_civil_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_civil_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_civil_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_civil_3rd_subjects_table.focus()
                                        content=self.student_civil_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_civil_3rd_subjects set civil_3rd_subjects=%s where cid=%s',(
                                        self.var_civil_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_civil_3rd_subjects()
                                    clear_civil_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_civil_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_civil_3rd_subjects where civil_3rd_subjects=%s ',(self.var_civil_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_civil_3rd_data()
                                    fetch_civil_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def civil_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_civil_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_civil_3rd_subjects where civil_3rd_subjects LIKE '%{self.var_civil_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_civil_3rd_subjects_table.delete(*self.student_civil_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_civil_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                civil_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                civil_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_civil_3rd_subject)
                civil_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_civil_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=civil_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_civil_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_civil_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_civil_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_civil_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_civil_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','civil_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_civil_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_civil_3rd_subjects_table.yview)

            
                self.student_civil_3rd_subjects_table.heading('semister',text='Semister')
                self.student_civil_3rd_subjects_table.heading('branch',text='Branch')
                self.student_civil_3rd_subjects_table.heading('civil_3rd_subjects',text='Subjects')

                self.student_civil_3rd_subjects_table.column('semister',width=100)
                self.student_civil_3rd_subjects_table.column('branch',width=200)
                self.student_civil_3rd_subjects_table.column('civil_3rd_subjects',width=200)

                self.student_civil_3rd_subjects_table['show']='headings'

                self.student_civil_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_civil_3rd_subjects()
                self.student_civil_3rd_subjects_table.bind('<ButtonRelease-1>',get_civil_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                def add_civil_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_civil_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_civil_4th_subjects (semister,branch,civil_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_civil_4th_subject.get()
                        ))
                        con.commit()
                        fetch_civil_4th_subjects()
                        con.close()
                def fetch_civil_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_civil_4th_subjects')
                        rows=cur.fetchall()
                        self.student_civil_4th_subjects_table.delete(*self.student_civil_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_civil_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_civil_4th_data(ev):
                    read=self.student_civil_4th_subjects_table.focus()
                    content=self.student_civil_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_civil_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_civil_4th_data():
                    fetch_civil_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_civil_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_civil_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_civil_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_civil_4th_subjects_table.focus()
                                        content=self.student_civil_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_civil_4th_subjects set civil_4th_subjects=%s where cid=%s',(
                                        self.var_civil_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_civil_4th_subjects()
                                    clear_civil_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_civil_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_civil_4th_subjects where civil_4th_subjects=%s ',(self.var_civil_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_civil_4th_data()
                                    fetch_civil_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def civil_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_civil_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_civil_4th_subjects where civil_4th_subjects LIKE '%{self.var_civil_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_civil_4th_subjects_table.delete(*self.student_civil_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_civil_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                civil_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                civil_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_civil_4th_subject)
                civil_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_civil_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=civil_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_civil_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_civil_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_civil_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_civil_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_civil_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','civil_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_civil_4th_subjects_table.xview)
                newscrolly.config(command=self.student_civil_4th_subjects_table.yview)

               
                self.student_civil_4th_subjects_table.heading('semister',text='Semister')
                self.student_civil_4th_subjects_table.heading('branch',text='Branch')
                self.student_civil_4th_subjects_table.heading('civil_4th_subjects',text='Subjects')

           
                self.student_civil_4th_subjects_table.column('semister',width=100)
                self.student_civil_4th_subjects_table.column('branch',width=200)
                self.student_civil_4th_subjects_table.column('civil_4th_subjects',width=200)

                self.student_civil_4th_subjects_table['show']='headings'

                self.student_civil_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_civil_4th_subjects()
                self.student_civil_4th_subjects_table.bind('<ButtonRelease-1>',get_civil_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                def add_civil_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_civil_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_civil_5th_subjects (semister,branch,civil_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_civil_5th_subject.get()
                        ))
                        con.commit()
                        fetch_civil_5th_subjects()
                        con.close()
                def fetch_civil_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_civil_5th_subjects')
                        rows=cur.fetchall()
                        self.student_civil_5th_subjects_table.delete(*self.student_civil_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_civil_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_civil_5th_data(ev):
                    read=self.student_civil_5th_subjects_table.focus()
                    content=self.student_civil_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_civil_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_civil_5th_data():
                    fetch_civil_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_civil_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_civil_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_civil_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_civil_5th_subjects_table.focus()
                                        content=self.student_civil_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_civil_5th_subjects set civil_5th_subjects=%s where cid=%s',(
                                        self.var_civil_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_civil_5th_subjects()
                                    clear_civil_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_civil_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_civil_5th_subjects where civil_5th_subjects=%s ',(self.var_civil_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_civil_5th_data()
                                    fetch_civil_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def civil_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_civil_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_civil_5th_subjects where civil_5th_subjects LIKE '%{self.var_civil_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_civil_5th_subjects_table.delete(*self.student_civil_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_civil_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                civil_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                civil_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_civil_5th_subject)
                civil_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_civil_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=civil_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_civil_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_civil_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_civil_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_civil_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_civil_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','civil_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_civil_5th_subjects_table.xview)
                newscrolly.config(command=self.student_civil_5th_subjects_table.yview)

        
                self.student_civil_5th_subjects_table.heading('semister',text='Semister')
                self.student_civil_5th_subjects_table.heading('branch',text='Branch')
                self.student_civil_5th_subjects_table.heading('civil_5th_subjects',text='Subjects')

              
                self.student_civil_5th_subjects_table.column('semister',width=100)
                self.student_civil_5th_subjects_table.column('branch',width=200)
                self.student_civil_5th_subjects_table.column('civil_5th_subjects',width=200)

                self.student_civil_5th_subjects_table['show']='headings'

                self.student_civil_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_civil_5th_subjects()
                self.student_civil_5th_subjects_table.bind('<ButtonRelease-1>',get_civil_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                def add_civil_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_civil_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_civil_6th_subjects (semister,branch,civil_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_civil_6th_subject.get()
                        ))
                        con.commit()
                        fetch_civil_6th_subjects()
                        con.close()
                def fetch_civil_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_civil_6th_subjects')
                        rows=cur.fetchall()
                        self.student_civil_6th_subjects_table.delete(*self.student_civil_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_civil_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_civil_6th_data(ev):
                    read=self.student_civil_6th_subjects_table.focus()
                    content=self.student_civil_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_civil_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_civil_6th_data():
                    fetch_civil_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_civil_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_civil_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_civil_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_civil_6th_subjects_table.focus()
                                        content=self.student_civil_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_civil_6th_subjects set civil_6th_subjects=%s where cid=%s',(
                                        self.var_civil_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_civil_6th_subjects()
                                    clear_civil_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_civil_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_civil_6th_subjects where civil_6th_subjects=%s ',(self.var_civil_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_civil_6th_data()
                                    fetch_civil_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def civil_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_civil_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_civil_6th_subjects where civil_6th_subjects LIKE '%{self.var_civil_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_civil_6th_subjects_table.delete(*self.student_civil_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_civil_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                civil_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                civil_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_civil_6th_subject)
                civil_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_civil_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=civil_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_civil_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_civil_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_civil_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_civil_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_civil_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','civil_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_civil_6th_subjects_table.xview)
                newscrolly.config(command=self.student_civil_6th_subjects_table.yview)

              
                self.student_civil_6th_subjects_table.heading('semister',text='Semister')
                self.student_civil_6th_subjects_table.heading('branch',text='Branch')
                self.student_civil_6th_subjects_table.heading('civil_6th_subjects',text='Subjects')

                self.student_civil_6th_subjects_table.column('semister',width=100)
                self.student_civil_6th_subjects_table.column('branch',width=200)
                self.student_civil_6th_subjects_table.column('civil_6th_subjects',width=200)

                self.student_civil_6th_subjects_table['show']='headings'

                self.student_civil_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_civil_6th_subjects()
                self.student_civil_6th_subjects_table.bind('<ButtonRelease-1>',get_civil_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                def add_civil_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_civil_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_civil_7th_subjects (semister,branch,civil_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_civil_7th_subject.get()
                        ))
                        con.commit()
                        fetch_civil_7th_subjects()
                        con.close()
                def fetch_civil_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_civil_7th_subjects')
                        rows=cur.fetchall()
                        self.student_civil_7th_subjects_table.delete(*self.student_civil_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_civil_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_civil_7th_data(ev):
                    read=self.student_civil_7th_subjects_table.focus()
                    content=self.student_civil_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_civil_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_civil_7th_data():
                    fetch_civil_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_civil_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_civil_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_civil_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_civil_7th_subjects_table.focus()
                                        content=self.student_civil_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_civil_7th_subjects set civil_7th_subjects=%s where cid=%s',(
                                        self.var_civil_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_civil_7th_subjects()
                                    clear_civil_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_civil_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_civil_7th_subjects where civil_7th_subjects=%s ',(self.var_civil_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_civil_7th_data()
                                    fetch_civil_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def civil_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_civil_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_civil_7th_subjects where civil_7th_subjects LIKE '%{self.var_civil_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_civil_7th_subjects_table.delete(*self.student_civil_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_civil_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                civil_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                civil_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_civil_7th_subject)
                civil_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_civil_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=civil_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_civil_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_civil_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_civil_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_civil_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_civil_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','civil_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_civil_7th_subjects_table.xview)
                newscrolly.config(command=self.student_civil_7th_subjects_table.yview)

                self.student_civil_7th_subjects_table.heading('semister',text='Semister')
                self.student_civil_7th_subjects_table.heading('branch',text='Branch')
                self.student_civil_7th_subjects_table.heading('civil_7th_subjects',text='Subjects')

                self.student_civil_7th_subjects_table.column('semister',width=100)
                self.student_civil_7th_subjects_table.column('branch',width=200)
                self.student_civil_7th_subjects_table.column('civil_7th_subjects',width=200)

                self.student_civil_7th_subjects_table['show']='headings'

                self.student_civil_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_civil_7th_subjects()
                self.student_civil_7th_subjects_table.bind('<ButtonRelease-1>',get_civil_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                def add_civil_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_civil_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_civil_8th_subjects (semister,branch,civil_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_civil_8th_subject.get()
                        ))
                        con.commit()
                        fetch_civil_8th_subjects()
                        con.close()
                def fetch_civil_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_civil_8th_subjects')
                        rows=cur.fetchall()
                        self.student_civil_8th_subjects_table.delete(*self.student_civil_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_civil_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_civil_8th_data(ev):
                    read=self.student_civil_8th_subjects_table.focus()
                    content=self.student_civil_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_civil_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_civil_8th_data():
                    fetch_civil_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_civil_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_civil_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_civil_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_civil_8th_subjects_table.focus()
                                        content=self.student_civil_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_civil_8th_subjects set civil_8th_subjects=%s where cid=%s',(
                                        self.var_civil_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_civil_8th_subjects()
                                    clear_civil_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_civil_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_civil_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_civil_8th_subjects where civil_8th_subjects=%s ',(self.var_civil_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_civil_8th_data()
                                    fetch_civil_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def civil_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_civil_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_civil_8th_subjects where civil_8th_subjects LIKE '%{self.var_civil_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_civil_8th_subjects_table.delete(*self.student_civil_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_civil_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                civil_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                civil_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_civil_8th_subject)
                civil_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_civil_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=civil_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_civil_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_civil_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_civil_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_civil_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_civil_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','civil_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_civil_8th_subjects_table.xview)
                newscrolly.config(command=self.student_civil_8th_subjects_table.yview)

           
                self.student_civil_8th_subjects_table.heading('semister',text='Semister')
                self.student_civil_8th_subjects_table.heading('branch',text='Branch')
                self.student_civil_8th_subjects_table.heading('civil_8th_subjects',text='Subjects')

                self.student_civil_8th_subjects_table.column('semister',width=100)
                self.student_civil_8th_subjects_table.column('branch',width=200)
                self.student_civil_8th_subjects_table.column('civil_8th_subjects',width=200)

                self.student_civil_8th_subjects_table['show']='headings'

                self.student_civil_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_civil_8th_subjects()
                self.student_civil_8th_subjects_table.bind('<ButtonRelease-1>',get_civil_8th_data)
        #######################################################################  mechnaical
       
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                def add_mech_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_mech_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_mech_3rd_subjects (semister,branch,mech_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_mech_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_mech_3rd_subjects()
                        con.close()
                def fetch_mech_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_mech_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_mech_3rd_subjects_table.delete(*self.student_mech_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_mech_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_mech_3rd_data(ev):
                    read=self.student_mech_3rd_subjects_table.focus()
                    content=self.student_mech_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_mech_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_mech_3rd_data():
                    fetch_mech_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_mech_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_mech_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_mech_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_mech_3rd_subjects_table.focus()
                                        content=self.student_mech_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_mech_3rd_subjects set mech_3rd_subjects=%s where cid=%s',(
                                        self.var_mech_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_mech_3rd_subjects()
                                    clear_mech_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_mech_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_mech_3rd_subjects where mech_3rd_subjects=%s ',(self.var_mech_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_mech_3rd_data()
                                    fetch_mech_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def mech_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_mech_3rd_subjects where mech_3rd_subjects LIKE '%{self.var_mech_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_mech_3rd_subjects_table.delete(*self.student_mech_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_mech_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                mech_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                mech_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_mech_3rd_subject)
                mech_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_mech_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=mech_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_mech_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_mech_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_mech_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_mech_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_mech_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','mech_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_mech_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_mech_3rd_subjects_table.yview)

             
                self.student_mech_3rd_subjects_table.heading('semister',text='Semister')
                self.student_mech_3rd_subjects_table.heading('branch',text='Branch')
                self.student_mech_3rd_subjects_table.heading('mech_3rd_subjects',text='Subjects')

                self.student_mech_3rd_subjects_table.column('semister',width=100)
                self.student_mech_3rd_subjects_table.column('branch',width=200)
                self.student_mech_3rd_subjects_table.column('mech_3rd_subjects',width=200)

                self.student_mech_3rd_subjects_table['show']='headings'

                self.student_mech_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_mech_3rd_subjects()
                self.student_mech_3rd_subjects_table.bind('<ButtonRelease-1>',get_mech_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                def add_mech_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_mech_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_mech_4th_subjects (semister,branch,mech_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_mech_4th_subject.get()
                        ))
                        con.commit()
                        fetch_mech_4th_subjects()
                        con.close()
                def fetch_mech_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_mech_4th_subjects')
                        rows=cur.fetchall()
                        self.student_mech_4th_subjects_table.delete(*self.student_mech_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_mech_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_mech_4th_data(ev):
                    read=self.student_mech_4th_subjects_table.focus()
                    content=self.student_mech_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_mech_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_mech_4th_data():
                    fetch_mech_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_mech_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_mech_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_mech_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_mech_4th_subjects_table.focus()
                                        content=self.student_mech_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_mech_4th_subjects set mech_4th_subjects=%s where cid=%s',(
                                        self.var_mech_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_mech_4th_subjects()
                                    clear_mech_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_mech_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_mech_4th_subjects where mech_4th_subjects=%s ',(self.var_mech_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_mech_4th_data()
                                    fetch_mech_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def mech_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_mech_4th_subjects where mech_4th_subjects LIKE '%{self.var_mech_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_mech_4th_subjects_table.delete(*self.student_mech_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_mech_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                mech_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                mech_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_mech_4th_subject)
                mech_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_mech_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=mech_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_mech_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_mech_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_mech_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_mech_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_mech_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','mech_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_mech_4th_subjects_table.xview)
                newscrolly.config(command=self.student_mech_4th_subjects_table.yview)

               
                self.student_mech_4th_subjects_table.heading('semister',text='Semister')
                self.student_mech_4th_subjects_table.heading('branch',text='Branch')
                self.student_mech_4th_subjects_table.heading('mech_4th_subjects',text='Subjects')

           
                self.student_mech_4th_subjects_table.column('semister',width=100)
                self.student_mech_4th_subjects_table.column('branch',width=200)
                self.student_mech_4th_subjects_table.column('mech_4th_subjects',width=200)

                self.student_mech_4th_subjects_table['show']='headings'

                self.student_mech_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_mech_4th_subjects()
                self.student_mech_4th_subjects_table.bind('<ButtonRelease-1>',get_mech_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                def add_mech_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_mech_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_mech_5th_subjects (semister,branch,mech_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_mech_5th_subject.get()
                        ))
                        con.commit()
                        fetch_mech_5th_subjects()
                        con.close()
                def fetch_mech_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_mech_5th_subjects')
                        rows=cur.fetchall()
                        self.student_mech_5th_subjects_table.delete(*self.student_mech_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_mech_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_mech_5th_data(ev):
                    read=self.student_mech_5th_subjects_table.focus()
                    content=self.student_mech_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_mech_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_mech_5th_data():
                    fetch_mech_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_mech_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_mech_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_mech_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_mech_5th_subjects_table.focus()
                                        content=self.student_mech_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_mech_5th_subjects set mech_5th_subjects=%s where cid=%s',(
                                        self.var_mech_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_mech_5th_subjects()
                                    clear_mech_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_mech_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_mech_5th_subjects where mech_5th_subjects=%s ',(self.var_mech_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_mech_5th_data()
                                    fetch_mech_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def mech_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_mech_5th_subjects where mech_5th_subjects LIKE '%{self.var_mech_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_mech_5th_subjects_table.delete(*self.student_mech_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_mech_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                mech_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                mech_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_mech_5th_subject)
                mech_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_mech_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=mech_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_mech_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_mech_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_mech_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_mech_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_mech_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','mech_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_mech_5th_subjects_table.xview)
                newscrolly.config(command=self.student_mech_5th_subjects_table.yview)

                
                self.student_mech_5th_subjects_table.heading('semister',text='Semister')
                self.student_mech_5th_subjects_table.heading('branch',text='Branch')
                self.student_mech_5th_subjects_table.heading('mech_5th_subjects',text='Subjects')

                self.student_mech_5th_subjects_table.column(width=100)
                self.student_mech_5th_subjects_table.column('semister',width=100)
                self.student_mech_5th_subjects_table.column('branch',width=200)
                self.student_mech_5th_subjects_table.column('mech_5th_subjects',width=200)

                self.student_mech_5th_subjects_table['show']='headings'

                self.student_mech_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_mech_5th_subjects()
                self.student_mech_5th_subjects_table.bind('<ButtonRelease-1>',get_mech_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                def add_mech_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_mech_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_mech_6th_subjects (semister,branch,mech_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_mech_6th_subject.get()
                        ))
                        con.commit()
                        fetch_mech_6th_subjects()
                        con.close()
                def fetch_mech_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_mech_6th_subjects')
                        rows=cur.fetchall()
                        self.student_mech_6th_subjects_table.delete(*self.student_mech_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_mech_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_mech_6th_data(ev):
                    read=self.student_mech_6th_subjects_table.focus()
                    content=self.student_mech_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_mech_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_mech_6th_data():
                    fetch_mech_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_mech_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_mech_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_mech_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_mech_6th_subjects_table.focus()
                                        content=self.student_mech_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_mech_6th_subjects set mech_6th_subjects=%s where cid=%s',(
                                        self.var_mech_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_mech_6th_subjects()
                                    clear_mech_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_mech_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_mech_6th_subjects where mech_6th_subjects=%s ',(self.var_mech_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_mech_6th_data()
                                    fetch_mech_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def mech_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_mech_6th_subjects where mech_6th_subjects LIKE '%{self.var_mech_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_mech_6th_subjects_table.delete(*self.student_mech_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_mech_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                mech_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                mech_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_mech_6th_subject)
                mech_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_mech_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=mech_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_mech_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_mech_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_mech_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_mech_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_mech_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','mech_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_mech_6th_subjects_table.xview)
                newscrolly.config(command=self.student_mech_6th_subjects_table.yview)

               
                self.student_mech_6th_subjects_table.heading('semister',text='Semister')
                self.student_mech_6th_subjects_table.heading('branch',text='Branch')
                self.student_mech_6th_subjects_table.heading('mech_6th_subjects',text='Subjects')

                
                self.student_mech_6th_subjects_table.column('semister',width=100)
                self.student_mech_6th_subjects_table.column('branch',width=200)
                self.student_mech_6th_subjects_table.column('mech_6th_subjects',width=200)

                self.student_mech_6th_subjects_table['show']='headings'

                self.student_mech_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_mech_6th_subjects()
                self.student_mech_6th_subjects_table.bind('<ButtonRelease-1>',get_mech_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                def add_mech_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_mech_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_mech_7th_subjects (semister,branch,mech_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_mech_7th_subject.get()
                        ))
                        con.commit()
                        fetch_mech_7th_subjects()
                        con.close()
                def fetch_mech_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_mech_7th_subjects')
                        rows=cur.fetchall()
                        self.student_mech_7th_subjects_table.delete(*self.student_mech_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_mech_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_mech_7th_data(ev):
                    read=self.student_mech_7th_subjects_table.focus()
                    content=self.student_mech_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_mech_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_mech_7th_data():
                    fetch_mech_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_mech_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_mech_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_mech_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_mech_7th_subjects_table.focus()
                                        content=self.student_mech_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_mech_7th_subjects set mech_7th_subjects=%s where cid=%s',(
                                        self.var_mech_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_mech_7th_subjects()
                                    clear_mech_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_mech_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_mech_7th_subjects where mech_7th_subjects=%s ',(self.var_mech_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_mech_7th_data()
                                    fetch_mech_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def mech_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_mech_7th_subjects where mech_7th_subjects LIKE '%{self.var_mech_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_mech_7th_subjects_table.delete(*self.student_mech_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_mech_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                mech_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                mech_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_mech_7th_subject)
                mech_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_mech_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=mech_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_mech_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_mech_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_mech_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_mech_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_mech_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','mech_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_mech_7th_subjects_table.xview)
                newscrolly.config(command=self.student_mech_7th_subjects_table.yview)

                
                self.student_mech_7th_subjects_table.heading('semister',text='Semister')
                self.student_mech_7th_subjects_table.heading('branch',text='Branch')
                self.student_mech_7th_subjects_table.heading('mech_7th_subjects',text='Subjects')

                self.student_mech_7th_subjects_table.column('semister',width=100)
                self.student_mech_7th_subjects_table.column('branch',width=200)
                self.student_mech_7th_subjects_table.column('mech_7th_subjects',width=200)

                self.student_mech_7th_subjects_table['show']='headings'

                self.student_mech_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_mech_7th_subjects()
                self.student_mech_7th_subjects_table.bind('<ButtonRelease-1>',get_mech_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                def add_mech_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_mech_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_mech_8th_subjects (semister,branch,mech_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_mech_8th_subject.get()
                        ))
                        con.commit()
                        fetch_mech_8th_subjects()
                        con.close()
                def fetch_mech_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_mech_8th_subjects')
                        rows=cur.fetchall()
                        self.student_mech_8th_subjects_table.delete(*self.student_mech_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_mech_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_mech_8th_data(ev):
                    read=self.student_mech_8th_subjects_table.focus()
                    content=self.student_mech_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_mech_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_mech_8th_data():
                    fetch_mech_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_mech_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_mech_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_mech_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_mech_8th_subjects_table.focus()
                                        content=self.student_mech_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_mech_8th_subjects set mech_8th_subjects=%s where cid=%s',(
                                        self.var_mech_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_mech_8th_subjects()
                                    clear_mech_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_mech_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_mech_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_mech_8th_subjects where mech_8th_subjects=%s ',(self.var_mech_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_mech_8th_data()
                                    fetch_mech_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def mech_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_mech_8th_subjects where mech_8th_subjects LIKE '%{self.var_mech_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_mech_8th_subjects_table.delete(*self.student_mech_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_mech_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                mech_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                mech_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_mech_8th_subject)
                mech_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_mech_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=mech_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_mech_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_mech_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_mech_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_mech_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_mech_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','mech_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_mech_8th_subjects_table.xview)
                newscrolly.config(command=self.student_mech_8th_subjects_table.yview)

                
                self.student_mech_8th_subjects_table.heading('semister',text='Semister')
                self.student_mech_8th_subjects_table.heading('branch',text='Branch')
                self.student_mech_8th_subjects_table.heading('mech_8th_subjects',text='Subjects')

           
                self.student_mech_8th_subjects_table.column('semister',width=100)
                self.student_mech_8th_subjects_table.column('branch',width=200)
                self.student_mech_8th_subjects_table.column('mech_8th_subjects',width=200)

                self.student_mech_8th_subjects_table['show']='headings'

                self.student_mech_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_mech_8th_subjects()
                self.student_mech_8th_subjects_table.bind('<ButtonRelease-1>',get_mech_8th_data)
      

        
        ########################################################### electronic and communication 
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                def add_ece_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ece_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ece_3rd_subjects (semister,branch,ece_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ece_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_ece_3rd_subjects()
                        con.close()
                def fetch_ece_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ece_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_ece_3rd_subjects_table.delete(*self.student_ece_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_ece_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ece_3rd_data(ev):
                    read=self.student_ece_3rd_subjects_table.focus()
                    content=self.student_ece_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ece_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ece_3rd_data():
                    fetch_ece_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ece_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ece_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ece_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ece_3rd_subjects_table.focus()
                                        content=self.student_ece_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ece_3rd_subjects set ece_3rd_subjects=%s where cid=%s',(
                                        self.var_ece_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ece_3rd_subjects()
                                    clear_ece_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ece_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ece_3rd_subjects where ece_3rd_subjects=%s ',(self.var_ece_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ece_3rd_data()
                                    fetch_ece_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ece_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ece_3rd_subjects where ece_3rd_subjects LIKE '%{self.var_ece_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ece_3rd_subjects_table.delete(*self.student_ece_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_ece_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ece_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ece_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ece_3rd_subject)
                ece_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ece_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ece_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ece_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ece_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ece_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ece_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ece_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ece_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ece_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_ece_3rd_subjects_table.yview)

                self.student_ece_3rd_subjects_table.heading('semister',text='Semister')
                self.student_ece_3rd_subjects_table.heading('branch',text='Branch')
                self.student_ece_3rd_subjects_table.heading('ece_3rd_subjects',text='Subjects')

                self.student_ece_3rd_subjects_table.column('semister',width=100)
                self.student_ece_3rd_subjects_table.column('branch',width=200)
                self.student_ece_3rd_subjects_table.column('ece_3rd_subjects',width=200)

                self.student_ece_3rd_subjects_table['show']='headings'

                self.student_ece_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ece_3rd_subjects()
                self.student_ece_3rd_subjects_table.bind('<ButtonRelease-1>',get_ece_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                def add_ece_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ece_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ece_4th_subjects (semister,branch,ece_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ece_4th_subject.get()
                        ))
                        con.commit()
                        fetch_ece_4th_subjects()
                        con.close()
                def fetch_ece_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ece_4th_subjects')
                        rows=cur.fetchall()
                        self.student_ece_4th_subjects_table.delete(*self.student_ece_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_ece_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ece_4th_data(ev):
                    read=self.student_ece_4th_subjects_table.focus()
                    content=self.student_ece_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ece_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ece_4th_data():
                    fetch_ece_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ece_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ece_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ece_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ece_4th_subjects_table.focus()
                                        content=self.student_ece_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ece_4th_subjects set ece_4th_subjects=%s where cid=%s',(
                                        self.var_ece_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ece_4th_subjects()
                                    clear_ece_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ece_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ece_4th_subjects where ece_4th_subjects=%s ',(self.var_ece_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ece_4th_data()
                                    fetch_ece_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ece_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ece_4th_subjects where ece_4th_subjects LIKE '%{self.var_ece_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ece_4th_subjects_table.delete(*self.student_ece_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_ece_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ece_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ece_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ece_4th_subject)
                ece_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ece_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ece_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ece_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ece_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ece_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ece_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ece_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ece_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ece_4th_subjects_table.xview)
                newscrolly.config(command=self.student_ece_4th_subjects_table.yview)

                self.student_ece_4th_subjects_table.heading('semister',text='Semister')
                self.student_ece_4th_subjects_table.heading('branch',text='Branch')
                self.student_ece_4th_subjects_table.heading('ece_4th_subjects',text='Subjects')

 
                self.student_ece_4th_subjects_table.column('semister',width=100)
                self.student_ece_4th_subjects_table.column('branch',width=200)
                self.student_ece_4th_subjects_table.column('ece_4th_subjects',width=200)

                self.student_ece_4th_subjects_table['show']='headings'

                self.student_ece_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ece_4th_subjects()
                self.student_ece_4th_subjects_table.bind('<ButtonRelease-1>',get_ece_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                def add_ece_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ece_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ece_5th_subjects (semister,branch,ece_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ece_5th_subject.get()
                        ))
                        con.commit()
                        fetch_ece_5th_subjects()
                        con.close()
                def fetch_ece_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ece_5th_subjects')
                        rows=cur.fetchall()
                        self.student_ece_5th_subjects_table.delete(*self.student_ece_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_ece_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ece_5th_data(ev):
                    read=self.student_ece_5th_subjects_table.focus()
                    content=self.student_ece_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ece_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ece_5th_data():
                    fetch_ece_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ece_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ece_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ece_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ece_5th_subjects_table.focus()
                                        content=self.student_ece_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ece_5th_subjects set ece_5th_subjects=%s where cid=%s',(
                                        self.var_ece_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ece_5th_subjects()
                                    clear_ece_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ece_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ece_5th_subjects where ece_5th_subjects=%s ',(self.var_ece_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ece_5th_data()
                                    fetch_ece_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ece_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ece_5th_subjects where ece_5th_subjects LIKE '%{self.var_ece_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ece_5th_subjects_table.delete(*self.student_ece_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_ece_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ece_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ece_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ece_5th_subject)
                ece_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ece_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ece_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ece_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ece_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ece_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ece_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ece_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ece_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ece_5th_subjects_table.xview)
                newscrolly.config(command=self.student_ece_5th_subjects_table.yview)

                
                self.student_ece_5th_subjects_table.heading('semister',text='Semister')
                self.student_ece_5th_subjects_table.heading('branch',text='Branch')
                self.student_ece_5th_subjects_table.heading('ece_5th_subjects',text='Subjects')

                
                self.student_ece_5th_subjects_table.column('semister',width=100)
                self.student_ece_5th_subjects_table.column('branch',width=200)
                self.student_ece_5th_subjects_table.column('ece_5th_subjects',width=200)

                self.student_ece_5th_subjects_table['show']='headings'

                self.student_ece_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ece_5th_subjects()
                self.student_ece_5th_subjects_table.bind('<ButtonRelease-1>',get_ece_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                def add_ece_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ece_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ece_6th_subjects (semister,branch,ece_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ece_6th_subject.get()
                        ))
                        con.commit()
                        fetch_ece_6th_subjects()
                        con.close()
                def fetch_ece_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ece_6th_subjects')
                        rows=cur.fetchall()
                        self.student_ece_6th_subjects_table.delete(*self.student_ece_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_ece_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ece_6th_data(ev):
                    read=self.student_ece_6th_subjects_table.focus()
                    content=self.student_ece_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ece_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ece_6th_data():
                    fetch_ece_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ece_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ece_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ece_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ece_6th_subjects_table.focus()
                                        content=self.student_ece_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ece_6th_subjects set ece_6th_subjects=%s where cid=%s',(
                                        self.var_ece_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ece_6th_subjects()
                                    clear_ece_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ece_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ece_6th_subjects where ece_6th_subjects=%s ',(self.var_ece_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ece_6th_data()
                                    fetch_ece_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ece_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ece_6th_subjects where ece_6th_subjects LIKE '%{self.var_ece_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ece_6th_subjects_table.delete(*self.student_ece_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_ece_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ece_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ece_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ece_6th_subject)
                ece_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ece_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ece_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ece_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ece_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ece_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ece_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ece_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ece_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ece_6th_subjects_table.xview)
                newscrolly.config(command=self.student_ece_6th_subjects_table.yview)

            
                self.student_ece_6th_subjects_table.heading('semister',text='Semister')
                self.student_ece_6th_subjects_table.heading('branch',text='Branch')
                self.student_ece_6th_subjects_table.heading('ece_6th_subjects',text='Subjects')

                self.student_ece_6th_subjects_table.column('semister',width=100)
                self.student_ece_6th_subjects_table.column('branch',width=200)
                self.student_ece_6th_subjects_table.column('ece_6th_subjects',width=200)

                self.student_ece_6th_subjects_table['show']='headings'

                self.student_ece_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ece_6th_subjects()
                self.student_ece_6th_subjects_table.bind('<ButtonRelease-1>',get_ece_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                def add_ece_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ece_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ece_7th_subjects (semister,branch,ece_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ece_7th_subject.get()
                        ))
                        con.commit()
                        fetch_ece_7th_subjects()
                        con.close()
                def fetch_ece_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ece_7th_subjects')
                        rows=cur.fetchall()
                        self.student_ece_7th_subjects_table.delete(*self.student_ece_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_ece_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ece_7th_data(ev):
                    read=self.student_ece_7th_subjects_table.focus()
                    content=self.student_ece_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ece_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ece_7th_data():
                    fetch_ece_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ece_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ece_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ece_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ece_7th_subjects_table.focus()
                                        content=self.student_ece_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ece_7th_subjects set ece_7th_subjects=%s where cid=%s',(
                                        self.var_ece_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ece_7th_subjects()
                                    clear_ece_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ece_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ece_7th_subjects where ece_7th_subjects=%s ',(self.var_ece_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ece_7th_data()
                                    fetch_ece_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ece_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ece_7th_subjects where ece_7th_subjects LIKE '%{self.var_ece_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ece_7th_subjects_table.delete(*self.student_ece_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_ece_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ece_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ece_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ece_7th_subject)
                ece_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ece_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ece_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ece_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ece_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ece_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ece_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ece_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ece_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ece_7th_subjects_table.xview)
                newscrolly.config(command=self.student_ece_7th_subjects_table.yview)

                self.student_ece_7th_subjects_table.heading('semister',text='Semister')
                self.student_ece_7th_subjects_table.heading('branch',text='Branch')
                self.student_ece_7th_subjects_table.heading('ece_7th_subjects',text='Subjects')

               
                self.student_ece_7th_subjects_table.column('semister',width=100)
                self.student_ece_7th_subjects_table.column('branch',width=200)
                self.student_ece_7th_subjects_table.column('ece_7th_subjects',width=200)

                self.student_ece_7th_subjects_table['show']='headings'

                self.student_ece_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ece_7th_subjects()
                self.student_ece_7th_subjects_table.bind('<ButtonRelease-1>',get_ece_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                def add_ece_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ece_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ece_8th_subjects (semister,branch,ece_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ece_8th_subject.get()
                        ))
                        con.commit()
                        fetch_ece_8th_subjects()
                        con.close()
                def fetch_ece_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ece_8th_subjects')
                        rows=cur.fetchall()
                        self.student_ece_8th_subjects_table.delete(*self.student_ece_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_ece_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ece_8th_data(ev):
                    read=self.student_ece_8th_subjects_table.focus()
                    content=self.student_ece_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ece_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ece_8th_data():
                    fetch_ece_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ece_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ece_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ece_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ece_8th_subjects_table.focus()
                                        content=self.student_ece_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ece_8th_subjects set ece_8th_subjects=%s where cid=%s',(
                                        self.var_ece_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ece_8th_subjects()
                                    clear_ece_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ece_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ece_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ece_8th_subjects where ece_8th_subjects=%s ',(self.var_ece_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ece_8th_data()
                                    fetch_ece_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ece_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ece_8th_subjects where ece_8th_subjects LIKE '%{self.var_ece_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ece_8th_subjects_table.delete(*self.student_ece_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_ece_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ece_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ece_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ece_8th_subject)
                ece_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ece_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ece_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ece_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ece_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ece_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ece_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ece_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ece_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ece_8th_subjects_table.xview)
                newscrolly.config(command=self.student_ece_8th_subjects_table.yview)

             
                self.student_ece_8th_subjects_table.heading('semister',text='Semister')
                self.student_ece_8th_subjects_table.heading('branch',text='Branch')
                self.student_ece_8th_subjects_table.heading('ece_8th_subjects',text='Subjects')

             
                self.student_ece_8th_subjects_table.column('semister',width=100)
                self.student_ece_8th_subjects_table.column('branch',width=200)
                self.student_ece_8th_subjects_table.column('ece_8th_subjects',width=200)

                self.student_ece_8th_subjects_table['show']='headings'

                self.student_ece_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ece_8th_subjects()
                self.student_ece_8th_subjects_table.bind('<ButtonRelease-1>',get_ece_8th_data)
        #######################################################################  

        
        #################################################################### telecommunication
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                def add_ete_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ete_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ete_3rd_subjects (semister,branch,ete_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ete_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_ete_3rd_subjects()
                        con.close()
                def fetch_ete_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ete_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_ete_3rd_subjects_table.delete(*self.student_ete_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_ete_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ete_3rd_data(ev):
                    read=self.student_ete_3rd_subjects_table.focus()
                    content=self.student_ete_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ete_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ete_3rd_data():
                    fetch_ete_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ete_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ete_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ete_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ete_3rd_subjects_table.focus()
                                        content=self.student_ete_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ete_3rd_subjects set ete_3rd_subjects=%s where cid=%s',(
                                        self.var_ete_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ete_3rd_subjects()
                                    clear_ete_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ete_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ete_3rd_subjects where ete_3rd_subjects=%s ',(self.var_ete_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ete_3rd_data()
                                    fetch_ete_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ete_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ete_3rd_subjects where ete_3rd_subjects LIKE '%{self.var_ete_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ete_3rd_subjects_table.delete(*self.student_ete_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_ete_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ete_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ete_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ete_3rd_subject)
                ete_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ete_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ete_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ete_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ete_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ete_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ete_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ete_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ete_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ete_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_ete_3rd_subjects_table.yview)

                
                self.student_ete_3rd_subjects_table.heading('semister',text='Semister')
                self.student_ete_3rd_subjects_table.heading('branch',text='Branch')
                self.student_ete_3rd_subjects_table.heading('ete_3rd_subjects',text='Subjects')

                self.student_ete_3rd_subjects_table.column('semister',width=100)
                self.student_ete_3rd_subjects_table.column('branch',width=200)
                self.student_ete_3rd_subjects_table.column('ete_3rd_subjects',width=200)

                self.student_ete_3rd_subjects_table['show']='headings'

                self.student_ete_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ete_3rd_subjects()
                self.student_ete_3rd_subjects_table.bind('<ButtonRelease-1>',get_ete_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                def add_ete_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ete_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ete_4th_subjects (semister,branch,ete_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ete_4th_subject.get()
                        ))
                        con.commit()
                        fetch_ete_4th_subjects()
                        con.close()
                def fetch_ete_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ete_4th_subjects')
                        rows=cur.fetchall()
                        self.student_ete_4th_subjects_table.delete(*self.student_ete_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_ete_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ete_4th_data(ev):
                    read=self.student_ete_4th_subjects_table.focus()
                    content=self.student_ete_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ete_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ete_4th_data():
                    fetch_ete_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ete_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ete_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ete_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ete_4th_subjects_table.focus()
                                        content=self.student_ete_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ete_4th_subjects set ete_4th_subjects=%s where cid=%s',(
                                        self.var_ete_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ete_4th_subjects()
                                    clear_ete_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ete_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ete_4th_subjects where ete_4th_subjects=%s ',(self.var_ete_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ete_4th_data()
                                    fetch_ete_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ete_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ete_4th_subjects where ete_4th_subjects LIKE '%{self.var_ete_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ete_4th_subjects_table.delete(*self.student_ete_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_ete_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ete_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ete_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ete_4th_subject)
                ete_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ete_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ete_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ete_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ete_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ete_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ete_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ete_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ete_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ete_4th_subjects_table.xview)
                newscrolly.config(command=self.student_ete_4th_subjects_table.yview)

    
                self.student_ete_4th_subjects_table.heading('semister',text='Semister')
                self.student_ete_4th_subjects_table.heading('branch',text='Branch')
                self.student_ete_4th_subjects_table.heading('ete_4th_subjects',text='Subjects')

                self.student_ete_4th_subjects_table.column('semister',width=100)
                self.student_ete_4th_subjects_table.column('branch',width=200)
                self.student_ete_4th_subjects_table.column('ete_4th_subjects',width=200)

                self.student_ete_4th_subjects_table['show']='headings'

                self.student_ete_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ete_4th_subjects()
                self.student_ete_4th_subjects_table.bind('<ButtonRelease-1>',get_ete_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                def add_ete_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ete_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ete_5th_subjects (semister,branch,ete_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ete_5th_subject.get()
                        ))
                        con.commit()
                        fetch_ete_5th_subjects()
                        con.close()
                def fetch_ete_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ete_5th_subjects')
                        rows=cur.fetchall()
                        self.student_ete_5th_subjects_table.delete(*self.student_ete_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_ete_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ete_5th_data(ev):
                    read=self.student_ete_5th_subjects_table.focus()
                    content=self.student_ete_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ete_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ete_5th_data():
                    fetch_ete_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ete_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ete_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ete_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ete_5th_subjects_table.focus()
                                        content=self.student_ete_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ete_5th_subjects set ete_5th_subjects=%s where cid=%s',(
                                        self.var_ete_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ete_5th_subjects()
                                    clear_ete_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ete_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ete_5th_subjects where ete_5th_subjects=%s ',(self.var_ete_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ete_5th_data()
                                    fetch_ete_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ete_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ete_5th_subjects where ete_5th_subjects LIKE '%{self.var_ete_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ete_5th_subjects_table.delete(*self.student_ete_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_ete_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ete_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ete_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ete_5th_subject)
                ete_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ete_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ete_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ete_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ete_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ete_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ete_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ete_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ete_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ete_5th_subjects_table.xview)
                newscrolly.config(command=self.student_ete_5th_subjects_table.yview)

                self.student_ete_5th_subjects_table.heading('semister',text='Semister')
                self.student_ete_5th_subjects_table.heading('branch',text='Branch')
                self.student_ete_5th_subjects_table.heading('ete_5th_subjects',text='Subjects')

                self.student_ete_5th_subjects_table.column('semister',width=100)
                self.student_ete_5th_subjects_table.column('branch',width=200)
                self.student_ete_5th_subjects_table.column('ete_5th_subjects',width=200)

                self.student_ete_5th_subjects_table['show']='headings'

                self.student_ete_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ete_5th_subjects()
                self.student_ete_5th_subjects_table.bind('<ButtonRelease-1>',get_ete_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                def add_ete_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ete_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ete_6th_subjects (semister,branch,ete_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ete_6th_subject.get()
                        ))
                        con.commit()
                        fetch_ete_6th_subjects()
                        con.close()
                def fetch_ete_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ete_6th_subjects')
                        rows=cur.fetchall()
                        self.student_ete_6th_subjects_table.delete(*self.student_ete_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_ete_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ete_6th_data(ev):
                    read=self.student_ete_6th_subjects_table.focus()
                    content=self.student_ete_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ete_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ete_6th_data():
                    fetch_ete_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ete_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ete_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ete_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ete_6th_subjects_table.focus()
                                        content=self.student_ete_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ete_6th_subjects set ete_6th_subjects=%s where cid=%s',(
                                        self.var_ete_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ete_6th_subjects()
                                    clear_ete_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ete_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ete_6th_subjects where ete_6th_subjects=%s ',(self.var_ete_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ete_6th_data()
                                    fetch_ete_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ete_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ete_6th_subjects where ete_6th_subjects LIKE '%{self.var_ete_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ete_6th_subjects_table.delete(*self.student_ete_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_ete_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ete_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ete_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ete_6th_subject)
                ete_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ete_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ete_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ete_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ete_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ete_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ete_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ete_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ete_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ete_6th_subjects_table.xview)
                newscrolly.config(command=self.student_ete_6th_subjects_table.yview)

       
                self.student_ete_6th_subjects_table.heading('semister',text='Semister')
                self.student_ete_6th_subjects_table.heading('branch',text='Branch')
                self.student_ete_6th_subjects_table.heading('ete_6th_subjects',text='Subjects')

                self.student_ete_6th_subjects_table.column('semister',width=100)
                self.student_ete_6th_subjects_table.column('branch',width=200)
                self.student_ete_6th_subjects_table.column('ete_6th_subjects',width=200)

                self.student_ete_6th_subjects_table['show']='headings'

                self.student_ete_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ete_6th_subjects()
                self.student_ete_6th_subjects_table.bind('<ButtonRelease-1>',get_ete_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                def add_ete_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ete_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ete_7th_subjects (semister,branch,ete_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ete_7th_subject.get()
                        ))
                        con.commit()
                        fetch_ete_7th_subjects()
                        con.close()
                def fetch_ete_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ete_7th_subjects')
                        rows=cur.fetchall()
                        self.student_ete_7th_subjects_table.delete(*self.student_ete_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_ete_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ete_7th_data(ev):
                    read=self.student_ete_7th_subjects_table.focus()
                    content=self.student_ete_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ete_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ete_7th_data():
                    fetch_ete_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ete_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ete_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ete_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ete_7th_subjects_table.focus()
                                        content=self.student_ete_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ete_7th_subjects set ete_7th_subjects=%s where cid=%s',(
                                        self.var_ete_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ete_7th_subjects()
                                    clear_ete_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ete_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ete_7th_subjects where ete_7th_subjects=%s ',(self.var_ete_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ete_7th_data()
                                    fetch_ete_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ete_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ete_7th_subjects where ete_7th_subjects LIKE '%{self.var_ete_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ete_7th_subjects_table.delete(*self.student_ete_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_ete_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ete_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ete_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ete_7th_subject)
                ete_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ete_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ete_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ete_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ete_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ete_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ete_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ete_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ete_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ete_7th_subjects_table.xview)
                newscrolly.config(command=self.student_ete_7th_subjects_table.yview)

                self.student_ete_7th_subjects_table.heading('semister',text='Semister')
                self.student_ete_7th_subjects_table.heading('branch',text='Branch')
                self.student_ete_7th_subjects_table.heading('ete_7th_subjects',text='Subjects')

                self.student_ete_7th_subjects_table.column('semister',width=100)
                self.student_ete_7th_subjects_table.column('branch',width=200)
                self.student_ete_7th_subjects_table.column('ete_7th_subjects',width=200)

                self.student_ete_7th_subjects_table['show']='headings'

                self.student_ete_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ete_7th_subjects()
                self.student_ete_7th_subjects_table.bind('<ButtonRelease-1>',get_ete_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                def add_ete_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ete_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ete_8th_subjects (semister,branch,ete_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ete_8th_subject.get()
                        ))
                        con.commit()
                        fetch_ete_8th_subjects()
                        con.close()
                def fetch_ete_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ete_8th_subjects')
                        rows=cur.fetchall()
                        self.student_ete_8th_subjects_table.delete(*self.student_ete_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_ete_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ete_8th_data(ev):
                    read=self.student_ete_8th_subjects_table.focus()
                    content=self.student_ete_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ete_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ete_8th_data():
                    fetch_ete_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ete_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ete_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ete_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ete_8th_subjects_table.focus()
                                        content=self.student_ete_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ete_8th_subjects set ete_8th_subjects=%s where cid=%s',(
                                        self.var_ete_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ete_8th_subjects()
                                    clear_ete_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ete_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ete_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ete_8th_subjects where ete_8th_subjects=%s ',(self.var_ete_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ete_8th_data()
                                    fetch_ete_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ete_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ete_8th_subjects where ete_8th_subjects LIKE '%{self.var_ete_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ete_8th_subjects_table.delete(*self.student_ete_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_ete_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ete_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ete_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ete_8th_subject)
                ete_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ete_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ete_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ete_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ete_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ete_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ete_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ete_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ete_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ete_8th_subjects_table.xview)
                newscrolly.config(command=self.student_ete_8th_subjects_table.yview)

            
                self.student_ete_8th_subjects_table.heading('semister',text='Semister')
                self.student_ete_8th_subjects_table.heading('branch',text='Branch')
                self.student_ete_8th_subjects_table.heading('ete_8th_subjects',text='Subjects')

            
                self.student_ete_8th_subjects_table.column('semister',width=100)
                self.student_ete_8th_subjects_table.column('branch',width=200)
                self.student_ete_8th_subjects_table.column('ete_8th_subjects',width=200)

                self.student_ete_8th_subjects_table['show']='headings'

                self.student_ete_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ete_8th_subjects()
                self.student_ete_8th_subjects_table.bind('<ButtonRelease-1>',get_ete_8th_data)
        #######################################################################  

        
              
        ##################################################################  information science
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                def add_ise_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ise_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ise_3rd_subjects (semister,branch,ise_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ise_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_ise_3rd_subjects()
                        con.close()
                def fetch_ise_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ise_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_ise_3rd_subjects_table.delete(*self.student_ise_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_ise_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ise_3rd_data(ev):
                    read=self.student_ise_3rd_subjects_table.focus()
                    content=self.student_ise_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ise_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ise_3rd_data():
                    fetch_ise_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ise_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ise_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ise_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ise_3rd_subjects_table.focus()
                                        content=self.student_ise_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ise_3rd_subjects set ise_3rd_subjects=%s where cid=%s',(
                                        self.var_ise_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ise_3rd_subjects()
                                    clear_ise_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ise_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ise_3rd_subjects where ise_3rd_subjects=%s ',(self.var_ise_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ise_3rd_data()
                                    fetch_ise_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ise_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ise_3rd_subjects where ise_3rd_subjects LIKE '%{self.var_ise_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ise_3rd_subjects_table.delete(*self.student_ise_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_ise_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ise_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ise_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ise_3rd_subject)
                ise_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ise_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ise_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ise_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ise_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ise_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ise_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ise_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ise_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ise_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_ise_3rd_subjects_table.yview)

           
                self.student_ise_3rd_subjects_table.heading('semister',text='Semister')
                self.student_ise_3rd_subjects_table.heading('branch',text='Branch')
                self.student_ise_3rd_subjects_table.heading('ise_3rd_subjects',text='Subjects')

              
                self.student_ise_3rd_subjects_table.column('semister',width=100)
                self.student_ise_3rd_subjects_table.column('branch',width=200)
                self.student_ise_3rd_subjects_table.column('ise_3rd_subjects',width=200)

                self.student_ise_3rd_subjects_table['show']='headings'

                self.student_ise_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ise_3rd_subjects()
                self.student_ise_3rd_subjects_table.bind('<ButtonRelease-1>',get_ise_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                def add_ise_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ise_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ise_4th_subjects (semister,branch,ise_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ise_4th_subject.get()
                        ))
                        con.commit()
                        fetch_ise_4th_subjects()
                        con.close()
                def fetch_ise_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ise_4th_subjects')
                        rows=cur.fetchall()
                        self.student_ise_4th_subjects_table.delete(*self.student_ise_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_ise_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ise_4th_data(ev):
                    read=self.student_ise_4th_subjects_table.focus()
                    content=self.student_ise_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ise_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ise_4th_data():
                    fetch_ise_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ise_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ise_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ise_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ise_4th_subjects_table.focus()
                                        content=self.student_ise_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ise_4th_subjects set ise_4th_subjects=%s where cid=%s',(
                                        self.var_ise_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ise_4th_subjects()
                                    clear_ise_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ise_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ise_4th_subjects where ise_4th_subjects=%s ',(self.var_ise_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ise_4th_data()
                                    fetch_ise_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ise_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ise_4th_subjects where ise_4th_subjects LIKE '%{self.var_ise_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ise_4th_subjects_table.delete(*self.student_ise_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_ise_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ise_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ise_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ise_4th_subject)
                ise_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ise_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ise_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ise_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ise_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ise_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ise_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ise_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ise_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ise_4th_subjects_table.xview)
                newscrolly.config(command=self.student_ise_4th_subjects_table.yview)

                self.student_ise_4th_subjects_table.heading('semister',text='Semister')
                self.student_ise_4th_subjects_table.heading('branch',text='Branch')
                self.student_ise_4th_subjects_table.heading('ise_4th_subjects',text='Subjects')

                self.student_ise_4th_subjects_table.column('semister',width=100)
                self.student_ise_4th_subjects_table.column('branch',width=200)
                self.student_ise_4th_subjects_table.column('ise_4th_subjects',width=200)

                self.student_ise_4th_subjects_table['show']='headings'

                self.student_ise_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ise_4th_subjects()
                self.student_ise_4th_subjects_table.bind('<ButtonRelease-1>',get_ise_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                def add_ise_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ise_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ise_5th_subjects (semister,branch,ise_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ise_5th_subject.get()
                        ))
                        con.commit()
                        fetch_ise_5th_subjects()
                        con.close()
                def fetch_ise_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ise_5th_subjects')
                        rows=cur.fetchall()
                        self.student_ise_5th_subjects_table.delete(*self.student_ise_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_ise_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ise_5th_data(ev):
                    read=self.student_ise_5th_subjects_table.focus()
                    content=self.student_ise_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ise_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ise_5th_data():
                    fetch_ise_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ise_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ise_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ise_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ise_5th_subjects_table.focus()
                                        content=self.student_ise_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ise_5th_subjects set ise_5th_subjects=%s where cid=%s',(
                                        self.var_ise_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ise_5th_subjects()
                                    clear_ise_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ise_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ise_5th_subjects where ise_5th_subjects=%s ',(self.var_ise_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ise_5th_data()
                                    fetch_ise_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ise_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ise_5th_subjects where ise_5th_subjects LIKE '%{self.var_ise_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ise_5th_subjects_table.delete(*self.student_ise_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_ise_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ise_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ise_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ise_5th_subject)
                ise_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ise_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ise_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ise_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ise_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ise_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ise_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ise_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ise_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ise_5th_subjects_table.xview)
                newscrolly.config(command=self.student_ise_5th_subjects_table.yview)

            
                self.student_ise_5th_subjects_table.heading('semister',text='Semister')
                self.student_ise_5th_subjects_table.heading('branch',text='Branch')
                self.student_ise_5th_subjects_table.heading('ise_5th_subjects',text='Subjects')


                self.student_ise_5th_subjects_table.column('semister',width=100)
                self.student_ise_5th_subjects_table.column('branch',width=200)
                self.student_ise_5th_subjects_table.column('ise_5th_subjects',width=200)

                self.student_ise_5th_subjects_table['show']='headings'

                self.student_ise_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ise_5th_subjects()
                self.student_ise_5th_subjects_table.bind('<ButtonRelease-1>',get_ise_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                def add_ise_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ise_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ise_6th_subjects (semister,branch,ise_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ise_6th_subject.get()
                        ))
                        con.commit()
                        fetch_ise_6th_subjects()
                        con.close()
                def fetch_ise_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ise_6th_subjects')
                        rows=cur.fetchall()
                        self.student_ise_6th_subjects_table.delete(*self.student_ise_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_ise_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ise_6th_data(ev):
                    read=self.student_ise_6th_subjects_table.focus()
                    content=self.student_ise_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ise_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ise_6th_data():
                    fetch_ise_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ise_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ise_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ise_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ise_6th_subjects_table.focus()
                                        content=self.student_ise_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ise_6th_subjects set ise_6th_subjects=%s where cid=%s',(
                                        self.var_ise_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ise_6th_subjects()
                                    clear_ise_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ise_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ise_6th_subjects where ise_6th_subjects=%s ',(self.var_ise_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ise_6th_data()
                                    fetch_ise_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ise_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ise_6th_subjects where ise_6th_subjects LIKE '%{self.var_ise_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ise_6th_subjects_table.delete(*self.student_ise_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_ise_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ise_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ise_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ise_6th_subject)
                ise_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ise_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ise_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ise_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ise_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ise_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ise_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ise_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ise_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ise_6th_subjects_table.xview)
                newscrolly.config(command=self.student_ise_6th_subjects_table.yview)

                self.student_ise_6th_subjects_table.heading('semister',text='Semister')
                self.student_ise_6th_subjects_table.heading('branch',text='Branch')
                self.student_ise_6th_subjects_table.heading('ise_6th_subjects',text='Subjects')

            
                self.student_ise_6th_subjects_table.column('semister',width=100)
                self.student_ise_6th_subjects_table.column('branch',width=200)
                self.student_ise_6th_subjects_table.column('ise_6th_subjects',width=200)

                self.student_ise_6th_subjects_table['show']='headings'

                self.student_ise_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ise_6th_subjects()
                self.student_ise_6th_subjects_table.bind('<ButtonRelease-1>',get_ise_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                def add_ise_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ise_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ise_7th_subjects (semister,branch,ise_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ise_7th_subject.get()
                        ))
                        con.commit()
                        fetch_ise_7th_subjects()
                        con.close()
                def fetch_ise_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ise_7th_subjects')
                        rows=cur.fetchall()
                        self.student_ise_7th_subjects_table.delete(*self.student_ise_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_ise_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ise_7th_data(ev):
                    read=self.student_ise_7th_subjects_table.focus()
                    content=self.student_ise_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ise_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ise_7th_data():
                    fetch_ise_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ise_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ise_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ise_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ise_7th_subjects_table.focus()
                                        content=self.student_ise_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ise_7th_subjects set ise_7th_subjects=%s where cid=%s',(
                                        self.var_ise_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ise_7th_subjects()
                                    clear_ise_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ise_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ise_7th_subjects where ise_7th_subjects=%s ',(self.var_ise_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ise_7th_data()
                                    fetch_ise_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ise_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ise_7th_subjects where ise_7th_subjects LIKE '%{self.var_ise_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ise_7th_subjects_table.delete(*self.student_ise_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_ise_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ise_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ise_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ise_7th_subject)
                ise_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ise_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ise_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ise_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ise_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ise_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ise_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ise_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ise_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ise_7th_subjects_table.xview)
                newscrolly.config(command=self.student_ise_7th_subjects_table.yview)

                self.student_ise_7th_subjects_table.heading('semister',text='Semister')
                self.student_ise_7th_subjects_table.heading('branch',text='Branch')
                self.student_ise_7th_subjects_table.heading('ise_7th_subjects',text='Subjects')

            
                self.student_ise_7th_subjects_table.column('semister',width=100)
                self.student_ise_7th_subjects_table.column('branch',width=200)
                self.student_ise_7th_subjects_table.column('ise_7th_subjects',width=200)

                self.student_ise_7th_subjects_table['show']='headings'

                self.student_ise_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ise_7th_subjects()
                self.student_ise_7th_subjects_table.bind('<ButtonRelease-1>',get_ise_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                def add_ise_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_ise_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_ise_8th_subjects (semister,branch,ise_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_ise_8th_subject.get()
                        ))
                        con.commit()
                        fetch_ise_8th_subjects()
                        con.close()
                def fetch_ise_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_ise_8th_subjects')
                        rows=cur.fetchall()
                        self.student_ise_8th_subjects_table.delete(*self.student_ise_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_ise_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_ise_8th_data(ev):
                    read=self.student_ise_8th_subjects_table.focus()
                    content=self.student_ise_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_ise_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_ise_8th_data():
                    fetch_ise_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_ise_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_ise_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_ise_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_ise_8th_subjects_table.focus()
                                        content=self.student_ise_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_ise_8th_subjects set ise_8th_subjects=%s where cid=%s',(
                                        self.var_ise_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_ise_8th_subjects()
                                    clear_ise_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_ise_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_ise_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_ise_8th_subjects where ise_8th_subjects=%s ',(self.var_ise_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_ise_8th_data()
                                    fetch_ise_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def ise_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_ise_8th_subjects where ise_8th_subjects LIKE '%{self.var_ise_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_ise_8th_subjects_table.delete(*self.student_ise_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_ise_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                ise_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                ise_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_ise_8th_subject)
                ise_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_ise_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=ise_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_ise_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_ise_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_ise_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_ise_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_ise_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','ise_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_ise_8th_subjects_table.xview)
                newscrolly.config(command=self.student_ise_8th_subjects_table.yview)

              
                self.student_ise_8th_subjects_table.heading('semister',text='Semister')
                self.student_ise_8th_subjects_table.heading('branch',text='Branch')
                self.student_ise_8th_subjects_table.heading('ise_8th_subjects',text='Subjects')

             
                self.student_ise_8th_subjects_table.column('semister',width=100)
                self.student_ise_8th_subjects_table.column('branch',width=200)
                self.student_ise_8th_subjects_table.column('ise_8th_subjects',width=200)

                self.student_ise_8th_subjects_table['show']='headings'

                self.student_ise_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_ise_8th_subjects()
                self.student_ise_8th_subjects_table.bind('<ButtonRelease-1>',get_ise_8th_data)
        ####################################################################### 

       
            
        ################################################################## computer science
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                def add_cs_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_cs_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_cs_3rd_subjects (semister,branch,cs_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_cs_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_cs_3rd_subjects()
                        con.close()
                def fetch_cs_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_cs_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_cs_3rd_subjects_table.delete(*self.student_cs_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_cs_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_cs_3rd_data(ev):
                    read=self.student_cs_3rd_subjects_table.focus()
                    content=self.student_cs_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_cs_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_cs_3rd_data():
                    fetch_cs_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_cs_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_cs_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_cs_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_cs_3rd_subjects_table.focus()
                                        content=self.student_cs_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_cs_3rd_subjects set cs_3rd_subjects=%s where cid=%s',(
                                        self.var_cs_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_cs_3rd_subjects()
                                    clear_cs_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_cs_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_cs_3rd_subjects where cs_3rd_subjects=%s ',(self.var_cs_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_cs_3rd_data()
                                    fetch_cs_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def cs_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_cs_3rd_subjects where cs_3rd_subjects LIKE '%{self.var_cs_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_cs_3rd_subjects_table.delete(*self.student_cs_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_cs_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                cs_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                cs_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_cs_3rd_subject)
                cs_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_cs_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=cs_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_cs_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_cs_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_cs_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_cs_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_cs_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','cs_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_cs_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_cs_3rd_subjects_table.yview)

              
                self.student_cs_3rd_subjects_table.heading('semister',text='Semister')
                self.student_cs_3rd_subjects_table.heading('branch',text='Branch')
                self.student_cs_3rd_subjects_table.heading('cs_3rd_subjects',text='Subjects')

                self.student_cs_3rd_subjects_table.column('semister',width=100)
                self.student_cs_3rd_subjects_table.column('branch',width=200)
                self.student_cs_3rd_subjects_table.column('cs_3rd_subjects',width=200)

                self.student_cs_3rd_subjects_table['show']='headings'

                self.student_cs_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_cs_3rd_subjects()
                self.student_cs_3rd_subjects_table.bind('<ButtonRelease-1>',get_cs_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                def add_cs_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_cs_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_cs_4th_subjects (semister,branch,cs_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_cs_4th_subject.get()
                        ))
                        con.commit()
                        fetch_cs_4th_subjects()
                        con.close()
                def fetch_cs_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_cs_4th_subjects')
                        rows=cur.fetchall()
                        self.student_cs_4th_subjects_table.delete(*self.student_cs_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_cs_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_cs_4th_data(ev):
                    read=self.student_cs_4th_subjects_table.focus()
                    content=self.student_cs_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_cs_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_cs_4th_data():
                    fetch_cs_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_cs_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_cs_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_cs_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_cs_4th_subjects_table.focus()
                                        content=self.student_cs_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_cs_4th_subjects set cs_4th_subjects=%s where cid=%s',(
                                        self.var_cs_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_cs_4th_subjects()
                                    clear_cs_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_cs_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_cs_4th_subjects where cs_4th_subjects=%s ',(self.var_cs_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_cs_4th_data()
                                    fetch_cs_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def cs_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_cs_4th_subjects where cs_4th_subjects LIKE '%{self.var_cs_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_cs_4th_subjects_table.delete(*self.student_cs_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_cs_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                cs_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                cs_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_cs_4th_subject)
                cs_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_cs_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=cs_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_cs_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_cs_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_cs_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_cs_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_cs_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','cs_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_cs_4th_subjects_table.xview)
                newscrolly.config(command=self.student_cs_4th_subjects_table.yview)

                
                self.student_cs_4th_subjects_table.heading('semister',text='Semister')
                self.student_cs_4th_subjects_table.heading('branch',text='Branch')
                self.student_cs_4th_subjects_table.heading('cs_4th_subjects',text='Subjects')

                self.student_cs_4th_subjects_table.column('semister',width=100)
                self.student_cs_4th_subjects_table.column('branch',width=200)
                self.student_cs_4th_subjects_table.column('cs_4th_subjects',width=200)

                self.student_cs_4th_subjects_table['show']='headings'

                self.student_cs_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_cs_4th_subjects()
                self.student_cs_4th_subjects_table.bind('<ButtonRelease-1>',get_cs_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                def add_cs_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_cs_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_cs_5th_subjects (semister,branch,cs_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_cs_5th_subject.get()
                        ))
                        con.commit()
                        fetch_cs_5th_subjects()
                        con.close()
                def fetch_cs_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_cs_5th_subjects')
                        rows=cur.fetchall()
                        self.student_cs_5th_subjects_table.delete(*self.student_cs_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_cs_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_cs_5th_data(ev):
                    read=self.student_cs_5th_subjects_table.focus()
                    content=self.student_cs_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_cs_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_cs_5th_data():
                    fetch_cs_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_cs_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_cs_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_cs_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_cs_5th_subjects_table.focus()
                                        content=self.student_cs_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_cs_5th_subjects set cs_5th_subjects=%s where cid=%s',(
                                        self.var_cs_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_cs_5th_subjects()
                                    clear_cs_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_cs_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_cs_5th_subjects where cs_5th_subjects=%s ',(self.var_cs_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_cs_5th_data()
                                    fetch_cs_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def cs_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_cs_5th_subjects where cs_5th_subjects LIKE '%{self.var_cs_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_cs_5th_subjects_table.delete(*self.student_cs_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_cs_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                cs_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                cs_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_cs_5th_subject)
                cs_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_cs_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=cs_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_cs_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_cs_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_cs_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_cs_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_cs_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','cs_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_cs_5th_subjects_table.xview)
                newscrolly.config(command=self.student_cs_5th_subjects_table.yview)

                self.student_cs_5th_subjects_table.heading('semister',text='Semister')
                self.student_cs_5th_subjects_table.heading('branch',text='Branch')
                self.student_cs_5th_subjects_table.heading('cs_5th_subjects',text='Subjects')

                self.student_cs_5th_subjects_table.column('semister',width=100)
                self.student_cs_5th_subjects_table.column('branch',width=200)
                self.student_cs_5th_subjects_table.column('cs_5th_subjects',width=200)

                self.student_cs_5th_subjects_table['show']='headings'

                self.student_cs_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_cs_5th_subjects()
                self.student_cs_5th_subjects_table.bind('<ButtonRelease-1>',get_cs_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                def add_cs_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_cs_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_cs_6th_subjects (semister,branch,cs_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_cs_6th_subject.get()
                        ))
                        con.commit()
                        fetch_cs_6th_subjects()
                        con.close()
                def fetch_cs_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_cs_6th_subjects')
                        rows=cur.fetchall()
                        self.student_cs_6th_subjects_table.delete(*self.student_cs_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_cs_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_cs_6th_data(ev):
                    read=self.student_cs_6th_subjects_table.focus()
                    content=self.student_cs_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_cs_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_cs_6th_data():
                    fetch_cs_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_cs_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_cs_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_cs_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_cs_6th_subjects_table.focus()
                                        content=self.student_cs_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_cs_6th_subjects set cs_6th_subjects=%s where cid=%s',(
                                        self.var_cs_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_cs_6th_subjects()
                                    clear_cs_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_cs_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_cs_6th_subjects where cs_6th_subjects=%s ',(self.var_cs_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_cs_6th_data()
                                    fetch_cs_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def cs_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_cs_6th_subjects where cs_6th_subjects LIKE '%{self.var_cs_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_cs_6th_subjects_table.delete(*self.student_cs_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_cs_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                cs_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                cs_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_cs_6th_subject)
                cs_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_cs_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=cs_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_cs_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_cs_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_cs_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_cs_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_cs_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','cs_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_cs_6th_subjects_table.xview)
                newscrolly.config(command=self.student_cs_6th_subjects_table.yview)

                self.student_cs_6th_subjects_table.heading('semister',text='Semister')
                self.student_cs_6th_subjects_table.heading('branch',text='Branch')
                self.student_cs_6th_subjects_table.heading('cs_6th_subjects',text='Subjects')

                self.student_cs_6th_subjects_table.column('semister',width=100)
                self.student_cs_6th_subjects_table.column('branch',width=200)
                self.student_cs_6th_subjects_table.column('cs_6th_subjects',width=200)

                self.student_cs_6th_subjects_table['show']='headings'

                self.student_cs_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_cs_6th_subjects()
                self.student_cs_6th_subjects_table.bind('<ButtonRelease-1>',get_cs_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                def add_cs_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_cs_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_cs_7th_subjects (semister,branch,cs_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_cs_7th_subject.get()
                        ))
                        con.commit()
                        fetch_cs_7th_subjects()
                        con.close()
                def fetch_cs_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_cs_7th_subjects')
                        rows=cur.fetchall()
                        self.student_cs_7th_subjects_table.delete(*self.student_cs_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_cs_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_cs_7th_data(ev):
                    read=self.student_cs_7th_subjects_table.focus()
                    content=self.student_cs_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_cs_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_cs_7th_data():
                    fetch_cs_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_cs_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_cs_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_cs_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_cs_7th_subjects_table.focus()
                                        content=self.student_cs_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_cs_7th_subjects set cs_7th_subjects=%s where cid=%s',(
                                        self.var_cs_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_cs_7th_subjects()
                                    clear_cs_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_cs_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_cs_7th_subjects where cs_7th_subjects=%s ',(self.var_cs_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_cs_7th_data()
                                    fetch_cs_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def cs_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_cs_7th_subjects where cs_7th_subjects LIKE '%{self.var_cs_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_cs_7th_subjects_table.delete(*self.student_cs_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_cs_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                cs_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                cs_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_cs_7th_subject)
                cs_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_cs_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=cs_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_cs_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_cs_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_cs_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_cs_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_cs_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','cs_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_cs_7th_subjects_table.xview)
                newscrolly.config(command=self.student_cs_7th_subjects_table.yview)

         
                self.student_cs_7th_subjects_table.heading('semister',text='Semister')
                self.student_cs_7th_subjects_table.heading('branch',text='Branch')
                self.student_cs_7th_subjects_table.heading('cs_7th_subjects',text='Subjects')

    
                self.student_cs_7th_subjects_table.column('semister',width=100)
                self.student_cs_7th_subjects_table.column('branch',width=200)
                self.student_cs_7th_subjects_table.column('cs_7th_subjects',width=200)

                self.student_cs_7th_subjects_table['show']='headings'

                self.student_cs_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_cs_7th_subjects()
                self.student_cs_7th_subjects_table.bind('<ButtonRelease-1>',get_cs_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                def add_cs_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_cs_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_cs_8th_subjects (semister,branch,cs_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_cs_8th_subject.get()
                        ))
                        con.commit()
                        fetch_cs_8th_subjects()
                        con.close()
                def fetch_cs_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_cs_8th_subjects')
                        rows=cur.fetchall()
                        self.student_cs_8th_subjects_table.delete(*self.student_cs_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_cs_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_cs_8th_data(ev):
                    read=self.student_cs_8th_subjects_table.focus()
                    content=self.student_cs_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_cs_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_cs_8th_data():
                    fetch_cs_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_cs_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_cs_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_cs_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_cs_8th_subjects_table.focus()
                                        content=self.student_cs_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_cs_8th_subjects set cs_8th_subjects=%s where cid=%s',(
                                        self.var_cs_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_cs_8th_subjects()
                                    clear_cs_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_cs_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_cs_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_cs_8th_subjects where cs_8th_subjects=%s ',(self.var_cs_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_cs_8th_data()
                                    fetch_cs_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def cs_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_cs_8th_subjects where cs_8th_subjects LIKE '%{self.var_cs_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_cs_8th_subjects_table.delete(*self.student_cs_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_cs_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                cs_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                cs_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_cs_8th_subject)
                cs_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_cs_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=cs_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_cs_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_cs_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_cs_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_cs_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_cs_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','cs_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_cs_8th_subjects_table.xview)
                newscrolly.config(command=self.student_cs_8th_subjects_table.yview)

                
                self.student_cs_8th_subjects_table.heading('semister',text='Semister')
                self.student_cs_8th_subjects_table.heading('branch',text='Branch')
                self.student_cs_8th_subjects_table.heading('cs_8th_subjects',text='Subjects')

                self.student_cs_8th_subjects_table.column('semister',width=100)
                self.student_cs_8th_subjects_table.column('branch',width=200)
                self.student_cs_8th_subjects_table.column('cs_8th_subjects',width=200)

                self.student_cs_8th_subjects_table['show']='headings'

                self.student_cs_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_cs_8th_subjects()
                self.student_cs_8th_subjects_table.bind('<ButtonRelease-1>',get_cs_8th_data)
        #######################################################################  mechnaical

        
        
        ##################################################################  electrical and elctronic
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                def add_eee_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_eee_3rd_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_eee_3rd_subjects (semister,branch,eee_3rd_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_eee_3rd_subject.get()
                        ))
                        con.commit()
                        fetch_eee_3rd_subjects()
                        con.close()
                def fetch_eee_3rd_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_eee_3rd_subjects')
                        rows=cur.fetchall()
                        self.student_eee_3rd_subjects_table.delete(*self.student_eee_3rd_subjects_table.get_children())

                        for row in rows:
                            self.student_eee_3rd_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_eee_3rd_data(ev):
                    read=self.student_eee_3rd_subjects_table.focus()
                    content=self.student_eee_3rd_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_eee_3rd_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_eee_3rd_data():
                    fetch_eee_3rd_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_eee_3rd_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_eee_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_eee_3rd_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_eee_3rd_subjects_table.focus()
                                        content=self.student_eee_3rd_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_eee_3rd_subjects set eee_3rd_subjects=%s where cid=%s',(
                                        self.var_eee_3rd_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_eee_3rd_subjects()
                                    clear_eee_3rd_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_eee_3rd_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_3rd_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_eee_3rd_subjects where eee_3rd_subjects=%s ',(self.var_eee_3rd_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_eee_3rd_data()
                                    fetch_eee_3rd_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def eee_3rd_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_3rd_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_eee_3rd_subjects where eee_3rd_subjects LIKE '%{self.var_eee_3rd_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_eee_3rd_subjects_table.delete(*self.student_eee_3rd_subjects_table.get_children())
                            for row in rows:
                                self.student_eee_3rd_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                eee_3rdmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                eee_3rdmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_eee_3rd_subject)
                eee_3rdmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_eee_3rd_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=eee_3rd_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_eee_3rd_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_eee_3rd_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_eee_3rd_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_eee_3rd_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_eee_3rd_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','eee_3rd_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_eee_3rd_subjects_table.xview)
                newscrolly.config(command=self.student_eee_3rd_subjects_table.yview)

                
                self.student_eee_3rd_subjects_table.heading('semister',text='Semister')
                self.student_eee_3rd_subjects_table.heading('branch',text='Branch')
                self.student_eee_3rd_subjects_table.heading('eee_3rd_subjects',text='Subjects')

             
                self.student_eee_3rd_subjects_table.column('semister',width=100)
                self.student_eee_3rd_subjects_table.column('branch',width=200)
                self.student_eee_3rd_subjects_table.column('eee_3rd_subjects',width=200)

                self.student_eee_3rd_subjects_table['show']='headings'

                self.student_eee_3rd_subjects_table.pack(fill=BOTH,expand=1)
                fetch_eee_3rd_subjects()
                self.student_eee_3rd_subjects_table.bind('<ButtonRelease-1>',get_eee_3rd_data)

        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                def add_eee_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_eee_4th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_eee_4th_subjects (semister,branch,eee_4th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_eee_4th_subject.get()
                        ))
                        con.commit()
                        fetch_eee_4th_subjects()
                        con.close()
                def fetch_eee_4th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_eee_4th_subjects')
                        rows=cur.fetchall()
                        self.student_eee_4th_subjects_table.delete(*self.student_eee_4th_subjects_table.get_children())

                        for row in rows:
                            self.student_eee_4th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_eee_4th_data(ev):
                    read=self.student_eee_4th_subjects_table.focus()
                    content=self.student_eee_4th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_eee_4th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_eee_4th_data():
                    fetch_eee_4th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_eee_4th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_eee_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_eee_4th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_eee_4th_subjects_table.focus()
                                        content=self.student_eee_4th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_eee_4th_subjects set eee_4th_subjects=%s where cid=%s',(
                                        self.var_eee_4th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_eee_4th_subjects()
                                    clear_eee_4th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_eee_4th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_4th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_eee_4th_subjects where eee_4th_subjects=%s ',(self.var_eee_4th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_eee_4th_data()
                                    fetch_eee_4th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def eee_4th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_4th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_eee_4th_subjects where eee_4th_subjects LIKE '%{self.var_eee_4th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_eee_4th_subjects_table.delete(*self.student_eee_4th_subjects_table.get_children())
                            for row in rows:
                                self.student_eee_4th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                eee_4thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                eee_4thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_eee_4th_subject)
                eee_4thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_eee_4th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=eee_4th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_eee_4th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_eee_4th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_eee_4th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_eee_4th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_eee_4th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','eee_4th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_eee_4th_subjects_table.xview)
                newscrolly.config(command=self.student_eee_4th_subjects_table.yview)

               
                self.student_eee_4th_subjects_table.heading('semister',text='Semister')
                self.student_eee_4th_subjects_table.heading('branch',text='Branch')
                self.student_eee_4th_subjects_table.heading('eee_4th_subjects',text='Subjects')

               
                self.student_eee_4th_subjects_table.column('semister',width=100)
                self.student_eee_4th_subjects_table.column('branch',width=200)
                self.student_eee_4th_subjects_table.column('eee_4th_subjects',width=200)

                self.student_eee_4th_subjects_table['show']='headings'

                self.student_eee_4th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_eee_4th_subjects()
                self.student_eee_4th_subjects_table.bind('<ButtonRelease-1>',get_eee_4th_data)


        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                def add_eee_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_eee_5th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_eee_5th_subjects (semister,branch,eee_5th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_eee_5th_subject.get()
                        ))
                        con.commit()
                        fetch_eee_5th_subjects()
                        con.close()
                def fetch_eee_5th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_eee_5th_subjects')
                        rows=cur.fetchall()
                        self.student_eee_5th_subjects_table.delete(*self.student_eee_5th_subjects_table.get_children())

                        for row in rows:
                            self.student_eee_5th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_eee_5th_data(ev):
                    read=self.student_eee_5th_subjects_table.focus()
                    content=self.student_eee_5th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_eee_5th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_eee_5th_data():
                    fetch_eee_5th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_eee_5th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_eee_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_eee_5th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_eee_5th_subjects_table.focus()
                                        content=self.student_eee_5th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_eee_5th_subjects set eee_5th_subjects=%s where cid=%s',(
                                        self.var_eee_5th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_eee_5th_subjects()
                                    clear_eee_5th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_eee_5th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_5th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_eee_5th_subjects where eee_5th_subjects=%s ',(self.var_eee_5th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_eee_5th_data()
                                    fetch_eee_5th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def eee_5th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_5th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_eee_5th_subjects where eee_5th_subjects LIKE '%{self.var_eee_5th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_eee_5th_subjects_table.delete(*self.student_eee_5th_subjects_table.get_children())
                            for row in rows:
                                self.student_eee_5th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                eee_5thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                eee_5thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_eee_5th_subject)
                eee_5thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_eee_5th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=eee_5th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_eee_5th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_eee_5th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_eee_5th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_eee_5th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_eee_5th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','eee_5th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_eee_5th_subjects_table.xview)
                newscrolly.config(command=self.student_eee_5th_subjects_table.yview)

               
                self.student_eee_5th_subjects_table.heading('semister',text='Semister')
                self.student_eee_5th_subjects_table.heading('branch',text='Branch')
                self.student_eee_5th_subjects_table.heading('eee_5th_subjects',text='Subjects')

                self.student_eee_5th_subjects_table.column('semister',width=100)
                self.student_eee_5th_subjects_table.column('branch',width=200)
                self.student_eee_5th_subjects_table.column('eee_5th_subjects',width=200)

                self.student_eee_5th_subjects_table['show']='headings'

                self.student_eee_5th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_eee_5th_subjects()
                self.student_eee_5th_subjects_table.bind('<ButtonRelease-1>',get_eee_5th_data)
        
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                def add_eee_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_eee_6th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_eee_6th_subjects (semister,branch,eee_6th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_eee_6th_subject.get()
                        ))
                        con.commit()
                        fetch_eee_6th_subjects()
                        con.close()
                def fetch_eee_6th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_eee_6th_subjects')
                        rows=cur.fetchall()
                        self.student_eee_6th_subjects_table.delete(*self.student_eee_6th_subjects_table.get_children())

                        for row in rows:
                            self.student_eee_6th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_eee_6th_data(ev):
                    read=self.student_eee_6th_subjects_table.focus()
                    content=self.student_eee_6th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_eee_6th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_eee_6th_data():
                    fetch_eee_6th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_eee_6th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_eee_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_eee_6th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_eee_6th_subjects_table.focus()
                                        content=self.student_eee_6th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_eee_6th_subjects set eee_6th_subjects=%s where cid=%s',(
                                        self.var_eee_6th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_eee_6th_subjects()
                                    clear_eee_6th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_eee_6th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_6th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_eee_6th_subjects where eee_6th_subjects=%s ',(self.var_eee_6th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_eee_6th_data()
                                    fetch_eee_6th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def eee_6th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_6th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_eee_6th_subjects where eee_6th_subjects LIKE '%{self.var_eee_6th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_eee_6th_subjects_table.delete(*self.student_eee_6th_subjects_table.get_children())
                            for row in rows:
                                self.student_eee_6th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                eee_6thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                eee_6thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_eee_6th_subject)
                eee_6thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_eee_6th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=eee_6th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_eee_6th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_eee_6th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_eee_6th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_eee_6th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_eee_6th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','eee_6th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_eee_6th_subjects_table.xview)
                newscrolly.config(command=self.student_eee_6th_subjects_table.yview)

            
                self.student_eee_6th_subjects_table.heading('semister',text='Semister')
                self.student_eee_6th_subjects_table.heading('branch',text='Branch')
                self.student_eee_6th_subjects_table.heading('eee_6th_subjects',text='Subjects')

           
                self.student_eee_6th_subjects_table.column('semister',width=100)
                self.student_eee_6th_subjects_table.column('branch',width=200)
                self.student_eee_6th_subjects_table.column('eee_6th_subjects',width=200)

                self.student_eee_6th_subjects_table['show']='headings'

                self.student_eee_6th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_eee_6th_subjects()
                self.student_eee_6th_subjects_table.bind('<ButtonRelease-1>',get_eee_6th_data)
        
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                def add_eee_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_eee_7th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_eee_7th_subjects (semister,branch,eee_7th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_eee_7th_subject.get()
                        ))
                        con.commit()
                        fetch_eee_7th_subjects()
                        con.close()
                def fetch_eee_7th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_eee_7th_subjects')
                        rows=cur.fetchall()
                        self.student_eee_7th_subjects_table.delete(*self.student_eee_7th_subjects_table.get_children())

                        for row in rows:
                            self.student_eee_7th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_eee_7th_data(ev):
                    read=self.student_eee_7th_subjects_table.focus()
                    content=self.student_eee_7th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_eee_7th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_eee_7th_data():
                    fetch_eee_7th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_eee_7th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_eee_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_eee_7th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_eee_7th_subjects_table.focus()
                                        content=self.student_eee_7th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_eee_7th_subjects set eee_7th_subjects=%s where cid=%s',(
                                        self.var_eee_7th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_eee_7th_subjects()
                                    clear_eee_7th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_eee_7th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_7th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_eee_7th_subjects where eee_7th_subjects=%s ',(self.var_eee_7th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_eee_7th_data()
                                    fetch_eee_7th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def eee_7th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_7th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_eee_7th_subjects where eee_7th_subjects LIKE '%{self.var_eee_7th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_eee_7th_subjects_table.delete(*self.student_eee_7th_subjects_table.get_children())
                            for row in rows:
                                self.student_eee_7th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                eee_7thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                eee_7thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_eee_7th_subject)
                eee_7thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_eee_7th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=eee_7th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_eee_7th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_eee_7th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_eee_7th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_eee_7th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_eee_7th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','eee_7th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_eee_7th_subjects_table.xview)
                newscrolly.config(command=self.student_eee_7th_subjects_table.yview)

                self.student_eee_7th_subjects_table.heading('semister',text='Semister')
                self.student_eee_7th_subjects_table.heading('branch',text='Branch')
                self.student_eee_7th_subjects_table.heading('eee_7th_subjects',text='Subjects')

              
                self.student_eee_7th_subjects_table.column('semister',width=100)
                self.student_eee_7th_subjects_table.column('branch',width=200)
                self.student_eee_7th_subjects_table.column('eee_7th_subjects',width=200)

                self.student_eee_7th_subjects_table['show']='headings'

                self.student_eee_7th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_eee_7th_subjects()
                self.student_eee_7th_subjects_table.bind('<ButtonRelease-1>',get_eee_7th_data)
        
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                def add_eee_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.var_eee_8th_subject.get()=='':
                        messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                    else:
                        cur.execute('insert into all_eee_8th_subjects (semister,branch,eee_8th_subjects) values(%s,%s,%s)',(
                            self.var_sem_select.get(),
                            self.var_branch_select.get(),
                            self.var_eee_8th_subject.get()
                        ))
                        con.commit()
                        fetch_eee_8th_subjects()
                        con.close()
                def fetch_eee_8th_subjects():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from all_eee_8th_subjects')
                        rows=cur.fetchall()
                        self.student_eee_8th_subjects_table.delete(*self.student_eee_8th_subjects_table.get_children())

                        for row in rows:
                            self.student_eee_8th_subjects_table.insert('',END,values=row)
                    except Exception as sr:
                        messagebox.showerror('Error',f'Error due to {str(sr)}')

                def get_eee_8th_data(ev):
                    read=self.student_eee_8th_subjects_table.focus()
                    content=self.student_eee_8th_subjects_table.item(read)
                    row=content['values']

                    self.var_sem_select.set(row[0])
                    self.var_branch_select.set(row[1])
                    self.var_eee_8th_subject.set(row[2])
                    messagebox.showinfo('Info','The data get successfuly...',parent=menu_frame1)
                def clear_eee_8th_data():
                    fetch_eee_8th_subjects()
                    
                    self.var_sem_select.set('')
                    self.var_branch_select.set('')
                    self.var_eee_8th_subject.set('')
                    messagebox.showinfo('Info','The data clear successfly..',parent=menu_frame1)

                def update_eee_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:

                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    cur.execute('select * from all_eee_8th_subjects where semister=%s',(self.var_sem_select.get(),))
                                    row=cur.fetchall()
                                    if row==None:
                                        messagebox.showerror('Error','Select the semister and branch from the subject table',parent=menu_frame1)
                                    else:
                                        r=self.student_eee_8th_subjects_table.focus()
                                        content=self.student_eee_8th_subjects_table.item(r)
                                        row=content["values"]
                                        cur.execute('update all_eee_8th_subjects set eee_8th_subjects=%s where cid=%s',(
                                        self.var_eee_8th_subject.get(),
                                        row[0]
                                        ))
                                    con.commit()
                                    fetch_eee_8th_subjects()
                                    clear_eee_8th_data()
                                    messagebox.showinfo('Info','The data updatede successfuly...',parent=menu_frame1)
                                    
                                    con.close()
                    except Exception as ex:
                        messagebox.showerror('Error',f' The error due to {str(ex)}',parent=menu_frame1)
                def delete_eee_8th_data():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_sem_select.get()=='':
                            messagebox.showerror('Error','The student semister must be rquired',parent=menu_frame1)
                        else:
                            if self.var_branch_select.get()=="":
                                messagebox.showerror('Error','The student branch must be required',parent=menu_frame1)
                            else:
                                if self.var_eee_8th_subject.get()=="":
                                    messagebox.showerror('Error','The subjects must be rquired',parent=menu_frame1)
                                else:
                                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                                    if option1==True:
                                        cur.execute('DELETE  from all_eee_8th_subjects where eee_8th_subjects=%s ',(self.var_eee_8th_subject.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The data deleted successfulty',parent=menu_frame1)
                                    clear_eee_8th_data()
                                    fetch_eee_8th_subjects()
                                    con.close()
                        
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=menu_frame1)
                def eee_8th_subjects_serach():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_8th_subject_serach.get()=='':
                            messagebox.showerror('Error','The subject must be required',parent=menu_frame1)
                        else:
                            cur.execute(f"select * from all_eee_8th_subjects where eee_8th_subjects LIKE '%{self.var_eee_8th_subject_serach.get()}%' ")
                            rows=cur.fetchall()
                            self.student_eee_8th_subjects_table.delete(*self.student_eee_8th_subjects_table.get_children())
                            for row in rows:
                                self.student_eee_8th_subjects_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=menu_frame1)


                menu_frame1=LabelFrame(self.root,font=('times now roman',10,'bold'),fg='#262626',bg='white')
                menu_frame1.place(x=10,y=100,width=1035,height=325)
                eee_8thmistry_subjects_label=Label(menu_frame1,text='Enter Subjects',font=('times new roman',13,'bold'),bg='white').place(x=10,y=10)
                eee_8thmistry_subjects_entry=ttk.Entry(menu_frame1,width=40,textvariable=self.var_eee_8th_subject)
                eee_8thmistry_subjects_entry.place(x=130,y=11)

                search_subjects_label=Label(menu_frame1,text='Search Subjects:',font=('times new roman',13,'bold'),bg='white').place(x=400,y=10)
                search_subjects_entry=ttk.Entry(menu_frame1,width=30,textvariable=self.var_eee_8th_subject_serach)
                search_subjects_entry.place(x=530,y=11)
                serach_button=ttk.Button(menu_frame1,width=20,text='Search.',command=eee_8th_subjects_serach)
                serach_button.place(x=730,y=10)

                menu_frame2=LabelFrame(menu_frame1,bg='white')
                menu_frame2.place(x=10,y=50,width=220,height=260)

                
                add_database_button=ttk.Button(menu_frame2,width=30,text='Add Database.',command=add_eee_8th_subjects)
                add_database_button.place(x=10,y=20)

                delete_button=ttk.Button(menu_frame2,width=30,text='delete Data.',command=delete_eee_8th_data)
                delete_button.place(x=10,y=50)

                update_button=ttk.Button(menu_frame2,width=30,text='upadte Data.',command=update_eee_8th_data)
                update_button.place(x=10,y=80)

                clear_button=ttk.Button(menu_frame2,width=30,text='Clear.',command=clear_eee_8th_data)
                clear_button.place(x=10,y=110)


                ########################################################
                self.treeview_frame=Frame(menu_frame1)
                self.treeview_frame.place(x=235,y=50,width=790,height=260)

                #########################################################
                newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
                newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
                self.student_eee_8th_subjects_table=ttk.Treeview(self.treeview_frame,columns=('semister','branch','eee_8th_subjects'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
                
                newscrollx.pack(side=BOTTOM,fill=X)
                newscrolly.pack(side=RIGHT,fill=Y)

                newscrollx.config(command=self.student_eee_8th_subjects_table.xview)
                newscrolly.config(command=self.student_eee_8th_subjects_table.yview)

                self.student_eee_8th_subjects_table.heading('semister',text='Semister')
                self.student_eee_8th_subjects_table.heading('branch',text='Branch')
                self.student_eee_8th_subjects_table.heading('eee_8th_subjects',text='Subjects')

     
                self.student_eee_8th_subjects_table.column('semister',width=100)
                self.student_eee_8th_subjects_table.column('branch',width=200)
                self.student_eee_8th_subjects_table.column('eee_8th_subjects',width=200)

                self.student_eee_8th_subjects_table['show']='headings'

                self.student_eee_8th_subjects_table.pack(fill=BOTH,expand=1)
                fetch_eee_8th_subjects()
                self.student_eee_8th_subjects_table.bind('<ButtonRelease-1>',get_eee_8th_data)
        ####################################################################### 

        
        
if __name__=='__main__':
    root=tk.Tk()
    ob1=AddSubjects(root)
    root.mainloop()