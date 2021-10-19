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

class AddStudentResult():
    def __init__(self,root):
        self.root=root
        self.root.title("Add Student Result")
        self.root.geometry('1055x440+213+145')
        self.root.resizable(False,False)
        self.root.configure(bg='white')
        top_label=tk.Label(self.root,text='Add Student Result',font=('Bahnschrift',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)

        ################################
        self.var_branch_select=StringVar()
        self.var_sem_select=StringVar()
        self.var_che_subjects_code=StringVar()
        self.var_che_subjects=StringVar()
        self.var_scheme_select=StringVar()
        self.var_semister_select=StringVar()
        self.var_scheme_select=StringVar()
        self.var_subjects_marks=StringVar()
        self.var_student_che_usn=StringVar()

        self.var_phy_subjects_code=StringVar()
        self.var_phy_subjects=StringVar()
        self.var_scheme_select=StringVar()
        self.var_semister_select=StringVar()
        self.var_scheme_select=StringVar()
        self.var_phy_subjects_marks=StringVar()
        self.var_student_phy_usn=StringVar()


        self.var_civil_3rd_subjects_code=StringVar()
        self.var_civil_3rd_subjects=StringVar()
        self.var_civil_3rd_subjects_marks=StringVar()
        self.var_student_civil_3rd_usn=StringVar()

        self.var_civil_4th_subjects_code=StringVar()
        self.var_civil_4th_subjects=StringVar()
        self.var_civil_4th_subjects_marks=StringVar()
        self.var_student_civil_4th_usn=StringVar()

        self.var_civil_5th_subjects_code=StringVar()
        self.var_civil_5th_subjects=StringVar()
        self.var_civil_5th_subjects_marks=StringVar()
        self.var_student_civil_5th_usn=StringVar()

        self.var_civil_6th_subjects_code=StringVar()
        self.var_civil_6th_subjects=StringVar()
        self.var_civil_6th_subjects_marks=StringVar()
        self.var_student_civil_6th_usn=StringVar()

        self.var_civil_7th_subjects_code=StringVar()
        self.var_civil_7th_subjects=StringVar()
        self.var_civil_7th_subjects_marks=StringVar()
        self.var_student_civil_7th_usn=StringVar()

        self.var_civil_8th_subjects_code=StringVar()
        self.var_civil_8th_subjects=StringVar()
        self.var_civil_8th_subjects_marks=StringVar()
        self.var_student_civil_8th_usn=StringVar()

        ########################################################
        self.var_mech_3rd_subjects_code=StringVar()
        self.var_mech_3rd_subjects=StringVar()
        self.var_mech_3rd_subjects_marks=StringVar()
        self.var_student_mech_3rd_usn=StringVar()

        self.var_mech_4th_subjects_code=StringVar()
        self.var_mech_4th_subjects=StringVar()
        self.var_mech_4th_subjects_marks=StringVar()
        self.var_student_mech_4th_usn=StringVar()

        self.var_mech_5th_subjects_code=StringVar()
        self.var_mech_5th_subjects=StringVar()
        self.var_mech_5th_subjects_marks=StringVar()
        self.var_student_mech_5th_usn=StringVar()

        self.var_mech_6th_subjects_code=StringVar()
        self.var_mech_6th_subjects=StringVar()
        self.var_mech_6th_subjects_marks=StringVar()
        self.var_student_mech_6th_usn=StringVar()

        self.var_mech_7th_subjects_code=StringVar()
        self.var_mech_7th_subjects=StringVar()
        self.var_mech_7th_subjects_marks=StringVar()
        self.var_student_mech_7th_usn=StringVar()

        self.var_mech_8th_subjects_code=StringVar()
        self.var_mech_8th_subjects=StringVar()
        self.var_mech_8th_subjects_marks=StringVar()
        self.var_student_mech_8th_usn=StringVar()
        ###############################################
        self.var_ece_3rd_subjects_code=StringVar()
        self.var_ece_3rd_subjects=StringVar()
        self.var_ece_3rd_subjects_marks=StringVar()
        self.var_student_ece_3rd_usn=StringVar()

        self.var_ece_4th_subjects_code=StringVar()
        self.var_ece_4th_subjects=StringVar()
        self.var_ece_4th_subjects_marks=StringVar()
        self.var_student_ece_4th_usn=StringVar()

        self.var_ece_5th_subjects_code=StringVar()
        self.var_ece_5th_subjects=StringVar()
        self.var_ece_5th_subjects_marks=StringVar()
        self.var_student_ece_5th_usn=StringVar()

        self.var_ece_6th_subjects_code=StringVar()
        self.var_ece_6th_subjects=StringVar()
        self.var_ece_6th_subjects_marks=StringVar()
        self.var_student_ece_6th_usn=StringVar()

        self.var_ece_7th_subjects_code=StringVar()
        self.var_ece_7th_subjects=StringVar()
        self.var_ece_7th_subjects_marks=StringVar()
        self.var_student_ece_7th_usn=StringVar()

        self.var_ece_8th_subjects_code=StringVar()
        self.var_ece_8th_subjects=StringVar()
        self.var_ece_8th_subjects_marks=StringVar()
        self.var_student_ece_8th_usn=StringVar()
        ###########################################3
        self.var_eee_3rd_subjects_code=StringVar()
        self.var_eee_3rd_subjects=StringVar()
        self.var_eee_3rd_subjects_marks=StringVar()
        self.var_student_eee_3rd_usn=StringVar()

        self.var_eee_4th_subjects_code=StringVar()
        self.var_eee_4th_subjects=StringVar()
        self.var_eee_4th_subjects_marks=StringVar()
        self.var_student_eee_4th_usn=StringVar()

        self.var_eee_5th_subjects_code=StringVar()
        self.var_eee_5th_subjects=StringVar()
        self.var_eee_5th_subjects_marks=StringVar()
        self.var_student_eee_5th_usn=StringVar()

        self.var_eee_6th_subjects_code=StringVar()
        self.var_eee_6th_subjects=StringVar()
        self.var_eee_6th_subjects_marks=StringVar()
        self.var_student_eee_6th_usn=StringVar()

        self.var_eee_7th_subjects_code=StringVar()
        self.var_eee_7th_subjects=StringVar()
        self.var_eee_7th_subjects_marks=StringVar()
        self.var_student_eee_7th_usn=StringVar()

        self.var_eee_8th_subjects_code=StringVar()
        self.var_eee_8th_subjects=StringVar()
        self.var_eee_8th_subjects_marks=StringVar()
        self.var_student_eee_8th_usn=StringVar()
        #########################################################
        self.var_cs_3rd_subjects_code=StringVar()
        self.var_cs_3rd_subjects=StringVar()
        self.var_cs_3rd_subjects_marks=StringVar()
        self.var_student_cs_3rd_usn=StringVar()

        self.var_cs_4th_subjects_code=StringVar()
        self.var_cs_4th_subjects=StringVar()
        self.var_cs_4th_subjects_marks=StringVar()
        self.var_student_cs_4th_usn=StringVar()

        self.var_cs_5th_subjects_code=StringVar()
        self.var_cs_5th_subjects=StringVar()
        self.var_cs_5th_subjects_marks=StringVar()
        self.var_student_cs_5th_usn=StringVar()

        self.var_cs_6th_subjects_code=StringVar()
        self.var_cs_6th_subjects=StringVar()
        self.var_cs_6th_subjects_marks=StringVar()
        self.var_student_cs_6th_usn=StringVar()

        self.var_cs_7th_subjects_code=StringVar()
        self.var_cs_7th_subjects=StringVar()
        self.var_cs_7th_subjects_marks=StringVar()
        self.var_student_cs_7th_usn=StringVar()

        self.var_cs_8th_subjects_code=StringVar()
        self.var_cs_8th_subjects=StringVar()
        self.var_cs_8th_subjects_marks=StringVar()
        self.var_student_cs_8th_usn=StringVar()
        ############################################
        self.var_ise_3rd_subjects_code=StringVar()
        self.var_ise_3rd_subjects=StringVar()
        self.var_ise_3rd_subjects_marks=StringVar()
        self.var_student_ise_3rd_usn=StringVar()

        self.var_ise_4th_subjects_code=StringVar()
        self.var_ise_4th_subjects=StringVar()
        self.var_ise_4th_subjects_marks=StringVar()
        self.var_student_ise_4th_usn=StringVar()

        self.var_ise_5th_subjects_code=StringVar()
        self.var_ise_5th_subjects=StringVar()
        self.var_ise_5th_subjects_marks=StringVar()
        self.var_student_ise_5th_usn=StringVar()

        self.var_ise_6th_subjects_code=StringVar()
        self.var_ise_6th_subjects=StringVar()
        self.var_ise_6th_subjects_marks=StringVar()
        self.var_student_ise_6th_usn=StringVar()

        self.var_ise_7th_subjects_code=StringVar()
        self.var_ise_7th_subjects=StringVar()
        self.var_ise_7th_subjects_marks=StringVar()
        self.var_student_ise_7th_usn=StringVar()

        self.var_ise_8th_subjects_code=StringVar()
        self.var_ise_8th_subjects=StringVar()
        self.var_ise_8th_subjects_marks=StringVar()
        self.var_student_ise_8th_usn=StringVar()
        ###############################################
        self.var_ete_3rd_subjects_code=StringVar()
        self.var_ete_3rd_subjects=StringVar()
        self.var_ete_3rd_subjects_marks=StringVar()
        self.var_student_ete_3rd_usn=StringVar()

        self.var_ete_4th_subjects_code=StringVar()
        self.var_ete_4th_subjects=StringVar()
        self.var_ete_4th_subjects_marks=StringVar()
        self.var_student_ete_4th_usn=StringVar()

        self.var_ete_5th_subjects_code=StringVar()
        self.var_ete_5th_subjects=StringVar()
        self.var_ete_5th_subjects_marks=StringVar()
        self.var_student_ete_5th_usn=StringVar()

        self.var_ete_6th_subjects_code=StringVar()
        self.var_ete_6th_subjects=StringVar()
        self.var_ete_6th_subjects_marks=StringVar()
        self.var_student_ete_6th_usn=StringVar()

        self.var_ete_7th_subjects_code=StringVar()
        self.var_ete_7th_subjects=StringVar()
        self.var_ete_7th_subjects_marks=StringVar()
        self.var_student_ete_7th_usn=StringVar()

        self.var_ete_8th_subjects_code=StringVar()
        self.var_ete_8th_subjects=StringVar()
        self.var_ete_8th_subjects_marks=StringVar()
        self.var_student_ete_8th_usn=StringVar()







      
        ####################################
        
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
        if self.var_sem_select.get()=='1st_Semister':
            if self.var_branch_select.get()=='CHEMISTRY_cycle':
                if self.var_scheme_select.get()=='2018':
                    che_student_usn_list=[]
                    def fetch_che_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    che_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    che_subjects_list=[]
                    def fetch_che_subjects():
                        #all_che_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select che_subjects from all_che_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    che_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_che_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_che_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_che_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_che_usn.get()=='':
                                                        messagebox.showerror('Error','The student USN must be reuired.',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into che_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_che_subjects_code.get(),
                                                        self.var_che_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        self.var_subjects_marks.get(),
                                                        self.var_student_che_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_che_data()
                                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_che_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from che_student_resultss')
                            rows=cur.fetchall()
                            tree_che_treeview.delete(*tree_che_treeview.get_children())
                            for row in rows:
                                tree_che_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_che_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from che_student_resultss where subjects=%s',(self.var_che_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_che_subjects where subjects=%s ',(self.var_che_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_che_data()
                                    fetch_che_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_che_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update che_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_che_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_subjects_marks.get(),
                                                    self.var_student_che_usn.get(),
                                                    self.var_che_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_che_data()
                                fetch_che_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_che_data():
                        fetch_che_data()
                        self.var_che_subjects_code.set('')
                        self.var_che_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_subjects_marks.set('')
                        self.var_student_che_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_che_data(ev):
                        read=tree_che_treeview.focus()
                        content=tree_che_treeview.item(read)
                        rows=content['values']

                        self.var_che_subjects_code.set(row[0])
                        self.var_che_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_subjects_marks.set(row[5])
                        self.var_student_che_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)   
                                     
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_che_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT21',
                        '18CHEL26',
                        '18CPS23',
                        '18ELN24',
                        '18ME25',
                        '18CHEL26',
                        '18CPL27',
                        '18EGH28'
                    )
                    fetch_che_subjects()
                    che_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_che_subjects,values=che_subjects_list,state='readonly')
                    che_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_che_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_che_usn,values=che_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_che_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_che_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_che_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_che_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    fetch_che_data()
                    tree_che_treeview.bind('<ButtonRelease-1>',get_che_data)
                    #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='2nd_Semister':
            if self.var_branch_select.get()=='PHYSICS_cycle':
                if self.var_scheme_select.get()=='2018':
                    phy_student_usn_list=[]
                    def fetch_phy_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    phy_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    phy_subjects_list=[]
                    def fetch_phy_subjects():
                        #all_phy_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select phy_subjects from all_phy_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    phy_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_phy_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_phy_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_phy_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_phy_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_phy_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into phy_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_phy_subjects_code.get(),
                                                        self.var_phy_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                      
                                                        self.var_phy_subjects_marks.get(),
                                                        self.var_student_phy_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_phy_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_phy_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from phy_student_resultss')
                            rows=cur.fetchall()
                            tree_phy_treeview.delete(*tree_phy_treeview.get_children())
                            for row in rows:
                                tree_phy_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_phy_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from phy_student_resultss where subjects=%s',(self.var_phy_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from phy_student_resultss where subjects=%s ',(self.var_phy_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_phy_data()
                                    fetch_phy_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_phy_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update phy_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_phy_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_phy_subjects_marks.get(),
                                                    self.var_student_phy_usn.get(),
                                                    self.var_phy_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_phy_data()
                                fetch_phy_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_phy_data():
                        fetch_phy_data()
                        self.var_phy_subjects_code.set('')
                        self.var_phy_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_phy_subjects_marks.set('')
                        self.var_student_phy_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_phy_data(ev):
                        read=tree_phy_treeview.focus()
                        content=tree_phy_treeview.item(read)
                        rows=content['values']

                        self.var_phy_subjects_code.set(row[0])
                        self.var_phy_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_phy_subjects_marks.set(row[5])
                        self.var_student_phy_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)                    
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_phy_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT11',
                        '18PHY12',
                        '18CIV14',
                        '18EGDL15',
                        '18PHYL16',
                        '18ELEL17',
                        '18EGH18',
                        '18ELE13'
                    )
                    fetch_phy_subjects()
                    phy_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_phy_subjects,values=phy_subjects_list,state='readonly')
                    phy_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_phy_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)

                    fetch_phy_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_phy_usn,values=phy_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_phy_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_phy_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_phy_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_phy_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_phy_treeview.heading('student_usn',text="USN")
                    

                 
                    tree_phy_treeview.column('subject_code',width=200)
                    tree_phy_treeview.column('subjects',width=200)
                    tree_phy_treeview.column('semister',width=200)
                    tree_phy_treeview.column('scheme',width=200)
                    tree_phy_treeview.column('branch',width=200)
                    tree_phy_treeview.column('marks',width=200)
                    tree_phy_treeview.column('student_usn',width=200)

                    tree_phy_treeview['show']='headings'
                    
                    tree_phy_treeview.pack(fill=BOTH,expand=1)
                    fetch_phy_data()
                    tree_phy_treeview.bind('<ButtonRelease-1>',get_phy_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                if self.var_scheme_select.get()=='2018':
                    civil_3rd_student_usn_list=[]
                    def fetch_civil_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    civil_3rd_subjects_list=[]
                    def fetch_civil_3rd_subjects():
                        #all_civil_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select civil_3rd_subjects from all_civil_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_civil_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_civil_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_civil_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_civil_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_civil_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into civil_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_civil_3rd_subjects_code.get(),
                                                        self.var_civil_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_civil_3rd_subjects_marks.get(),
                                                        self.var_student_civil_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_civil_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_civil_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from civil_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_civil_3rd_treeview.delete(*tree_civil_3rd_treeview.get_children())
                            for row in rows:
                                tree_civil_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from civil_3rd_student_resultss where subjects=%s',(self.var_civil_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_civil_3rd_subjects where subjects=%s ',(self.var_civil_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_civil_3rd_data()
                                    fetch_civil_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update civil_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_civil_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_civil_3rd_subjects_marks.get(),
                                                    self.var_student_civil_3rd_usn.get(),
                                                    self.var_civil_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_civil_3rd_data()
                                fetch_civil_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_civil_3rd_data():
                        fetch_civil_3rd_data()
                        self.var_civil_3rd_subjects_code.set('')
                        self.var_civil_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_civil_3rd_usn.set('')
                        self.var_civil_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_civil_3rd_data(ev):
                        read=tree_civil_3rd_treeview.focus()
                        content=tree_civil_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_civil_3rd_subjects_code.set(row[0])
                        self.var_civil_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_civil_3rd_subjects_marks.set(row[5])
                        self.var_student_civil_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_civil_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_civil_3rd_subjects()
                    civil_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_civil_3rd_subjects,values=civil_3rd_subjects_list,state='readonly')
                    civil_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_civil_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_civil_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_civil_3rd_usn,values=civil_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_civil_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_civil_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_civil_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_civil_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_civil_3rd_treeview.heading('student_usn',text='USN')
                    

                    tree_civil_3rd_treeview.column('subject_code',width=200)
                    tree_civil_3rd_treeview.column('subjects',width=200)
                    tree_civil_3rd_treeview.column('semister',width=200)
                    tree_civil_3rd_treeview.column('scheme',width=200)
                    tree_civil_3rd_treeview.column('branch',width=200)
                    tree_civil_3rd_treeview.column('marks',width=200)
                    tree_civil_3rd_treeview.column('student_usn',width=200)

                    tree_civil_3rd_treeview['show']='headings'
                    
                    tree_civil_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_civil_3rd_data()
                    tree_civil_3rd_treeview.bind('<ButtonRelease-1>',get_civil_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                if self.var_scheme_select.get()=='2018':
                    civil_4th_student_usn_list=[]
                    def fetch_civil_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    civil_4th_subjects_list=[]
                    def fetch_civil_4th_subjects():
                        #all_civil_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select civil_4th_subjects from all_civil_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_civil_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_civil_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_civil_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_civil_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_civil_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into civil_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_civil_4th_subjects_code.get(),
                                                        self.var_civil_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_civil_4th_subjects_marks.get(),
                                                        self.var_student_civil_4th_usn.get(),
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_civil_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_civil_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from civil_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_civil_4th_treeview.delete(*tree_civil_4th_treeview.get_children())
                            for row in rows:
                                tree_civil_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from civil_4th_student_resultss where subjects=%s',(self.var_civil_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_civil_4th_subjects where subjects=%s ',(self.var_civil_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_civil_4th_data()
                                    fetch_civil_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update civil_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_civil_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_civil_4th_subjects_marks.get(),
                                                    self.var_student_civil_4th_usn.get(),
                                                    self.var_civil_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_civil_4th_data()
                                fetch_civil_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_civil_4th_data():
                        fetch_civil_4th_data()
                        self.var_civil_4th_subjects_code.set('')
                        self.var_civil_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_civil_4th_subjects_marks.set('')
                        self.var_student_civil_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_civil_4th_data(ev):
                        read=tree_civil_4th_treeview.focus()
                        content=tree_civil_4th_treeview.item(read)
                        rows=content['values']

                        self.var_civil_4th_subjects_code.set(row[0])
                        self.var_civil_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_civil_4th_subjects_marks.set(row[5])
                        self.var_student_civil_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_civil_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_civil_4th_subjects()
                    civil_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_civil_4th_subjects,values=civil_4th_subjects_list,state='readonly')
                    civil_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_civil_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_civil_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_civil_4th_usn,values=civil_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_civil_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_civil_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_civil_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_civil_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_civil_4th_treeview.heading('student_usn',text='USN')
                    

                    tree_civil_4th_treeview.column('subject_code',width=200)
                    tree_civil_4th_treeview.column('subjects',width=200)
                    tree_civil_4th_treeview.column('semister',width=200)
                    tree_civil_4th_treeview.column('scheme',width=200)
                    tree_civil_4th_treeview.column('branch',width=200)
                    tree_civil_4th_treeview.column('marks',width=200)
                    tree_civil_4th_treeview.column('student_usn',width=200)

                    tree_civil_4th_treeview['show']='headings'
                    
                    tree_civil_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_civil_4th_data()
                    tree_civil_4th_treeview.bind('<ButtonRelease-1>',get_civil_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                if self.var_scheme_select.get()=='2018':
                    civil_5th_student_usn_list=[]
                    def fetch_civil_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    civil_5th_subjects_list=[]
                    def fetch_civil_5th_subjects():
                        #all_civil_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select civil_5th_subjects from all_civil_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_civil_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_civil_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_civil_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_civil_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_civil_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into civil_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_civil_5th_subjects_code.get(),
                                                        self.var_civil_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                       
                                                        self.var_civil_5th_subjects_marks.get(),
                                                         self.var_student_civil_5th_usn.get(),
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_civil_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_civil_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from civil_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_civil_5th_treeview.delete(*tree_civil_5th_treeview.get_children())
                            for row in rows:
                                tree_civil_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from civil_5th_student_resultss where subjects=%s',(self.var_civil_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_civil_5th_subjects where subjects=%s ',(self.var_civil_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_civil_5th_data()
                                    fetch_civil_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update civil_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_civil_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_civil_5th_subjects_marks.get(),
                                                    self.var_student_civil_5th_usn.get(),
                                                    self.var_civil_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_civil_5th_data()
                                fetch_civil_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_civil_5th_data():
                        fetch_civil_5th_data()
                        self.var_civil_5th_subjects_code.set('')
                        self.var_civil_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_civil_5th_subjects_marks.set('')
                        self.var_student_civil_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_civil_5th_data(ev):
                        read=tree_civil_5th_treeview.focus()
                        content=tree_civil_5th_treeview.item(read)
                        rows=content['values']

                        self.var_civil_5th_subjects_code.set(row[0])
                        self.var_civil_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_civil_5th_subjects_marks.set(row[5])
                        self.var_student_civil_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_civil_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_civil_5th_subjects()
                    civil_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_civil_5th_subjects,values=civil_5th_subjects_list,state='readonly')
                    civil_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_civil_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_civil_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_civil_5th_usn,values=civil_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_civil_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_civil_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_civil_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_civil_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_civil_5th_treeview.heading('student_usn',text='USN')
                    

                    tree_civil_5th_treeview.column('subject_code',width=200)
                    tree_civil_5th_treeview.column('subjects',width=200)
                    tree_civil_5th_treeview.column('semister',width=200)
                    tree_civil_5th_treeview.column('scheme',width=200)
                    tree_civil_5th_treeview.column('branch',width=200)
                    tree_civil_5th_treeview.column('marks',width=200)
                    tree_civil_5th_treeview.column('student_usn',width=200)

                    tree_civil_5th_treeview['show']='headings'
                    
                    tree_civil_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_civil_5th_data()
                    tree_civil_5th_treeview.bind('<ButtonRelease-1>',get_civil_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                if self.var_scheme_select.get()=='2018':
                    civil_6th_student_usn_list=[]
                    def fetch_civil_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    civil_6th_subjects_list=[]
                    def fetch_civil_6th_subjects():
                        #all_civil_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select civil_6th_subjects from all_civil_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_civil_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_civil_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_civil_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_civil_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_civil_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into civil_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_civil_6th_subjects_code.get(),
                                                        self.var_civil_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_civil_6th_subjects_marks.get(),
                                                        self.var_student_civil_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_civil_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_civil_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from civil_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_civil_6th_treeview.delete(*tree_civil_6th_treeview.get_children())
                            for row in rows:
                                tree_civil_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from civil_6th_student_resultss where subjects=%s',(self.var_civil_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_civil_6th_subjects where subjects=%s ',(self.var_civil_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_civil_6th_data()
                                    fetch_civil_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update civil_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_civil_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_civil_6th_subjects_marks.get(),
                                                    self.var_student_civil_6th_usn.get(),
                                                    self.var_civil_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_civil_6th_data()
                                fetch_civil_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_civil_6th_data():
                        fetch_civil_6th_data()
                        self.var_civil_6th_subjects_code.set('')
                        self.var_civil_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_civil_6th_usn.set('')
                        self.var_civil_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_civil_6th_data(ev):
                        read=tree_civil_6th_treeview.focus()
                        content=tree_civil_6th_treeview.item(read)
                        rows=content['values']

                        self.var_civil_6th_subjects_code.set(row[0])
                        self.var_civil_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_civil_6th_subjects_marks.set(row[5])
                        self.var_student_civil_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_civil_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_civil_6th_subjects()
                    civil_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_civil_6th_subjects,values=civil_6th_subjects_list,state='readonly')
                    civil_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_civil_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_civil_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_civil_6th_usn,values=civil_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_civil_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_civil_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_civil_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_civil_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_civil_6th_treeview.heading('student_usn',text='USN')
                    

            
                    tree_civil_6th_treeview.column('subject_code',width=200)
                    tree_civil_6th_treeview.column('subjects',width=200)
                    tree_civil_6th_treeview.column('semister',width=200)
                    tree_civil_6th_treeview.column('scheme',width=200)
                    tree_civil_6th_treeview.column('branch',width=200)
                    tree_civil_6th_treeview.column('marks',width=200)
                    tree_civil_6th_treeview.column('student_usn',width=200)

                    tree_civil_6th_treeview['show']='headings'
                    
                    tree_civil_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_civil_6th_data()
                    tree_civil_6th_treeview.bind('<ButtonRelease-1>',get_civil_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                if self.var_scheme_select.get()=='2018':
                    civil_7th_student_usn_list=[]
                    def fetch_civil_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    civil_7th_subjects_list=[]
                    def fetch_civil_7th_subjects():
                        #all_civil_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select civil_7th_subjects from all_civil_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_civil_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_civil_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_civil_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_civil_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_civil_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into civil_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_civil_7th_subjects_code.get(),
                                                        self.var_civil_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_civil_7th_subjects_marks.get(),
                                                        self.var_student_civil_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_civil_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_civil_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from civil_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_civil_7th_treeview.delete(*tree_civil_7th_treeview.get_children())
                            for row in rows:
                                tree_civil_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from civil_7th_student_resultss where subjects=%s',(self.var_civil_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_civil_7th_subjects where subjects=%s ',(self.var_civil_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_civil_7th_data()
                                    fetch_civil_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update civil_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_civil_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_civil_7th_subjects_marks.get(),
                                                    self.var_student_civil_7th_usn.get(),
                                                    self.var_civil_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_civil_7th_data()
                                fetch_civil_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_civil_7th_data():
                        fetch_civil_7th_data()
                        self.var_civil_7th_subjects_code.set('')
                        self.var_civil_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_civil_7th_subjects_marks.set('')
                        self.var_student_civil_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_civil_7th_data(ev):
                        read=tree_civil_7th_treeview.focus()
                        content=tree_civil_7th_treeview.item(read)
                        rows=content['values']

                        self.var_civil_7th_subjects_code.set(row[0])
                        self.var_civil_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_civil_7th_subjects_marks.set(row[5])
                        self.var_student_civil_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_civil_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_civil_7th_subjects()
                    civil_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_civil_7th_subjects,values=civil_7th_subjects_list,state='readonly')
                    civil_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_civil_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_civil_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_civil_7th_usn,values=civil_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_civil_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_civil_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_civil_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_civil_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_civil_7th_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_civil_7th_treeview.column('subject_code',width=200)
                    tree_civil_7th_treeview.column('subjects',width=200)
                    tree_civil_7th_treeview.column('semister',width=200)
                    tree_civil_7th_treeview.column('scheme',width=200)
                    tree_civil_7th_treeview.column('branch',width=200)
                    tree_civil_7th_treeview.column('marks',width=200)
                    tree_civil_7th_treeview.column('student_usn',width=200)

                    tree_civil_7th_treeview['show']='headings'
                    
                    tree_civil_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_civil_7th_data()
                    tree_civil_7th_treeview.bind('<ButtonRelease-1>',get_civil_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Civil_Engineering':
                if self.var_scheme_select.get()=='2018':
                    civil_8th_student_usn_list=[]
                    def fetch_civil_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    civil_8th_subjects_list=[]
                    def fetch_civil_8th_subjects():
                        #all_civil_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select civil_8th_subjects from all_civil_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    civil_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_civil_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_civil_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_civil_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_civil_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_civil_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into civil_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_civil_8th_subjects_code.get(),
                                                        self.var_civil_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_civil_8th_subjects_marks.get(),
                                                        self.var_student_civil_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_civil_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_civil_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from civil_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_civil_8th_treeview.delete(*tree_civil_8th_treeview.get_children())
                            for row in rows:
                                tree_civil_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from civil_8th_student_resultss where subjects=%s',(self.var_civil_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_civil_8th_subjects where subjects=%s ',(self.var_civil_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_civil_8th_data()
                                    fetch_civil_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_civil_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update civil_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_civil_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_civil_8th_subjects_marks.get(),
                                                    self.var_student_civil_8th_usn.get(),
                                                    self.var_civil_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_civil_8th_data()
                                fetch_civil_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_civil_8th_data():
                        fetch_civil_8th_data()
                        self.var_civil_8th_subjects_code.set('')
                        self.var_civil_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_civil_8th_subjects_marks.set('')
                        self.var_student_civil_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_civil_8th_data(ev):
                        read=tree_civil_8th_treeview.focus()
                        content=tree_civil_8th_treeview.item(read)
                        rows=content['values']

                        self.var_civil_8th_subjects_code.set(row[0])
                        self.var_civil_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_civil_8th_subjects_marks.set(row[5])
                        self.var_student_civil_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_civil_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_civil_8th_subjects()
                    civil_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_civil_8th_subjects,values=civil_8th_subjects_list,state='readonly')
                    civil_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_civil_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_civil_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_civil_8th_usn,values=civil_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_civil_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_civil_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_civil_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_civil_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_civil_8th_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_civil_8th_treeview.column('subject_code',width=200)
                    tree_civil_8th_treeview.column('subjects',width=200)
                    tree_civil_8th_treeview.column('semister',width=200)
                    tree_civil_8th_treeview.column('scheme',width=200)
                    tree_civil_8th_treeview.column('branch',width=200)
                    tree_civil_8th_treeview.column('marks',width=200)
                    tree_civil_8th_treeview.column('student_usn',width=200)

                    tree_civil_8th_treeview['show']='headings'
                    
                    tree_civil_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_civil_8th_data()
                    tree_civil_8th_treeview.bind('<ButtonRelease-1>',get_civil_8th_data)
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                if self.var_scheme_select.get()=='2018':
                    mech_3rd_student_usn_list=[]
                    def fetch_mech_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    mech_3rd_subjects_list=[]
                    def fetch_mech_3rd_subjects():
                        #all_mech_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select mech_3rd_subjects from all_mech_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_mech_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_mech_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_mech_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_mech_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_mech_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into mech_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_mech_3rd_subjects_code.get(),
                                                        self.var_mech_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_mech_3rd_subjects_marks.get(),
                                                        self.var_student_mech_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_mech_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_mech_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from mech_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_mech_3rd_treeview.delete(*tree_mech_3rd_treeview.get_children())
                            for row in rows:
                                tree_mech_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from mech_3rd_student_resultss where subjects=%s',(self.var_mech_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_mech_3rd_subjects where subjects=%s ',(self.var_mech_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_mech_3rd_data()
                                    fetch_mech_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update mech_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_mech_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_mech_3rd_subjects_marks.get(),
                                                    self.var_student_mech_3rd_usn.get(),
                                                    self.var_mech_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_mech_3rd_data()
                                fetch_mech_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_mech_3rd_data():
                        fetch_mech_3rd_data()
                        self.var_mech_3rd_subjects_code.set('')
                        self.var_mech_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_mech_3rd_usn.set('')
                        self.var_mech_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_mech_3rd_data(ev):
                        read=tree_mech_3rd_treeview.focus()
                        content=tree_mech_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_mech_3rd_subjects_code.set(row[0])
                        self.var_mech_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_mech_3rd_subjects_marks.set(row[5])
                        self.var_student_mech_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_mech_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_mech_3rd_subjects()
                    mech_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_mech_3rd_subjects,values=mech_3rd_subjects_list,state='readonly')
                    mech_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_mech_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_mech_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_mech_3rd_usn,values=mech_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_mech_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_mech_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_mech_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_mech_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_mech_3rd_treeview.heading('student_usn',text='USN')
                    

                    tree_mech_3rd_treeview.column('subject_code',width=200)
                    tree_mech_3rd_treeview.column('subjects',width=200)
                    tree_mech_3rd_treeview.column('semister',width=200)
                    tree_mech_3rd_treeview.column('scheme',width=200)
                    tree_mech_3rd_treeview.column('branch',width=200)
                    tree_mech_3rd_treeview.column('marks',width=200)
                    tree_mech_3rd_treeview.column('student_usn',width=200)

                    tree_mech_3rd_treeview['show']='headings'
                    
                    tree_mech_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_mech_3rd_data()
                    tree_mech_3rd_treeview.bind('<ButtonRelease-1>',get_mech_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                if self.var_scheme_select.get()=='2018':
                    mech_4th_student_usn_list=[]
                    def fetch_mech_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    mech_4th_subjects_list=[]
                    def fetch_mech_4th_subjects():
                        #all_mech_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select mech_4th_subjects from all_mech_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_mech_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_mech_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_mech_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_mech_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_mech_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into mech_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_mech_4th_subjects_code.get(),
                                                        self.var_mech_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_mech_4th_subjects_marks.get(),
                                                        self.var_student_mech_4th_usn.get(),
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_mech_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_mech_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from mech_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_mech_4th_treeview.delete(*tree_mech_4th_treeview.get_children())
                            for row in rows:
                                tree_mech_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from mech_4th_student_resultss where subjects=%s',(self.var_mech_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_mech_4th_subjects where subjects=%s ',(self.var_mech_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_mech_4th_data()
                                    fetch_mech_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update mech_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_mech_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_mech_4th_subjects_marks.get(),
                                                    self.var_student_mech_4th_usn.get(),
                                                    self.var_mech_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_mech_4th_data()
                                fetch_mech_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_mech_4th_data():
                        fetch_mech_4th_data()
                        self.var_mech_4th_subjects_code.set('')
                        self.var_mech_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_mech_4th_subjects_marks.set('')
                        self.var_student_mech_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_mech_4th_data(ev):
                        read=tree_mech_4th_treeview.focus()
                        content=tree_mech_4th_treeview.item(read)
                        rows=content['values']

                        self.var_mech_4th_subjects_code.set(row[0])
                        self.var_mech_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_mech_4th_subjects_marks.set(row[5])
                        self.var_student_mech_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_mech_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_mech_4th_subjects()
                    mech_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_mech_4th_subjects,values=mech_4th_subjects_list,state='readonly')
                    mech_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_mech_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_mech_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_mech_4th_usn,values=mech_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_mech_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_mech_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_mech_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_mech_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_mech_4th_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_mech_4th_treeview.column('subject_code',width=200)
                    tree_mech_4th_treeview.column('subjects',width=200)
                    tree_mech_4th_treeview.column('semister',width=200)
                    tree_mech_4th_treeview.column('scheme',width=200)
                    tree_mech_4th_treeview.column('branch',width=200)
                    tree_mech_4th_treeview.column('marks',width=200)
                    tree_mech_4th_treeview.column('student_usn',width=200)

                    tree_mech_4th_treeview['show']='headings'
                    
                    tree_mech_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_mech_4th_data()
                    tree_mech_4th_treeview.bind('<ButtonRelease-1>',get_mech_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                if self.var_scheme_select.get()=='2018':
                    mech_5th_student_usn_list=[]
                    def fetch_mech_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    mech_5th_subjects_list=[]
                    def fetch_mech_5th_subjects():
                        #all_mech_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select mech_5th_subjects from all_mech_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_mech_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_mech_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_mech_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_mech_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_mech_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into mech_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_mech_5th_subjects_code.get(),
                                                        self.var_mech_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_mech_5th_subjects_marks.get(),
                                                        self.var_student_mech_5th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_mech_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_mech_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from mech_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_mech_5th_treeview.delete(*tree_mech_5th_treeview.get_children())
                            for row in rows:
                                tree_mech_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from mech_5th_student_resultss where subjects=%s',(self.var_mech_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_mech_5th_subjects where subjects=%s ',(self.var_mech_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_mech_5th_data()
                                    fetch_mech_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update mech_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_mech_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_mech_5th_subjects_marks.get(),
                                                    self.var_student_mech_5th_usn.get(),
                                                    self.var_mech_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_mech_5th_data()
                                fetch_mech_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_mech_5th_data():
                        fetch_mech_5th_data()
                        self.var_mech_5th_subjects_code.set('')
                        self.var_mech_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_mech_5th_subjects_marks.set('')
                        self.var_student_mech_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_mech_5th_data(ev):
                        read=tree_mech_5th_treeview.focus()
                        content=tree_mech_5th_treeview.item(read)
                        rows=content['values']

                        self.var_mech_5th_subjects_code.set(row[0])
                        self.var_mech_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_mech_5th_subjects_marks.set(row[5])
                        self.var_student_mech_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_mech_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_mech_5th_subjects()
                    mech_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_mech_5th_subjects,values=mech_5th_subjects_list,state='readonly')
                    mech_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_mech_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_mech_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_mech_5th_usn,values=mech_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_mech_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_mech_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_mech_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_mech_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_mech_5th_treeview.heading('student_usn',text='USN')
                    

                    tree_mech_5th_treeview.column('subject_code',width=200)
                    tree_mech_5th_treeview.column('subjects',width=200)
                    tree_mech_5th_treeview.column('semister',width=200)
                    tree_mech_5th_treeview.column('scheme',width=200)
                    tree_mech_5th_treeview.column('branch',width=200)
                    tree_mech_5th_treeview.column('marks',width=200)
                    tree_mech_5th_treeview.column('student_usn',width=200)

                    tree_mech_5th_treeview['show']='headings'
                    
                    tree_mech_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_mech_5th_data()
                    tree_mech_5th_treeview.bind('<ButtonRelease-1>',get_mech_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                if self.var_scheme_select.get()=='2018':
                    mech_6th_student_usn_list=[]
                    def fetch_mech_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    mech_6th_subjects_list=[]
                    def fetch_mech_6th_subjects():
                        #all_mech_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select mech_6th_subjects from all_mech_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_mech_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_mech_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_mech_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_mech_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_mech_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into mech_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_mech_6th_subjects_code.get(),
                                                        self.var_mech_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_mech_6th_subjects_marks.get(),
                                                        self.var_student_mech_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_mech_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_mech_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from mech_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_mech_6th_treeview.delete(*tree_mech_6th_treeview.get_children())
                            for row in rows:
                                tree_mech_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from mech_6th_student_resultss where subjects=%s',(self.var_mech_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_mech_6th_subjects where subjects=%s ',(self.var_mech_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_mech_6th_data()
                                    fetch_mech_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update mech_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_mech_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_mech_6th_subjects_marks.get(),
                                                    self.var_student_mech_6th_usn.get(),
                                                    self.var_mech_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_mech_6th_data()
                                fetch_mech_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_mech_6th_data():
                        fetch_mech_6th_data()
                        self.var_mech_6th_subjects_code.set('')
                        self.var_mech_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_mech_6th_usn.set('')
                        self.var_mech_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_mech_6th_data(ev):
                        read=tree_mech_6th_treeview.focus()
                        content=tree_mech_6th_treeview.item(read)
                        rows=content['values']

                        self.var_mech_6th_subjects_code.set(row[0])
                        self.var_mech_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_mech_6th_subjects_marks.set(row[5])
                        self.var_student_mech_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_mech_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_mech_6th_subjects()
                    mech_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_mech_6th_subjects,values=mech_6th_subjects_list,state='readonly')
                    mech_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_mech_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_mech_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_mech_6th_usn,values=mech_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_mech_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_mech_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_mech_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_mech_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_mech_6th_treeview.heading('student_usn',text='USN')
                    

                    tree_mech_6th_treeview.column('subject_code',width=200)
                    tree_mech_6th_treeview.column('subjects',width=200)
                    tree_mech_6th_treeview.column('semister',width=200)
                    tree_mech_6th_treeview.column('scheme',width=200)
                    tree_mech_6th_treeview.column('branch',width=200)
                    tree_mech_6th_treeview.column('marks',width=200)
                    tree_mech_6th_treeview.column('student_usn',width=200)

                    tree_mech_6th_treeview['show']='headings'
                    
                    tree_mech_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_mech_6th_data()
                    tree_mech_6th_treeview.bind('<ButtonRelease-1>',get_mech_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                if self.var_scheme_select.get()=='2018':
                    mech_7th_student_usn_list=[]
                    def fetch_mech_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    mech_7th_subjects_list=[]
                    def fetch_mech_7th_subjects():
                        #all_mech_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select mech_7th_subjects from all_mech_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_mech_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_mech_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_mech_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_mech_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_mech_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into mech_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_mech_7th_subjects_code.get(),
                                                        self.var_mech_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_mech_7th_subjects_marks.get(),
                                                        self.var_student_mech_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_mech_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_mech_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from mech_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_mech_7th_treeview.delete(*tree_mech_7th_treeview.get_children())
                            for row in rows:
                                tree_mech_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from mech_7th_student_resultss where subjects=%s',(self.var_mech_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_mech_7th_subjects where subjects=%s ',(self.var_mech_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_mech_7th_data()
                                    fetch_mech_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update mech_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_mech_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_mech_7th_subjects_marks.get(),
                                                    self.var_student_mech_7th_usn.get(),
                                                    self.var_mech_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_mech_7th_data()
                                fetch_mech_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_mech_7th_data():
                        fetch_mech_7th_data()
                        self.var_mech_7th_subjects_code.set('')
                        self.var_mech_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_mech_7th_subjects_marks.set('')
                        self.var_student_mech_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_mech_7th_data(ev):
                        read=tree_mech_7th_treeview.focus()
                        content=tree_mech_7th_treeview.item(read)
                        rows=content['values']

                        self.var_mech_7th_subjects_code.set(row[0])
                        self.var_mech_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_mech_7th_subjects_marks.set(row[5])
                        self.var_student_mech_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_mech_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_mech_7th_subjects()
                    mech_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_mech_7th_subjects,values=mech_7th_subjects_list,state='readonly')
                    mech_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_mech_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_mech_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_mech_7th_usn,values=mech_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_mech_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_mech_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_mech_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_mech_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_mech_7th_treeview.heading('student_usn',text='USN')
                    

                 
                    tree_mech_7th_treeview.column('subject_code',width=200)
                    tree_mech_7th_treeview.column('subjects',width=200)
                    tree_mech_7th_treeview.column('semister',width=200)
                    tree_mech_7th_treeview.column('scheme',width=200)
                    tree_mech_7th_treeview.column('branch',width=200)
                    tree_mech_7th_treeview.column('marks',width=200)
                    tree_mech_7th_treeview.column('student_usn',width=200)

                    tree_mech_7th_treeview['show']='headings'
                    
                    tree_mech_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_mech_7th_data()
                    tree_mech_7th_treeview.bind('<ButtonRelease-1>',get_mech_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Mechanical_Engineering':
                if self.var_scheme_select.get()=='2018':
                    mech_8th_student_usn_list=[]
                    def fetch_mech_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    mech_8th_subjects_list=[]
                    def fetch_mech_8th_subjects():
                        #all_mech_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select mech_8th_subjects from all_mech_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    mech_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_mech_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_mech_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_mech_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_mech_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_mech_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into mech_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_mech_8th_subjects_code.get(),
                                                        self.var_mech_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_mech_8th_subjects_marks.get(),
                                                        self.var_student_mech_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_mech_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_mech_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from mech_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_mech_8th_treeview.delete(*tree_mech_8th_treeview.get_children())
                            for row in rows:
                                tree_mech_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from mech_8th_student_resultss where subjects=%s',(self.var_mech_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_mech_8th_subjects where subjects=%s ',(self.var_mech_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_mech_8th_data()
                                    fetch_mech_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_mech_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update mech_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_mech_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_mech_8th_subjects_marks.get(),
                                                    self.var_student_mech_8th_usn.get(),
                                                    self.var_mech_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_mech_8th_data()
                                fetch_mech_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_mech_8th_data():
                        fetch_mech_8th_data()
                        self.var_mech_8th_subjects_code.set('')
                        self.var_mech_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_mech_8th_subjects_marks.set('')
                        self.var_student_mech_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_mech_8th_data(ev):
                        read=tree_mech_8th_treeview.focus()
                        content=tree_mech_8th_treeview.item(read)
                        rows=content['values']

                        self.var_mech_8th_subjects_code.set(row[0])
                        self.var_mech_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_mech_8th_subjects_marks.set(row[5])
                        self.var_student_mech_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_mech_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_mech_8th_subjects()
                    mech_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_mech_8th_subjects,values=mech_8th_subjects_list,state='readonly')
                    mech_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_mech_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_mech_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_mech_8th_usn,values=mech_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_mech_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_mech_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_mech_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_mech_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_mech_8th_treeview.heading('student_usn',text='USN')
                    

                  
                    tree_mech_8th_treeview.column('subject_code',width=200)
                    tree_mech_8th_treeview.column('subjects',width=200)
                    tree_mech_8th_treeview.column('semister',width=200)
                    tree_mech_8th_treeview.column('scheme',width=200)
                    tree_mech_8th_treeview.column('branch',width=200)
                    tree_mech_8th_treeview.column('marks',width=200)
                    tree_mech_8th_treeview.column('student_usn',width=200)

                    tree_mech_8th_treeview['show']='headings'
                    
                    tree_mech_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_mech_8th_data()
                    tree_mech_8th_treeview.bind('<ButtonRelease-1>',get_mech_8th_data)
    
    
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ece_3rd_student_usn_list=[]
                    def fetch_ece_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ece_3rd_subjects_list=[]
                    def fetch_ece_3rd_subjects():
                        #all_ece_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ece_3rd_subjects from all_ece_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ece_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ece_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ece_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ece_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ece_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ece_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ece_3rd_subjects_code.get(),
                                                        self.var_ece_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ece_3rd_subjects_marks.get(),
                                                        self.var_student_ece_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ece_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ece_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ece_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_ece_3rd_treeview.delete(*tree_ece_3rd_treeview.get_children())
                            for row in rows:
                                tree_ece_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ece_3rd_student_resultss where subjects=%s',(self.var_ece_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ece_3rd_subjects where subjects=%s ',(self.var_ece_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ece_3rd_data()
                                    fetch_ece_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ece_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ece_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ece_3rd_subjects_marks.get(),
                                                    self.var_student_ece_3rd_usn.get(),
                                                    self.var_ece_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ece_3rd_data()
                                fetch_ece_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ece_3rd_data():
                        fetch_ece_3rd_data()
                        self.var_ece_3rd_subjects_code.set('')
                        self.var_ece_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_ece_3rd_usn.set('')
                        self.var_ece_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ece_3rd_data(ev):
                        read=tree_ece_3rd_treeview.focus()
                        content=tree_ece_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_ece_3rd_subjects_code.set(row[0])
                        self.var_ece_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ece_3rd_subjects_marks.set(row[5])
                        self.var_student_ece_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ece_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_ece_3rd_subjects()
                    ece_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ece_3rd_subjects,values=ece_3rd_subjects_list,state='readonly')
                    ece_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ece_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ece_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ece_3rd_usn,values=ece_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ece_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ece_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ece_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ece_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ece_3rd_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_ece_3rd_treeview.column('subject_code',width=200)
                    tree_ece_3rd_treeview.column('subjects',width=200)
                    tree_ece_3rd_treeview.column('semister',width=200)
                    tree_ece_3rd_treeview.column('scheme',width=200)
                    tree_ece_3rd_treeview.column('branch',width=200)
                    tree_ece_3rd_treeview.column('marks',width=200)
                    tree_ece_3rd_treeview.column('student_usn',width=200)

                    tree_ece_3rd_treeview['show']='headings'
                    
                    tree_ece_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_ece_3rd_data()
                    tree_ece_3rd_treeview.bind('<ButtonRelease-1>',get_ece_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ece_4th_student_usn_list=[]
                    def fetch_ece_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ece_4th_subjects_list=[]
                    def fetch_ece_4th_subjects():
                        #all_ece_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ece_4th_subjects from all_ece_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ece_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ece_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ece_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ece_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ece_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ece_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ece_4th_subjects_code.get(),
                                                        self.var_ece_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ece_4th_subjects_marks.get(),
                                                        self.var_student_ece_4th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ece_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ece_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ece_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_ece_4th_treeview.delete(*tree_ece_4th_treeview.get_children())
                            for row in rows:
                                tree_ece_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ece_4th_student_resultss where subjects=%s',(self.var_ece_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ece_4th_subjects where subjects=%s ',(self.var_ece_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ece_4th_data()
                                    fetch_ece_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ece_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ece_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ece_4th_subjects_marks.get(),
                                                    self.var_student_ece_4th_usn.get(),
                                                    self.var_ece_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ece_4th_data()
                                fetch_ece_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ece_4th_data():
                        fetch_ece_4th_data()
                        self.var_ece_4th_subjects_code.set('')
                        self.var_ece_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ece_4th_subjects_marks.set('')
                        self.var_student_ece_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ece_4th_data(ev):
                        read=tree_ece_4th_treeview.focus()
                        content=tree_ece_4th_treeview.item(read)
                        rows=content['values']

                        self.var_ece_4th_subjects_code.set(row[0])
                        self.var_ece_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ece_4th_subjects_marks.set(row[5])
                        self.var_student_ece_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ece_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_ece_4th_subjects()
                    ece_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ece_4th_subjects,values=ece_4th_subjects_list,state='readonly')
                    ece_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ece_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ece_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ece_4th_usn,values=ece_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ece_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ece_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ece_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ece_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ece_4th_treeview.heading('student_usn',text='USN')
                    

                    tree_ece_4th_treeview.column('subject_code',width=200)
                    tree_ece_4th_treeview.column('subjects',width=200)
                    tree_ece_4th_treeview.column('semister',width=200)
                    tree_ece_4th_treeview.column('scheme',width=200)
                    tree_ece_4th_treeview.column('branch',width=200)
                    tree_ece_4th_treeview.column('marks',width=200)
                    tree_ece_4th_treeview.column('student_usn',width=200)

                    tree_ece_4th_treeview['show']='headings'
                    
                    tree_ece_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ece_4th_data()
                    tree_ece_4th_treeview.bind('<ButtonRelease-1>',get_ece_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ece_5th_student_usn_list=[]
                    def fetch_ece_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ece_5th_subjects_list=[]
                    def fetch_ece_5th_subjects():
                        #all_ece_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ece_5th_subjects from all_ece_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ece_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ece_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ece_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ece_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ece_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ece_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ece_5th_subjects_code.get(),
                                                        self.var_ece_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ece_5th_subjects_marks.get(),
                                                        self.var_student_ece_5th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ece_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ece_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ece_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_ece_5th_treeview.delete(*tree_ece_5th_treeview.get_children())
                            for row in rows:
                                tree_ece_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ece_5th_student_resultss where subjects=%s',(self.var_ece_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ece_5th_subjects where subjects=%s ',(self.var_ece_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ece_5th_data()
                                    fetch_ece_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ece_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ece_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ece_5th_subjects_marks.get(),
                                                    self.var_student_ece_5th_usn.get(),
                                                    self.var_ece_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ece_5th_data()
                                fetch_ece_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ece_5th_data():
                        fetch_ece_5th_data()
                        self.var_ece_5th_subjects_code.set('')
                        self.var_ece_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ece_5th_subjects_marks.set('')
                        self.var_student_ece_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ece_5th_data(ev):
                        read=tree_ece_5th_treeview.focus()
                        content=tree_ece_5th_treeview.item(read)
                        rows=content['values']

                        self.var_ece_5th_subjects_code.set(row[0])
                        self.var_ece_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ece_5th_subjects_marks.set(row[5])
                        self.var_student_ece_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ece_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_ece_5th_subjects()
                    ece_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ece_5th_subjects,values=ece_5th_subjects_list,state='readonly')
                    ece_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ece_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ece_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ece_5th_usn,values=ece_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ece_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ece_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ece_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ece_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ece_5th_treeview.heading('student_usn',text='USN')
                    

                    tree_ece_5th_treeview.column('subject_code',width=200)
                    tree_ece_5th_treeview.column('subjects',width=200)
                    tree_ece_5th_treeview.column('semister',width=200)
                    tree_ece_5th_treeview.column('scheme',width=200)
                    tree_ece_5th_treeview.column('branch',width=200)
                    tree_ece_5th_treeview.column('marks',width=200)
                    tree_ece_5th_treeview.column('student_usn',width=200)

                    tree_ece_5th_treeview['show']='headings'
                    
                    tree_ece_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ece_5th_data()
                    tree_ece_5th_treeview.bind('<ButtonRelease-1>',get_ece_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ece_6th_student_usn_list=[]
                    def fetch_ece_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ece_6th_subjects_list=[]
                    def fetch_ece_6th_subjects():
                        #all_ece_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ece_6th_subjects from all_ece_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ece_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ece_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ece_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ece_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ece_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ece_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ece_6th_subjects_code.get(),
                                                        self.var_ece_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ece_6th_subjects_marks.get(),
                                                        self.var_student_ece_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ece_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ece_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ece_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_ece_6th_treeview.delete(*tree_ece_6th_treeview.get_children())
                            for row in rows:
                                tree_ece_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ece_6th_student_resultss where subjects=%s',(self.var_ece_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ece_6th_subjects where subjects=%s ',(self.var_ece_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ece_6th_data()
                                    fetch_ece_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ece_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ece_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ece_6th_subjects_marks.get(),
                                                    self.var_student_ece_6th_usn.get(),
                                                    self.var_ece_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ece_6th_data()
                                fetch_ece_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ece_6th_data():
                        fetch_ece_6th_data()
                        self.var_ece_6th_subjects_code.set('')
                        self.var_ece_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_ece_6th_usn.set('')
                        self.var_ece_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ece_6th_data(ev):
                        read=tree_ece_6th_treeview.focus()
                        content=tree_ece_6th_treeview.item(read)
                        rows=content['values']

                        self.var_ece_6th_subjects_code.set(row[0])
                        self.var_ece_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ece_6th_subjects_marks.set(row[5])
                        self.var_student_ece_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ece_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_ece_6th_subjects()
                    ece_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ece_6th_subjects,values=ece_6th_subjects_list,state='readonly')
                    ece_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ece_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ece_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ece_6th_usn,values=ece_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ece_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ece_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ece_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ece_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ece_6th_treeview.heading('student_usn',text='USN')
                    

                    tree_ece_6th_treeview.column('subject_code',width=200)
                    tree_ece_6th_treeview.column('subjects',width=200)
                    tree_ece_6th_treeview.column('semister',width=200)
                    tree_ece_6th_treeview.column('scheme',width=200)
                    tree_ece_6th_treeview.column('branch',width=200)
                    tree_ece_6th_treeview.column('marks',width=200)
                    tree_ece_6th_treeview.column('student_usn',width=200)

                    tree_ece_6th_treeview['show']='headings'
                    
                    tree_ece_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ece_6th_data()
                    tree_ece_6th_treeview.bind('<ButtonRelease-1>',get_ece_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ece_7th_student_usn_list=[]
                    def fetch_ece_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ece_7th_subjects_list=[]
                    def fetch_ece_7th_subjects():
                        #all_ece_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ece_7th_subjects from all_ece_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ece_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ece_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ece_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ece_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ece_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ece_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ece_7th_subjects_code.get(),
                                                        self.var_ece_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ece_7th_subjects_marks.get(),
                                                        self.var_student_ece_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ece_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ece_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ece_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_ece_7th_treeview.delete(*tree_ece_7th_treeview.get_children())
                            for row in rows:
                                tree_ece_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ece_7th_student_resultss where subjects=%s',(self.var_ece_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ece_7th_subjects where subjects=%s ',(self.var_ece_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ece_7th_data()
                                    fetch_ece_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ece_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ece_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ece_7th_subjects_marks.get(),
                                                    self.var_student_ece_7th_usn.get(),
                                                    self.var_ece_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ece_7th_data()
                                fetch_ece_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ece_7th_data():
                        fetch_ece_7th_data()
                        self.var_ece_7th_subjects_code.set('')
                        self.var_ece_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ece_7th_subjects_marks.set('')
                        self.var_student_ece_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ece_7th_data(ev):
                        read=tree_ece_7th_treeview.focus()
                        content=tree_ece_7th_treeview.item(read)
                        rows=content['values']

                        self.var_ece_7th_subjects_code.set(row[0])
                        self.var_ece_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ece_7th_subjects_marks.set(row[5])
                        self.var_student_ece_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ece_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_ece_7th_subjects()
                    ece_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ece_7th_subjects,values=ece_7th_subjects_list,state='readonly')
                    ece_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ece_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ece_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ece_7th_usn,values=ece_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ece_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ece_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ece_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ece_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ece_7th_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_ece_7th_treeview.column('subject_code',width=200)
                    tree_ece_7th_treeview.column('subjects',width=200)
                    tree_ece_7th_treeview.column('semister',width=200)
                    tree_ece_7th_treeview.column('scheme',width=200)
                    tree_ece_7th_treeview.column('branch',width=200)
                    tree_ece_7th_treeview.column('marks',width=200)
                    tree_ece_7th_treeview.column('student_usn',width=200)

                    tree_ece_7th_treeview['show']='headings'
                    
                    tree_ece_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ece_7th_data()
                    tree_ece_7th_treeview.bind('<ButtonRelease-1>',get_ece_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Communication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ece_8th_student_usn_list=[]
                    def fetch_ece_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ece_8th_subjects_list=[]
                    def fetch_ece_8th_subjects():
                        #all_ece_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ece_8th_subjects from all_ece_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ece_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ece_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ece_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ece_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ece_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ece_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ece_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ece_8th_subjects_code.get(),
                                                        self.var_ece_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ece_8th_subjects_marks.get(),
                                                        self.var_student_ece_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ece_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ece_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ece_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_ece_8th_treeview.delete(*tree_ece_8th_treeview.get_children())
                            for row in rows:
                                tree_ece_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ece_8th_student_resultss where subjects=%s',(self.var_ece_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ece_8th_subjects where subjects=%s ',(self.var_ece_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ece_8th_data()
                                    fetch_ece_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ece_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ece_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ece_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ece_8th_subjects_marks.get(),
                                                    self.var_student_ece_8th_usn.get(),
                                                    self.var_ece_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ece_8th_data()
                                fetch_ece_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ece_8th_data():
                        fetch_ece_8th_data()
                        self.var_ece_8th_subjects_code.set('')
                        self.var_ece_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ece_8th_subjects_marks.set('')
                        self.var_student_ece_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ece_8th_data(ev):
                        read=tree_ece_8th_treeview.focus()
                        content=tree_ece_8th_treeview.item(read)
                        rows=content['values']

                        self.var_ece_8th_subjects_code.set(row[0])
                        self.var_ece_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ece_8th_subjects_marks.set(row[5])
                        self.var_student_ece_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ece_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_ece_8th_subjects()
                    ece_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ece_8th_subjects,values=ece_8th_subjects_list,state='readonly')
                    ece_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ece_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ece_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ece_8th_usn,values=ece_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ece_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ece_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ece_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ece_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ece_8th_treeview.heading('student_usn',text='USN')
                    

                    tree_ece_8th_treeview.column('subject_code',width=200)
                    tree_ece_8th_treeview.column('subjects',width=200)
                    tree_ece_8th_treeview.column('semister',width=200)
                    tree_ece_8th_treeview.column('scheme',width=200)
                    tree_ece_8th_treeview.column('branch',width=200)
                    tree_ece_8th_treeview.column('marks',width=200)
                    tree_ece_8th_treeview.column('student_usn',width=200)

                    tree_ece_8th_treeview['show']='headings'
                    
                    tree_ece_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ece_8th_data()
                    tree_ece_8th_treeview.bind('<ButtonRelease-1>',get_ece_8th_data)

        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                if self.var_scheme_select.get()=='2018':
                    eee_3rd_student_usn_list=[]
                    def fetch_eee_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    eee_3rd_subjects_list=[]
                    def fetch_eee_3rd_subjects():
                        #all_eee_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select eee_3rd_subjects from all_eee_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_eee_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_eee_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_eee_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_eee_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_eee_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into eee_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_eee_3rd_subjects_code.get(),
                                                        self.var_eee_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_eee_3rd_subjects_marks.get(),
                                                        self.var_student_eee_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_eee_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_eee_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from eee_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_eee_3rd_treeview.delete(*tree_eee_3rd_treeview.get_children())
                            for row in rows:
                                tree_eee_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from eee_3rd_student_resultss where subjects=%s',(self.var_eee_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_eee_3rd_subjects where subjects=%s ',(self.var_eee_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_eee_3rd_data()
                                    fetch_eee_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update eee_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_eee_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_eee_3rd_subjects_marks.get(),
                                                    self.var_student_eee_3rd_usn.get(),
                                                    self.var_eee_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_eee_3rd_data()
                                fetch_eee_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_eee_3rd_data():
                        fetch_eee_3rd_data()
                        self.var_eee_3rd_subjects_code.set('')
                        self.var_eee_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_eee_3rd_usn.set('')
                        self.var_eee_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_eee_3rd_data(ev):
                        read=tree_eee_3rd_treeview.focus()
                        content=tree_eee_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_eee_3rd_subjects_code.set(row[0])
                        self.var_eee_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_eee_3rd_subjects_marks.set(row[5])
                        self.var_student_eee_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_eee_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_eee_3rd_subjects()
                    eee_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_eee_3rd_subjects,values=eee_3rd_subjects_list,state='readonly')
                    eee_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_eee_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_eee_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_eee_3rd_usn,values=eee_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_eee_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_eee_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_eee_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_eee_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_eee_3rd_treeview.heading('student_usn',text='USN')
                    

                    tree_eee_3rd_treeview.column('subject_code',width=200)
                    tree_eee_3rd_treeview.column('subjects',width=200)
                    tree_eee_3rd_treeview.column('semister',width=200)
                    tree_eee_3rd_treeview.column('scheme',width=200)
                    tree_eee_3rd_treeview.column('branch',width=200)
                    tree_eee_3rd_treeview.column('marks',width=200)
                    tree_eee_3rd_treeview.column('student_usn',width=200)

                    tree_eee_3rd_treeview['show']='headings'
                    
                    tree_eee_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_eee_3rd_data()
                    tree_eee_3rd_treeview.bind('<ButtonRelease-1>',get_eee_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                if self.var_scheme_select.get()=='2018':
                    eee_4th_student_usn_list=[]
                    def fetch_eee_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    eee_4th_subjects_list=[]
                    def fetch_eee_4th_subjects():
                        #all_eee_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select eee_4th_subjects from all_eee_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_eee_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_eee_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_eee_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_eee_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_eee_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into eee_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_eee_4th_subjects_code.get(),
                                                        self.var_eee_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_eee_4th_subjects_marks.get(),
                                                        self.var_student_eee_4th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_eee_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_eee_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from eee_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_eee_4th_treeview.delete(*tree_eee_4th_treeview.get_children())
                            for row in rows:
                                tree_eee_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from eee_4th_student_resultss where subjects=%s',(self.var_eee_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_eee_4th_subjects where subjects=%s ',(self.var_eee_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_eee_4th_data()
                                    fetch_eee_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update eee_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_eee_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_eee_4th_subjects_marks.get(),
                                                    self.var_student_eee_4th_usn.get(),
                                                    self.var_eee_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_eee_4th_data()
                                fetch_eee_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_eee_4th_data():
                        fetch_eee_4th_data()
                        self.var_eee_4th_subjects_code.set('')
                        self.var_eee_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_eee_4th_subjects_marks.set('')
                        self.var_student_eee_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_eee_4th_data(ev):
                        read=tree_eee_4th_treeview.focus()
                        content=tree_eee_4th_treeview.item(read)
                        rows=content['values']

                        self.var_eee_4th_subjects_code.set(row[0])
                        self.var_eee_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_eee_4th_subjects_marks.set(row[5])
                        self.var_student_eee_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_eee_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_eee_4th_subjects()
                    eee_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_eee_4th_subjects,values=eee_4th_subjects_list,state='readonly')
                    eee_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_eee_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_eee_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_eee_4th_usn,values=eee_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_eee_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_eee_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_eee_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_eee_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_eee_4th_treeview.heading('student_usn',text='USN')
                    

                    tree_eee_4th_treeview.column('subject_code',width=200)
                    tree_eee_4th_treeview.column('subjects',width=200)
                    tree_eee_4th_treeview.column('semister',width=200)
                    tree_eee_4th_treeview.column('scheme',width=200)
                    tree_eee_4th_treeview.column('branch',width=200)
                    tree_eee_4th_treeview.column('marks',width=200)
                    tree_eee_4th_treeview.column('student_usn',width=200)

                    tree_eee_4th_treeview['show']='headings'
                    
                    tree_eee_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_eee_4th_data()
                    tree_eee_4th_treeview.bind('<ButtonRelease-1>',get_eee_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                if self.var_scheme_select.get()=='2018':
                    eee_5th_student_usn_list=[]
                    def fetch_eee_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    eee_5th_subjects_list=[]
                    def fetch_eee_5th_subjects():
                        #all_eee_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select eee_5th_subjects from all_eee_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_eee_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_eee_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_eee_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_eee_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_eee_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into eee_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_eee_5th_subjects_code.get(),
                                                        self.var_eee_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_eee_5th_subjects_marks.get(),
                                                        self.var_student_eee_5th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_eee_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_eee_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from eee_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_eee_5th_treeview.delete(*tree_eee_5th_treeview.get_children())
                            for row in rows:
                                tree_eee_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from eee_5th_student_resultss where subjects=%s',(self.var_eee_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_eee_5th_subjects where subjects=%s ',(self.var_eee_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_eee_5th_data()
                                    fetch_eee_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update eee_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_eee_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_eee_5th_subjects_marks.get(),
                                                    self.var_student_eee_5th_usn.get(),
                                                    self.var_eee_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_eee_5th_data()
                                fetch_eee_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_eee_5th_data():
                        fetch_eee_5th_data()
                        self.var_eee_5th_subjects_code.set('')
                        self.var_eee_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_eee_5th_subjects_marks.set('')
                        self.var_student_eee_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_eee_5th_data(ev):
                        read=tree_eee_5th_treeview.focus()
                        content=tree_eee_5th_treeview.item(read)
                        rows=content['values']

                        self.var_eee_5th_subjects_code.set(row[0])
                        self.var_eee_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_eee_5th_subjects_marks.set(row[5])
                        self.var_student_eee_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_eee_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_eee_5th_subjects()
                    eee_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_eee_5th_subjects,values=eee_5th_subjects_list,state='readonly')
                    eee_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_eee_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_eee_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_eee_5th_usn,values=eee_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_eee_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_eee_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_eee_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_eee_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_eee_5th_treeview.heading('student_usn',text='USN')
                    

                    tree_eee_5th_treeview.column('subject_code',width=200)
                    tree_eee_5th_treeview.column('subjects',width=200)
                    tree_eee_5th_treeview.column('semister',width=200)
                    tree_eee_5th_treeview.column('scheme',width=200)
                    tree_eee_5th_treeview.column('branch',width=200)
                    tree_eee_5th_treeview.column('marks',width=200)
                    tree_eee_5th_treeview.column('student_usn',width=200)

                    tree_eee_5th_treeview['show']='headings'
                    
                    tree_eee_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_eee_5th_data()
                    tree_eee_5th_treeview.bind('<ButtonRelease-1>',get_eee_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                if self.var_scheme_select.get()=='2018':
                    eee_6th_student_usn_list=[]
                    def fetch_eee_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    eee_6th_subjects_list=[]
                    def fetch_eee_6th_subjects():
                        #all_eee_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select eee_6th_subjects from all_eee_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_eee_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_eee_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_eee_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_eee_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_eee_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into eee_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_eee_6th_subjects_code.get(),
                                                        self.var_eee_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_eee_6th_subjects_marks.get(),
                                                        self.var_student_eee_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_eee_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_eee_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from eee_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_eee_6th_treeview.delete(*tree_eee_6th_treeview.get_children())
                            for row in rows:
                                tree_eee_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from eee_6th_student_resultss where subjects=%s',(self.var_eee_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_eee_6th_subjects where subjects=%s ',(self.var_eee_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_eee_6th_data()
                                    fetch_eee_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update eee_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_eee_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_eee_6th_subjects_marks.get(),
                                                    self.var_student_eee_6th_usn.get(),
                                                    self.var_eee_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_eee_6th_data()
                                fetch_eee_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_eee_6th_data():
                        fetch_eee_6th_data()
                        self.var_eee_6th_subjects_code.set('')
                        self.var_eee_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_eee_6th_usn.set('')
                        self.var_eee_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_eee_6th_data(ev):
                        read=tree_eee_6th_treeview.focus()
                        content=tree_eee_6th_treeview.item(read)
                        rows=content['values']

                        self.var_eee_6th_subjects_code.set(row[0])
                        self.var_eee_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_eee_6th_subjects_marks.set(row[5])
                        self.var_student_eee_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_eee_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_eee_6th_subjects()
                    eee_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_eee_6th_subjects,values=eee_6th_subjects_list,state='readonly')
                    eee_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_eee_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_eee_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_eee_6th_usn,values=eee_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_eee_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_eee_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_eee_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_eee_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_eee_6th_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_eee_6th_treeview.column('subject_code',width=200)
                    tree_eee_6th_treeview.column('subjects',width=200)
                    tree_eee_6th_treeview.column('semister',width=200)
                    tree_eee_6th_treeview.column('scheme',width=200)
                    tree_eee_6th_treeview.column('branch',width=200)
                    tree_eee_6th_treeview.column('marks',width=200)
                    tree_eee_6th_treeview.column('student_usn',width=200)

                    tree_eee_6th_treeview['show']='headings'
                    
                    tree_eee_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_eee_6th_data()
                    tree_eee_6th_treeview.bind('<ButtonRelease-1>',get_eee_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                if self.var_scheme_select.get()=='2018':
                    eee_7th_student_usn_list=[]
                    def fetch_eee_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    eee_7th_subjects_list=[]
                    def fetch_eee_7th_subjects():
                        #all_eee_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select eee_7th_subjects from all_eee_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_eee_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_eee_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_eee_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_eee_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_eee_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into eee_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_eee_7th_subjects_code.get(),
                                                        self.var_eee_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_eee_7th_subjects_marks.get(),
                                                        self.var_student_eee_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_eee_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_eee_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from eee_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_eee_7th_treeview.delete(*tree_eee_7th_treeview.get_children())
                            for row in rows:
                                tree_eee_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from eee_7th_student_resultss where subjects=%s',(self.var_eee_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_eee_7th_subjects where subjects=%s ',(self.var_eee_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_eee_7th_data()
                                    fetch_eee_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update eee_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_eee_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_eee_7th_subjects_marks.get(),
                                                    self.var_student_eee_7th_usn.get(),
                                                    self.var_eee_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_eee_7th_data()
                                fetch_eee_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_eee_7th_data():
                        fetch_eee_7th_data()
                        self.var_eee_7th_subjects_code.set('')
                        self.var_eee_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_eee_7th_subjects_marks.set('')
                        self.var_student_eee_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_eee_7th_data(ev):
                        read=tree_eee_7th_treeview.focus()
                        content=tree_eee_7th_treeview.item(read)
                        rows=content['values']

                        self.var_eee_7th_subjects_code.set(row[0])
                        self.var_eee_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_eee_7th_subjects_marks.set(row[5])
                        self.var_student_eee_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_eee_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_eee_7th_subjects()
                    eee_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_eee_7th_subjects,values=eee_7th_subjects_list,state='readonly')
                    eee_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_eee_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_eee_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_eee_7th_usn,values=eee_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_eee_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_eee_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_eee_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_eee_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_eee_7th_treeview.heading('student_usn',text='USN')
                    

                 
                    tree_eee_7th_treeview.column('subject_code',width=200)
                    tree_eee_7th_treeview.column('subjects',width=200)
                    tree_eee_7th_treeview.column('semister',width=200)
                    tree_eee_7th_treeview.column('scheme',width=200)
                    tree_eee_7th_treeview.column('branch',width=200)
                    tree_eee_7th_treeview.column('marks',width=200)
                    tree_eee_7th_treeview.column('student_usn',width=200)

                    tree_eee_7th_treeview['show']='headings'
                    
                    tree_eee_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_eee_7th_data()
                    tree_eee_7th_treeview.bind('<ButtonRelease-1>',get_eee_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Electrical_And_Electronic_Engineering':
                if self.var_scheme_select.get()=='2018':
                    eee_8th_student_usn_list=[]
                    def fetch_eee_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    eee_8th_subjects_list=[]
                    def fetch_eee_8th_subjects():
                        #all_eee_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select eee_8th_subjects from all_eee_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    eee_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_eee_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_eee_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_eee_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_eee_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_eee_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into eee_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_eee_8th_subjects_code.get(),
                                                        self.var_eee_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_eee_8th_subjects_marks.get(),
                                                        self.var_student_eee_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_eee_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_eee_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from eee_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_eee_8th_treeview.delete(*tree_eee_8th_treeview.get_children())
                            for row in rows:
                                tree_eee_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from eee_8th_student_resultss where subjects=%s',(self.var_eee_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_eee_8th_subjects where subjects=%s ',(self.var_eee_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_eee_8th_data()
                                    fetch_eee_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_eee_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update eee_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_eee_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_eee_8th_subjects_marks.get(),
                                                    self.var_student_eee_8th_usn.get(),
                                                    self.var_eee_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_eee_8th_data()
                                fetch_eee_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_eee_8th_data():
                        fetch_eee_8th_data()
                        self.var_eee_8th_subjects_code.set('')
                        self.var_eee_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_eee_8th_subjects_marks.set('')
                        self.var_student_eee_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_eee_8th_data(ev):
                        read=tree_eee_8th_treeview.focus()
                        content=tree_eee_8th_treeview.item(read)
                        rows=content['values']

                        self.var_eee_8th_subjects_code.set(row[0])
                        self.var_eee_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_eee_8th_subjects_marks.set(row[5])
                        self.var_student_eee_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_eee_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_eee_8th_subjects()
                    eee_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_eee_8th_subjects,values=eee_8th_subjects_list,state='readonly')
                    eee_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_eee_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_eee_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_eee_8th_usn,values=eee_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_eee_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_eee_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_eee_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_eee_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_eee_8th_treeview.heading('student_usn',text='USN')
                    

                    tree_eee_8th_treeview.column('subject_code',width=200)
                    tree_eee_8th_treeview.column('subjects',width=200)
                    tree_eee_8th_treeview.column('semister',width=200)
                    tree_eee_8th_treeview.column('scheme',width=200)
                    tree_eee_8th_treeview.column('branch',width=200)
                    tree_eee_8th_treeview.column('marks',width=200)
                    tree_eee_8th_treeview.column('student_usn',width=200)

                    tree_eee_8th_treeview['show']='headings'
                    
                    tree_eee_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_eee_8th_data()
                    tree_eee_8th_treeview.bind('<ButtonRelease-1>',get_eee_8th_data)
    
    
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                if self.var_scheme_select.get()=='2018':
                    cs_3rd_student_usn_list=[]
                    def fetch_cs_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    cs_3rd_subjects_list=[]
                    def fetch_cs_3rd_subjects():
                        #all_cs_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select cs_3rd_subjects from all_cs_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_cs_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_cs_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_cs_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_cs_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_cs_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into cs_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_cs_3rd_subjects_code.get(),
                                                        self.var_cs_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_cs_3rd_subjects_marks.get(),
                                                        self.var_student_cs_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_cs_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_cs_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from cs_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_cs_3rd_treeview.delete(*tree_cs_3rd_treeview.get_children())
                            for row in rows:
                                tree_cs_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from cs_3rd_student_resultss where subjects=%s',(self.var_cs_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_cs_3rd_subjects where subjects=%s ',(self.var_cs_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_cs_3rd_data()
                                    fetch_cs_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update cs_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_cs_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_cs_3rd_subjects_marks.get(),
                                                    self.var_student_cs_3rd_usn.get(),
                                                    self.var_cs_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_cs_3rd_data()
                                fetch_cs_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_cs_3rd_data():
                        fetch_cs_3rd_data()
                        self.var_cs_3rd_subjects_code.set('')
                        self.var_cs_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_cs_3rd_usn.set('')
                        self.var_cs_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_cs_3rd_data(ev):
                        read=tree_cs_3rd_treeview.focus()
                        content=tree_cs_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_cs_3rd_subjects_code.set(row[0])
                        self.var_cs_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_cs_3rd_subjects_marks.set(row[5])
                        self.var_student_cs_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_cs_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_cs_3rd_subjects()
                    cs_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_cs_3rd_subjects,values=cs_3rd_subjects_list,state='readonly')
                    cs_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_cs_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_cs_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_cs_3rd_usn,values=cs_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_cs_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_cs_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_cs_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_cs_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_cs_3rd_treeview.heading('student_usn',text='USN')
                    

          
                    tree_cs_3rd_treeview.column('subject_code',width=200)
                    tree_cs_3rd_treeview.column('subjects',width=200)
                    tree_cs_3rd_treeview.column('semister',width=200)
                    tree_cs_3rd_treeview.column('scheme',width=200)
                    tree_cs_3rd_treeview.column('branch',width=200)
                    tree_cs_3rd_treeview.column('marks',width=200)
                    tree_cs_3rd_treeview.column('student_usn',width=200)

                    tree_cs_3rd_treeview['show']='headings'
                    
                    tree_cs_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_cs_3rd_data()
                    tree_cs_3rd_treeview.bind('<ButtonRelease-1>',get_cs_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                if self.var_scheme_select.get()=='2018':
                    cs_4th_student_usn_list=[]
                    def fetch_cs_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    cs_4th_subjects_list=[]
                    def fetch_cs_4th_subjects():
                        #all_cs_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select cs_4th_subjects from all_cs_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_cs_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_cs_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_cs_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_cs_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_cs_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into cs_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_cs_4th_subjects_code.get(),
                                                        self.var_cs_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_cs_4th_subjects_marks.get(),
                                                        self.var_student_cs_4th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_cs_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_cs_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from cs_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_cs_4th_treeview.delete(*tree_cs_4th_treeview.get_children())
                            for row in rows:
                                tree_cs_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from cs_4th_student_resultss where subjects=%s',(self.var_cs_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_cs_4th_subjects where subjects=%s ',(self.var_cs_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_cs_4th_data()
                                    fetch_cs_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update cs_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_cs_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_cs_4th_subjects_marks.get(),
                                                    self.var_student_cs_4th_usn.get(),
                                                    self.var_cs_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_cs_4th_data()
                                fetch_cs_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_cs_4th_data():
                        fetch_cs_4th_data()
                        self.var_cs_4th_subjects_code.set('')
                        self.var_cs_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_cs_4th_subjects_marks.set('')
                        self.var_student_cs_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_cs_4th_data(ev):
                        read=tree_cs_4th_treeview.focus()
                        content=tree_cs_4th_treeview.item(read)
                        rows=content['values']

                        self.var_cs_4th_subjects_code.set(row[0])
                        self.var_cs_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_cs_4th_subjects_marks.set(row[5])
                        self.var_student_cs_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_cs_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_cs_4th_subjects()
                    cs_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_cs_4th_subjects,values=cs_4th_subjects_list,state='readonly')
                    cs_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_cs_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_cs_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_cs_4th_usn,values=cs_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_cs_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_cs_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_cs_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_cs_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_cs_4th_treeview.heading('student_usn',text='USN')
                    

                    tree_cs_4th_treeview.column('subject_code',width=200)
                    tree_cs_4th_treeview.column('subjects',width=200)
                    tree_cs_4th_treeview.column('semister',width=200)
                    tree_cs_4th_treeview.column('scheme',width=200)
                    tree_cs_4th_treeview.column('branch',width=200)
                    tree_cs_4th_treeview.column('marks',width=200)
                    tree_cs_4th_treeview.column('student_usn',width=200)

                    tree_cs_4th_treeview['show']='headings'
                    
                    tree_cs_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_cs_4th_data()
                    tree_cs_4th_treeview.bind('<ButtonRelease-1>',get_cs_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                if self.var_scheme_select.get()=='2018':
                    cs_5th_student_usn_list=[]
                    def fetch_cs_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    cs_5th_subjects_list=[]
                    def fetch_cs_5th_subjects():
                        #all_cs_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select cs_5th_subjects from all_cs_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_cs_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_cs_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_cs_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_cs_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_cs_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into cs_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_cs_5th_subjects_code.get(),
                                                        self.var_cs_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_cs_5th_subjects_marks.get(),
                                                        self.var_student_cs_5th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_cs_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_cs_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from cs_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_cs_5th_treeview.delete(*tree_cs_5th_treeview.get_children())
                            for row in rows:
                                tree_cs_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from cs_5th_student_resultss where subjects=%s',(self.var_cs_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_cs_5th_subjects where subjects=%s ',(self.var_cs_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_cs_5th_data()
                                    fetch_cs_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update cs_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_cs_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_cs_5th_subjects_marks.get(),
                                                    self.var_student_cs_5th_usn.get(),
                                                    self.var_cs_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_cs_5th_data()
                                fetch_cs_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_cs_5th_data():
                        fetch_cs_5th_data()
                        self.var_cs_5th_subjects_code.set('')
                        self.var_cs_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_cs_5th_subjects_marks.set('')
                        self.var_student_cs_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_cs_5th_data(ev):
                        read=tree_cs_5th_treeview.focus()
                        content=tree_cs_5th_treeview.item(read)
                        rows=content['values']

                        self.var_cs_5th_subjects_code.set(row[0])
                        self.var_cs_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_cs_5th_subjects_marks.set(row[5])
                        self.var_student_cs_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_cs_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_cs_5th_subjects()
                    cs_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_cs_5th_subjects,values=cs_5th_subjects_list,state='readonly')
                    cs_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_cs_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_cs_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_cs_5th_usn,values=cs_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_cs_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_cs_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_cs_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_cs_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_cs_5th_treeview.heading('student_usn',text='USN')
                    

        
                    tree_cs_5th_treeview.column('subject_code',width=200)
                    tree_cs_5th_treeview.column('subjects',width=200)
                    tree_cs_5th_treeview.column('semister',width=200)
                    tree_cs_5th_treeview.column('scheme',width=200)
                    tree_cs_5th_treeview.column('branch',width=200)
                    tree_cs_5th_treeview.column('marks',width=200)
                    tree_cs_5th_treeview.column('student_usn',width=200)

                    tree_cs_5th_treeview['show']='headings'
                    
                    tree_cs_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_cs_5th_data()
                    tree_cs_5th_treeview.bind('<ButtonRelease-1>',get_cs_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                if self.var_scheme_select.get()=='2018':
                    cs_6th_student_usn_list=[]
                    def fetch_cs_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    cs_6th_subjects_list=[]
                    def fetch_cs_6th_subjects():
                        #all_cs_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select cs_6th_subjects from all_cs_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_cs_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_cs_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_cs_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_cs_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_cs_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into cs_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_cs_6th_subjects_code.get(),
                                                        self.var_cs_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_cs_6th_subjects_marks.get(),
                                                        self.var_student_cs_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_cs_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_cs_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from cs_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_cs_6th_treeview.delete(*tree_cs_6th_treeview.get_children())
                            for row in rows:
                                tree_cs_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from cs_6th_student_resultss where subjects=%s',(self.var_cs_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_cs_6th_subjects where subjects=%s ',(self.var_cs_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_cs_6th_data()
                                    fetch_cs_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update cs_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_cs_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_cs_6th_subjects_marks.get(),
                                                    self.var_student_cs_6th_usn.get(),
                                                    self.var_cs_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_cs_6th_data()
                                fetch_cs_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_cs_6th_data():
                        fetch_cs_6th_data()
                        self.var_cs_6th_subjects_code.set('')
                        self.var_cs_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_cs_6th_usn.set('')
                        self.var_cs_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_cs_6th_data(ev):
                        read=tree_cs_6th_treeview.focus()
                        content=tree_cs_6th_treeview.item(read)
                        rows=content['values']

                        self.var_cs_6th_subjects_code.set(row[0])
                        self.var_cs_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_cs_6th_subjects_marks.set(row[5])
                        self.var_student_cs_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_cs_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_cs_6th_subjects()
                    cs_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_cs_6th_subjects,values=cs_6th_subjects_list,state='readonly')
                    cs_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_cs_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_cs_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_cs_6th_usn,values=cs_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_cs_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_cs_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_cs_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_cs_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_cs_6th_treeview.heading('student_usn',text='USN')
                    

               
                    tree_cs_6th_treeview.column('subject_code',width=200)
                    tree_cs_6th_treeview.column('subjects',width=200)
                    tree_cs_6th_treeview.column('semister',width=200)
                    tree_cs_6th_treeview.column('scheme',width=200)
                    tree_cs_6th_treeview.column('branch',width=200)
                    tree_cs_6th_treeview.column('marks',width=200)
                    tree_cs_6th_treeview.column('student_usn',width=200)

                    tree_cs_6th_treeview['show']='headings'
                    
                    tree_cs_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_cs_6th_data()
                    tree_cs_6th_treeview.bind('<ButtonRelease-1>',get_cs_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                if self.var_scheme_select.get()=='2018':
                    cs_7th_student_usn_list=[]
                    def fetch_cs_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    cs_7th_subjects_list=[]
                    def fetch_cs_7th_subjects():
                        #all_cs_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select cs_7th_subjects from all_cs_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_cs_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_cs_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_cs_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_cs_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_cs_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into cs_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_cs_7th_subjects_code.get(),
                                                        self.var_cs_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_cs_7th_subjects_marks.get(),
                                                        self.var_student_cs_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_cs_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_cs_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from cs_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_cs_7th_treeview.delete(*tree_cs_7th_treeview.get_children())
                            for row in rows:
                                tree_cs_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from cs_7th_student_resultss where subjects=%s',(self.var_cs_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_cs_7th_subjects where subjects=%s ',(self.var_cs_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_cs_7th_data()
                                    fetch_cs_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update cs_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_cs_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_cs_7th_subjects_marks.get(),
                                                    self.var_student_cs_7th_usn.get(),
                                                    self.var_cs_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_cs_7th_data()
                                fetch_cs_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_cs_7th_data():
                        fetch_cs_7th_data()
                        self.var_cs_7th_subjects_code.set('')
                        self.var_cs_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_cs_7th_subjects_marks.set('')
                        self.var_student_cs_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_cs_7th_data(ev):
                        read=tree_cs_7th_treeview.focus()
                        content=tree_cs_7th_treeview.item(read)
                        rows=content['values']

                        self.var_cs_7th_subjects_code.set(row[0])
                        self.var_cs_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_cs_7th_subjects_marks.set(row[5])
                        self.var_student_cs_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_cs_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_cs_7th_subjects()
                    cs_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_cs_7th_subjects,values=cs_7th_subjects_list,state='readonly')
                    cs_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_cs_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_cs_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_cs_7th_usn,values=cs_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_cs_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_cs_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_cs_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_cs_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_cs_7th_treeview.heading('student_usn',text='USN')
                    

                
                    tree_cs_7th_treeview.column('subject_code',width=200)
                    tree_cs_7th_treeview.column('subjects',width=200)
                    tree_cs_7th_treeview.column('semister',width=200)
                    tree_cs_7th_treeview.column('scheme',width=200)
                    tree_cs_7th_treeview.column('branch',width=200)
                    tree_cs_7th_treeview.column('marks',width=200)
                    tree_cs_7th_treeview.column('student_usn',width=200)

                    tree_cs_7th_treeview['show']='headings'
                    
                    tree_cs_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_cs_7th_data()
                    tree_cs_7th_treeview.bind('<ButtonRelease-1>',get_cs_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Computer_Science_Engineering':
                if self.var_scheme_select.get()=='2018':
                    cs_8th_student_usn_list=[]
                    def fetch_cs_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    cs_8th_subjects_list=[]
                    def fetch_cs_8th_subjects():
                        #all_cs_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select cs_8th_subjects from all_cs_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    cs_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_cs_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_cs_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_cs_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_cs_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_cs_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into cs_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_cs_8th_subjects_code.get(),
                                                        self.var_cs_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_cs_8th_subjects_marks.get(),
                                                        self.var_student_cs_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_cs_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_cs_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from cs_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_cs_8th_treeview.delete(*tree_cs_8th_treeview.get_children())
                            for row in rows:
                                tree_cs_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from cs_8th_student_resultss where subjects=%s',(self.var_cs_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_cs_8th_subjects where subjects=%s ',(self.var_cs_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_cs_8th_data()
                                    fetch_cs_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_cs_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update cs_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_cs_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_cs_8th_subjects_marks.get(),
                                                    self.var_student_cs_8th_usn.get(),
                                                    self.var_cs_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_cs_8th_data()
                                fetch_cs_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_cs_8th_data():
                        fetch_cs_8th_data()
                        self.var_cs_8th_subjects_code.set('')
                        self.var_cs_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_cs_8th_subjects_marks.set('')
                        self.var_student_cs_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_cs_8th_data(ev):
                        read=tree_cs_8th_treeview.focus()
                        content=tree_cs_8th_treeview.item(read)
                        rows=content['values']

                        self.var_cs_8th_subjects_code.set(row[0])
                        self.var_cs_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_cs_8th_subjects_marks.set(row[5])
                        self.var_student_cs_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_cs_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_cs_8th_subjects()
                    cs_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_cs_8th_subjects,values=cs_8th_subjects_list,state='readonly')
                    cs_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_cs_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_cs_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_cs_8th_usn,values=cs_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_cs_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_cs_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_cs_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_cs_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_cs_8th_treeview.heading('student_usn',text='USN')
                    

               
                    tree_cs_8th_treeview.column('subject_code',width=200)
                    tree_cs_8th_treeview.column('subjects',width=200)
                    tree_cs_8th_treeview.column('semister',width=200)
                    tree_cs_8th_treeview.column('scheme',width=200)
                    tree_cs_8th_treeview.column('branch',width=200)
                    tree_cs_8th_treeview.column('marks',width=200)
                    tree_cs_8th_treeview.column('student_usn',width=200)

                    tree_cs_8th_treeview['show']='headings'
                    
                    tree_cs_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_cs_8th_data()
                    tree_cs_8th_treeview.bind('<ButtonRelease-1>',get_cs_8th_data)
    
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ise_3rd_student_usn_list=[]
                    def fetch_ise_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ise_3rd_subjects_list=[]
                    def fetch_ise_3rd_subjects():
                        #all_ise_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ise_3rd_subjects from all_ise_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ise_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ise_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ise_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ise_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ise_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ise_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ise_3rd_subjects_code.get(),
                                                        self.var_ise_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ise_3rd_subjects_marks.get(),
                                                        self.var_student_ise_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ise_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ise_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ise_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_ise_3rd_treeview.delete(*tree_ise_3rd_treeview.get_children())
                            for row in rows:
                                tree_ise_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ise_3rd_student_resultss where subjects=%s',(self.var_ise_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ise_3rd_subjects where subjects=%s ',(self.var_ise_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ise_3rd_data()
                                    fetch_ise_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ise_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ise_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ise_3rd_subjects_marks.get(),
                                                    self.var_student_ise_3rd_usn.get(),
                                                    self.var_ise_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ise_3rd_data()
                                fetch_ise_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ise_3rd_data():
                        fetch_ise_3rd_data()
                        self.var_ise_3rd_subjects_code.set('')
                        self.var_ise_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_ise_3rd_usn.set('')
                        self.var_ise_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ise_3rd_data(ev):
                        read=tree_ise_3rd_treeview.focus()
                        content=tree_ise_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_ise_3rd_subjects_code.set(row[0])
                        self.var_ise_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ise_3rd_subjects_marks.set(row[5])
                        self.var_student_ise_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ise_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_ise_3rd_subjects()
                    ise_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ise_3rd_subjects,values=ise_3rd_subjects_list,state='readonly')
                    ise_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ise_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ise_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ise_3rd_usn,values=ise_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ise_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ise_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ise_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ise_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

                    tree_frame1=Frame(label_frame3)
                    tree_frame1.pack(fill=BOTH,expand=1)

                    scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                    scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                    tree_ise_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_code','subjects','semister','scheme','branch','marks','student_usn'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                    scrollx.pack(side=BOTTOM,fill=X)
                    scrolly.pack(side=RIGHT,fill=Y)

                    scrollx.configure(command=tree_ise_3rd_treeview.xview)
                    scrolly.configure(command=tree_ise_3rd_treeview.yview)

                 
                    tree_ise_3rd_treeview.heading('subject_code',text="Subject Code")
                    tree_ise_3rd_treeview.heading('subjects',text="Subjects")
                    tree_ise_3rd_treeview.heading('semister',text="Semister")
                    tree_ise_3rd_treeview.heading('scheme',text="Scheme")
                    tree_ise_3rd_treeview.heading('branch',text="Branch")
                    tree_ise_3rd_treeview.heading('marks',text="Marks")
                    tree_ise_3rd_treeview.heading('student_usn',text='USN')
                    

                    
                    tree_ise_3rd_treeview.column('subject_code',width=200)
                    tree_ise_3rd_treeview.column('subjects',width=200)
                    tree_ise_3rd_treeview.column('semister',width=200)
                    tree_ise_3rd_treeview.column('scheme',width=200)
                    tree_ise_3rd_treeview.column('branch',width=200)
                    tree_ise_3rd_treeview.column('marks',width=200)
                    tree_ise_3rd_treeview.column('student_usn',width=200)

                    tree_ise_3rd_treeview['show']='headings'
                    
                    tree_ise_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_ise_3rd_data()
                    tree_ise_3rd_treeview.bind('<ButtonRelease-1>',get_ise_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ise_4th_student_usn_list=[]
                    def fetch_ise_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ise_4th_subjects_list=[]
                    def fetch_ise_4th_subjects():
                        #all_ise_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ise_4th_subjects from all_ise_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ise_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ise_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ise_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ise_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ise_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ise_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ise_4th_subjects_code.get(),
                                                        self.var_ise_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ise_4th_subjects_marks.get(),
                                                        self.var_student_ise_4th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ise_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ise_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ise_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_ise_4th_treeview.delete(*tree_ise_4th_treeview.get_children())
                            for row in rows:
                                tree_ise_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ise_4th_student_resultss where subjects=%s',(self.var_ise_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ise_4th_subjects where subjects=%s ',(self.var_ise_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ise_4th_data()
                                    fetch_ise_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ise_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ise_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ise_4th_subjects_marks.get(),
                                                    self.var_student_ise_4th_usn.get(),
                                                    self.var_ise_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ise_4th_data()
                                fetch_ise_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ise_4th_data():
                        fetch_ise_4th_data()
                        self.var_ise_4th_subjects_code.set('')
                        self.var_ise_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ise_4th_subjects_marks.set('')
                        self.var_student_ise_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ise_4th_data(ev):
                        read=tree_ise_4th_treeview.focus()
                        content=tree_ise_4th_treeview.item(read)
                        rows=content['values']

                        self.var_ise_4th_subjects_code.set(row[0])
                        self.var_ise_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ise_4th_subjects_marks.set(row[5])
                        self.var_student_ise_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ise_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_ise_4th_subjects()
                    ise_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ise_4th_subjects,values=ise_4th_subjects_list,state='readonly')
                    ise_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ise_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ise_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ise_4th_usn,values=ise_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ise_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ise_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ise_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ise_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ise_4th_treeview.heading('student_usn',text='USN')
                    

                    tree_ise_4th_treeview.column('subject_code',width=200)
                    tree_ise_4th_treeview.column('subjects',width=200)
                    tree_ise_4th_treeview.column('semister',width=200)
                    tree_ise_4th_treeview.column('scheme',width=200)
                    tree_ise_4th_treeview.column('branch',width=200)
                    tree_ise_4th_treeview.column('marks',width=200)
                    tree_ise_4th_treeview.column('student_usn',width=200)

                    tree_ise_4th_treeview['show']='headings'
                    
                    tree_ise_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ise_4th_data()
                    tree_ise_4th_treeview.bind('<ButtonRelease-1>',get_ise_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ise_5th_student_usn_list=[]
                    def fetch_ise_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ise_5th_subjects_list=[]
                    def fetch_ise_5th_subjects():
                        #all_ise_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ise_5th_subjects from all_ise_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ise_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ise_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ise_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ise_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ise_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ise_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ise_5th_subjects_code.get(),
                                                        self.var_ise_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ise_5th_subjects_marks.get(),
                                                        self.var_student_ise_5th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ise_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ise_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ise_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_ise_5th_treeview.delete(*tree_ise_5th_treeview.get_children())
                            for row in rows:
                                tree_ise_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ise_5th_student_resultss where subjects=%s',(self.var_ise_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ise_5th_subjects where subjects=%s ',(self.var_ise_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ise_5th_data()
                                    fetch_ise_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ise_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ise_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ise_5th_subjects_marks.get(),
                                                    self.var_student_ise_5th_usn.get(),
                                                    self.var_ise_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ise_5th_data()
                                fetch_ise_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ise_5th_data():
                        fetch_ise_5th_data()
                        self.var_ise_5th_subjects_code.set('')
                        self.var_ise_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ise_5th_subjects_marks.set('')
                        self.var_student_ise_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ise_5th_data(ev):
                        read=tree_ise_5th_treeview.focus()
                        content=tree_ise_5th_treeview.item(read)
                        rows=content['values']

                        self.var_ise_5th_subjects_code.set(row[0])
                        self.var_ise_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ise_5th_subjects_marks.set(row[5])
                        self.var_student_ise_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ise_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_ise_5th_subjects()
                    ise_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ise_5th_subjects,values=ise_5th_subjects_list,state='readonly')
                    ise_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ise_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ise_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ise_5th_usn,values=ise_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ise_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ise_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ise_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ise_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ise_5th_treeview.heading('student_usn',text='USN')
                    
                    tree_ise_5th_treeview.column('subject_code',width=200)
                    tree_ise_5th_treeview.column('subjects',width=200)
                    tree_ise_5th_treeview.column('semister',width=200)
                    tree_ise_5th_treeview.column('scheme',width=200)
                    tree_ise_5th_treeview.column('branch',width=200)
                    tree_ise_5th_treeview.column('marks',width=200)
                    tree_ise_5th_treeview.column('student_usn',width=200)

                    tree_ise_5th_treeview['show']='headings'
                    
                    tree_ise_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ise_5th_data()
                    tree_ise_5th_treeview.bind('<ButtonRelease-1>',get_ise_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ise_6th_student_usn_list=[]
                    def fetch_ise_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ise_6th_subjects_list=[]
                    def fetch_ise_6th_subjects():
                        #all_ise_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ise_6th_subjects from all_ise_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ise_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ise_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ise_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ise_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ise_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ise_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ise_6th_subjects_code.get(),
                                                        self.var_ise_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ise_6th_subjects_marks.get(),
                                                        self.var_student_ise_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ise_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ise_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ise_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_ise_6th_treeview.delete(*tree_ise_6th_treeview.get_children())
                            for row in rows:
                                tree_ise_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ise_6th_student_resultss where subjects=%s',(self.var_ise_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ise_6th_subjects where subjects=%s ',(self.var_ise_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ise_6th_data()
                                    fetch_ise_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ise_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ise_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ise_6th_subjects_marks.get(),
                                                    self.var_student_ise_6th_usn.get(),
                                                    self.var_ise_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ise_6th_data()
                                fetch_ise_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ise_6th_data():
                        fetch_ise_6th_data()
                        self.var_ise_6th_subjects_code.set('')
                        self.var_ise_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_ise_6th_usn.set('')
                        self.var_ise_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ise_6th_data(ev):
                        read=tree_ise_6th_treeview.focus()
                        content=tree_ise_6th_treeview.item(read)
                        rows=content['values']

                        self.var_ise_6th_subjects_code.set(row[0])
                        self.var_ise_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ise_6th_subjects_marks.set(row[5])
                        self.var_student_ise_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ise_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_ise_6th_subjects()
                    ise_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ise_6th_subjects,values=ise_6th_subjects_list,state='readonly')
                    ise_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ise_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ise_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ise_6th_usn,values=ise_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ise_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ise_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ise_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ise_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ise_6th_treeview.heading('student_usn',text='USN')
                    

                
                    tree_ise_6th_treeview.column('subject_code',width=200)
                    tree_ise_6th_treeview.column('subjects',width=200)
                    tree_ise_6th_treeview.column('semister',width=200)
                    tree_ise_6th_treeview.column('scheme',width=200)
                    tree_ise_6th_treeview.column('branch',width=200)
                    tree_ise_6th_treeview.column('marks',width=200)
                    tree_ise_6th_treeview.column('student_usn',width=200)

                    tree_ise_6th_treeview['show']='headings'
                    
                    tree_ise_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ise_6th_data()
                    tree_ise_6th_treeview.bind('<ButtonRelease-1>',get_ise_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ise_7th_student_usn_list=[]
                    def fetch_ise_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ise_7th_subjects_list=[]
                    def fetch_ise_7th_subjects():
                        #all_ise_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ise_7th_subjects from all_ise_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ise_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ise_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ise_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ise_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ise_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ise_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ise_7th_subjects_code.get(),
                                                        self.var_ise_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ise_7th_subjects_marks.get(),
                                                        self.var_student_ise_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ise_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ise_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ise_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_ise_7th_treeview.delete(*tree_ise_7th_treeview.get_children())
                            for row in rows:
                                tree_ise_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ise_7th_student_resultss where subjects=%s',(self.var_ise_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ise_7th_subjects where subjects=%s ',(self.var_ise_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ise_7th_data()
                                    fetch_ise_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ise_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ise_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ise_7th_subjects_marks.get(),
                                                    self.var_student_ise_7th_usn.get(),
                                                    self.var_ise_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ise_7th_data()
                                fetch_ise_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ise_7th_data():
                        fetch_ise_7th_data()
                        self.var_ise_7th_subjects_code.set('')
                        self.var_ise_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ise_7th_subjects_marks.set('')
                        self.var_student_ise_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ise_7th_data(ev):
                        read=tree_ise_7th_treeview.focus()
                        content=tree_ise_7th_treeview.item(read)
                        rows=content['values']

                        self.var_ise_7th_subjects_code.set(row[0])
                        self.var_ise_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ise_7th_subjects_marks.set(row[5])
                        self.var_student_ise_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ise_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_ise_7th_subjects()
                    ise_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ise_7th_subjects,values=ise_7th_subjects_list,state='readonly')
                    ise_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ise_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ise_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ise_7th_usn,values=ise_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ise_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ise_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ise_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ise_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ise_7th_treeview.heading('student_usn',text='USN')
                    

                   
                    tree_ise_7th_treeview.column('subject_code',width=200)
                    tree_ise_7th_treeview.column('subjects',width=200)
                    tree_ise_7th_treeview.column('semister',width=200)
                    tree_ise_7th_treeview.column('scheme',width=200)
                    tree_ise_7th_treeview.column('branch',width=200)
                    tree_ise_7th_treeview.column('marks',width=200)
                    tree_ise_7th_treeview.column('student_usn',width=200)

                    tree_ise_7th_treeview['show']='headings'
                    
                    tree_ise_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ise_7th_data()
                    tree_ise_7th_treeview.bind('<ButtonRelease-1>',get_ise_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Information_Science_and_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ise_8th_student_usn_list=[]
                    def fetch_ise_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ise_8th_subjects_list=[]
                    def fetch_ise_8th_subjects():
                        #all_ise_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ise_8th_subjects from all_ise_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ise_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ise_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ise_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ise_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ise_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ise_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ise_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ise_8th_subjects_code.get(),
                                                        self.var_ise_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ise_8th_subjects_marks.get(),
                                                        self.var_student_ise_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ise_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ise_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ise_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_ise_8th_treeview.delete(*tree_ise_8th_treeview.get_children())
                            for row in rows:
                                tree_ise_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ise_8th_student_resultss where subjects=%s',(self.var_ise_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ise_8th_subjects where subjects=%s ',(self.var_ise_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ise_8th_data()
                                    fetch_ise_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ise_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ise_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ise_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ise_8th_subjects_marks.get(),
                                                    self.var_student_ise_8th_usn.get(),
                                                    self.var_ise_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ise_8th_data()
                                fetch_ise_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ise_8th_data():
                        fetch_ise_8th_data()
                        self.var_ise_8th_subjects_code.set('')
                        self.var_ise_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ise_8th_subjects_marks.set('')
                        self.var_student_ise_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ise_8th_data(ev):
                        read=tree_ise_8th_treeview.focus()
                        content=tree_ise_8th_treeview.item(read)
                        rows=content['values']

                        self.var_ise_8th_subjects_code.set(row[0])
                        self.var_ise_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ise_8th_subjects_marks.set(row[5])
                        self.var_student_ise_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ise_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_ise_8th_subjects()
                    ise_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ise_8th_subjects,values=ise_8th_subjects_list,state='readonly')
                    ise_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ise_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ise_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ise_8th_usn,values=ise_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ise_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ise_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ise_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ise_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ise_8th_treeview.heading('student_usn',text='USN')
                    

               
                    tree_ise_8th_treeview.column('subject_code',width=200)
                    tree_ise_8th_treeview.column('subjects',width=200)
                    tree_ise_8th_treeview.column('semister',width=200)
                    tree_ise_8th_treeview.column('scheme',width=200)
                    tree_ise_8th_treeview.column('branch',width=200)
                    tree_ise_8th_treeview.column('marks',width=200)
                    tree_ise_8th_treeview.column('student_usn',width=200)

                    tree_ise_8th_treeview['show']='headings'
                    
                    tree_ise_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ise_8th_data()
                    tree_ise_8th_treeview.bind('<ButtonRelease-1>',get_ise_8th_data)
    
        if self.var_sem_select.get()=='3rd_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ete_3rd_student_usn_list=[]
                    def fetch_ete_3rd_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_3rd_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ete_3rd_subjects_list=[]
                    def fetch_ete_3rd_subjects():
                        #all_ete_3rd_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ete_3rd_subjects from all_ete_3rd_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_3rd_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ete_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ete_3rd_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ete_3rd_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ete_3rd_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ete_3rd_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be reuired',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ete_3rd_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ete_3rd_subjects_code.get(),
                                                        self.var_ete_3rd_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ete_3rd_subjects_marks.get(),
                                                        self.var_student_ete_3rd_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ete_3rd_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ete_3rd_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ete_3rd_student_resultss')
                            rows=cur.fetchall()
                            tree_ete_3rd_treeview.delete(*tree_ete_3rd_treeview.get_children())
                            for row in rows:
                                tree_ete_3rd_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ete_3rd_student_resultss where subjects=%s',(self.var_ete_3rd_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ete_3rd_subjects where subjects=%s ',(self.var_ete_3rd_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ete_3rd_data()
                                    fetch_ete_3rd_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_3rd_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ete_3rd_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ete_3rd_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ete_3rd_subjects_marks.get(),
                                                    self.var_student_ete_3rd_usn.get(),
                                                    self.var_ete_3rd_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ete_3rd_data()
                                fetch_ete_3rd_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ete_3rd_data():
                        fetch_ete_3rd_data()
                        self.var_ete_3rd_subjects_code.set('')
                        self.var_ete_3rd_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_ete_3rd_usn.set('')
                        self.var_ete_3rd_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ete_3rd_data(ev):
                        read=tree_ete_3rd_treeview.focus()
                        content=tree_ete_3rd_treeview.item(read)
                        rows=content['values']

                        self.var_ete_3rd_subjects_code.set(row[0])
                        self.var_ete_3rd_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ete_3rd_subjects_marks.set(row[5])
                        self.var_student_ete_3rd_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ete_3rd_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT31',
                        '18CV32',
                        '18CV33',
                        '18CV34',
                        '18CV35',
                        '18CV36',
                        '18CVL37',
                        '18CVL38',
                        '18KVK39',
                        '18KAK39',
                        '18CPC39',
                        '18MATDIP31'
                    )
                    fetch_ete_3rd_subjects()
                    ete_3rd_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ete_3rd_subjects,values=ete_3rd_subjects_list,state='readonly')
                    ete_3rd_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ete_3rd_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ete_3rd_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ete_3rd_usn,values=ete_3rd_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ete_3rd_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ete_3rd_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ete_3rd_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ete_3rd_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ete_3rd_treeview.heading('student_usn',text='USN')
                    

                   
                    tree_ete_3rd_treeview.column('subject_code',width=200)
                    tree_ete_3rd_treeview.column('subjects',width=200)
                    tree_ete_3rd_treeview.column('semister',width=200)
                    tree_ete_3rd_treeview.column('scheme',width=200)
                    tree_ete_3rd_treeview.column('branch',width=200)
                    tree_ete_3rd_treeview.column('marks',width=200)
                    tree_ete_3rd_treeview.column('student_usn',width=200)

                    tree_ete_3rd_treeview['show']='headings'
                    
                    tree_ete_3rd_treeview.pack(fill=BOTH,expand=1)
                    fetch_ete_3rd_data()
                    tree_ete_3rd_treeview.bind('<ButtonRelease-1>',get_ete_3rd_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='4th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ete_4th_student_usn_list=[]
                    def fetch_ete_4th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_4th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ete_4th_subjects_list=[]
                    def fetch_ete_4th_subjects():
                        #all_ete_4th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ete_4th_subjects from all_ete_4th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_4th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ete_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ete_4th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ete_4th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ete_4th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ete_4th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ete_4th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ete_4th_subjects_code.get(),
                                                        self.var_ete_4th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ete_4th_subjects_marks.get(),
                                                        self.var_student_ete_4th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ete_4th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ete_4th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ete_4th_student_resultss')
                            rows=cur.fetchall()
                            tree_ete_4th_treeview.delete(*tree_ete_4th_treeview.get_children())
                            for row in rows:
                                tree_ete_4th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ete_4th_student_resultss where subjects=%s',(self.var_ete_4th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ete_4th_subjects where subjects=%s ',(self.var_ete_4th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ete_4th_data()
                                    fetch_ete_4th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_4th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ete_4th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ete_4th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ete_4th_subjects_marks.get(),
                                                    self.var_student_ete_4th_usn.get(),
                                                    self.var_ete_4th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ete_4th_data()
                                fetch_ete_4th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ete_4th_data():
                        fetch_ete_4th_data()
                        self.var_ete_4th_subjects_code.set('')
                        self.var_ete_4th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ete_4th_subjects_marks.set('')
                        self.var_student_ete_4th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ete_4th_data(ev):
                        read=tree_ete_4th_treeview.focus()
                        content=tree_ete_4th_treeview.item(read)
                        rows=content['values']

                        self.var_ete_4th_subjects_code.set(row[0])
                        self.var_ete_4th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ete_4th_subjects_marks.set(row[5])
                        self.var_student_ete_4th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ete_4th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18MAT41',
                        '18CV42',
                        '18CV43',
                        '18CV44',
                        '18CV45',
                        '18CV46',
                        '18CVL47',
                        '18CVL48',
                        '18KVK49',
                        '18KAK49',
                        '18CPC49',
                        '18MATDIP41'
                    )
                    fetch_ete_4th_subjects()
                    ete_4th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ete_4th_subjects,values=ete_4th_subjects_list,state='readonly')
                    ete_4th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ete_4th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ete_4th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ete_4th_usn,values=ete_4th_student_usn_list)
                    enter_usn.place(x=300,y=0)
                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ete_4th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ete_4th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ete_4th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ete_4th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ete_4th_treeview.heading('student_usn',text='USN')
                    

                    tree_ete_4th_treeview.column('subject_code',width=200)
                    tree_ete_4th_treeview.column('subjects',width=200)
                    tree_ete_4th_treeview.column('semister',width=200)
                    tree_ete_4th_treeview.column('scheme',width=200)
                    tree_ete_4th_treeview.column('branch',width=200)
                    tree_ete_4th_treeview.column('marks',width=200)
                    tree_ete_4th_treeview.column('student_usn',width=200)

                    tree_ete_4th_treeview['show']='headings'
                    
                    tree_ete_4th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ete_4th_data()
                    tree_ete_4th_treeview.bind('<ButtonRelease-1>',get_ete_4th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='5th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ete_5th_student_usn_list=[]
                    def fetch_ete_5th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_5th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ete_5th_subjects_list=[]
                    def fetch_ete_5th_subjects():
                        #all_ete_5th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ete_5th_subjects from all_ete_5th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_5th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ete_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ete_5th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ete_5th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ete_5th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ete_5th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ete_5th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ete_5th_subjects_code.get(),
                                                        self.var_ete_5th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ete_5th_subjects_marks.get(),
                                                        self.var_student_ete_5th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ete_5th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ete_5th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ete_5th_student_resultss')
                            rows=cur.fetchall()
                            tree_ete_5th_treeview.delete(*tree_ete_5th_treeview.get_children())
                            for row in rows:
                                tree_ete_5th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ete_5th_student_resultss where subjects=%s',(self.var_ete_5th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ete_5th_subjects where subjects=%s ',(self.var_ete_5th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ete_5th_data()
                                    fetch_ete_5th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_5th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ete_5th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ete_5th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ete_5th_subjects_marks.get(),
                                                    self.var_student_ete_5th_usn.get(),
                                                    self.var_ete_5th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ete_5th_data()
                                fetch_ete_5th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ete_5th_data():
                        fetch_ete_5th_data()
                        self.var_ete_5th_subjects_code.set('')
                        self.var_ete_5th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ete_5th_subjects_marks.set('')
                        self.var_student_ete_5th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ete_5th_data(ev):
                        read=tree_ete_5th_treeview.focus()
                        content=tree_ete_5th_treeview.item(read)
                        rows=content['values']

                        self.var_ete_5th_subjects_code.set(row[0])
                        self.var_ete_5th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ete_5th_subjects_marks.set(row[5])
                        self.var_student_ete_5th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ete_5th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV51',
                        '18CV52',
                        '18CV53',
                        '18CV54',
                        '18CV55',
                        '18CV56',
                        '18CVL57',
                        '18CVL58',
                        '18CIV59'
                      
                    )
                    fetch_ete_5th_subjects()
                    ete_5th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ete_5th_subjects,values=ete_5th_subjects_list,state='readonly')
                    ete_5th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ete_5th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ete_5th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ete_5th_usn,values=ete_5th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ete_5th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ete_5th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ete_5th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ete_5th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ete_5th_treeview.heading('student_usn',text='USN')
                    

            
                    tree_ete_5th_treeview.column('subject_code',width=200)
                    tree_ete_5th_treeview.column('subjects',width=200)
                    tree_ete_5th_treeview.column('semister',width=200)
                    tree_ete_5th_treeview.column('scheme',width=200)
                    tree_ete_5th_treeview.column('branch',width=200)
                    tree_ete_5th_treeview.column('marks',width=200)
                    tree_ete_5th_treeview.column('student_usn',width=200)

                    tree_ete_5th_treeview['show']='headings'
                    
                    tree_ete_5th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ete_5th_data()
                    tree_ete_5th_treeview.bind('<ButtonRelease-1>',get_ete_5th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='6th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ete_6th_student_usn_list=[]
                    def fetch_ete_6th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_6th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ete_6th_subjects_list=[]
                    def fetch_ete_6th_subjects():
                        #all_ete_6th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ete_6th_subjects from all_ete_6th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_6th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ete_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ete_6th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ete_6th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ete_6th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ete_6th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ete_6th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ete_6th_subjects_code.get(),
                                                        self.var_ete_6th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ete_6th_subjects_marks.get(),
                                                        self.var_student_ete_6th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ete_6th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ete_6th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ete_6th_student_resultss')
                            rows=cur.fetchall()
                            tree_ete_6th_treeview.delete(*tree_ete_6th_treeview.get_children())
                            for row in rows:
                                tree_ete_6th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ete_6th_student_resultss where subjects=%s',(self.var_ete_6th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ete_6th_subjects where subjects=%s ',(self.var_ete_6th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ete_6th_data()
                                    fetch_ete_6th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_6th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ete_6th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ete_6th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ete_6th_subjects_marks.get(),
                                                    self.var_student_ete_6th_usn.get(),
                                                    self.var_ete_6th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ete_6th_data()
                                fetch_ete_6th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ete_6th_data():
                        fetch_ete_6th_data()
                        self.var_ete_6th_subjects_code.set('')
                        self.var_ete_6th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_student_ete_6th_usn.set('')
                        self.var_ete_6th_subjects_marks.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ete_6th_data(ev):
                        read=tree_ete_6th_treeview.focus()
                        content=tree_ete_6th_treeview.item(read)
                        rows=content['values']

                        self.var_ete_6th_subjects_code.set(row[0])
                        self.var_ete_6th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ete_6th_subjects_marks.set(row[5])
                        self.var_student_ete_6th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ete_6th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV61',
                        '18CV62',
                        '18CV63',
                        '18CV64',
                        '18CV65',
                        '18CV66',
                        '18CVL67',
                        '18CVL68',
                        '18CV641',
                        '18CV642',
                        '18CV643 ',
                        '18CV644',
                        '18CV644',
                        '18CV651',
                        '18CV651',
                        '18CV653',
                        '18CV654',
                        '18CV655',
                        '18CV656'
                        
                    )
                    fetch_ete_6th_subjects()
                    ete_6th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ete_6th_subjects,values=ete_6th_subjects_list,state='readonly')
                    ete_6th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ete_6th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ete_6th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ete_6th_usn,values=ete_6th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ete_6th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ete_6th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ete_6th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ete_6th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ete_6th_treeview.heading('student_usn',text='USN')
                    

      
                    tree_ete_6th_treeview.column('subject_code',width=200)
                    tree_ete_6th_treeview.column('subjects',width=200)
                    tree_ete_6th_treeview.column('semister',width=200)
                    tree_ete_6th_treeview.column('scheme',width=200)
                    tree_ete_6th_treeview.column('branch',width=200)
                    tree_ete_6th_treeview.column('marks',width=200)
                    tree_ete_6th_treeview.column('student_usn',width=200)

                    tree_ete_6th_treeview['show']='headings'
                    
                    tree_ete_6th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ete_6th_data()
                    tree_ete_6th_treeview.bind('<ButtonRelease-1>',get_ete_6th_data)

                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='7th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ete_7th_student_usn_list=[]
                    def fetch_ete_7th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_7th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ete_7th_subjects_list=[]
                    def fetch_ete_7th_subjects():
                        #all_ete_7th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ete_7th_subjects from all_ete_7th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_7th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ete_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ete_7th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ete_7th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ete_7th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ete_7th_usn.get()=='':
                                                        messagebox.showerror('Error','the student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ete_7th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ete_7th_subjects_code.get(),
                                                        self.var_ete_7th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ete_7th_subjects_marks.get(),
                                                        self.var_student_ete_7th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ete_7th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ete_7th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ete_7th_student_resultss')
                            rows=cur.fetchall()
                            tree_ete_7th_treeview.delete(*tree_ete_7th_treeview.get_children())
                            for row in rows:
                                tree_ete_7th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ete_7th_student_resultss where subjects=%s',(self.var_ete_7th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ete_7th_subjects where subjects=%s ',(self.var_ete_7th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ete_7th_data()
                                    fetch_ete_7th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_7th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ete_7th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ete_7th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ete_7th_subjects_marks.get(),
                                                    self.var_student_ete_7th_usn.get(),
                                                    self.var_ete_7th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ete_7th_data()
                                fetch_ete_7th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ete_7th_data():
                        fetch_ete_7th_data()
                        self.var_ete_7th_subjects_code.set('')
                        self.var_ete_7th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ete_7th_subjects_marks.set('')
                        self.var_student_ete_7th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ete_7th_data(ev):
                        read=tree_ete_7th_treeview.focus()
                        content=tree_ete_7th_treeview.item(read)
                        rows=content['values']

                        self.var_ete_7th_subjects_code.set(row[0])
                        self.var_ete_7th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ete_7th_subjects_marks.set(row[5])
                        self.var_student_ete_7th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ete_7th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV71',
                        '18CV72',
                        '18CV73',
                        '18CV74',
                        '18CV75',
                        '18CV76',
                        '18CV737',
                        '18CVL78',
                        '18CV731',
                        '18CV731',
                        '18CV732',
                        '18CV733',
                        '18CV734',
                        '18CV735',
                        '18CV741',
                        '18CV742',
                        '18CV743',
                        '18CV744',
                        '18CV745',
                        '18CV751',
                        '18CV752',
                        '18CV753'
                    )
                    fetch_ete_7th_subjects()
                    ete_7th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ete_7th_subjects,values=ete_7th_subjects_list,state='readonly')
                    ete_7th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ete_7th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ete_7th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ete_7th_usn,values=ete_7th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ete_7th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ete_7th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ete_7th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ete_7th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ete_7th_treeview.heading('student_usn',text='USN')
                    

                 
                    tree_ete_7th_treeview.column('subject_code',width=200)
                    tree_ete_7th_treeview.column('subjects',width=200)
                    tree_ete_7th_treeview.column('semister',width=200)
                    tree_ete_7th_treeview.column('scheme',width=200)
                    tree_ete_7th_treeview.column('branch',width=200)
                    tree_ete_7th_treeview.column('marks',width=200)
                    tree_ete_7th_treeview.column('student_usn',width=200)

                    tree_ete_7th_treeview['show']='headings'
                    
                    tree_ete_7th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ete_7th_data()
                    tree_ete_7th_treeview.bind('<ButtonRelease-1>',get_ete_7th_data)
                     #####################################################################################################################################
                    #########################################################################################################################################
                    ############################################################################################################################################
                    ##########################################################################################################################################
        if self.var_sem_select.get()=='8th_Semister':
            if self.var_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                if self.var_scheme_select.get()=='2018':
                    ete_8th_student_usn_list=[]
                    def fetch_ete_8th_student_usn():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select roll_number from StudentDetailsdatabase ')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_8th_student_usn_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    ete_8th_subjects_list=[]
                    def fetch_ete_8th_subjects():
                        #all_ete_8th_subjects
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select ete_8th_subjects from all_ete_8th_subjects')
                            rows=cur.fetchall()
                            if len(rows)>0:
                                for row in rows:
                                    ete_8th_subjects_list.append(row[0])
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                    def add_ete_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            if self.var_ete_8th_subjects_code.get()=='':
                                messagebox.showerror('Error','The  subjects code must be requered.',parent=main_frame)
                            else:
                                if self.var_ete_8th_subjects.get()=='':
                                    messagebox.showerror('Error','The subjects name must be required',parent=main_frame)
                                else:
                                    if self.var_sem_select.get()=='':
                                        messagebox.showerror('Error','The you tube video link  must be required',parent=main_frame)
                                    else:
                                        if self.var_scheme_select.get()=='':
                                            messagebox.showerror('Error','The scheme must be required',parent=main_frame)
                                        else:
                                            if self.var_branch_select.get()=='':
                                                messagebox.showerror('Error','The Branch must be required',parent=main_frame)
                                            else:
                                                if self.var_ete_8th_subjects_marks.get()=='':
                                                    messagebox.showerror('Error','The subjects must be required',parent=main_frame)
                                                else:
                                                    if self.var_student_ete_8th_usn.get()=='':
                                                        messagebox.showerror('Error','The student usn must be required',parent=main_frame)
                                                    else:
                                                        #'subject_code','subjects','semister','scheme','branch'
                                                        cur.execute('insert into ete_8th_student_resultss(subject_code,subjects,semister,scheme,branch,marks,student_usn) values(%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_ete_8th_subjects_code.get(),
                                                        self.var_ete_8th_subjects.get(),
                                                        self.var_sem_select.get(),
                                                        self.var_scheme_select.get(),
                                                        self.var_branch_select.get(),
                                                        
                                                        self.var_ete_8th_subjects_marks.get(),
                                                        self.var_student_ete_8th_usn.get()
                                                        ))
                                                        con.commit()
                                                        messagebox.showinfo('info','The data add succssfuly....',parent=main_frame)
                                                        fetch_ete_8th_data()
                                                        con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

                    def fetch_ete_8th_data():
                        con=psycopg2.connect(
                        host="ec2-23-21-4-7.compute-1.amazonaws.com",
                        database="d3cgb3tsbur7dj",
                        user="huzavcwsvfccit",
                        password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                        port="5432",
                        )
                        cur=con.cursor()
                        try:
                            cur.execute('select * from ete_8th_student_resultss')
                            rows=cur.fetchall()
                            tree_ete_8th_treeview.delete(*tree_ete_8th_treeview.get_children())
                            for row in rows:
                                tree_ete_8th_treeview.insert('',END,values=row)

                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:
                                cur.execute('select * from ete_8th_student_resultss where subjects=%s',(self.var_ete_8th_subjects.get(),))
                                row=cur.fetchone()
                                if row==None:
                                    messagebox.showerror('Error','Select the subjects name from the table',parennt=main_frame)
                                else:
                                    option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=main_frame)
                                    if option==True:
                                        cur.execute('delete from var_ete_8th_subjects where subjects=%s ',(self.var_ete_8th_subjects.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','the data is deleted successflly....',parent=main_frame)
                                    clear_ete_8th_data()
                                    fetch_ete_8th_data()
                                    con.close()
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)

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
                            if self.var_ete_8th_subjects.get()=='':
                                messagebox.showerror('Error','The subjects name must be reuired',parent=main_frame)
                            else:#'subject_code','subjects','semister','scheme','branch'
                                cur.execute('update ete_8th_student_resultss set subject_code=%s,semister=%s,scheme=%s,branch=%s,marks=%s,student_usn=%s where subjects=%s',(
                                                    self.var_ete_8th_subjects_code.get(),
                                                    self.var_sem_select.get(),
                                                    self.var_scheme_select.get(),
                                                    self.var_branch_select.get(),
                                                    self.var_ete_8th_subjects_marks.get(),
                                                    self.var_student_ete_8th_usn.get(),
                                                    self.var_ete_8th_subjects.get()
                                ))
                                con.commit()
                                messagebox.showinfo('Info','The data updated succssflly....',parent=main_frame)
                                clear_ete_8th_data()
                                fetch_ete_8th_data()
                                con.close()
                                        
                        except Exception as ex:
                            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=main_frame)
                        
                    def clear_ete_8th_data():
                        fetch_ete_8th_data()
                        self.var_ete_8th_subjects_code.set('')
                        self.var_ete_8th_subjects.set('')
                        self.var_sem_select.set('')
                        self.var_scheme_select.set('')
                        self.var_branch_select.set('')
                        self.var_ete_8th_subjects_marks.set('')
                        self.var_student_ete_8th_usn.set('')
                        messagebox.showinfo('Info','The data clear is succssfuly.....',parent=main_frame)

                    def get_ete_8th_data(ev):
                        read=tree_ete_8th_treeview.focus()
                        content=tree_ete_8th_treeview.item(read)
                        rows=content['values']

                        self.var_ete_8th_subjects_code.set(row[0])
                        self.var_ete_8th_subjects.set(row[1])
                        self.var_sem_select.set(row[2])
                        self.var_scheme_select.set(row[3])
                        self.var_branch_select.set(row[4])
                        self.var_ete_8th_subjects_marks.set(row[5])
                        self.var_student_ete_8th_usn.set(row[6])
                        messagebox.showinfo('Info','The data get is succssfuly.....',parent=main_frame)                    
                    
                    main_frame=Frame(self.root,bg='white')
                    main_frame.place(x=0,y=100,width=1055,height=330)   
                    label_frame=Label(main_frame,text='Subject Code                  Subjects                              Sem                          Scheme                            	Branch                                  Marks Obotened              ',font=('times new roman',11,'bold'),bg='#E8DAEF',relief=RIDGE,bd=1)
                    label_frame.place(x=10,y=30,width=1035,height=30)
                    subjects_code=ttk.Combobox(main_frame,textvariable=self.var_ete_8th_subjects_code,width=25,state='readonly')
                    subjects_code.place(x=10,y=61,height=20)
                    subjects_code['values']=(
                        '18CV81 ',
                        '18CV82',
                        '18CP83',
                        '18CVS84',
                        '18CVI85',
                        '18CV821',
                        '18CV822',
                        '18CV823',
                        '18CV824',
                        '18CV825'
                        
                    )
                    fetch_ete_8th_subjects()
                    ete_8th_subjects_entry=ttk.Combobox(main_frame,width=25,textvariable=self.var_ete_8th_subjects,values=ete_8th_subjects_list,state='readonly')
                    ete_8th_subjects_entry.place(x=185,y=61)

                    semister_select=ttk.Entry(main_frame,width=21,textvariable=self.var_sem_select,state='readonly')
                    semister_select.place(x=360,y=61)
                    
                    scheme_select=ttk.Entry(main_frame,width=26,textvariable=self.var_scheme_select,state='readonly')
                    scheme_select.place(x=495,y=61)

                    branch_select=ttk.Entry(main_frame,width=29,textvariable=self.var_branch_select,state='readonly')
                    branch_select.place(x=660,y=61)

                    subjects_marks_entry=ttk.Entry(main_frame,width=33,textvariable=self.var_ete_8th_subjects_marks)
                    subjects_marks_entry.place(x=843,y=61)
                    fetch_ete_8th_student_usn()
                    enter_usn=ttk.Combobox(main_frame,textvariable=self.var_student_ete_8th_usn,values=ete_8th_student_usn_list)
                    enter_usn.place(x=300,y=0)

                    button2=ttk.Button(main_frame,text='Add to Data Base',width=20,command=add_ete_8th_data).place(x=600,y=0)
                    button3=ttk.Button(main_frame,text='Update',width=15,command=update_ete_8th_data).place(x=730,y=0)
                    button4=ttk.Button(main_frame,text='Delete',width=15,command=delete_ete_8th_data).place(x=830,y=0)
                    button4=ttk.Button(main_frame,text='Clear',width=15,command=clear_ete_8th_data).place(x=930,y=0)
                    

                    label_frame3=LabelFrame(main_frame)
                    label_frame3.place(x=10,y=85,width=1040,height=240)

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
                    tree_ete_8th_treeview.heading('student_usn',text='USN')
                    

                    tree_ete_8th_treeview.column('subject_code',width=200)
                    tree_ete_8th_treeview.column('subjects',width=200)
                    tree_ete_8th_treeview.column('semister',width=200)
                    tree_ete_8th_treeview.column('scheme',width=200)
                    tree_ete_8th_treeview.column('branch',width=200)
                    tree_ete_8th_treeview.column('marks',width=200)
                    tree_ete_8th_treeview.column('student_usn',width=200)

                    tree_ete_8th_treeview['show']='headings'
                    
                    tree_ete_8th_treeview.pack(fill=BOTH,expand=1)
                    fetch_ete_8th_data()
                    tree_ete_8th_treeview.bind('<ButtonRelease-1>',get_ete_8th_data)
         
if __name__=='__main__':
    root=tk.Tk()
    ob1=AddStudentResult(root)
    root.mainloop()