import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
import psycopg2

class AddFaculty():
    def __init__(self,root):
        self.root=root
        self.root.title(' Add Faculty')
        self.root.geometry('1055x440+213+145')
        self.root.config(bg='white')
        
        #######################################
        self.var_sem_select=StringVar()
        self.var_branch_select=StringVar()
        self.var_faculty_select=StringVar()
        self.var_faculty_select=StringVar()
        self.var_faculty=StringVar()
        self.var_faculty_branch=StringVar()
        self.var_faculty_serch=StringVar()
        self.var_faculty_subject=StringVar()


        self.var_physics_cycle_faculty_select=StringVar()
        self.var_physics_cycle_faculty_select=StringVar()
        self.var_physics_cycle_faculty_name=StringVar()
        self.var_physics_cycle_faculty_branch=StringVar()
        self.var_physics_cycle_faculty_serch=StringVar()
        self.var_physics_cycle_faculty_subject=StringVar()

        self.var_3rd_semister_faculty_select=StringVar()#################FOR CIVIL
        self.var_3rd_semister_faculty_select=StringVar()
        self.var_3rd_semister_faculty_name=StringVar()
        self.var_3rd_semister_faculty_branch=StringVar()
        self.var_3rd_semister_faculty_serch=StringVar()
        self.var_3rd_semister_faculty_subject=StringVar()

        self.var_mech_3rd_semister_faculty_select=StringVar()
        self.var_mech_3rd_semister_faculty_select=StringVar()
        self.var_mech_3rd_semister_faculty_name=StringVar()
        self.var_mech_3rd_semister_faculty_branch=StringVar()
        self.var_mech_3rd_semister_faculty_serch=StringVar()
        self.var_mech_3rd_semister_faculty_subject=StringVar()

        self.var_eee_3rd_semister_faculty_select=StringVar()
        self.var_eee_3rd_semister_faculty_select=StringVar()
        self.var_eee_3rd_semister_faculty_name=StringVar()
        self.var_eee_3rd_semister_faculty_branch=StringVar()
        self.var_eee_3rd_semister_faculty_serch=StringVar()
        self.var_eee_3rd_semister_faculty_subject=StringVar()

        self.var_ece_3rd_semister_faculty_select=StringVar()
        self.var_ece_3rd_semister_faculty_select=StringVar()
        self.var_ece_3rd_semister_faculty_name=StringVar()
        self.var_ece_3rd_semister_faculty_branch=StringVar()
        self.var_ece_3rd_semister_faculty_serch=StringVar()
        self.var_ece_3rd_semister_faculty_subject=StringVar()

        self.var_cs_3rd_semister_faculty_select=StringVar()
        self.var_cs_3rd_semister_faculty_select=StringVar()
        self.var_cs_3rd_semister_faculty_name=StringVar()
        self.var_cs_3rd_semister_faculty_branch=StringVar()
        self.var_cs_3rd_semister_faculty_serch=StringVar()
        self.var_cs_3rd_semister_faculty_subject=StringVar()

        self.var_ise_3rd_semister_faculty_select=StringVar()
        self.var_ise_3rd_semister_faculty_select=StringVar()
        self.var_ise_3rd_semister_faculty_name=StringVar()
        self.var_ise_3rd_semister_faculty_branch=StringVar()
        self.var_ise_3rd_semister_faculty_serch=StringVar()
        self.var_ise_3rd_semister_faculty_subject=StringVar()

        self.var_ete_3rd_semister_faculty_select=StringVar()
        self.var_ete_3rd_semister_faculty_select=StringVar()
        self.var_ete_3rd_semister_faculty_name=StringVar()
        self.var_ete_3rd_semister_faculty_branch=StringVar()
        self.var_ete_3rd_semister_faculty_serch=StringVar()
        self.var_ete_3rd_semister_faculty_subject=StringVar()
        ##########################################################################################################################################################################
        self.var_4th_semister_faculty_select=StringVar()#################FOR CIVIL
        self.var_4th_semister_faculty_select=StringVar()
        self.var_4th_semister_faculty_name=StringVar()
        self.var_4th_semister_faculty_branch=StringVar()
        self.var_4th_semister_faculty_serch=StringVar()
        self.var_4th_semister_faculty_subject=StringVar()

        self.var_mech_4th_semister_faculty_select=StringVar()
        self.var_mech_4th_semister_faculty_select=StringVar()
        self.var_mech_4th_semister_faculty_name=StringVar()
        self.var_mech_4th_semister_faculty_branch=StringVar()
        self.var_mech_4th_semister_faculty_serch=StringVar()
        self.var_mech_4th_semister_faculty_subject=StringVar()

        self.var_eee_4th_semister_faculty_select=StringVar()
        self.var_eee_4th_semister_faculty_select=StringVar()
        self.var_eee_4th_semister_faculty_name=StringVar()
        self.var_eee_4th_semister_faculty_branch=StringVar()
        self.var_eee_4th_semister_faculty_serch=StringVar()
        self.var_eee_4th_semister_faculty_subject=StringVar()

        self.var_ece_4th_semister_faculty_select=StringVar()
        self.var_ece_4th_semister_faculty_select=StringVar()
        self.var_ece_4th_semister_faculty_name=StringVar()
        self.var_ece_4th_semister_faculty_branch=StringVar()
        self.var_ece_4th_semister_faculty_serch=StringVar()
        self.var_ece_4th_semister_faculty_subject=StringVar()

        self.var_cs_4th_semister_faculty_select=StringVar()
        self.var_cs_4th_semister_faculty_select=StringVar()
        self.var_cs_4th_semister_faculty_name=StringVar()
        self.var_cs_4th_semister_faculty_branch=StringVar()
        self.var_cs_4th_semister_faculty_serch=StringVar()
        self.var_cs_4th_semister_faculty_subject=StringVar()

        self.var_ise_4th_semister_faculty_select=StringVar()
        self.var_ise_4th_semister_faculty_select=StringVar()
        self.var_ise_4th_semister_faculty_name=StringVar()
        self.var_ise_4th_semister_faculty_branch=StringVar()
        self.var_ise_4th_semister_faculty_serch=StringVar()
        self.var_ise_4th_semister_faculty_subject=StringVar()

        self.var_ete_4th_semister_faculty_select=StringVar()
        self.var_ete_4th_semister_faculty_select=StringVar()
        self.var_ete_4th_semister_faculty_name=StringVar()
        self.var_ete_4th_semister_faculty_branch=StringVar()
        self.var_ete_4th_semister_faculty_serch=StringVar()
        self.var_ete_4th_semister_faculty_subject=StringVar()
        ########################################

         ##########################################################################################################################################################################
        self.var_5th_semister_faculty_select=StringVar()#################FOR CIVIL
        self.var_5th_semister_faculty_select=StringVar()
        self.var_5th_semister_faculty_name=StringVar()
        self.var_5th_semister_faculty_branch=StringVar()
        self.var_5th_semister_faculty_serch=StringVar()
        self.var_5th_semister_faculty_subject=StringVar()

        self.var_mech_5th_semister_faculty_select=StringVar()
        self.var_mech_5th_semister_faculty_select=StringVar()
        self.var_mech_5th_semister_faculty_name=StringVar()
        self.var_mech_5th_semister_faculty_branch=StringVar()
        self.var_mech_5th_semister_faculty_serch=StringVar()
        self.var_mech_5th_semister_faculty_subject=StringVar()

        self.var_eee_5th_semister_faculty_select=StringVar()
        self.var_eee_5th_semister_faculty_select=StringVar()
        self.var_eee_5th_semister_faculty_name=StringVar()
        self.var_eee_5th_semister_faculty_branch=StringVar()
        self.var_eee_5th_semister_faculty_serch=StringVar()
        self.var_eee_5th_semister_faculty_subject=StringVar()

        self.var_ece_5th_semister_faculty_select=StringVar()
        self.var_ece_5th_semister_faculty_select=StringVar()
        self.var_ece_5th_semister_faculty_name=StringVar()
        self.var_ece_5th_semister_faculty_branch=StringVar()
        self.var_ece_5th_semister_faculty_serch=StringVar()
        self.var_ece_5th_semister_faculty_subject=StringVar()

        self.var_cs_5th_semister_faculty_select=StringVar()
        self.var_cs_5th_semister_faculty_select=StringVar()
        self.var_cs_5th_semister_faculty_name=StringVar()
        self.var_cs_5th_semister_faculty_branch=StringVar()
        self.var_cs_5th_semister_faculty_serch=StringVar()
        self.var_cs_5th_semister_faculty_subject=StringVar()

        self.var_ise_5th_semister_faculty_select=StringVar()
        self.var_ise_5th_semister_faculty_select=StringVar()
        self.var_ise_5th_semister_faculty_name=StringVar()
        self.var_ise_5th_semister_faculty_branch=StringVar()
        self.var_ise_5th_semister_faculty_serch=StringVar()
        self.var_ise_5th_semister_faculty_subject=StringVar()

        self.var_ete_5th_semister_faculty_select=StringVar()
        self.var_ete_5th_semister_faculty_select=StringVar()
        self.var_ete_5th_semister_faculty_name=StringVar()
        self.var_ete_5th_semister_faculty_branch=StringVar()
        self.var_ete_5th_semister_faculty_serch=StringVar()
        self.var_ete_5th_semister_faculty_subject=StringVar()
        ########################################
        ##########################################################################################################################################################################
        self.var_6th_semister_faculty_select=StringVar()#################FOR CIVIL
        self.var_6th_semister_faculty_select=StringVar()
        self.var_6th_semister_faculty_name=StringVar()
        self.var_6th_semister_faculty_branch=StringVar()
        self.var_6th_semister_faculty_serch=StringVar()
        self.var_6th_semister_faculty_subject=StringVar()

        self.var_mech_6th_semister_faculty_select=StringVar()
        self.var_mech_6th_semister_faculty_select=StringVar()
        self.var_mech_6th_semister_faculty_name=StringVar()
        self.var_mech_6th_semister_faculty_branch=StringVar()
        self.var_mech_6th_semister_faculty_serch=StringVar()
        self.var_mech_6th_semister_faculty_subject=StringVar()

        self.var_eee_6th_semister_faculty_select=StringVar()
        self.var_eee_6th_semister_faculty_select=StringVar()
        self.var_eee_6th_semister_faculty_name=StringVar()
        self.var_eee_6th_semister_faculty_branch=StringVar()
        self.var_eee_6th_semister_faculty_serch=StringVar()
        self.var_eee_6th_semister_faculty_subject=StringVar()

        self.var_ece_6th_semister_faculty_select=StringVar()
        self.var_ece_6th_semister_faculty_select=StringVar()
        self.var_ece_6th_semister_faculty_name=StringVar()
        self.var_ece_6th_semister_faculty_branch=StringVar()
        self.var_ece_6th_semister_faculty_serch=StringVar()
        self.var_ece_6th_semister_faculty_subject=StringVar()

        self.var_cs_6th_semister_faculty_select=StringVar()
        self.var_cs_6th_semister_faculty_select=StringVar()
        self.var_cs_6th_semister_faculty_name=StringVar()
        self.var_cs_6th_semister_faculty_branch=StringVar()
        self.var_cs_6th_semister_faculty_serch=StringVar()
        self.var_cs_6th_semister_faculty_subject=StringVar()

        self.var_ise_6th_semister_faculty_select=StringVar()
        self.var_ise_6th_semister_faculty_select=StringVar()
        self.var_ise_6th_semister_faculty_name=StringVar()
        self.var_ise_6th_semister_faculty_branch=StringVar()
        self.var_ise_6th_semister_faculty_serch=StringVar()
        self.var_ise_6th_semister_faculty_subject=StringVar()

        self.var_ete_6th_semister_faculty_select=StringVar()
        self.var_ete_6th_semister_faculty_select=StringVar()
        self.var_ete_6th_semister_faculty_name=StringVar()
        self.var_ete_6th_semister_faculty_branch=StringVar()
        self.var_ete_6th_semister_faculty_serch=StringVar()
        self.var_ete_6th_semister_faculty_subject=StringVar()
        ########################################

        ##########################################################################################################################################################################
        self.var_7th_semister_faculty_select=StringVar()#################FOR CIVIL
        self.var_7th_semister_faculty_select=StringVar()
        self.var_7th_semister_faculty_name=StringVar()
        self.var_7th_semister_faculty_branch=StringVar()
        self.var_7th_semister_faculty_serch=StringVar()
        self.var_7th_semister_faculty_subject=StringVar()

        self.var_mech_7th_semister_faculty_select=StringVar()
        self.var_mech_7th_semister_faculty_select=StringVar()
        self.var_mech_7th_semister_faculty_name=StringVar()
        self.var_mech_7th_semister_faculty_branch=StringVar()
        self.var_mech_7th_semister_faculty_serch=StringVar()
        self.var_mech_7th_semister_faculty_subject=StringVar()

        self.var_eee_7th_semister_faculty_select=StringVar()
        self.var_eee_7th_semister_faculty_select=StringVar()
        self.var_eee_7th_semister_faculty_name=StringVar()
        self.var_eee_7th_semister_faculty_branch=StringVar()
        self.var_eee_7th_semister_faculty_serch=StringVar()
        self.var_eee_7th_semister_faculty_subject=StringVar()

        self.var_ece_7th_semister_faculty_select=StringVar()
        self.var_ece_7th_semister_faculty_select=StringVar()
        self.var_ece_7th_semister_faculty_name=StringVar()
        self.var_ece_7th_semister_faculty_branch=StringVar()
        self.var_ece_7th_semister_faculty_serch=StringVar()
        self.var_ece_7th_semister_faculty_subject=StringVar()

        self.var_cs_7th_semister_faculty_select=StringVar()
        self.var_cs_7th_semister_faculty_select=StringVar()
        self.var_cs_7th_semister_faculty_name=StringVar()
        self.var_cs_7th_semister_faculty_branch=StringVar()
        self.var_cs_7th_semister_faculty_serch=StringVar()
        self.var_cs_7th_semister_faculty_subject=StringVar()

        self.var_ise_7th_semister_faculty_select=StringVar()
        self.var_ise_7th_semister_faculty_select=StringVar()
        self.var_ise_7th_semister_faculty_name=StringVar()
        self.var_ise_7th_semister_faculty_branch=StringVar()
        self.var_ise_7th_semister_faculty_serch=StringVar()
        self.var_ise_7th_semister_faculty_subject=StringVar()

        self.var_ete_7th_semister_faculty_select=StringVar()
        self.var_ete_7th_semister_faculty_select=StringVar()
        self.var_ete_7th_semister_faculty_name=StringVar()
        self.var_ete_7th_semister_faculty_branch=StringVar()
        self.var_ete_7th_semister_faculty_serch=StringVar()
        self.var_ete_7th_semister_faculty_subject=StringVar()
        ########################################

        ##########################################################################################################################################################################
        self.var_8th_semister_faculty_select=StringVar()#################FOR CIVIL
        self.var_8th_semister_faculty_select=StringVar()
        self.var_8th_semister_faculty_name=StringVar()
        self.var_8th_semister_faculty_branch=StringVar()
        self.var_8th_semister_faculty_serch=StringVar()
        self.var_8th_semister_faculty_subject=StringVar()

        self.var_mech_8th_semister_faculty_select=StringVar()
        self.var_mech_8th_semister_faculty_select=StringVar()
        self.var_mech_8th_semister_faculty_name=StringVar()
        self.var_mech_8th_semister_faculty_branch=StringVar()
        self.var_mech_8th_semister_faculty_serch=StringVar()
        self.var_mech_8th_semister_faculty_subject=StringVar()

        self.var_eee_8th_semister_faculty_select=StringVar()
        self.var_eee_8th_semister_faculty_select=StringVar()
        self.var_eee_8th_semister_faculty_name=StringVar()
        self.var_eee_8th_semister_faculty_branch=StringVar()
        self.var_eee_8th_semister_faculty_serch=StringVar()
        self.var_eee_8th_semister_faculty_subject=StringVar()

        self.var_ece_8th_semister_faculty_select=StringVar()
        self.var_ece_8th_semister_faculty_select=StringVar()
        self.var_ece_8th_semister_faculty_name=StringVar()
        self.var_ece_8th_semister_faculty_branch=StringVar()
        self.var_ece_8th_semister_faculty_serch=StringVar()
        self.var_ece_8th_semister_faculty_subject=StringVar()

        self.var_cs_8th_semister_faculty_select=StringVar()
        self.var_cs_8th_semister_faculty_select=StringVar()
        self.var_cs_8th_semister_faculty_name=StringVar()
        self.var_cs_8th_semister_faculty_branch=StringVar()
        self.var_cs_8th_semister_faculty_serch=StringVar()
        self.var_cs_8th_semister_faculty_subject=StringVar()

        self.var_ise_8th_semister_faculty_select=StringVar()
        self.var_ise_8th_semister_faculty_select=StringVar()
        self.var_ise_8th_semister_faculty_name=StringVar()
        self.var_ise_8th_semister_faculty_branch=StringVar()
        self.var_ise_8th_semister_faculty_serch=StringVar()
        self.var_ise_8th_semister_faculty_subject=StringVar()

        self.var_ete_8th_semister_faculty_select=StringVar()
        self.var_ete_8th_semister_faculty_select=StringVar()
        self.var_ete_8th_semister_faculty_name=StringVar()
        self.var_ete_8th_semister_faculty_branch=StringVar()
        self.var_ete_8th_semister_faculty_serch=StringVar()
        self.var_ete_8th_semister_faculty_subject=StringVar()
        ########################################
        

        ###########################################################################################################################################################################



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
        button1=ttk.Button(menu_frame,text='Search',width=15,command=self.faculty_select).grid(row=0,column=2,padx=4,pady=3)
        button2=ttk.Button(menu_frame,text='Add to Data Base',width=20).grid(row=0,column=3,padx=4,pady=3)
        button3=ttk.Button(menu_frame,text='Update',width=15).grid(row=0,column=4,padx=4,pady=3)
        button4=ttk.Button(menu_frame,text='Delete',width=15).grid(row=0,column=5,padx=4,pady=3)
        button4=ttk.Button(menu_frame,text='Clear',width=15).grid(row=0,column=6,padx=4,pady=3)
        
    def faculty_select(self):
        
        if self.var_sem_select.get()=="CHEMISTRY_cycle":
            if self.var_branch_select.get() == "1st_semister":
                table_frame=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame.place(x=10,y=120) 
                #self.query()
                


        ################################################################################################
                def add_faculty_into_database():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )

                    cur=con.cursor()
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    #cur=con.cursor()
                    if self.var_faculty.get()=='':
                        messagebox.showerror('Error','The faculty name must be required')
                    else:
                        if self.var_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required')
                        else:
                            if self.var_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame10)
                            else:
                                cur.execute('INSERT INTO add_faculty1(faculty_name,faculty_branch,faculty_subject) values(%s,%s,%s)',(
                                    self.var_faculty.get(),
                                    self.var_faculty_branch.get(),
                                    self.var_faculty_subject.get()
                                    
                                    ))

                    
                                #cur.execute('insert into add_faculty1(faculty_name,faculty_branch,faculty_subject) values(?,?,?)',(
                                #self.var_faculty.get(),
                                #self.var_faculty_branch.get(),
                                #self.var_faculty_subject.get()
                           # ))
                            con.commit()
                            fetch_chemistry_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame)
                def fetch_chemistry_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    #cur=con.cursor()
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()

                    try:
                        cur.execute('''select * from add_faculty1''')
                        rows=cur.fetchall()
                        self.faculty_table_treeview.delete(*self.faculty_table_treeview.get_children())
                        for row in rows:
                            self.faculty_table_treeview.insert('',END,values=row)
                        con.commit()
                        con.close()
                        #cur.execute('select * from add_faculty1')
                        #rows=cur.fetchall()
                        #self.faculty_table_treeview.delete(*self.faculty_table_treeview.get_children())
                        #for row in rows:
                        #    self.faculty_table_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame)

                def chemistry_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame)
                        else:
                            cur.execute(f"select * from add_faculty1 where faculty_name LIKE '%{self.var_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.faculty_table_treeview.delete(*self.faculty_table_treeview.get_children())
                            for row in rows:
                                self.faculty_table_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame)
                def chemistry_faculty_data_get(ev):
                    r1=self.faculty_table_treeview.focus()
                    content1=self.faculty_table_treeview.item(r1)
                    row1=content1["values"]

                    self.var_faculty.set(row1[0])
                    self.var_faculty_branch.set(row1[1])
                    self.var_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame)

                def chemistry_faculty_data_clear():
                    fetch_chemistry_faculty_data()
                    self.var_faculty_serch.set("")
                    self.var_faculty.set("")
                    self.var_faculty_branch.set("")
                    self.var_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame)
                def chemistry_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_faculty.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame)
                        else:
                            cur.execute("select * from add_faculty1 where faculty_name=%s",(self.var_faculty.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame)
                            else:
                                cur.execute("update add_faculty1 set faculty_branch=%s,faculty_subject=%s where faculty_name=%s",(
                                #cur.execute("update add_faculty1 set faculty_branch=%s,faculty_subject=%s whre faculty_name=%s",(
                                    
                                    self.var_faculty_branch.get(),
                                    self.var_faculty_subject.get(),
                                    self.var_faculty.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=self.root)
                                fetch_chemistry_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame)
                def chemistry_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_faculty.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame)
                        else:
                            #cur.execute("select * from add_faculty1 where faculty_name=?",(self.var_faculty.get(),))
                            cur.execute("select * from add_faculty1 where faculty_name=%s",(self.var_faculty.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame)
                                if option==True:
                                    cur.execute('delete from add_faculty1 where faculty_name=%s',(self.var_faculty.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame)
                                    chemistry_faculty_data_clear()
                                    fetch_chemistry_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame)
                
################################################################################################

                label11=Label(table_frame,text='Chemistry Cycle:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame,width=29,textvariable=self.var_faculty)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame,width=29,textvariable=self.var_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame,width=29,textvariable=self.var_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=chemistry_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=chemistry_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=chemistry_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=chemistry_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.facuty_table_frame=Frame(table_frame,width=800,height=200,relief=GROOVE)
                self.facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.facuty_table_frame,orient=VERTICAL)
                self.faculty_table_treeview=ttk.Treeview(self.facuty_table_frame,columns=('faculty_name','faculty_branch','faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.faculty_table_treeview.xview)
                scrolly.configure(command=self.faculty_table_treeview.yview)

                
                self.faculty_table_treeview.heading('faculty_name',text='Faculty Name ')
                self.faculty_table_treeview.heading('faculty_branch',text='Faculty Branch ')
                self.faculty_table_treeview.heading('faculty_subject',text='Faculty Subject ')

          
                self.faculty_table_treeview.column('faculty_name',width=250)
                self.faculty_table_treeview.column('faculty_branch',width=260)
                self.faculty_table_treeview.column('faculty_subject',width=270)

                self.faculty_table_treeview['show']='headings'

                self.faculty_table_treeview.pack(fill=BOTH,expand=1)
                fetch_chemistry_faculty_data()
                self.faculty_table_treeview.bind('<ButtonRelease-1>',chemistry_faculty_data_get)


############################################# physics cycle#########################################################################################################################
        if self.var_sem_select.get()=="PHYSICS_cycle":
            if self.var_branch_select.get() == "2nd_semister":
                table_frame2=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame2.place(x=10,y=120) 

################################################################################################
                def add_physics_cycle_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_physics_cycle_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame2)
                    else:
                        if self.var_physics_cycle_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame2)
                        else:
                            if self.var_physics_cycle_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame2)
                            else:
                                cur.execute('insert into add_faculty_physics1(physics_cycle_faculty_name,physics_cycle_faculty_branch,physics_cycle_faculty_subject) values(%s,%s,%s)',(
                                self.var_physics_cycle_faculty_name.get(),
                                self.var_physics_cycle_faculty_branch.get(),
                                self.var_physics_cycle_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_physics_cycle_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame2)
                def fetch_physics_cycle_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_faculty_physics1')
                        rows=cur.fetchall()
                        self.physics_cycle_faculty_data_table.delete(*self.physics_cycle_faculty_data_table.get_children())
                        for row in rows:
                            self.physics_cycle_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame2)

                def physics_cycle_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_physics_cycle_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame2)
                        else:
                            cur.execute(f"select * from add_faculty_physics1 where physics_cycle_faculty_name LIKE '%{self.var_physics_cycle_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.physics_cycle_faculty_data_table.delete(*self.physics_cycle_faculty_data_table.get_children())
                            for row in rows:
                                self.physics_cycle_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame2)
                def physics_cycle_faculty_data_get(ev):
                    r1=self.physics_cycle_faculty_data_table.focus()
                    content1=self.physics_cycle_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_physics_cycle_faculty_name.set(row1[0])
                    self.var_physics_cycle_faculty_branch.set(row1[1])
                    self.var_physics_cycle_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame2)

                def physics_cycle_faculty_data_clear():
                    fetch_physics_cycle_faculty_data()
                    self.var_physics_cycle_faculty_serch.set("")
                    self.var_physics_cycle_faculty_name.set("")
                    self.var_physics_cycle_faculty_branch.set("")
                    self.var_physics_cycle_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame2)
                def physics_cycle_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_physics_cycle_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame2)
                        else:
                            cur.execute("select * from add_faculty_physics1 where physics_cycle_faculty_name=%s",(self.var_physics_cycle_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame2)
                            else:
                                cur.execute("update add_faculty_physics1 set physics_cycle_faculty_branch=%s,physics_cycle_faculty_subject=%s where physics_cycle_faculty_name=%s",(
                                    
                                    self.var_physics_cycle_faculty_branch.get(),
                                    self.var_physics_cycle_faculty_subject.get(),
                                    self.var_physics_cycle_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame2)
                                fetch_physics_cycle_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame2)
                def physics_cycle_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_physics_cycle_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame2)
                        else:
                            cur.execute("select * from add_faculty_physics1 where physics_cycle_faculty_name=%s",(self.var_physics_cycle_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame2)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame2)
                                if option==True:
                                    cur.execute('delete from add_faculty_physics1 where physics_cycle_faculty_name=%s',(self.var_physics_cycle_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame2)
                                    physics_cycle_faculty_data_clear()
                                    fetch_physics_cycle_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame2)
                
################################################################################################

                label11=Label(table_frame2,text='Physics Cycle:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame2,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame2,width=29,textvariable=self.var_physics_cycle_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame2,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame2,width=29,textvariable=self.var_physics_cycle_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame2,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame2,width=29,textvariable=self.var_physics_cycle_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame2,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_physics_cycle_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=physics_cycle_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=physics_cycle_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=physics_cycle_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_physics_cycle_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=physics_cycle_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.physics_cycle_facuty_table_frame=Frame(table_frame2,width=800,height=200,relief=GROOVE)
                self.physics_cycle_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.physics_cycle_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.physics_cycle_facuty_table_frame,orient=VERTICAL)
                self.physics_cycle_faculty_data_table=ttk.Treeview(self.physics_cycle_facuty_table_frame,columns=('physics_cycle_faculty_name','physics_cycle_faculty_branch','physics_cycle_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.physics_cycle_faculty_data_table.xview)
                scrolly.configure(command=self.physics_cycle_faculty_data_table.yview)

             
                self.physics_cycle_faculty_data_table.heading('physics_cycle_faculty_name',text='Faculty Name ')
                self.physics_cycle_faculty_data_table.heading('physics_cycle_faculty_branch',text='Faculty Branch ')
                self.physics_cycle_faculty_data_table.heading('physics_cycle_faculty_subject',text='Faculty Subject ')


                self.physics_cycle_faculty_data_table.column('physics_cycle_faculty_name',width=210)
                self.physics_cycle_faculty_data_table.column('physics_cycle_faculty_branch',width=300)
                self.physics_cycle_faculty_data_table.column('physics_cycle_faculty_subject',width=270)

                self.physics_cycle_faculty_data_table['show']='headings'

                self.physics_cycle_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_physics_cycle_faculty_data()
                self.physics_cycle_faculty_data_table.bind('<ButtonRelease-1>',physics_cycle_faculty_data_get)



############################################# 3rd semister   civil engineering #########################################################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Civil_Engineering":
                table_frame3=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame3.place(x=10,y=120) 

################################################################################################
                def add_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame3)
                    else:
                        if self.var_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame3)
                        else:
                            if self.var_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame3)
                            else:
                                cur.execute('insert into add_3rd_semsiter_faculty(rd3_semister_faculty_name,rd3_semister_faculty_branch,rd3_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_3rd_semister_faculty_name.get(),
                                self.var_3rd_semister_faculty_branch.get(),
                                self.var_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame3)
                def fetch_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.rd3_semister_faculty_data_table.delete(*self.rd3_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.rd3_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame3)

                def rd3_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame3)
                        else:
                            cur.execute(f"select * from add_3rd_semsiter_faculty where rd3_semister_faculty_name LIKE '%{self.var_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.rd3_semister_faculty_data_table.delete(*self.rd3_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.rd3_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame3)
                def rd3_semister_faculty_data_get(ev):
                    r1=self.rd3_semister_faculty_data_table.focus()
                    content1=self.rd3_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_3rd_semister_faculty_name.set(row1[0])
                    self.var_3rd_semister_faculty_branch.set(row1[1])
                    self.var_3rd_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame3)

                def rd3_semister_faculty_data_clear():
                    fetch_3rd_semister_faculty_data()
                    self.var_3rd_semister_faculty_serch.set("")
                    self.var_3rd_semister_faculty_name.set("")
                    self.var_3rd_semister_faculty_branch.set("")
                    self.var_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame3)
                def rd3_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame3)
                        else:
                            cur.execute("select * from add_3rd_semsiter_faculty where rd3_semister_faculty_name=%s",(self.var_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame3)
                            else:
                                cur.execute("update add_3rd_semsiter_faculty set rd3_semister_faculty_branch=%s,rd3_semister_faculty_subject=%s where rd3_semister_faculty_name=%s",(
                                    
                                    self.var_3rd_semister_faculty_branch.get(),
                                    self.var_3rd_semister_faculty_subject.get(),
                                    self.var_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame3)
                                fetch_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame3)
                def rd3_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame3)
                        else:
                            cur.execute("select * from add_3rd_semsiter_faculty where rd3_semister_faculty_name=%s",(self.var_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame3)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame3)
                                if option==True:
                                    cur.execute('delete from add_3rd_semsiter_faculty where rd3_semister_faculty_name=%s',(self.var_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame3)
                                    rd3_semister_faculty_data_clear()
                                    fetch_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame3)
                
################################################################################################

                label11=Label(table_frame3,text='3rd Semsiter civil:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame3,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame3,width=29,textvariable=self.var_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame3,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame3,width=29,textvariable=self.var_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame3,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame3,width=29,textvariable=self.var_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame3,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=rd3_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=rd3_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=rd3_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=rd3_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.rd3_semister_facuty_table_frame=Frame(table_frame3,width=800,height=200,relief=GROOVE)
                self.rd3_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.rd3_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.rd3_semister_facuty_table_frame,orient=VERTICAL)
                self.rd3_semister_faculty_data_table=ttk.Treeview(self.rd3_semister_facuty_table_frame,columns=('rd3_semister_faculty_name','rd3_semister_faculty_branch','rd3_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.rd3_semister_faculty_data_table.xview)
                scrolly.configure(command=self.rd3_semister_faculty_data_table.yview)

        
                self.rd3_semister_faculty_data_table.heading('rd3_semister_faculty_name',text='Faculty Name ')
                self.rd3_semister_faculty_data_table.heading('rd3_semister_faculty_branch',text='Faculty Branch ')
                self.rd3_semister_faculty_data_table.heading('rd3_semister_faculty_subject',text='Faculty Subject ')


                self.rd3_semister_faculty_data_table.column('rd3_semister_faculty_name',width=210)
                self.rd3_semister_faculty_data_table.column('rd3_semister_faculty_branch',width=300)
                self.rd3_semister_faculty_data_table.column('rd3_semister_faculty_subject',width=270)

                self.rd3_semister_faculty_data_table['show']='headings'

                self.rd3_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_3rd_semister_faculty_data()
                self.rd3_semister_faculty_data_table.bind('<ButtonRelease-1>',rd3_semister_faculty_data_get)



        
############################################# 3rd semister mech #########################################################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Mechanical_Engineering":
                table_frame4=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame4.place(x=10,y=120) 

################################################################################################
                def add_mech_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_mech_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame4)
                    else:
                        if self.var_mech_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame4)
                        else:
                            if self.var_mech_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame4)
                            else:
                                cur.execute('insert into add_mech_3rd_semsiter_faculty(mech_3rd_semister_faculty_name,mech_3rd_semister_faculty_branch,mech_3rd_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_mech_3rd_semister_faculty_name.get(),
                                self.var_mech_3rd_semister_faculty_branch.get(),
                                self.var_mech_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_mech_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame4)
                def fetch_mech_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_mech_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.mech_3rd_semister_faculty_data_table.delete(*self.mech_3rd_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.mech_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame4)

                def mech_3rd_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame4)
                        else:
                            cur.execute(f"select * from add_mech_3rd_semsiter_faculty where mech_3rd_semister_faculty_name LIKE '%{self.var_mech_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.mech_3rd_semister_faculty_data_table.delete(*self.mech_3rd_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.mech_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame4)
                def mech_3rd_semister_faculty_data_get(ev):
                    r1=self.mech_3rd_semister_faculty_data_table.focus()
                    content1=self.mech_3rd_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_mech_3rd_semister_faculty_name.set(row1[0])
                    self.var_mech_3rd_semister_faculty_branch.set(row1[1])
                    self.var_mech_3rd_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame4)

                def mech_3rd_semister_faculty_data_clear():
                    fetch_mech_3rd_semister_faculty_data()
                    self.var_mech_3rd_semister_faculty_serch.set("")
                    self.var_mech_3rd_semister_faculty_name.set("")
                    self.var_mech_3rd_semister_faculty_branch.set("")
                    self.var_mech_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame4)
                def mech_3rd_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame4)
                        else:
                            cur.execute("select * from add_mech_3rd_semsiter_faculty where mech_3rd_semister_faculty_name=%s",(self.var_mech_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame4)
                            else:
                                cur.execute("update add_mech_3rd_semsiter_faculty set mech_3rd_semister_faculty_branch=%s,mech_3rd_semister_faculty_subject=%s where mech_3rd_semister_faculty_name=%s",(
                                    
                                    self.var_mech_3rd_semister_faculty_branch.get(),
                                    self.var_mech_3rd_semister_faculty_subject.get(),
                                    self.var_mech_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame4)
                                fetch_mech_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame4)
                def mech_3rd_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame4)
                        else:
                            cur.execute("select * from add_mech_3rd_semsiter_faculty where mech_3rd_semister_faculty_name=%s",(self.var_mech_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame4)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame4)
                                if option==True:
                                    cur.execute('delete from add_mech_3rd_semsiter_faculty where mech_3rd_semister_faculty_name=%s',(self.var_mech_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame4)
                                    mech_3rd_semister_faculty_data_clear()
                                    fetch_mech_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame4)
                
################################################################################################

                label11=Label(table_frame4,text='3rd Semsiter MECH:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame4,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame4,width=29,textvariable=self.var_mech_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame4,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame4,width=29,textvariable=self.var_mech_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame4,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame4,width=29,textvariable=self.var_mech_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame4,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_mech_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=mech_3rd_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=mech_3rd_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=mech_3rd_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_mech_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=mech_3rd_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.mech_3rd_semister_facuty_table_frame=Frame(table_frame4,width=800,height=200,relief=GROOVE)
                self.mech_3rd_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.mech_3rd_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.mech_3rd_semister_facuty_table_frame,orient=VERTICAL)
                self.mech_3rd_semister_faculty_data_table=ttk.Treeview(self.mech_3rd_semister_facuty_table_frame,columns=('mech_3rd_semister_faculty_name','mech_3rd_semister_faculty_branch','mech_3rd_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.mech_3rd_semister_faculty_data_table.xview)
                scrolly.configure(command=self.mech_3rd_semister_faculty_data_table.yview)

                self.mech_3rd_semister_faculty_data_table.heading('mech_3rd_semister_faculty_name',text='Faculty Name ')
                self.mech_3rd_semister_faculty_data_table.heading('mech_3rd_semister_faculty_branch',text='Faculty Branch ')
                self.mech_3rd_semister_faculty_data_table.heading('mech_3rd_semister_faculty_subject',text='Faculty Subject ')

                self.mech_3rd_semister_faculty_data_table.column('mech_3rd_semister_faculty_name',width=210)
                self.mech_3rd_semister_faculty_data_table.column('mech_3rd_semister_faculty_branch',width=300)
                self.mech_3rd_semister_faculty_data_table.column('mech_3rd_semister_faculty_subject',width=270)

                self.mech_3rd_semister_faculty_data_table['show']='headings'

                self.mech_3rd_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_mech_3rd_semister_faculty_data()
                self.mech_3rd_semister_faculty_data_table.bind('<ButtonRelease-1>',mech_3rd_semister_faculty_data_get)
################################################################################ Electrical_And_Electronic_Engineering ############################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Electrical_And_Electronic_Engineering":
                table_frame5=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame5.place(x=10,y=120) 

################################################################################################
                def add_eee_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_eee_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame5)
                    else:
                        if self.var_eee_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame5)
                        else:
                            if self.var_eee_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame5)
                            else:
                                cur.execute('insert into add_eee_3rd_semsiter_faculty(eee_3rd_semister_faculty_name,eee_3rd_semister_faculty_branch,eee_3rd_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_eee_3rd_semister_faculty_name.get(),
                                self.var_eee_3rd_semister_faculty_branch.get(),
                                self.var_eee_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_eee_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame5)
                def fetch_eee_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_eee_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.eee_3rd_semister_faculty_data_table.delete(*self.eee_3rd_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.eee_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame5)

                def eee_3rd_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame5)
                        else:
                            cur.execute(f"select * from add_eee_3rd_semsiter_faculty where eee_3rd_semister_faculty_name LIKE '%{self.var_eee_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.eee_3rd_semister_faculty_data_table.delete(*self.eee_3rd_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.eee_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame5)
                def eee_3rd_semister_faculty_data_get(ev):
                    r1=self.eee_3rd_semister_faculty_data_table.focus()
                    content1=self.eee_3rd_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_eee_3rd_semister_faculty_name.set(row1[0])
                    self.var_eee_3rd_semister_faculty_branch.set(row1[1])
                    self.var_eee_3rd_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame5)

                def eee_3rd_semister_faculty_data_clear():
                    fetch_eee_3rd_semister_faculty_data()
                    self.var_eee_3rd_semister_faculty_serch.set("")
                    self.var_eee_3rd_semister_faculty_name.set("")
                    self.var_eee_3rd_semister_faculty_branch.set("")
                    self.var_eee_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame5)
                def eee_3rd_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame5)
                        else:
                            cur.execute("select * from add_eee_3rd_semsiter_faculty where eee_3rd_semister_faculty_name=%s",(self.var_eee_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame5)
                            else:
                                cur.execute("update add_eee_3rd_semsiter_faculty set eee_3rd_semister_faculty_branch=%s,eee_3rd_semister_faculty_subject=%s where eee_3rd_semister_faculty_name=%s",(
                                    
                                    self.var_eee_3rd_semister_faculty_branch.get(),
                                    self.var_eee_3rd_semister_faculty_subject.get(),
                                    self.var_eee_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame5)
                                fetch_eee_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame5)
                def eee_3rd_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame5)
                        else:
                            cur.execute("select * from add_eee_3rd_semsiter_faculty where eee_3rd_semister_faculty_name=%s",(self.var_eee_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame5)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame5)
                                if option==True:
                                    cur.execute('delete from add_eee_3rd_semsiter_faculty where eee_3rd_semister_faculty_name=%s',(self.var_eee_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame5)
                                    eee_3rd_semister_faculty_data_clear()
                                    fetch_eee_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame5)
                
################################################################################################

                label11=Label(table_frame5,text='3rd Semsiter EEE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame5,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame5,width=29,textvariable=self.var_eee_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame5,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame5,width=29,textvariable=self.var_eee_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame5,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame5,width=29,textvariable=self.var_eee_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame5,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_eee_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=eee_3rd_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=eee_3rd_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=eee_3rd_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_eee_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=eee_3rd_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.eee_3rd_semister_facuty_table_frame=Frame(table_frame5,width=800,height=200,relief=GROOVE)
                self.eee_3rd_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.eee_3rd_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.eee_3rd_semister_facuty_table_frame,orient=VERTICAL)
                self.eee_3rd_semister_faculty_data_table=ttk.Treeview(self.eee_3rd_semister_facuty_table_frame,columns=('eee_3rd_semister_faculty_name','eee_3rd_semister_faculty_branch','eee_3rd_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.eee_3rd_semister_faculty_data_table.xview)
                scrolly.configure(command=self.eee_3rd_semister_faculty_data_table.yview)

                
                self.eee_3rd_semister_faculty_data_table.heading('eee_3rd_semister_faculty_name',text='Faculty Name ')
                self.eee_3rd_semister_faculty_data_table.heading('eee_3rd_semister_faculty_branch',text='Faculty Branch ')
                self.eee_3rd_semister_faculty_data_table.heading('eee_3rd_semister_faculty_subject',text='Faculty Subject ')

       
                self.eee_3rd_semister_faculty_data_table.column('eee_3rd_semister_faculty_name',width=210)
                self.eee_3rd_semister_faculty_data_table.column('eee_3rd_semister_faculty_branch',width=300)
                self.eee_3rd_semister_faculty_data_table.column('eee_3rd_semister_faculty_subject',width=270)

                self.eee_3rd_semister_faculty_data_table['show']='headings'

                self.eee_3rd_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_eee_3rd_semister_faculty_data()
                self.eee_3rd_semister_faculty_data_table.bind('<ButtonRelease-1>',eee_3rd_semister_faculty_data_get)
        
############################################# 3rd semister ece #########################################################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Electronic_And_Communication_Engineering":
                table_frame6=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame6.place(x=10,y=120) 

################################################################################################
                def add_ece_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ece_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame6)
                    else:
                        if self.var_ece_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame6)
                        else:
                            if self.var_ece_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame6)
                            else:
                                cur.execute('insert into add_ece_3rd_semsiter_faculty(ece_3rd_semister_faculty_name,ece_3rd_semister_faculty_branch,ece_3rd_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ece_3rd_semister_faculty_name.get(),
                                self.var_ece_3rd_semister_faculty_branch.get(),
                                self.var_ece_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ece_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame6)
                def fetch_ece_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ece_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ece_3rd_semister_faculty_data_table.delete(*self.ece_3rd_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ece_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame6)

                def ece_3rd_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame6)
                        else:
                            cur.execute(f"select * from add_ece_3rd_semsiter_faculty where ece_3rd_semister_faculty_name LIKE '%{self.var_ece_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ece_3rd_semister_faculty_data_table.delete(*self.ece_3rd_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ece_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame6)
                def ece_3rd_semister_faculty_data_get(ev):
                    r1=self.ece_3rd_semister_faculty_data_table.focus()
                    content1=self.ece_3rd_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ece_3rd_semister_faculty_name.set(row1[0])
                    self.var_ece_3rd_semister_faculty_branch.set(row1[1])
                    self.var_ece_3rd_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame6)

                def ece_3rd_semister_faculty_data_clear():
                    fetch_ece_3rd_semister_faculty_data()
                    self.var_ece_3rd_semister_faculty_serch.set("")
                    self.var_ece_3rd_semister_faculty_name.set("")
                    self.var_ece_3rd_semister_faculty_branch.set("")
                    self.var_ece_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame6)
                def ece_3rd_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame6)
                        else:
                            cur.execute("select * from add_ece_3rd_semsiter_faculty where ece_3rd_semister_faculty_name=%s",(self.var_ece_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame6)
                            else:
                                cur.execute("update add_ece_3rd_semsiter_faculty set ece_3rd_semister_faculty_branch=%s,ece_3rd_semister_faculty_subject=%s where ece_3rd_semister_faculty_name=%s",(
                                    
                                    self.var_ece_3rd_semister_faculty_branch.get(),
                                    self.var_ece_3rd_semister_faculty_subject.get(),
                                    self.var_ece_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame6)
                                fetch_ece_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame6)
                def ece_3rd_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame6)
                        else:
                            cur.execute("select * from add_ece_3rd_semsiter_faculty where ece_3rd_semister_faculty_name=%s",(self.var_ece_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame6)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame6)
                                if option==True:
                                    cur.execute('delete from add_ece_3rd_semsiter_faculty where ece_3rd_semister_faculty_name=%s',(self.var_ece_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame6)
                                    ece_3rd_semister_faculty_data_clear()
                                    fetch_ece_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame6)
                
################################################################################################

                label11=Label(table_frame6,text='3rd Semister ECE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame6,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame6,width=29,textvariable=self.var_ece_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame6,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame6,width=29,textvariable=self.var_ece_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame6,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame6,width=29,textvariable=self.var_ece_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame6,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ece_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ece_3rd_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ece_3rd_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ece_3rd_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ece_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ece_3rd_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ece_3rd_semister_facuty_table_frame=Frame(table_frame6,width=800,height=200,relief=GROOVE)
                self.ece_3rd_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ece_3rd_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ece_3rd_semister_facuty_table_frame,orient=VERTICAL)
                self.ece_3rd_semister_faculty_data_table=ttk.Treeview(self.ece_3rd_semister_facuty_table_frame,columns=('ece_3rd_semister_faculty_name','ece_3rd_semister_faculty_branch','ece_3rd_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ece_3rd_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ece_3rd_semister_faculty_data_table.yview)

                
                self.ece_3rd_semister_faculty_data_table.heading('ece_3rd_semister_faculty_name',text='Faculty Name ')
                self.ece_3rd_semister_faculty_data_table.heading('ece_3rd_semister_faculty_branch',text='Faculty Branch ')
                self.ece_3rd_semister_faculty_data_table.heading('ece_3rd_semister_faculty_subject',text='Faculty Subject ')

                self.ece_3rd_semister_faculty_data_table.column('ece_3rd_semister_faculty_name',width=210)
                self.ece_3rd_semister_faculty_data_table.column('ece_3rd_semister_faculty_branch',width=300)
                self.ece_3rd_semister_faculty_data_table.column('ece_3rd_semister_faculty_subject',width=270)

                self.ece_3rd_semister_faculty_data_table['show']='headings'

                self.ece_3rd_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ece_3rd_semister_faculty_data()
                self.ece_3rd_semister_faculty_data_table.bind('<ButtonRelease-1>',ece_3rd_semister_faculty_data_get)
        ############################################# 3rd semister CS #########################################################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Computer_Science_Engineering":
                table_frame7=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame7.place(x=10,y=120) 

################################################################################################
                def add_cs_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_cs_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame7)
                    else:
                        if self.var_cs_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame7)
                        else:
                            if self.var_cs_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame7)
                            else:
                                cur.execute('insert into add_cs_3rd_semsiter_faculty(cs_3rd_semister_faculty_name,cs_3rd_semister_faculty_branch,cs_3rd_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_cs_3rd_semister_faculty_name.get(),
                                self.var_cs_3rd_semister_faculty_branch.get(),
                                self.var_cs_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_cs_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame7)
                def fetch_cs_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_cs_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.cs_3rd_semister_faculty_data_table.delete(*self.cs_3rd_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.cs_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame7)

                def cs_3rd_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame7)
                        else:
                            cur.execute(f"select * from add_cs_3rd_semsiter_faculty where cs_3rd_semister_faculty_name LIKE '%{self.var_cs_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.cs_3rd_semister_faculty_data_table.delete(*self.cs_3rd_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.cs_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame7)
                def cs_3rd_semister_faculty_data_get(ev):
                    r1=self.cs_3rd_semister_faculty_data_table.focus()
                    content1=self.cs_3rd_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_cs_3rd_semister_faculty_name.set(row1[1])
                    self.var_cs_3rd_semister_faculty_branch.set(row1[2])
                    self.var_cs_3rd_semister_faculty_subject.set(row1[3])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame7)

                def cs_3rd_semister_faculty_data_clear():
                    fetch_cs_3rd_semister_faculty_data()
                    self.var_cs_3rd_semister_faculty_serch.set("")
                    self.var_cs_3rd_semister_faculty_name.set("")
                    self.var_cs_3rd_semister_faculty_branch.set("")
                    self.var_cs_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame7)
                def cs_3rd_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame7)
                        else:
                            cur.execute("select * from add_cs_3rd_semsiter_faculty where cs_3rd_semister_faculty_name=%s",(self.var_cs_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame7)
                            else:
                                cur.execute("update add_cs_3rd_semsiter_faculty set cs_3rd_semister_faculty_branch=%s,cs_3rd_semister_faculty_subject=%s where cs_3rd_semister_faculty_name=%s",(
                                    
                                    self.var_cs_3rd_semister_faculty_branch.get(),
                                    self.var_cs_3rd_semister_faculty_subject.get(),
                                    self.var_cs_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame7)
                                fetch_cs_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame7)
                def cs_3rd_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame7)
                        else:
                            cur.execute("select * from add_cs_3rd_semsiter_faculty where cs_3rd_semister_faculty_name=%s",(self.var_cs_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame7)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame7)
                                if option==True:
                                    cur.execute('delete from add_cs_3rd_semsiter_faculty where cs_3rd_semister_faculty_name=%s',(self.var_cs_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame7)
                                    cs_3rd_semister_faculty_data_clear()
                                    fetch_cs_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame7)
                
################################################################################################

                label11=Label(table_frame7,text='3rd Semister CS:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame7,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame7,width=29,textvariable=self.var_cs_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame7,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame7,width=29,textvariable=self.var_cs_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame7,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame7,width=29,textvariable=self.var_cs_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame7,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_cs_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=cs_3rd_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=cs_3rd_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=cs_3rd_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_cs_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=cs_3rd_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.cs_3rd_semister_facuty_table_frame=Frame(table_frame7,width=800,height=200,relief=GROOVE)
                self.cs_3rd_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.cs_3rd_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.cs_3rd_semister_facuty_table_frame,orient=VERTICAL)
                self.cs_3rd_semister_faculty_data_table=ttk.Treeview(self.cs_3rd_semister_facuty_table_frame,columns=('cs_3rd_semister_faculty_name','cs_3rd_semister_faculty_branch','cs_3rd_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.cs_3rd_semister_faculty_data_table.xview)
                scrolly.configure(command=self.cs_3rd_semister_faculty_data_table.yview)

              
                self.cs_3rd_semister_faculty_data_table.heading('cs_3rd_semister_faculty_name',text='Faculty Name ')
                self.cs_3rd_semister_faculty_data_table.heading('cs_3rd_semister_faculty_branch',text='Faculty Branch ')
                self.cs_3rd_semister_faculty_data_table.heading('cs_3rd_semister_faculty_subject',text='Faculty Subject ')

                self.cs_3rd_semister_faculty_data_table.column('cs_3rd_semister_faculty_name',width=210)
                self.cs_3rd_semister_faculty_data_table.column('cs_3rd_semister_faculty_branch',width=300)
                self.cs_3rd_semister_faculty_data_table.column('cs_3rd_semister_faculty_subject',width=270)

                self.cs_3rd_semister_faculty_data_table['show']='headings'

                self.cs_3rd_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_cs_3rd_semister_faculty_data()
                self.cs_3rd_semister_faculty_data_table.bind('<ButtonRelease-1>',cs_3rd_semister_faculty_data_get)
 ############################################# 3rd semister ISE #########################################################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Information_Science_and_Engineering":
                table_frame8=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame8.place(x=10,y=120) 

################################################################################################
                def add_ise_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ise_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame8)
                    else:
                        if self.var_ise_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame8)
                        else:
                            if self.var_ise_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame8)
                            else:
                                cur.execute('insert into add_ise_3rd_semsiter_faculty(ise_3rd_semister_faculty_name,ise_3rd_semister_faculty_branch,ise_3rd_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ise_3rd_semister_faculty_name.get(),
                                self.var_ise_3rd_semister_faculty_branch.get(),
                                self.var_ise_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ise_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame8)
                def fetch_ise_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ise_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ise_3rd_semister_faculty_data_table.delete(*self.ise_3rd_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ise_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame8)

                def ise_3rd_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame8)
                        else:
                            cur.execute(f"select * from add_ise_3rd_semsiter_faculty where ise_3rd_semister_faculty_name LIKE '%{self.var_ise_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ise_3rd_semister_faculty_data_table.delete(*self.ise_3rd_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ise_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame8)
                def ise_3rd_semister_faculty_data_get(ev):
                    r1=self.ise_3rd_semister_faculty_data_table.focus()
                    content1=self.ise_3rd_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ise_3rd_semister_faculty_name.set(row1[0])
                    self.var_ise_3rd_semister_faculty_branch.set(row1[1])
                    self.var_ise_3rd_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame8)

                def ise_3rd_semister_faculty_data_clear():
                    fetch_ise_3rd_semister_faculty_data()
                    self.var_ise_3rd_semister_faculty_serch.set("")
                    self.var_ise_3rd_semister_faculty_name.set("")
                    self.var_ise_3rd_semister_faculty_branch.set("")
                    self.var_ise_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame8)
                def ise_3rd_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame8)
                        else:
                            cur.execute("select * from add_ise_3rd_semsiter_faculty where ise_3rd_semister_faculty_name=%s",(self.var_ise_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame8)
                            else:
                                cur.execute("update add_ise_3rd_semsiter_faculty set ise_3rd_semister_faculty_branch=%s,ise_3rd_semister_faculty_subject=%s where ise_3rd_semister_faculty_name=%s",(
                                    
                                    self.var_ise_3rd_semister_faculty_branch.get(),
                                    self.var_ise_3rd_semister_faculty_subject.get(),
                                    self.var_ise_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame8)
                                fetch_ise_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame8)
                def ise_3rd_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame8)
                        else:
                            cur.execute("select * from add_ise_3rd_semsiter_faculty where ise_3rd_semister_faculty_name=%s",(self.var_ise_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame8)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame8)
                                if option==True:
                                    cur.execute('delete from add_ise_3rd_semsiter_faculty where ise_3rd_semister_faculty_name=%s',(self.var_ise_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame8)
                                    ise_3rd_semister_faculty_data_clear()
                                    fetch_ise_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame8)
                
################################################################################################

                label11=Label(table_frame8,text='3rd Semister ISE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame8,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame8,width=29,textvariable=self.var_ise_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame8,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame8,width=29,textvariable=self.var_ise_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame8,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame8,width=29,textvariable=self.var_ise_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame8,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ise_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ise_3rd_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ise_3rd_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ise_3rd_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ise_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ise_3rd_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ise_3rd_semister_facuty_table_frame=Frame(table_frame8,width=800,height=200,relief=GROOVE)
                self.ise_3rd_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ise_3rd_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ise_3rd_semister_facuty_table_frame,orient=VERTICAL)
                self.ise_3rd_semister_faculty_data_table=ttk.Treeview(self.ise_3rd_semister_facuty_table_frame,columns=('ise_3rd_semister_faculty_name','ise_3rd_semister_faculty_branch','ise_3rd_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ise_3rd_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ise_3rd_semister_faculty_data_table.yview)

               
                self.ise_3rd_semister_faculty_data_table.heading('ise_3rd_semister_faculty_name',text='Faculty Name ')
                self.ise_3rd_semister_faculty_data_table.heading('ise_3rd_semister_faculty_branch',text='Faculty Branch ')
                self.ise_3rd_semister_faculty_data_table.heading('ise_3rd_semister_faculty_subject',text='Faculty Subject ')

               
                self.ise_3rd_semister_faculty_data_table.column('ise_3rd_semister_faculty_name',width=210)
                self.ise_3rd_semister_faculty_data_table.column('ise_3rd_semister_faculty_branch',width=300)
                self.ise_3rd_semister_faculty_data_table.column('ise_3rd_semister_faculty_subject',width=270)

                self.ise_3rd_semister_faculty_data_table['show']='headings'

                self.ise_3rd_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ise_3rd_semister_faculty_data()
                self.ise_3rd_semister_faculty_data_table.bind('<ButtonRelease-1>',ise_3rd_semister_faculty_data_get)
         ############################################# 3rd semister ETE #########################################################################################################################
        if self.var_sem_select.get()=="3rd_Semister":
            if self.var_branch_select.get() == "Electronic_And_Telecommunication_Engineering":
                table_frame9=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame9.place(x=10,y=120) 

################################################################################################
                def add_ete_3rd_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ete_3rd_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame9)
                    else:
                        if self.var_ete_3rd_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame9)
                        else:
                            if self.var_ete_3rd_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame9)
                            else:
                                cur.execute('insert into add_ete_3rd_semsiter_faculty(ete_3rd_semister_faculty_name,ete_3rd_semister_faculty_branch,ete_3rd_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ete_3rd_semister_faculty_name.get(),
                                self.var_ete_3rd_semister_faculty_branch.get(),
                                self.var_ete_3rd_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ete_3rd_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame9)
                def fetch_ete_3rd_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ete_3rd_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ete_3rd_semister_faculty_data_table.delete(*self.ete_3rd_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ete_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame9)

                def ete_3rd_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_3rd_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame9)
                        else:
                            cur.execute(f"select * from add_ete_3rd_semsiter_faculty where ete_3rd_semister_faculty_name LIKE '%{self.var_ete_3rd_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ete_3rd_semister_faculty_data_table.delete(*self.ete_3rd_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ete_3rd_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame9)
                def ete_3rd_semister_faculty_data_get(ev):
                    r1=self.ete_3rd_semister_faculty_data_table.focus()
                    content1=self.ete_3rd_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ete_3rd_semister_faculty_name.set(row1[0])
                    self.var_ete_3rd_semister_faculty_branch.set(row1[1])
                    self.var_ete_3rd_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame9)

                def ete_3rd_semister_faculty_data_clear():
                    fetch_ete_3rd_semister_faculty_data()
                    self.var_ete_3rd_semister_faculty_serch.set("")
                    self.var_ete_3rd_semister_faculty_name.set("")
                    self.var_ete_3rd_semister_faculty_branch.set("")
                    self.var_ete_3rd_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame9)
                def ete_3rd_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame9)
                        else:
                            cur.execute("select * from add_ete_3rd_semsiter_faculty where ete_3rd_semister_faculty_name=%s",(self.var_ete_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame9)
                            else:
                                cur.execute("update add_ete_3rd_semsiter_faculty set ete_3rd_semister_faculty_branch=%s,ete_3rd_semister_faculty_subject=%s where ete_3rd_semister_faculty_name=%s",(
                                    
                                    self.var_ete_3rd_semister_faculty_branch.get(),
                                    self.var_ete_3rd_semister_faculty_subject.get(),
                                    self.var_ete_3rd_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame9)
                                fetch_ete_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame9)
                def ete_3rd_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_3rd_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame9)
                        else:
                            cur.execute("select * from add_ete_3rd_semsiter_faculty where ete_3rd_semister_faculty_name=%s",(self.var_ete_3rd_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame9)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame9)
                                if option==True:
                                    cur.execute('delete from add_ete_3rd_semsiter_faculty where ete_3rd_semister_faculty_name=%s',(self.var_ete_3rd_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame9)
                                    ete_3rd_semister_faculty_data_clear()
                                    fetch_ete_3rd_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame9)
                
################################################################################################

                label11=Label(table_frame9,text='3rd Semister ETE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame9,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame9,width=29,textvariable=self.var_ete_3rd_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame9,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame9,width=29,textvariable=self.var_ete_3rd_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    '1sr semister',
                                    '2nd_semister',
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame9,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame9,width=29,textvariable=self.var_ete_3rd_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame9,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ete_3rd_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ete_3rd_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ete_3rd_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ete_3rd_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ete_3rd_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ete_3rd_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ete_3rd_semister_facuty_table_frame=Frame(table_frame9,width=800,height=200,relief=GROOVE)
                self.ete_3rd_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ete_3rd_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ete_3rd_semister_facuty_table_frame,orient=VERTICAL)
                self.ete_3rd_semister_faculty_data_table=ttk.Treeview(self.ete_3rd_semister_facuty_table_frame,columns=('ete_3rd_semister_faculty_name','ete_3rd_semister_faculty_branch','ete_3rd_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ete_3rd_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ete_3rd_semister_faculty_data_table.yview)

                self.ete_3rd_semister_faculty_data_table.heading('ete_3rd_semister_faculty_name',text='Faculty Name ')
                self.ete_3rd_semister_faculty_data_table.heading('ete_3rd_semister_faculty_branch',text='Faculty Branch ')
                self.ete_3rd_semister_faculty_data_table.heading('ete_3rd_semister_faculty_subject',text='Faculty Subject ')

                self.ete_3rd_semister_faculty_data_table.column('ete_3rd_semister_faculty_name',width=210)
                self.ete_3rd_semister_faculty_data_table.column('ete_3rd_semister_faculty_branch',width=300)
                self.ete_3rd_semister_faculty_data_table.column('ete_3rd_semister_faculty_subject',width=270)

                self.ete_3rd_semister_faculty_data_table['show']='headings'

                self.ete_3rd_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ete_3rd_semister_faculty_data()
                self.ete_3rd_semister_faculty_data_table.bind('<ButtonRelease-1>',ete_3rd_semister_faculty_data_get)
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
###########################################################4th semister #########################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Civil_Engineering":
                table_frame10=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame10.place(x=10,y=120) 

################################################################################################
                def add_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame10)
                    else:
                        if self.var_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame10)
                        else:
                            if self.var_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame10)
                            else:
                                cur.execute('insert into add_4th_semsiter_faculty(rd4_semister_faculty_name,rd4_semister_faculty_branch,rd4_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_4th_semister_faculty_name.get(),
                                self.var_4th_semister_faculty_branch.get(),
                                self.var_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame10)
                def fetch_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.rd4_semister_faculty_data_table.delete(*self.rd4_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.rd4_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame10)

                def rd4_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame10)
                        else:
                            cur.execute(f"select * from add_4th_semsiter_faculty where rd4_semister_faculty_name LIKE '%{self.var_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.rd4_semister_faculty_data_table.delete(*self.rd4_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.rd4_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame10)
                def rd4_semister_faculty_data_get(ev):
                    r1=self.rd4_semister_faculty_data_table.focus()
                    content1=self.rd4_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_4th_semister_faculty_name.set(row1[0])
                    self.var_4th_semister_faculty_branch.set(row1[1])
                    self.var_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame10)

                def rd4_semister_faculty_data_clear():
                    fetch_4th_semister_faculty_data()
                    self.var_4th_semister_faculty_serch.set("")
                    self.var_4th_semister_faculty_name.set("")
                    self.var_4th_semister_faculty_branch.set("")
                    self.var_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame10)
                def rd4_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame10)
                        else:
                            cur.execute("select * from add_4th_semsiter_faculty where rd4_semister_faculty_name=%s",(self.var_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame10)
                            else:
                                cur.execute("update add_4th_semsiter_faculty set rd4_semister_faculty_branch=%s,rd4_semister_faculty_subject=%s where rd4_semister_faculty_name=%s",(
                                    
                                    self.var_4th_semister_faculty_branch.get(),
                                    self.var_4th_semister_faculty_subject.get(),
                                    self.var_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame10)
                                fetch_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame10)
                def rd4_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame10)
                        else:
                            cur.execute("select * from add_4th_semsiter_faculty where rd4_semister_faculty_name=%s",(self.var_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame10)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame10)
                                if option==True:
                                    cur.execute('delete from add_4th_semsiter_faculty where rd4_semister_faculty_name=%s',(self.var_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame10)
                                    rd4_semister_faculty_data_clear()
                                    fetch_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame10)
                
################################################################################################

                label11=Label(table_frame10,text='4th Semsiter civil:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame10,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame10,width=29,textvariable=self.var_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame10,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame10,width=29,textvariable=self.var_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame10,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame10,width=29,textvariable=self.var_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame10,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=rd4_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=rd4_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=rd4_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=rd4_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.rd4_semister_facuty_table_frame=Frame(table_frame10,width=800,height=200,relief=GROOVE)
                self.rd4_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.rd4_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.rd4_semister_facuty_table_frame,orient=VERTICAL)
                self.rd4_semister_faculty_data_table=ttk.Treeview(self.rd4_semister_facuty_table_frame,columns=('rd4_semister_faculty_name','rd4_semister_faculty_branch','rd4_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.rd4_semister_faculty_data_table.xview)
                scrolly.configure(command=self.rd4_semister_faculty_data_table.yview)

                
                self.rd4_semister_faculty_data_table.heading('rd4_semister_faculty_name',text='Faculty Name ')
                self.rd4_semister_faculty_data_table.heading('rd4_semister_faculty_branch',text='Faculty Branch ')
                self.rd4_semister_faculty_data_table.heading('rd4_semister_faculty_subject',text='Faculty Subject ')

                self.rd4_semister_faculty_data_table.column('rd4_semister_faculty_name',width=210)
                self.rd4_semister_faculty_data_table.column('rd4_semister_faculty_branch',width=300)
                self.rd4_semister_faculty_data_table.column('rd4_semister_faculty_subject',width=270)

                self.rd4_semister_faculty_data_table['show']='headings'

                self.rd4_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_4th_semister_faculty_data()
                self.rd4_semister_faculty_data_table.bind('<ButtonRelease-1>',rd4_semister_faculty_data_get)



        
############################################# 4th semister mech #########################################################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Mechanical_Engineering":
                table_frame11=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame11.place(x=10,y=120) 

################################################################################################
                def add_mech_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_mech_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame11)
                    else:
                        if self.var_mech_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame11)
                        else:
                            if self.var_mech_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame11)
                            else:
                                cur.execute('insert into add_mech_4th_semsiter_faculty(mech_4th_semister_faculty_name,mech_4th_semister_faculty_branch,mech_4th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_mech_4th_semister_faculty_name.get(),
                                self.var_mech_4th_semister_faculty_branch.get(),
                                self.var_mech_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_mech_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame11)
                def fetch_mech_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_mech_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.mech_4th_semister_faculty_data_table.delete(*self.mech_4th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.mech_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame11)

                def mech_4th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame11)
                        else:
                            cur.execute(f"select * from add_mech_4th_semsiter_faculty where mech_4th_semister_faculty_name LIKE '%{self.var_mech_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.mech_4th_semister_faculty_data_table.delete(*self.mech_4th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.mech_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame11)
                def mech_4th_semister_faculty_data_get(ev):
                    r1=self.mech_4th_semister_faculty_data_table.focus()
                    content1=self.mech_4th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_mech_4th_semister_faculty_name.set(row1[0])
                    self.var_mech_4th_semister_faculty_branch.set(row1[1])
                    self.var_mech_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame11)

                def mech_4th_semister_faculty_data_clear():
                    fetch_mech_4th_semister_faculty_data()
                    self.var_mech_4th_semister_faculty_serch.set("")
                    self.var_mech_4th_semister_faculty_name.set("")
                    self.var_mech_4th_semister_faculty_branch.set("")
                    self.var_mech_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame11)
                def mech_4th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame11)
                        else:
                            cur.execute("select * from add_mech_4th_semsiter_faculty where mech_4th_semister_faculty_name=%s",(self.var_mech_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame11)
                            else:
                                cur.execute("update add_mech_4th_semsiter_faculty set mech_4th_semister_faculty_branch=%s,mech_4th_semister_faculty_subject=%s where mech_4th_semister_faculty_name=%s",(
                                    
                                    self.var_mech_4th_semister_faculty_branch.get(),
                                    self.var_mech_4th_semister_faculty_subject.get(),
                                    self.var_mech_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame11)
                                fetch_mech_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame11)
                def mech_4th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame11)
                        else:
                            cur.execute("select * from add_mech_4th_semsiter_faculty where mech_4th_semister_faculty_name=%s",(self.var_mech_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame11)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame11)
                                if option==True:
                                    cur.execute('delete from add_mech_4th_semsiter_faculty where mech_4th_semister_faculty_name=%s',(self.var_mech_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame11)
                                    mech_4th_semister_faculty_data_clear()
                                    fetch_mech_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame11)
                
################################################################################################

                label11=Label(table_frame11,text='4th Semsiter MECH:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame11,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame11,width=29,textvariable=self.var_mech_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame11,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame11,width=29,textvariable=self.var_mech_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame11,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame11,width=29,textvariable=self.var_mech_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame11,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_mech_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=mech_4th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=mech_4th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=mech_4th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_mech_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=mech_4th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.mech_4th_semister_facuty_table_frame=Frame(table_frame11,width=800,height=200,relief=GROOVE)
                self.mech_4th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.mech_4th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.mech_4th_semister_facuty_table_frame,orient=VERTICAL)
                self.mech_4th_semister_faculty_data_table=ttk.Treeview(self.mech_4th_semister_facuty_table_frame,columns=('mech_4th_semister_faculty_name','mech_4th_semister_faculty_branch','mech_4th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.mech_4th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.mech_4th_semister_faculty_data_table.yview)


                self.mech_4th_semister_faculty_data_table.heading('mech_4th_semister_faculty_name',text='Faculty Name ')
                self.mech_4th_semister_faculty_data_table.heading('mech_4th_semister_faculty_branch',text='Faculty Branch ')
                self.mech_4th_semister_faculty_data_table.heading('mech_4th_semister_faculty_subject',text='Faculty Subject ')

                self.mech_4th_semister_faculty_data_table.column('mech_4th_semister_faculty_name',width=210)
                self.mech_4th_semister_faculty_data_table.column('mech_4th_semister_faculty_branch',width=300)
                self.mech_4th_semister_faculty_data_table.column('mech_4th_semister_faculty_subject',width=270)

                self.mech_4th_semister_faculty_data_table['show']='headings'

                self.mech_4th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_mech_4th_semister_faculty_data()
                self.mech_4th_semister_faculty_data_table.bind('<ButtonRelease-1>',mech_4th_semister_faculty_data_get)
################################################################################ Electrical_And_Electronic_Engineering ############################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Electrical_And_Electronic_Engineering":
                table_frame12=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame12.place(x=10,y=120) 

################################################################################################
                def add_eee_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_eee_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame12)
                    else:
                        if self.var_eee_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame12)
                        else:
                            if self.var_eee_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame12)
                            else:
                                cur.execute('insert into add_eee_4th_semsiter_faculty(eee_4th_semister_faculty_name,eee_4th_semister_faculty_branch,eee_4th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_eee_4th_semister_faculty_name.get(),
                                self.var_eee_4th_semister_faculty_branch.get(),
                                self.var_eee_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_eee_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame12)
                def fetch_eee_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_eee_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.eee_4th_semister_faculty_data_table.delete(*self.eee_4th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.eee_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame12)

                def eee_4th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame12)
                        else:
                            cur.execute(f"select * from add_eee_4th_semsiter_faculty where eee_4th_semister_faculty_name LIKE '%{self.var_eee_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.eee_4th_semister_faculty_data_table.delete(*self.eee_4th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.eee_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame12)
                def eee_4th_semister_faculty_data_get(ev):
                    r1=self.eee_4th_semister_faculty_data_table.focus()
                    content1=self.eee_4th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_eee_4th_semister_faculty_name.set(row1[0])
                    self.var_eee_4th_semister_faculty_branch.set(row1[1])
                    self.var_eee_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame12)

                def eee_4th_semister_faculty_data_clear():
                    fetch_eee_4th_semister_faculty_data()
                    self.var_eee_4th_semister_faculty_serch.set("")
                    self.var_eee_4th_semister_faculty_name.set("")
                    self.var_eee_4th_semister_faculty_branch.set("")
                    self.var_eee_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame12)
                def eee_4th_semister_faculty_data_update():
                    con=sqlite3.connect(database='StudentDataBase.db')
                    cur=con.cursor()
                    try:
                        if self.var_eee_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame12)
                        else:
                            cur.execute("select * from add_eee_4th_semsiter_faculty where eee_4th_semister_faculty_name=%s",(self.var_eee_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame12)
                            else:
                                cur.execute("update add_eee_4th_semsiter_faculty set eee_4th_semister_faculty_branch=%s,eee_4th_semister_faculty_subject=%s where eee_4th_semister_faculty_name=%s",(
                                    
                                    self.var_eee_4th_semister_faculty_branch.get(),
                                    self.var_eee_4th_semister_faculty_subject.get(),
                                    self.var_eee_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame12)
                                fetch_eee_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame12)
                def eee_4th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame12)
                        else:
                            cur.execute("select * from add_eee_4th_semsiter_faculty where eee_4th_semister_faculty_name=%s",(self.var_eee_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame12)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame12)
                                if option==True:
                                    cur.execute('delete from add_eee_4th_semsiter_faculty where eee_4th_semister_faculty_name=%s',(self.var_eee_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame12)
                                    eee_4th_semister_faculty_data_clear()
                                    fetch_eee_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame12)
                
################################################################################################

                label11=Label(table_frame12,text='4th Semsiter EEE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame12,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame12,width=29,textvariable=self.var_eee_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame12,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame12,width=29,textvariable=self.var_eee_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame12,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame12,width=29,textvariable=self.var_eee_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame12,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_eee_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=eee_4th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=eee_4th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=eee_4th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_eee_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=eee_4th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.eee_4th_semister_facuty_table_frame=Frame(table_frame12,width=800,height=200,relief=GROOVE)
                self.eee_4th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.eee_4th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.eee_4th_semister_facuty_table_frame,orient=VERTICAL)
                self.eee_4th_semister_faculty_data_table=ttk.Treeview(self.eee_4th_semister_facuty_table_frame,columns=('eee_4th_semister_faculty_name','eee_4th_semister_faculty_branch','eee_4th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.eee_4th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.eee_4th_semister_faculty_data_table.yview)

                
                self.eee_4th_semister_faculty_data_table.heading('eee_4th_semister_faculty_name',text='Faculty Name ')
                self.eee_4th_semister_faculty_data_table.heading('eee_4th_semister_faculty_branch',text='Faculty Branch ')
                self.eee_4th_semister_faculty_data_table.heading('eee_4th_semister_faculty_subject',text='Faculty Subject ')

            
                self.eee_4th_semister_faculty_data_table.column('eee_4th_semister_faculty_name',width=210)
                self.eee_4th_semister_faculty_data_table.column('eee_4th_semister_faculty_branch',width=300)
                self.eee_4th_semister_faculty_data_table.column('eee_4th_semister_faculty_subject',width=270)

                self.eee_4th_semister_faculty_data_table['show']='headings'

                self.eee_4th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_eee_4th_semister_faculty_data()
                self.eee_4th_semister_faculty_data_table.bind('<ButtonRelease-1>',eee_4th_semister_faculty_data_get)
        
############################################# 4th semister ece #########################################################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Communication_Engineering":
                table_frame13=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame13.place(x=10,y=120) 

################################################################################################
                def add_ece_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ece_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame13)
                    else:
                        if self.var_ece_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame13)
                        else:
                            if self.var_ece_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame13)
                            else:
                                cur.execute('insert into add_ece_4th_semsiter_faculty(ece_4th_semister_faculty_name,ece_4th_semister_faculty_branch,ece_4th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ece_4th_semister_faculty_name.get(),
                                self.var_ece_4th_semister_faculty_branch.get(),
                                self.var_ece_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ece_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame13)
                def fetch_ece_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ece_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ece_4th_semister_faculty_data_table.delete(*self.ece_4th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ece_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame13)

                def ece_4th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame13)
                        else:
                            cur.execute(f"select * from add_ece_4th_semsiter_faculty where ece_4th_semister_faculty_name LIKE '%{self.var_ece_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ece_4th_semister_faculty_data_table.delete(*self.ece_4th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ece_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame13)
                def ece_4th_semister_faculty_data_get(ev):
                    r1=self.ece_4th_semister_faculty_data_table.focus()
                    content1=self.ece_4th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ece_4th_semister_faculty_name.set(row1[0])
                    self.var_ece_4th_semister_faculty_branch.set(row1[1])
                    self.var_ece_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame13)

                def ece_4th_semister_faculty_data_clear():
                    fetch_ece_4th_semister_faculty_data()
                    self.var_ece_4th_semister_faculty_serch.set("")
                    self.var_ece_4th_semister_faculty_name.set("")
                    self.var_ece_4th_semister_faculty_branch.set("")
                    self.var_ece_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame13)
                def ece_4th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame13)
                        else:
                            cur.execute("select * from add_ece_4th_semsiter_faculty where ece_4th_semister_faculty_name=%s",(self.var_ece_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame13)
                            else:
                                cur.execute("update add_ece_4th_semsiter_faculty set ece_4th_semister_faculty_branch=%s,ece_4th_semister_faculty_subject=%s where ece_4th_semister_faculty_name=%s",(
                                    
                                    self.var_ece_4th_semister_faculty_branch.get(),
                                    self.var_ece_4th_semister_faculty_subject.get(),
                                    self.var_ece_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame13)
                                fetch_ece_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame13)
                def ece_4th_semister_faculty_data_delete():
                    c#on=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame13)
                        else:
                            cur.execute("select * from add_ece_4th_semsiter_faculty where ece_4th_semister_faculty_name=%s",(self.var_ece_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame13)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame13)
                                if option==True:
                                    cur.execute('delete from add_ece_4th_semsiter_faculty where ece_4th_semister_faculty_name=%s',(self.var_ece_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame13)
                                    ece_4th_semister_faculty_data_clear()
                                    fetch_ece_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame13)
                
################################################################################################

                label11=Label(table_frame13,text='4th Semister ECE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame13,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame13,width=29,textvariable=self.var_ece_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame13,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame13,width=29,textvariable=self.var_ece_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame13,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame13,width=29,textvariable=self.var_ece_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame13,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ece_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ece_4th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ece_4th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ece_4th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ece_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ece_4th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ece_4th_semister_facuty_table_frame=Frame(table_frame13,width=800,height=200,relief=GROOVE)
                self.ece_4th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ece_4th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ece_4th_semister_facuty_table_frame,orient=VERTICAL)
                self.ece_4th_semister_faculty_data_table=ttk.Treeview(self.ece_4th_semister_facuty_table_frame,columns=('ece_4th_semister_faculty_name','ece_4th_semister_faculty_branch','ece_4th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ece_4th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ece_4th_semister_faculty_data_table.yview)

              
                self.ece_4th_semister_faculty_data_table.heading('ece_4th_semister_faculty_name',text='Faculty Name ')
                self.ece_4th_semister_faculty_data_table.heading('ece_4th_semister_faculty_branch',text='Faculty Branch ')
                self.ece_4th_semister_faculty_data_table.heading('ece_4th_semister_faculty_subject',text='Faculty Subject ')

         
                self.ece_4th_semister_faculty_data_table.column('ece_4th_semister_faculty_name',width=210)
                self.ece_4th_semister_faculty_data_table.column('ece_4th_semister_faculty_branch',width=300)
                self.ece_4th_semister_faculty_data_table.column('ece_4th_semister_faculty_subject',width=270)

                self.ece_4th_semister_faculty_data_table['show']='headings'

                self.ece_4th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ece_4th_semister_faculty_data()
                self.ece_4th_semister_faculty_data_table.bind('<ButtonRelease-1>',ece_4th_semister_faculty_data_get)
        ############################################# 4th semister CS #########################################################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Computer_Science_Engineering":
                table_frame14=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame14.place(x=10,y=120) 

################################################################################################
                def add_cs_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_cs_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame14)
                    else:
                        if self.var_cs_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame14)
                        else:
                            if self.var_cs_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame14)
                            else:
                                cur.execute('insert into add_cs_4th_semsiter_faculty(cs_4th_semister_faculty_name,cs_4th_semister_faculty_branch,cs_4th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_cs_4th_semister_faculty_name.get(),
                                self.var_cs_4th_semister_faculty_branch.get(),
                                self.var_cs_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_cs_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame14)
                def fetch_cs_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_cs_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.cs_4th_semister_faculty_data_table.delete(*self.cs_4th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.cs_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame14)

                def cs_4th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame14)
                        else:
                            cur.execute(f"select * from add_cs_4th_semsiter_faculty where cs_4th_semister_faculty_name LIKE '%{self.var_cs_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.cs_4th_semister_faculty_data_table.delete(*self.cs_4th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.cs_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame14)
                def cs_4th_semister_faculty_data_get(ev):
                    r1=self.cs_4th_semister_faculty_data_table.focus()
                    content1=self.cs_4th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_cs_4th_semister_faculty_name.set(row1[0])
                    self.var_cs_4th_semister_faculty_branch.set(row1[1])
                    self.var_cs_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame14)

                def cs_4th_semister_faculty_data_clear():
                    fetch_cs_4th_semister_faculty_data()
                    self.var_cs_4th_semister_faculty_serch.set("")
                    self.var_cs_4th_semister_faculty_name.set("")
                    self.var_cs_4th_semister_faculty_branch.set("")
                    self.var_cs_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame14)
                def cs_4th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame14)
                        else:
                            cur.execute("select * from add_cs_4th_semsiter_faculty where cs_4th_semister_faculty_name=%s",(self.var_cs_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame14)
                            else:
                                cur.execute("update add_cs_4th_semsiter_faculty set cs_4th_semister_faculty_branch=%s,cs_4th_semister_faculty_subject=%s where cs_4th_semister_faculty_name=%s",(
                                    
                                    self.var_cs_4th_semister_faculty_branch.get(),
                                    self.var_cs_4th_semister_faculty_subject.get(),
                                    self.var_cs_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame14)
                                fetch_cs_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame14)
                def cs_4th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame14)
                        else:
                            cur.execute("select * from add_cs_4th_semsiter_faculty where cs_4th_semister_faculty_name=%s",(self.var_cs_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame14)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame14)
                                if option==True:
                                    cur.execute('delete from add_cs_4th_semsiter_faculty where cs_4th_semister_faculty_name=%s',(self.var_cs_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame14)
                                    cs_4th_semister_faculty_data_clear()
                                    fetch_cs_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame14)
                
################################################################################################

                label11=Label(table_frame14,text='4th Semister CS:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame14,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame14,width=29,textvariable=self.var_cs_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame14,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame14,width=29,textvariable=self.var_cs_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame14,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame14,width=29,textvariable=self.var_cs_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame14,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_cs_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=cs_4th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=cs_4th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=cs_4th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_cs_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=cs_4th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.cs_4th_semister_facuty_table_frame=Frame(table_frame14,width=800,height=200,relief=GROOVE)
                self.cs_4th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.cs_4th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.cs_4th_semister_facuty_table_frame,orient=VERTICAL)
                self.cs_4th_semister_faculty_data_table=ttk.Treeview(self.cs_4th_semister_facuty_table_frame,columns=('cs_4th_semister_faculty_name','cs_4th_semister_faculty_branch','cs_4th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.cs_4th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.cs_4th_semister_faculty_data_table.yview)

         
                self.cs_4th_semister_faculty_data_table.heading('cs_4th_semister_faculty_name',text='Faculty Name ')
                self.cs_4th_semister_faculty_data_table.heading('cs_4th_semister_faculty_branch',text='Faculty Branch ')
                self.cs_4th_semister_faculty_data_table.heading('cs_4th_semister_faculty_subject',text='Faculty Subject ')

                
                self.cs_4th_semister_faculty_data_table.column('cs_4th_semister_faculty_name',width=210)
                self.cs_4th_semister_faculty_data_table.column('cs_4th_semister_faculty_branch',width=300)
                self.cs_4th_semister_faculty_data_table.column('cs_4th_semister_faculty_subject',width=270)

                self.cs_4th_semister_faculty_data_table['show']='headings'

                self.cs_4th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_cs_4th_semister_faculty_data()
                self.cs_4th_semister_faculty_data_table.bind('<ButtonRelease-1>',cs_4th_semister_faculty_data_get)
 ############################################# 4th semister ISE #########################################################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Information_Science_and_Engineering":
                table_frame15=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame15.place(x=10,y=120) 

################################################################################################
                def add_ise_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ise_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame15)
                    else:
                        if self.var_ise_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame15)
                        else:
                            if self.var_ise_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame15)
                            else:
                                cur.execute('insert into add_ise_4th_semsiter_faculty(ise_4th_semister_faculty_name,ise_4th_semister_faculty_branch,ise_4th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ise_4th_semister_faculty_name.get(),
                                self.var_ise_4th_semister_faculty_branch.get(),
                                self.var_ise_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ise_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame15)
                def fetch_ise_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ise_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ise_4th_semister_faculty_data_table.delete(*self.ise_4th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ise_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame15)

                def ise_4th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame15)
                        else:
                            cur.execute(f"select * from add_ise_4th_semsiter_faculty where ise_4th_semister_faculty_name LIKE '%{self.var_ise_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ise_4th_semister_faculty_data_table.delete(*self.ise_4th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ise_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame15)
                def ise_4th_semister_faculty_data_get(ev):
                    r1=self.ise_4th_semister_faculty_data_table.focus()
                    content1=self.ise_4th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ise_4th_semister_faculty_name.set(row1[0])
                    self.var_ise_4th_semister_faculty_branch.set(row1[1])
                    self.var_ise_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame15)

                def ise_4th_semister_faculty_data_clear():
                    fetch_ise_4th_semister_faculty_data()
                    self.var_ise_4th_semister_faculty_serch.set("")
                    self.var_ise_4th_semister_faculty_name.set("")
                    self.var_ise_4th_semister_faculty_branch.set("")
                    self.var_ise_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame15)
                def ise_4th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame15)
                        else:
                            cur.execute("select * from add_ise_4th_semsiter_faculty where ise_4th_semister_faculty_name=%s",(self.var_ise_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame15)
                            else:
                                cur.execute("update add_ise_4th_semsiter_faculty set ise_4th_semister_faculty_branch=%s,ise_4th_semister_faculty_subject=%s where ise_4th_semister_faculty_name=%s",(
                                    
                                    self.var_ise_4th_semister_faculty_branch.get(),
                                    self.var_ise_4th_semister_faculty_subject.get(),
                                    self.var_ise_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame15)
                                fetch_ise_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame15)
                def ise_4th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame15)
                        else:
                            cur.execute("select * from add_ise_4th_semsiter_faculty where ise_4th_semister_faculty_name=%s",(self.var_ise_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame15)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame15)
                                if option==True:
                                    cur.execute('delete from add_ise_4th_semsiter_faculty where ise_4th_semister_faculty_name=%s',(self.var_ise_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame15)
                                    ise_4th_semister_faculty_data_clear()
                                    fetch_ise_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame15)
                
################################################################################################

                label11=Label(table_frame15,text='4th Semister ISE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame15,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame15,width=29,textvariable=self.var_ise_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame15,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame15,width=29,textvariable=self.var_ise_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame15,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame15,width=29,textvariable=self.var_ise_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame15,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ise_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ise_4th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ise_4th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ise_4th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ise_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ise_4th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ise_4th_semister_facuty_table_frame=Frame(table_frame15,width=800,height=200,relief=GROOVE)
                self.ise_4th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ise_4th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ise_4th_semister_facuty_table_frame,orient=VERTICAL)
                self.ise_4th_semister_faculty_data_table=ttk.Treeview(self.ise_4th_semister_facuty_table_frame,columns=('ise_4th_semister_faculty_name','ise_4th_semister_faculty_branch','ise_4th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ise_4th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ise_4th_semister_faculty_data_table.yview)

                
                self.ise_4th_semister_faculty_data_table.heading('ise_4th_semister_faculty_name',text='Faculty Name ')
                self.ise_4th_semister_faculty_data_table.heading('ise_4th_semister_faculty_branch',text='Faculty Branch ')
                self.ise_4th_semister_faculty_data_table.heading('ise_4th_semister_faculty_subject',text='Faculty Subject ')

                self.ise_4th_semister_faculty_data_table.column('ise_4th_semister_faculty_name',width=210)
                self.ise_4th_semister_faculty_data_table.column('ise_4th_semister_faculty_branch',width=300)
                self.ise_4th_semister_faculty_data_table.column('ise_4th_semister_faculty_subject',width=270)

                self.ise_4th_semister_faculty_data_table['show']='headings'

                self.ise_4th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ise_4th_semister_faculty_data()
                self.ise_4th_semister_faculty_data_table.bind('<ButtonRelease-1>',ise_4th_semister_faculty_data_get)
         ############################################# 4th semister ETE #########################################################################################################################
        if self.var_sem_select.get()=="4th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Telecommunication_Engineering":
                table_frame16=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame16.place(x=10,y=120) 

################################################################################################
                def add_ete_4th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ete_4th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame16)
                    else:
                        if self.var_ete_4th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame16)
                        else:
                            if self.var_ete_4th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame16)
                            else:
                                cur.execute('insert into add_ete_4th_semsiter_faculty(ete_4th_semister_faculty_name,ete_4th_semister_faculty_branch,ete_4th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ete_4th_semister_faculty_name.get(),
                                self.var_ete_4th_semister_faculty_branch.get(),
                                self.var_ete_4th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ete_4th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame16)
                def fetch_ete_4th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ete_4th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ete_4th_semister_faculty_data_table.delete(*self.ete_4th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ete_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame16)

                def ete_4th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_4th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame16)
                        else:
                            cur.execute(f"select * from add_ete_4th_semsiter_faculty where ete_4th_semister_faculty_name LIKE '%{self.var_ete_4th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ete_4th_semister_faculty_data_table.delete(*self.ete_4th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ete_4th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame16)
                def ete_4th_semister_faculty_data_get(ev):
                    r1=self.ete_4th_semister_faculty_data_table.focus()
                    content1=self.ete_4th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ete_4th_semister_faculty_name.set(row1[0])
                    self.var_ete_4th_semister_faculty_branch.set(row1[1])
                    self.var_ete_4th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame16)

                def ete_4th_semister_faculty_data_clear():
                    fetch_ete_4th_semister_faculty_data()
                    self.var_ete_4th_semister_faculty_serch.set("")
                    self.var_ete_4th_semister_faculty_name.set("")
                    self.var_ete_4th_semister_faculty_branch.set("")
                    self.var_ete_4th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame16)
                def ete_4th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame16)
                        else:
                            cur.execute("select * from add_ete_4th_semsiter_faculty where ete_4th_semister_faculty_name=%s",(self.var_ete_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame16)
                            else:
                                cur.execute("update add_ete_4th_semsiter_faculty set ete_4th_semister_faculty_branch=%s,ete_4th_semister_faculty_subject=%s where ete_4th_semister_faculty_name=%s",(
                                    
                                    self.var_ete_4th_semister_faculty_branch.get(),
                                    self.var_ete_4th_semister_faculty_subject.get(),
                                    self.var_ete_4th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame16)
                                fetch_ete_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame16)
                def ete_4th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_4th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame16)
                        else:
                            cur.execute("select * from add_ete_4th_semsiter_faculty where ete_4th_semister_faculty_name=%s",(self.var_ete_4th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame16)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame16)
                                if option==True:
                                    cur.execute('delete from add_ete_4th_semsiter_faculty where ete_4th_semister_faculty_name=%s',(self.var_ete_4th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame16)
                                    ete_4th_semister_faculty_data_clear()
                                    fetch_ete_4th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame16)
                
################################################################################################

                label11=Label(table_frame16,text='4th Semister ETE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame16,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame16,width=29,textvariable=self.var_ete_4th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame16,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame16,width=29,textvariable=self.var_ete_4th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame16,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame16,width=29,textvariable=self.var_ete_4th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame16,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ete_4th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ete_4th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ete_4th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ete_4th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ete_4th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ete_4th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ete_4th_semister_facuty_table_frame=Frame(table_frame16,width=800,height=200,relief=GROOVE)
                self.ete_4th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ete_4th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ete_4th_semister_facuty_table_frame,orient=VERTICAL)
                self.ete_4th_semister_faculty_data_table=ttk.Treeview(self.ete_4th_semister_facuty_table_frame,columns=('ete_4th_semister_faculty_name','ete_4th_semister_faculty_branch','ete_4th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ete_4th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ete_4th_semister_faculty_data_table.yview)

      
                self.ete_4th_semister_faculty_data_table.heading('ete_4th_semister_faculty_name',text='Faculty Name ')
                self.ete_4th_semister_faculty_data_table.heading('ete_4th_semister_faculty_branch',text='Faculty Branch ')
                self.ete_4th_semister_faculty_data_table.heading('ete_4th_semister_faculty_subject',text='Faculty Subject ')

                self.ete_4th_semister_faculty_data_table.column('ete_4th_semister_faculty_name',width=210)
                self.ete_4th_semister_faculty_data_table.column('ete_4th_semister_faculty_branch',width=300)
                self.ete_4th_semister_faculty_data_table.column('ete_4th_semister_faculty_subject',width=270)

                self.ete_4th_semister_faculty_data_table['show']='headings'

                self.ete_4th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ete_4th_semister_faculty_data()
                self.ete_4th_semister_faculty_data_table.bind('<ButtonRelease-1>',ete_4th_semister_faculty_data_get)
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
##########################################################  5th semister #########################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Civil_Engineering":
                table_frame17=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame17.place(x=10,y=120) 

################################################################################################
                def add_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame17)
                    else:
                        if self.var_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame17)
                        else:
                            if self.var_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame17)
                            else:
                                cur.execute('insert into add_5th_semsiter_faculty(rd5_semister_faculty_name,rd5_semister_faculty_branch,rd5_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_5th_semister_faculty_name.get(),
                                self.var_5th_semister_faculty_branch.get(),
                                self.var_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame17)
                def fetch_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.rd5_semister_faculty_data_table.delete(*self.rd5_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.rd5_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame17)

                def rd5_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame17)
                        else:
                            cur.execute(f"select * from add_5th_semsiter_faculty where rd5_semister_faculty_name LIKE '%{self.var_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.rd5_semister_faculty_data_table.delete(*self.rd5_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.rd5_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame17)
                def rd5_semister_faculty_data_get(ev):
                    r1=self.rd5_semister_faculty_data_table.focus()
                    content1=self.rd5_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_5th_semister_faculty_name.set(row1[0])
                    self.var_5th_semister_faculty_branch.set(row1[1])
                    self.var_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame17)

                def rd5_semister_faculty_data_clear():
                    fetch_5th_semister_faculty_data()
                    self.var_5th_semister_faculty_serch.set("")
                    self.var_5th_semister_faculty_name.set("")
                    self.var_5th_semister_faculty_branch.set("")
                    self.var_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame17)
                def rd5_semister_faculty_data_update():
                    c#on=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame17)
                        else:
                            cur.execute("select * from add_5th_semsiter_faculty where rd5_semister_faculty_name=%s",(self.var_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame17)
                            else:
                                cur.execute("update add_5th_semsiter_faculty set rd5_semister_faculty_branch=%s,rd5_semister_faculty_subject=%s where rd5_semister_faculty_name=%s",(
                                    
                                    self.var_5th_semister_faculty_branch.get(),
                                    self.var_5th_semister_faculty_subject.get(),
                                    self.var_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame17)
                                fetch_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame17)
                def rd5_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame17)
                        else:
                            cur.execute("select * from add_5th_semsiter_faculty where rd5_semister_faculty_name=%s",(self.var_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame17)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame17)
                                if option==True:
                                    cur.execute('delete from add_5th_semsiter_faculty where rd5_semister_faculty_name=%s',(self.var_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame17)
                                    rd5_semister_faculty_data_clear()
                                    fetch_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame17)
                
################################################################################################

                label11=Label(table_frame17,text='5th Semsiter civil:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame17,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame17,width=29,textvariable=self.var_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame17,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame17,width=29,textvariable=self.var_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame17,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame17,width=29,textvariable=self.var_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame17,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=rd5_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=rd5_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=rd5_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=rd5_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.rd5_semister_facuty_table_frame=Frame(table_frame17,width=800,height=200,relief=GROOVE)
                self.rd5_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.rd5_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.rd5_semister_facuty_table_frame,orient=VERTICAL)
                self.rd5_semister_faculty_data_table=ttk.Treeview(self.rd5_semister_facuty_table_frame,columns=('rd5_semister_faculty_name','rd5_semister_faculty_branch','rd5_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.rd5_semister_faculty_data_table.xview)
                scrolly.configure(command=self.rd5_semister_faculty_data_table.yview)


                self.rd5_semister_faculty_data_table.heading('rd5_semister_faculty_name',text='Faculty Name ')
                self.rd5_semister_faculty_data_table.heading('rd5_semister_faculty_branch',text='Faculty Branch ')
                self.rd5_semister_faculty_data_table.heading('rd5_semister_faculty_subject',text='Faculty Subject ')

                self.rd5_semister_faculty_data_table.column('rd5_semister_faculty_name',width=210)
                self.rd5_semister_faculty_data_table.column('rd5_semister_faculty_branch',width=300)
                self.rd5_semister_faculty_data_table.column('rd5_semister_faculty_subject',width=270)

                self.rd5_semister_faculty_data_table['show']='headings'

                self.rd5_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_5th_semister_faculty_data()
                self.rd5_semister_faculty_data_table.bind('<ButtonRelease-1>',rd5_semister_faculty_data_get)



        
############################################# 5th semister mech #########################################################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Mechanical_Engineering":
                table_frame18=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame18.place(x=10,y=120) 

################################################################################################
                def add_mech_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_mech_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame18)
                    else:
                        if self.var_mech_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame18)
                        else:
                            if self.var_mech_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame18)
                            else:
                                cur.execute('insert into add_mech_5th_semsiter_faculty(mech_5th_semister_faculty_name,mech_5th_semister_faculty_branch,mech_5th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_mech_5th_semister_faculty_name.get(),
                                self.var_mech_5th_semister_faculty_branch.get(),
                                self.var_mech_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_mech_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame18)
                def fetch_mech_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_mech_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.mech_5th_semister_faculty_data_table.delete(*self.mech_5th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.mech_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame18)

                def mech_5th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame18)
                        else:
                            cur.execute(f"select * from add_mech_5th_semsiter_faculty where mech_5th_semister_faculty_name LIKE '%{self.var_mech_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.mech_5th_semister_faculty_data_table.delete(*self.mech_5th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.mech_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame18)
                def mech_5th_semister_faculty_data_get(ev):
                    r1=self.mech_5th_semister_faculty_data_table.focus()
                    content1=self.mech_5th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_mech_5th_semister_faculty_name.set(row1[0])
                    self.var_mech_5th_semister_faculty_branch.set(row1[1])
                    self.var_mech_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame18)

                def mech_5th_semister_faculty_data_clear():
                    fetch_mech_5th_semister_faculty_data()
                    self.var_mech_5th_semister_faculty_serch.set("")
                    self.var_mech_5th_semister_faculty_name.set("")
                    self.var_mech_5th_semister_faculty_branch.set("")
                    self.var_mech_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame18)
                def mech_5th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame18)
                        else:
                            cur.execute("select * from add_mech_5th_semsiter_faculty where mech_5th_semister_faculty_name=%s",(self.var_mech_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame18)
                            else:
                                cur.execute("update add_mech_5th_semsiter_faculty set mech_5th_semister_faculty_branch=%s,mech_5th_semister_faculty_subject=%s where mech_5th_semister_faculty_name=%s",(
                                    
                                    self.var_mech_5th_semister_faculty_branch.get(),
                                    self.var_mech_5th_semister_faculty_subject.get(),
                                    self.var_mech_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame18)
                                fetch_mech_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame18)
                def mech_5th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame18)
                        else:
                            cur.execute("select * from add_mech_5th_semsiter_faculty where mech_5th_semister_faculty_name=%s",(self.var_mech_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame18)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame18)
                                if option==True:
                                    cur.execute('delete from add_mech_5th_semsiter_faculty where mech_5th_semister_faculty_name=%s',(self.var_mech_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame18)
                                    mech_5th_semister_faculty_data_clear()
                                    fetch_mech_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame18)
                
################################################################################################

                label11=Label(table_frame18,text='5th Semsiter MECH:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame18,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame18,width=29,textvariable=self.var_mech_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame18,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame18,width=29,textvariable=self.var_mech_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame18,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame18,width=29,textvariable=self.var_mech_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame18,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_mech_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=mech_5th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=mech_5th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=mech_5th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_mech_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=mech_5th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.mech_5th_semister_facuty_table_frame=Frame(table_frame18,width=800,height=200,relief=GROOVE)
                self.mech_5th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.mech_5th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.mech_5th_semister_facuty_table_frame,orient=VERTICAL)
                self.mech_5th_semister_faculty_data_table=ttk.Treeview(self.mech_5th_semister_facuty_table_frame,columns=('mech_5th_semister_faculty_name','mech_5th_semister_faculty_branch','mech_5th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.mech_5th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.mech_5th_semister_faculty_data_table.yview)

           
                self.mech_5th_semister_faculty_data_table.heading('mech_5th_semister_faculty_name',text='Faculty Name ')
                self.mech_5th_semister_faculty_data_table.heading('mech_5th_semister_faculty_branch',text='Faculty Branch ')
                self.mech_5th_semister_faculty_data_table.heading('mech_5th_semister_faculty_subject',text='Faculty Subject ')

               
                self.mech_5th_semister_faculty_data_table.column('mech_5th_semister_faculty_name',width=210)
                self.mech_5th_semister_faculty_data_table.column('mech_5th_semister_faculty_branch',width=300)
                self.mech_5th_semister_faculty_data_table.column('mech_5th_semister_faculty_subject',width=270)

                self.mech_5th_semister_faculty_data_table['show']='headings'

                self.mech_5th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_mech_5th_semister_faculty_data()
                self.mech_5th_semister_faculty_data_table.bind('<ButtonRelease-1>',mech_5th_semister_faculty_data_get)
################################################################################ Electrical_And_Electronic_Engineering ############################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Electrical_And_Electronic_Engineering":
                table_frame19=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame19.place(x=10,y=120) 

################################################################################################
                def add_eee_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_eee_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame19)
                    else:
                        if self.var_eee_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame19)
                        else:
                            if self.var_eee_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame19)
                            else:
                                cur.execute('insert into add_eee_5th_semsiter_faculty(eee_5th_semister_faculty_name,eee_5th_semister_faculty_branch,eee_5th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_eee_5th_semister_faculty_name.get(),
                                self.var_eee_5th_semister_faculty_branch.get(),
                                self.var_eee_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_eee_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame19)
                def fetch_eee_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_eee_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.eee_5th_semister_faculty_data_table.delete(*self.eee_5th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.eee_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame19)

                def eee_5th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame19)
                        else:
                            cur.execute(f"select * from add_eee_5th_semsiter_faculty where eee_5th_semister_faculty_name LIKE '%{self.var_eee_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.eee_5th_semister_faculty_data_table.delete(*self.eee_5th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.eee_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame19)
                def eee_5th_semister_faculty_data_get(ev):
                    r1=self.eee_5th_semister_faculty_data_table.focus()
                    content1=self.eee_5th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_eee_5th_semister_faculty_name.set(row1[0])
                    self.var_eee_5th_semister_faculty_branch.set(row1[1])
                    self.var_eee_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame19)

                def eee_5th_semister_faculty_data_clear():
                    fetch_eee_5th_semister_faculty_data()
                    self.var_eee_5th_semister_faculty_serch.set("")
                    self.var_eee_5th_semister_faculty_name.set("")
                    self.var_eee_5th_semister_faculty_branch.set("")
                    self.var_eee_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame19)
                def eee_5th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame19)
                        else:
                            cur.execute("select * from add_eee_5th_semsiter_faculty where eee_5th_semister_faculty_name=%s",(self.var_eee_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame19)
                            else:
                                cur.execute("update add_eee_5th_semsiter_faculty set eee_5th_semister_faculty_branch=%s,eee_5th_semister_faculty_subject=%s where eee_5th_semister_faculty_name=%s",(
                                    
                                    self.var_eee_5th_semister_faculty_branch.get(),
                                    self.var_eee_5th_semister_faculty_subject.get(),
                                    self.var_eee_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame19)
                                fetch_eee_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame19)
                def eee_5th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame19)
                        else:
                            cur.execute("select * from add_eee_5th_semsiter_faculty where eee_5th_semister_faculty_name=%s",(self.var_eee_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame19)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame19)
                                if option==True:
                                    cur.execute('delete from add_eee_5th_semsiter_faculty where eee_5th_semister_faculty_name=%s',(self.var_eee_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame19)
                                    eee_5th_semister_faculty_data_clear()
                                    fetch_eee_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame19)
                
################################################################################################

                label11=Label(table_frame19,text='5th Semsiter EEE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame19,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame19,width=29,textvariable=self.var_eee_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame19,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame19,width=29,textvariable=self.var_eee_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame19,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame19,width=29,textvariable=self.var_eee_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame19,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_eee_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=eee_5th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=eee_5th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=eee_5th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_eee_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=eee_5th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.eee_5th_semister_facuty_table_frame=Frame(table_frame19,width=800,height=200,relief=GROOVE)
                self.eee_5th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.eee_5th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.eee_5th_semister_facuty_table_frame,orient=VERTICAL)
                self.eee_5th_semister_faculty_data_table=ttk.Treeview(self.eee_5th_semister_facuty_table_frame,columns=('eee_5th_semister_faculty_name','eee_5th_semister_faculty_branch','eee_5th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.eee_5th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.eee_5th_semister_faculty_data_table.yview)

                self.eee_5th_semister_faculty_data_table.heading('eee_5th_semister_faculty_name',text='Faculty Name ')
                self.eee_5th_semister_faculty_data_table.heading('eee_5th_semister_faculty_branch',text='Faculty Branch ')
                self.eee_5th_semister_faculty_data_table.heading('eee_5th_semister_faculty_subject',text='Faculty Subject ')

               
                self.eee_5th_semister_faculty_data_table.column('eee_5th_semister_faculty_name',width=210)
                self.eee_5th_semister_faculty_data_table.column('eee_5th_semister_faculty_branch',width=300)
                self.eee_5th_semister_faculty_data_table.column('eee_5th_semister_faculty_subject',width=270)

                self.eee_5th_semister_faculty_data_table['show']='headings'

                self.eee_5th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_eee_5th_semister_faculty_data()
                self.eee_5th_semister_faculty_data_table.bind('<ButtonRelease-1>',eee_5th_semister_faculty_data_get)
        
############################################# 5th semister ece #########################################################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Communication_Engineering":
                table_frame20=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame20.place(x=10,y=120) 

################################################################################################
                def add_ece_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ece_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame20)
                    else:
                        if self.var_ece_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame20)
                        else:
                            if self.var_ece_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame20)
                            else:
                                cur.execute('insert into add_ece_5th_semsiter_faculty(ece_5th_semister_faculty_name,ece_5th_semister_faculty_branch,ece_5th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ece_5th_semister_faculty_name.get(),
                                self.var_ece_5th_semister_faculty_branch.get(),
                                self.var_ece_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ece_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame20)
                def fetch_ece_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ece_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ece_5th_semister_faculty_data_table.delete(*self.ece_5th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ece_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame20)

                def ece_5th_semister_faculty_serch():
                    #on=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame20)
                        else:
                            cur.execute(f"select * from add_ece_5th_semsiter_faculty where ece_5th_semister_faculty_name LIKE '%{self.var_ece_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ece_5th_semister_faculty_data_table.delete(*self.ece_5th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ece_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame20)
                def ece_5th_semister_faculty_data_get(ev):
                    r1=self.ece_5th_semister_faculty_data_table.focus()
                    content1=self.ece_5th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ece_5th_semister_faculty_name.set(row1[0])
                    self.var_ece_5th_semister_faculty_branch.set(row1[1])
                    self.var_ece_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame20)

                def ece_5th_semister_faculty_data_clear():
                    fetch_ece_5th_semister_faculty_data()
                    self.var_ece_5th_semister_faculty_serch.set("")
                    self.var_ece_5th_semister_faculty_name.set("")
                    self.var_ece_5th_semister_faculty_branch.set("")
                    self.var_ece_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame20)
                def ece_5th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame20)
                        else:
                            cur.execute("select * from add_ece_5th_semsiter_faculty where ece_5th_semister_faculty_name=%s",(self.var_ece_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame20)
                            else:
                                cur.execute("update add_ece_5th_semsiter_faculty set ece_5th_semister_faculty_branch=%s,ece_5th_semister_faculty_subject=%s where ece_5th_semister_faculty_name=%s",(
                                    
                                    self.var_ece_5th_semister_faculty_branch.get(),
                                    self.var_ece_5th_semister_faculty_subject.get(),
                                    self.var_ece_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame20)
                                fetch_ece_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame20)
                def ece_5th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame20)
                        else:
                            cur.execute("select * from add_ece_5th_semsiter_faculty where ece_5th_semister_faculty_name=%s",(self.var_ece_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame20)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame20)
                                if option==True:
                                    cur.execute('delete from add_ece_5th_semsiter_faculty where ece_5th_semister_faculty_name=%s',(self.var_ece_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame20)
                                    ece_5th_semister_faculty_data_clear()
                                    fetch_ece_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame20)
                
################################################################################################

                label11=Label(table_frame20,text='5th Semister ECE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame20,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame20,width=29,textvariable=self.var_ece_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame20,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame20,width=29,textvariable=self.var_ece_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame20,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame20,width=29,textvariable=self.var_ece_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame20,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ece_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ece_5th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ece_5th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ece_5th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ece_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ece_5th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ece_5th_semister_facuty_table_frame=Frame(table_frame20,width=800,height=200,relief=GROOVE)
                self.ece_5th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ece_5th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ece_5th_semister_facuty_table_frame,orient=VERTICAL)
                self.ece_5th_semister_faculty_data_table=ttk.Treeview(self.ece_5th_semister_facuty_table_frame,columns=('ece_5th_semister_faculty_name','ece_5th_semister_faculty_branch','ece_5th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ece_5th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ece_5th_semister_faculty_data_table.yview)

                
                self.ece_5th_semister_faculty_data_table.heading('ece_5th_semister_faculty_name',text='Faculty Name ')
                self.ece_5th_semister_faculty_data_table.heading('ece_5th_semister_faculty_branch',text='Faculty Branch ')
                self.ece_5th_semister_faculty_data_table.heading('ece_5th_semister_faculty_subject',text='Faculty Subject ')

                self.ece_5th_semister_faculty_data_table.column('ece_5th_semister_faculty_name',width=210)
                self.ece_5th_semister_faculty_data_table.column('ece_5th_semister_faculty_branch',width=300)
                self.ece_5th_semister_faculty_data_table.column('ece_5th_semister_faculty_subject',width=270)

                self.ece_5th_semister_faculty_data_table['show']='headings'

                self.ece_5th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ece_5th_semister_faculty_data()
                self.ece_5th_semister_faculty_data_table.bind('<ButtonRelease-1>',ece_5th_semister_faculty_data_get)
        ############################################# 5th semister CS #########################################################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Computer_Science_Engineering":
                table_frame21=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame21.place(x=10,y=120) 

################################################################################################
                def add_cs_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_cs_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame21)
                    else:
                        if self.var_cs_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame21)
                        else:
                            if self.var_cs_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame21)
                            else:
                                cur.execute('insert into add_cs_5th_semsiter_faculty(cs_5th_semister_faculty_name,cs_5th_semister_faculty_branch,cs_5th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_cs_5th_semister_faculty_name.get(),
                                self.var_cs_5th_semister_faculty_branch.get(),
                                self.var_cs_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_cs_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame21)
                def fetch_cs_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_cs_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.cs_5th_semister_faculty_data_table.delete(*self.cs_5th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.cs_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame21)

                def cs_5th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame21)
                        else:
                            cur.execute(f"select * from add_cs_5th_semsiter_faculty where cs_5th_semister_faculty_name LIKE '%{self.var_cs_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.cs_5th_semister_faculty_data_table.delete(*self.cs_5th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.cs_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame21)
                def cs_5th_semister_faculty_data_get(ev):
                    r1=self.cs_5th_semister_faculty_data_table.focus()
                    content1=self.cs_5th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_cs_5th_semister_faculty_name.set(row1[0])
                    self.var_cs_5th_semister_faculty_branch.set(row1[1])
                    self.var_cs_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame21)

                def cs_5th_semister_faculty_data_clear():
                    fetch_cs_5th_semister_faculty_data()
                    self.var_cs_5th_semister_faculty_serch.set("")
                    self.var_cs_5th_semister_faculty_name.set("")
                    self.var_cs_5th_semister_faculty_branch.set("")
                    self.var_cs_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame21)
                def cs_5th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame21)
                        else:
                            cur.execute("select * from add_cs_5th_semsiter_faculty where cs_5th_semister_faculty_name=%s",(self.var_cs_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame21)
                            else:
                                cur.execute("update add_cs_5th_semsiter_faculty set cs_5th_semister_faculty_branch=%s,cs_5th_semister_faculty_subject=%s where cs_5th_semister_faculty_name=%s",(
                                    
                                    self.var_cs_5th_semister_faculty_branch.get(),
                                    self.var_cs_5th_semister_faculty_subject.get(),
                                    self.var_cs_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame21)
                                fetch_cs_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame21)
                def cs_5th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame21)
                        else:
                            cur.execute("select * from add_cs_5th_semsiter_faculty where cs_5th_semister_faculty_name=%s",(self.var_cs_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame21)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame21)
                                if option==True:
                                    cur.execute('delete from add_cs_5th_semsiter_faculty where cs_5th_semister_faculty_name=%s',(self.var_cs_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame21)
                                    cs_5th_semister_faculty_data_clear()
                                    fetch_cs_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame21)
                
################################################################################################

                label11=Label(table_frame21,text='5th Semister CS:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame21,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame21,width=29,textvariable=self.var_cs_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame21,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame21,width=29,textvariable=self.var_cs_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame21,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame21,width=29,textvariable=self.var_cs_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame21,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_cs_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=cs_5th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=cs_5th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=cs_5th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_cs_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=cs_5th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.cs_5th_semister_facuty_table_frame=Frame(table_frame21,width=800,height=200,relief=GROOVE)
                self.cs_5th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.cs_5th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.cs_5th_semister_facuty_table_frame,orient=VERTICAL)
                self.cs_5th_semister_faculty_data_table=ttk.Treeview(self.cs_5th_semister_facuty_table_frame,columns=('cs_5th_semister_faculty_name','cs_5th_semister_faculty_branch','cs_5th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.cs_5th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.cs_5th_semister_faculty_data_table.yview)

            
                self.cs_5th_semister_faculty_data_table.heading('cs_5th_semister_faculty_name',text='Faculty Name ')
                self.cs_5th_semister_faculty_data_table.heading('cs_5th_semister_faculty_branch',text='Faculty Branch ')
                self.cs_5th_semister_faculty_data_table.heading('cs_5th_semister_faculty_subject',text='Faculty Subject ')


                self.cs_5th_semister_faculty_data_table.column('cs_5th_semister_faculty_name',width=210)
                self.cs_5th_semister_faculty_data_table.column('cs_5th_semister_faculty_branch',width=300)
                self.cs_5th_semister_faculty_data_table.column('cs_5th_semister_faculty_subject',width=270)

                self.cs_5th_semister_faculty_data_table['show']='headings'

                self.cs_5th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_cs_5th_semister_faculty_data()
                self.cs_5th_semister_faculty_data_table.bind('<ButtonRelease-1>',cs_5th_semister_faculty_data_get)
 ############################################# 5th semister ISE #########################################################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Information_Science_and_Engineering":
                table_frame22=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame22.place(x=10,y=120) 

################################################################################################
                def add_ise_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ise_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame22)
                    else:
                        if self.var_ise_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame22)
                        else:
                            if self.var_ise_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame22)
                            else:
                                cur.execute('insert into add_ise_5th_semsiter_faculty(ise_5th_semister_faculty_name,ise_5th_semister_faculty_branch,ise_5th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ise_5th_semister_faculty_name.get(),
                                self.var_ise_5th_semister_faculty_branch.get(),
                                self.var_ise_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ise_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame22)
                def fetch_ise_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ise_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ise_5th_semister_faculty_data_table.delete(*self.ise_5th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ise_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame22)

                def ise_5th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame22)
                        else:
                            cur.execute(f"select * from add_ise_5th_semsiter_faculty where ise_5th_semister_faculty_name LIKE '%{self.var_ise_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ise_5th_semister_faculty_data_table.delete(*self.ise_5th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ise_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame22)
                def ise_5th_semister_faculty_data_get(ev):
                    r1=self.ise_5th_semister_faculty_data_table.focus()
                    content1=self.ise_5th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ise_5th_semister_faculty_name.set(row1[0])
                    self.var_ise_5th_semister_faculty_branch.set(row1[1])
                    self.var_ise_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame22)

                def ise_5th_semister_faculty_data_clear():
                    fetch_ise_5th_semister_faculty_data()
                    self.var_ise_5th_semister_faculty_serch.set("")
                    self.var_ise_5th_semister_faculty_name.set("")
                    self.var_ise_5th_semister_faculty_branch.set("")
                    self.var_ise_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame22)
                def ise_5th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame22)
                        else:
                            cur.execute("select * from add_ise_5th_semsiter_faculty where ise_5th_semister_faculty_name=%s",(self.var_ise_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame22)
                            else:
                                cur.execute("update add_ise_5th_semsiter_faculty set ise_5th_semister_faculty_branch=%s,ise_5th_semister_faculty_subject=%s where ise_5th_semister_faculty_name=%s",(
                                    
                                    self.var_ise_5th_semister_faculty_branch.get(),
                                    self.var_ise_5th_semister_faculty_subject.get(),
                                    self.var_ise_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame22)
                                fetch_ise_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame22)
                def ise_5th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame22)
                        else:
                            cur.execute("select * from add_ise_5th_semsiter_faculty where ise_5th_semister_faculty_name=%s",(self.var_ise_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame22)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame22)
                                if option==True:
                                    cur.execute('delete from add_ise_5th_semsiter_faculty where ise_5th_semister_faculty_name=%s',(self.var_ise_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame22)
                                    ise_5th_semister_faculty_data_clear()
                                    fetch_ise_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame22)
                
################################################################################################

                label11=Label(table_frame22,text='5th Semister ISE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame22,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame22,width=29,textvariable=self.var_ise_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame22,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame22,width=29,textvariable=self.var_ise_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame22,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame22,width=29,textvariable=self.var_ise_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame22,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ise_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ise_5th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ise_5th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ise_5th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ise_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ise_5th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ise_5th_semister_facuty_table_frame=Frame(table_frame22,width=800,height=200,relief=GROOVE)
                self.ise_5th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ise_5th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ise_5th_semister_facuty_table_frame,orient=VERTICAL)
                self.ise_5th_semister_faculty_data_table=ttk.Treeview(self.ise_5th_semister_facuty_table_frame,columns=('ise_5th_semister_faculty_name','ise_5th_semister_faculty_branch','ise_5th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ise_5th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ise_5th_semister_faculty_data_table.yview)

                #self.ise_5th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ise_5th_semister_faculty_data_table.heading('ise_5th_semister_faculty_name',text='Faculty Name ')
                self.ise_5th_semister_faculty_data_table.heading('ise_5th_semister_faculty_branch',text='Faculty Branch ')
                self.ise_5th_semister_faculty_data_table.heading('ise_5th_semister_faculty_subject',text='Faculty Subject ')

                #self.ise_5th_semister_faculty_data_table.column('cid',width=150)
                self.ise_5th_semister_faculty_data_table.column('ise_5th_semister_faculty_name',width=210)
                self.ise_5th_semister_faculty_data_table.column('ise_5th_semister_faculty_branch',width=300)
                self.ise_5th_semister_faculty_data_table.column('ise_5th_semister_faculty_subject',width=270)

                self.ise_5th_semister_faculty_data_table['show']='headings'

                self.ise_5th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ise_5th_semister_faculty_data()
                self.ise_5th_semister_faculty_data_table.bind('<ButtonRelease-1>',ise_5th_semister_faculty_data_get)
         ############################################# 5th semister ETE #########################################################################################################################
        if self.var_sem_select.get()=="5th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Telecommunication_Engineering":
                table_frame23=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame23.place(x=10,y=120) 

################################################################################################
                def add_ete_5th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                   # con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ete_5th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame23)
                    else:
                        if self.var_ete_5th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame23)
                        else:
                            if self.var_ete_5th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame23)
                            else:
                                cur.execute('insert into add_ete_5th_semsiter_faculty(ete_5th_semister_faculty_name,ete_5th_semister_faculty_branch,ete_5th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ete_5th_semister_faculty_name.get(),
                                self.var_ete_5th_semister_faculty_branch.get(),
                                self.var_ete_5th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ete_5th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame23)
                def fetch_ete_5th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ete_5th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ete_5th_semister_faculty_data_table.delete(*self.ete_5th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ete_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame23)

                def ete_5th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_5th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame23)
                        else:
                            cur.execute(f"select * from add_ete_5th_semsiter_faculty where ete_5th_semister_faculty_name LIKE '%{self.var_ete_5th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ete_5th_semister_faculty_data_table.delete(*self.ete_5th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ete_5th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame23)
                def ete_5th_semister_faculty_data_get(ev):
                    r1=self.ete_5th_semister_faculty_data_table.focus()
                    content1=self.ete_5th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ete_5th_semister_faculty_name.set(row1[0])
                    self.var_ete_5th_semister_faculty_branch.set(row1[1])
                    self.var_ete_5th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame23)

                def ete_5th_semister_faculty_data_clear():
                    fetch_ete_5th_semister_faculty_data()
                    self.var_ete_5th_semister_faculty_serch.set("")
                    self.var_ete_5th_semister_faculty_name.set("")
                    self.var_ete_5th_semister_faculty_branch.set("")
                    self.var_ete_5th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame23)
                def ete_5th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame23)
                        else:
                            cur.execute("select * from add_ete_5th_semsiter_faculty where ete_5th_semister_faculty_name=%s",(self.var_ete_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame23)
                            else:
                                cur.execute("update add_ete_5th_semsiter_faculty set ete_5th_semister_faculty_branch=%s,ete_5th_semister_faculty_subject=%s where ete_5th_semister_faculty_name=%s",(
                                    
                                    self.var_ete_5th_semister_faculty_branch.get(),
                                    self.var_ete_5th_semister_faculty_subject.get(),
                                    self.var_ete_5th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame23)
                                fetch_ete_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame23)
                def ete_5th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_5th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame23)
                        else:
                            cur.execute("select * from add_ete_5th_semsiter_faculty where ete_5th_semister_faculty_name=%s",(self.var_ete_5th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame23)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame23)
                                if option==True:
                                    cur.execute('delete from add_ete_5th_semsiter_faculty where ete_5th_semister_faculty_name=%s',(self.var_ete_5th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame23)
                                    ete_5th_semister_faculty_data_clear()
                                    fetch_ete_5th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame23)
                
################################################################################################

                label11=Label(table_frame23,text='5th Semister ETE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame23,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame23,width=29,textvariable=self.var_ete_5th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame23,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame23,width=29,textvariable=self.var_ete_5th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame23,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame23,width=29,textvariable=self.var_ete_5th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame23,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ete_5th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ete_5th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ete_5th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ete_5th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ete_5th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ete_5th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ete_5th_semister_facuty_table_frame=Frame(table_frame23,width=800,height=200,relief=GROOVE)
                self.ete_5th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ete_5th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ete_5th_semister_facuty_table_frame,orient=VERTICAL)
                self.ete_5th_semister_faculty_data_table=ttk.Treeview(self.ete_5th_semister_facuty_table_frame,columns=('ete_5th_semister_faculty_name','ete_5th_semister_faculty_branch','ete_5th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ete_5th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ete_5th_semister_faculty_data_table.yview)

                #self.ete_5th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ete_5th_semister_faculty_data_table.heading('ete_5th_semister_faculty_name',text='Faculty Name ')
                self.ete_5th_semister_faculty_data_table.heading('ete_5th_semister_faculty_branch',text='Faculty Branch ')
                self.ete_5th_semister_faculty_data_table.heading('ete_5th_semister_faculty_subject',text='Faculty Subject ')

                #self.ete_5th_semister_faculty_data_table.column('cid',width=150)
                self.ete_5th_semister_faculty_data_table.column('ete_5th_semister_faculty_name',width=210)
                self.ete_5th_semister_faculty_data_table.column('ete_5th_semister_faculty_branch',width=300)
                self.ete_5th_semister_faculty_data_table.column('ete_5th_semister_faculty_subject',width=270)

                self.ete_5th_semister_faculty_data_table['show']='headings'

                self.ete_5th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ete_5th_semister_faculty_data()
                self.ete_5th_semister_faculty_data_table.bind('<ButtonRelease-1>',ete_5th_semister_faculty_data_get)
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
##########################################################  6th semister #########################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Civil_Engineering":
                table_frame24=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame24.place(x=10,y=120) 

################################################################################################
                def add_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame24)
                    else:
                        if self.var_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame24)
                        else:
                            if self.var_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame24)
                            else:
                                cur.execute('insert into add_6th_semsiter_faculty(rd6_semister_faculty_name,rd6_semister_faculty_branch,rd6_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_6th_semister_faculty_name.get(),
                                self.var_6th_semister_faculty_branch.get(),
                                self.var_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame24)
                def fetch_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.rd6_semister_faculty_data_table.delete(*self.rd6_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.rd6_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame24)

                def rd6_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame24)
                        else:
                            cur.execute(f"select * from add_6th_semsiter_faculty where rd6_semister_faculty_name LIKE '%{self.var_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.rd6_semister_faculty_data_table.delete(*self.rd6_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.rd6_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame24)
                def rd6_semister_faculty_data_get(ev):
                    r1=self.rd6_semister_faculty_data_table.focus()
                    content1=self.rd6_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_6th_semister_faculty_name.set(row1[0])
                    self.var_6th_semister_faculty_branch.set(row1[1])
                    self.var_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame24)

                def rd6_semister_faculty_data_clear():
                    fetch_6th_semister_faculty_data()
                    self.var_6th_semister_faculty_serch.set("")
                    self.var_6th_semister_faculty_name.set("")
                    self.var_6th_semister_faculty_branch.set("")
                    self.var_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame24)
                def rd6_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame24)
                        else:
                            cur.execute("select * from add_6th_semsiter_faculty where rd6_semister_faculty_name=%s",(self.var_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame24)
                            else:
                                cur.execute("update add_6th_semsiter_faculty set rd6_semister_faculty_branch=%s,rd6_semister_faculty_subject=%s where rd6_semister_faculty_name=%s",(
                                    
                                    self.var_6th_semister_faculty_branch.get(),
                                    self.var_6th_semister_faculty_subject.get(),
                                    self.var_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame24)
                                fetch_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame24)
                def rd6_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame24)
                        else:
                            cur.execute("select * from add_6th_semsiter_faculty where rd6_semister_faculty_name=%s",(self.var_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame24)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame24)
                                if option==True:
                                    cur.execute('delete from add_6th_semsiter_faculty where rd6_semister_faculty_name=%s',(self.var_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame24)
                                    rd6_semister_faculty_data_clear()
                                    fetch_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame24)
                
################################################################################################

                label11=Label(table_frame24,text='6th Semsiter civil:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame24,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame24,width=29,textvariable=self.var_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame24,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame24,width=29,textvariable=self.var_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame24,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame24,width=29,textvariable=self.var_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame24,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=rd6_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=rd6_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=rd6_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=rd6_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.rd6_semister_facuty_table_frame=Frame(table_frame24,width=800,height=200,relief=GROOVE)
                self.rd6_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.rd6_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.rd6_semister_facuty_table_frame,orient=VERTICAL)
                self.rd6_semister_faculty_data_table=ttk.Treeview(self.rd6_semister_facuty_table_frame,columns=('rd6_semister_faculty_name','rd6_semister_faculty_branch','rd6_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.rd6_semister_faculty_data_table.xview)
                scrolly.configure(command=self.rd6_semister_faculty_data_table.yview)

                #self.rd6_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.rd6_semister_faculty_data_table.heading('rd6_semister_faculty_name',text='Faculty Name ')
                self.rd6_semister_faculty_data_table.heading('rd6_semister_faculty_branch',text='Faculty Branch ')
                self.rd6_semister_faculty_data_table.heading('rd6_semister_faculty_subject',text='Faculty Subject ')

                #self.rd6_semister_faculty_data_table.column('cid',width=150)
                self.rd6_semister_faculty_data_table.column('rd6_semister_faculty_name',width=210)
                self.rd6_semister_faculty_data_table.column('rd6_semister_faculty_branch',width=220)
                self.rd6_semister_faculty_data_table.column('rd6_semister_faculty_subject',width=210)

                self.rd6_semister_faculty_data_table['show']='headings'

                self.rd6_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_6th_semister_faculty_data()
                self.rd6_semister_faculty_data_table.bind('<ButtonRelease-1>',rd6_semister_faculty_data_get)



        
############################################# 6th semister mech #########################################################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Mechanical_Engineering":
                table_frame25=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame25.place(x=10,y=120) 

################################################################################################
                def add_mech_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_mech_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame25)
                    else:
                        if self.var_mech_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame25)
                        else:
                            if self.var_mech_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame25)
                            else:
                                cur.execute('insert into add_mech_6th_semsiter_faculty(mech_6th_semister_faculty_name,mech_6th_semister_faculty_branch,mech_6th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_mech_6th_semister_faculty_name.get(),
                                self.var_mech_6th_semister_faculty_branch.get(),
                                self.var_mech_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_mech_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame25)
                def fetch_mech_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_mech_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.mech_6th_semister_faculty_data_table.delete(*self.mech_6th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.mech_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame25)

                def mech_6th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame25)
                        else:
                            cur.execute(f"select * from add_mech_6th_semsiter_faculty where mech_6th_semister_faculty_name LIKE '%{self.var_mech_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.mech_6th_semister_faculty_data_table.delete(*self.mech_6th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.mech_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame25)
                def mech_6th_semister_faculty_data_get(ev):
                    r1=self.mech_6th_semister_faculty_data_table.focus()
                    content1=self.mech_6th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_mech_6th_semister_faculty_name.set(row1[0])
                    self.var_mech_6th_semister_faculty_branch.set(row1[1])
                    self.var_mech_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame25)

                def mech_6th_semister_faculty_data_clear():
                    fetch_mech_6th_semister_faculty_data()
                    self.var_mech_6th_semister_faculty_serch.set("")
                    self.var_mech_6th_semister_faculty_name.set("")
                    self.var_mech_6th_semister_faculty_branch.set("")
                    self.var_mech_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame25)
                def mech_6th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame25)
                        else:
                            cur.execute("select * from add_mech_6th_semsiter_faculty where mech_6th_semister_faculty_name=%s",(self.var_mech_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame25)
                            else:
                                cur.execute("update add_mech_6th_semsiter_faculty set mech_6th_semister_faculty_branch=%s,mech_6th_semister_faculty_subject=%s where mech_6th_semister_faculty_name=%s",(
                                    
                                    self.var_mech_6th_semister_faculty_branch.get(),
                                    self.var_mech_6th_semister_faculty_subject.get(),
                                    self.var_mech_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame25)
                                fetch_mech_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame25)
                def mech_6th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame25)
                        else:
                            cur.execute("select * from add_mech_6th_semsiter_faculty where mech_6th_semister_faculty_name=%s",(self.var_mech_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame25)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame25)
                                if option==True:
                                    cur.execute('delete from add_mech_6th_semsiter_faculty where mech_6th_semister_faculty_name=%s',(self.var_mech_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame25)
                                    mech_6th_semister_faculty_data_clear()
                                    fetch_mech_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame25)
                
################################################################################################

                label11=Label(table_frame25,text='6th Semsiter MECH:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame25,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame25,width=29,textvariable=self.var_mech_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame25,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame25,width=29,textvariable=self.var_mech_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame25,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame25,width=29,textvariable=self.var_mech_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame25,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_mech_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=mech_6th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=mech_6th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=mech_6th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_mech_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=mech_6th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.mech_6th_semister_facuty_table_frame=Frame(table_frame25,width=800,height=200,relief=GROOVE)
                self.mech_6th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.mech_6th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.mech_6th_semister_facuty_table_frame,orient=VERTICAL)
                self.mech_6th_semister_faculty_data_table=ttk.Treeview(self.mech_6th_semister_facuty_table_frame,columns=('mech_6th_semister_faculty_name','mech_6th_semister_faculty_branch','mech_6th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.mech_6th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.mech_6th_semister_faculty_data_table.yview)

                
                self.mech_6th_semister_faculty_data_table.heading('mech_6th_semister_faculty_name',text='Faculty Name ')
                self.mech_6th_semister_faculty_data_table.heading('mech_6th_semister_faculty_branch',text='Faculty Branch ')
                self.mech_6th_semister_faculty_data_table.heading('mech_6th_semister_faculty_subject',text='Faculty Subject ')

                self.mech_6th_semister_faculty_data_table.column('mech_6th_semister_faculty_name',width=210)
                self.mech_6th_semister_faculty_data_table.column('mech_6th_semister_faculty_branch',width=300)
                self.mech_6th_semister_faculty_data_table.column('mech_6th_semister_faculty_subject',width=270)

                self.mech_6th_semister_faculty_data_table['show']='headings'

                self.mech_6th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_mech_6th_semister_faculty_data()
                self.mech_6th_semister_faculty_data_table.bind('<ButtonRelease-1>',mech_6th_semister_faculty_data_get)
################################################################################ Electrical_And_Electronic_Engineering ############################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Electrical_And_Electronic_Engineering":
                table_frame26=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame26.place(x=10,y=120) 

################################################################################################
                def add_eee_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_eee_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame26)
                    else:
                        if self.var_eee_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame26)
                        else:
                            if self.var_eee_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame26)
                            else:
                                cur.execute('insert into add_eee_6th_semsiter_faculty(eee_6th_semister_faculty_name,eee_6th_semister_faculty_branch,eee_6th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_eee_6th_semister_faculty_name.get(),
                                self.var_eee_6th_semister_faculty_branch.get(),
                                self.var_eee_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_eee_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame26)
                def fetch_eee_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_eee_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.eee_6th_semister_faculty_data_table.delete(*self.eee_6th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.eee_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame26)

                def eee_6th_semister_faculty_serch():
                    #on=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame26)
                        else:
                            cur.execute(f"select * from add_eee_6th_semsiter_faculty where eee_6th_semister_faculty_name LIKE '%{self.var_eee_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.eee_6th_semister_faculty_data_table.delete(*self.eee_6th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.eee_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame26)
                def eee_6th_semister_faculty_data_get(ev):
                    r1=self.eee_6th_semister_faculty_data_table.focus()
                    content1=self.eee_6th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_eee_6th_semister_faculty_name.set(row1[0])
                    self.var_eee_6th_semister_faculty_branch.set(row1[1])
                    self.var_eee_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame26)

                def eee_6th_semister_faculty_data_clear():
                    fetch_eee_6th_semister_faculty_data()
                    self.var_eee_6th_semister_faculty_serch.set("")
                    self.var_eee_6th_semister_faculty_name.set("")
                    self.var_eee_6th_semister_faculty_branch.set("")
                    self.var_eee_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame26)
                def eee_6th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame26)
                        else:
                            cur.execute("select * from add_eee_6th_semsiter_faculty where eee_6th_semister_faculty_name=%s",(self.var_eee_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame26)
                            else:
                                cur.execute("update add_eee_6th_semsiter_faculty set eee_6th_semister_faculty_branch=%s,eee_6th_semister_faculty_subject=%s where eee_6th_semister_faculty_name=%s",(
                                    
                                    self.var_eee_6th_semister_faculty_branch.get(),
                                    self.var_eee_6th_semister_faculty_subject.get(),
                                    self.var_eee_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame26)
                                fetch_eee_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame26)
                def eee_6th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame26)
                        else:
                            cur.execute("select * from add_eee_6th_semsiter_faculty where eee_6th_semister_faculty_name=%s",(self.var_eee_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame26)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame26)
                                if option==True:
                                    cur.execute('delete from add_eee_6th_semsiter_faculty where eee_6th_semister_faculty_name=%s',(self.var_eee_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame26)
                                    eee_6th_semister_faculty_data_clear()
                                    fetch_eee_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame26)
                
################################################################################################

                label11=Label(table_frame26,text='6th Semsiter EEE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame26,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame26,width=29,textvariable=self.var_eee_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame26,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame26,width=29,textvariable=self.var_eee_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame26,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame26,width=29,textvariable=self.var_eee_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame26,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_eee_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=eee_6th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=eee_6th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=eee_6th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_eee_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=eee_6th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.eee_6th_semister_facuty_table_frame=Frame(table_frame26,width=800,height=200,relief=GROOVE)
                self.eee_6th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.eee_6th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.eee_6th_semister_facuty_table_frame,orient=VERTICAL)
                self.eee_6th_semister_faculty_data_table=ttk.Treeview(self.eee_6th_semister_facuty_table_frame,columns=('eee_6th_semister_faculty_name','eee_6th_semister_faculty_branch','eee_6th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.eee_6th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.eee_6th_semister_faculty_data_table.yview)

                #self.eee_6th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.eee_6th_semister_faculty_data_table.heading('eee_6th_semister_faculty_name',text='Faculty Name ')
                self.eee_6th_semister_faculty_data_table.heading('eee_6th_semister_faculty_branch',text='Faculty Branch ')
                self.eee_6th_semister_faculty_data_table.heading('eee_6th_semister_faculty_subject',text='Faculty Subject ')

                #self.eee_6th_semister_faculty_data_table.column('cid',width=150)
                self.eee_6th_semister_faculty_data_table.column('eee_6th_semister_faculty_name',width=210)
                self.eee_6th_semister_faculty_data_table.column('eee_6th_semister_faculty_branch',width=300)
                self.eee_6th_semister_faculty_data_table.column('eee_6th_semister_faculty_subject',width=270)

                self.eee_6th_semister_faculty_data_table['show']='headings'

                self.eee_6th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_eee_6th_semister_faculty_data()
                self.eee_6th_semister_faculty_data_table.bind('<ButtonRelease-1>',eee_6th_semister_faculty_data_get)
        
############################################# 6th semister ece #########################################################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Communication_Engineering":
                table_frame27=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame27.place(x=10,y=120) 

################################################################################################
                def add_ece_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ece_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame27)
                    else:
                        if self.var_ece_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame27)
                        else:
                            if self.var_ece_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame27)
                            else:
                                cur.execute('insert into add_ece_6th_semsiter_faculty(ece_6th_semister_faculty_name,ece_6th_semister_faculty_branch,ece_6th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ece_6th_semister_faculty_name.get(),
                                self.var_ece_6th_semister_faculty_branch.get(),
                                self.var_ece_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ece_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame27)
                def fetch_ece_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ece_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ece_6th_semister_faculty_data_table.delete(*self.ece_6th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ece_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame27)

                def ece_6th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame27)
                        else:
                            cur.execute(f"select * from add_ece_6th_semsiter_faculty where ece_6th_semister_faculty_name LIKE '%{self.var_ece_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ece_6th_semister_faculty_data_table.delete(*self.ece_6th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ece_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame27)
                def ece_6th_semister_faculty_data_get(ev):
                    r1=self.ece_6th_semister_faculty_data_table.focus()
                    content1=self.ece_6th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ece_6th_semister_faculty_name.set(row1[0])
                    self.var_ece_6th_semister_faculty_branch.set(row1[1])
                    self.var_ece_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame27)

                def ece_6th_semister_faculty_data_clear():
                    fetch_ece_6th_semister_faculty_data()
                    self.var_ece_6th_semister_faculty_serch.set("")
                    self.var_ece_6th_semister_faculty_name.set("")
                    self.var_ece_6th_semister_faculty_branch.set("")
                    self.var_ece_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame27)
                def ece_6th_semister_faculty_data_update():
                    #on=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame27)
                        else:
                            cur.execute("select * from add_ece_6th_semsiter_faculty where ece_6th_semister_faculty_name=%s",(self.var_ece_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame27)
                            else:
                                cur.execute("update add_ece_6th_semsiter_faculty set ece_6th_semister_faculty_branch=%s,ece_6th_semister_faculty_subject=%s where ece_6th_semister_faculty_name=%s",(
                                    
                                    self.var_ece_6th_semister_faculty_branch.get(),
                                    self.var_ece_6th_semister_faculty_subject.get(),
                                    self.var_ece_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame27)
                                fetch_ece_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame27)
                def ece_6th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame27)
                        else:
                            cur.execute("select * from add_ece_6th_semsiter_faculty where ece_6th_semister_faculty_name=%s",(self.var_ece_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame27)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame27)
                                if option==True:
                                    cur.execute('delete from add_ece_6th_semsiter_faculty where ece_6th_semister_faculty_name=%s',(self.var_ece_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame27)
                                    ece_6th_semister_faculty_data_clear()
                                    fetch_ece_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame27)
                
################################################################################################

                label11=Label(table_frame27,text='6th Semister ECE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame27,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame27,width=29,textvariable=self.var_ece_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame27,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame27,width=29,textvariable=self.var_ece_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame27,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame27,width=29,textvariable=self.var_ece_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame27,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ece_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ece_6th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ece_6th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ece_6th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ece_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ece_6th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ece_6th_semister_facuty_table_frame=Frame(table_frame27,width=800,height=200,relief=GROOVE)
                self.ece_6th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ece_6th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ece_6th_semister_facuty_table_frame,orient=VERTICAL)
                self.ece_6th_semister_faculty_data_table=ttk.Treeview(self.ece_6th_semister_facuty_table_frame,columns=('ece_6th_semister_faculty_name','ece_6th_semister_faculty_branch','ece_6th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ece_6th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ece_6th_semister_faculty_data_table.yview)

               
                self.ece_6th_semister_faculty_data_table.heading('ece_6th_semister_faculty_name',text='Faculty Name ')
                self.ece_6th_semister_faculty_data_table.heading('ece_6th_semister_faculty_branch',text='Faculty Branch ')
                self.ece_6th_semister_faculty_data_table.heading('ece_6th_semister_faculty_subject',text='Faculty Subject ')

                #self.ece_6th_semister_faculty_data_table.column('cid',width=150)
                self.ece_6th_semister_faculty_data_table.column('ece_6th_semister_faculty_name',width=210)
                self.ece_6th_semister_faculty_data_table.column('ece_6th_semister_faculty_branch',width=300)
                self.ece_6th_semister_faculty_data_table.column('ece_6th_semister_faculty_subject',width=270)

                self.ece_6th_semister_faculty_data_table['show']='headings'

                self.ece_6th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ece_6th_semister_faculty_data()
                self.ece_6th_semister_faculty_data_table.bind('<ButtonRelease-1>',ece_6th_semister_faculty_data_get)
        ############################################# 6th semister CS #########################################################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Computer_Science_Engineering":
                table_frame28=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame28.place(x=10,y=120) 

################################################################################################
                def add_cs_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_cs_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame28)
                    else:
                        if self.var_cs_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame28)
                        else:
                            if self.var_cs_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame28)
                            else:
                                cur.execute('insert into add_cs_6th_semsiter_faculty(cs_6th_semister_faculty_name,cs_6th_semister_faculty_branch,cs_6th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_cs_6th_semister_faculty_name.get(),
                                self.var_cs_6th_semister_faculty_branch.get(),
                                self.var_cs_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_cs_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame28)
                def fetch_cs_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_cs_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.cs_6th_semister_faculty_data_table.delete(*self.cs_6th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.cs_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame28)

                def cs_6th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame28)
                        else:
                            cur.execute(f"select * from add_cs_6th_semsiter_faculty where cs_6th_semister_faculty_name LIKE '%{self.var_cs_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.cs_6th_semister_faculty_data_table.delete(*self.cs_6th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.cs_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame28)
                def cs_6th_semister_faculty_data_get(ev):
                    r1=self.cs_6th_semister_faculty_data_table.focus()
                    content1=self.cs_6th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_cs_6th_semister_faculty_name.set(row1[0])
                    self.var_cs_6th_semister_faculty_branch.set(row1[1])
                    self.var_cs_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame28)

                def cs_6th_semister_faculty_data_clear():
                    fetch_cs_6th_semister_faculty_data()
                    self.var_cs_6th_semister_faculty_serch.set("")
                    self.var_cs_6th_semister_faculty_name.set("")
                    self.var_cs_6th_semister_faculty_branch.set("")
                    self.var_cs_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame28)
                def cs_6th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame28)
                        else:
                            cur.execute("select * from add_cs_6th_semsiter_faculty where cs_6th_semister_faculty_name=%s",(self.var_cs_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame28)
                            else:
                                cur.execute("update add_cs_6th_semsiter_faculty set cs_6th_semister_faculty_branch=%s,cs_6th_semister_faculty_subject=%s where cs_6th_semister_faculty_name=%s",(
                                    
                                    self.var_cs_6th_semister_faculty_branch.get(),
                                    self.var_cs_6th_semister_faculty_subject.get(),
                                    self.var_cs_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame28)
                                fetch_cs_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame28)
                def cs_6th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame28)
                        else:
                            cur.execute("select * from add_cs_6th_semsiter_faculty where cs_6th_semister_faculty_name=%s",(self.var_cs_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame28)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame28)
                                if option==True:
                                    cur.execute('delete from add_cs_6th_semsiter_faculty where cs_6th_semister_faculty_name=%s',(self.var_cs_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame28)
                                    cs_6th_semister_faculty_data_clear()
                                    fetch_cs_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame28)
                
################################################################################################

                label11=Label(table_frame28,text='6th Semister CS:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame28,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame28,width=29,textvariable=self.var_cs_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame28,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame28,width=29,textvariable=self.var_cs_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame28,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame28,width=29,textvariable=self.var_cs_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame28,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_cs_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=cs_6th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=cs_6th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=cs_6th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_cs_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=cs_6th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.cs_6th_semister_facuty_table_frame=Frame(table_frame28,width=800,height=200,relief=GROOVE)
                self.cs_6th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.cs_6th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.cs_6th_semister_facuty_table_frame,orient=VERTICAL)
                self.cs_6th_semister_faculty_data_table=ttk.Treeview(self.cs_6th_semister_facuty_table_frame,columns=('cs_6th_semister_faculty_name','cs_6th_semister_faculty_branch','cs_6th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.cs_6th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.cs_6th_semister_faculty_data_table.yview)

               # self.cs_6th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.cs_6th_semister_faculty_data_table.heading('cs_6th_semister_faculty_name',text='Faculty Name ')
                self.cs_6th_semister_faculty_data_table.heading('cs_6th_semister_faculty_branch',text='Faculty Branch ')
                self.cs_6th_semister_faculty_data_table.heading('cs_6th_semister_faculty_subject',text='Faculty Subject ')

               # self.cs_6th_semister_faculty_data_table.column('cid',width=150)
                self.cs_6th_semister_faculty_data_table.column('cs_6th_semister_faculty_name',width=210)
                self.cs_6th_semister_faculty_data_table.column('cs_6th_semister_faculty_branch',width=300)
                self.cs_6th_semister_faculty_data_table.column('cs_6th_semister_faculty_subject',width=270)

                self.cs_6th_semister_faculty_data_table['show']='headings'

                self.cs_6th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_cs_6th_semister_faculty_data()
                self.cs_6th_semister_faculty_data_table.bind('<ButtonRelease-1>',cs_6th_semister_faculty_data_get)
 ############################################# 6th semister ISE #########################################################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Information_Science_and_Engineering":
                table_frame29=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame29.place(x=10,y=120) 

################################################################################################
                def add_ise_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ise_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame29)
                    else:
                        if self.var_ise_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame29)
                        else:
                            if self.var_ise_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame29)
                            else:
                                cur.execute('insert into add_ise_6th_semsiter_faculty(ise_6th_semister_faculty_name,ise_6th_semister_faculty_branch,ise_6th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ise_6th_semister_faculty_name.get(),
                                self.var_ise_6th_semister_faculty_branch.get(),
                                self.var_ise_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ise_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame29)
                def fetch_ise_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ise_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ise_6th_semister_faculty_data_table.delete(*self.ise_6th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ise_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame29)

                def ise_6th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame29)
                        else:
                            cur.execute(f"select * from add_ise_6th_semsiter_faculty where ise_6th_semister_faculty_name LIKE '%{self.var_ise_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ise_6th_semister_faculty_data_table.delete(*self.ise_6th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ise_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame29)
                def ise_6th_semister_faculty_data_get(ev):
                    r1=self.ise_6th_semister_faculty_data_table.focus()
                    content1=self.ise_6th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ise_6th_semister_faculty_name.set(row1[0])
                    self.var_ise_6th_semister_faculty_branch.set(row1[1])
                    self.var_ise_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame29)

                def ise_6th_semister_faculty_data_clear():
                    fetch_ise_6th_semister_faculty_data()
                    self.var_ise_6th_semister_faculty_serch.set("")
                    self.var_ise_6th_semister_faculty_name.set("")
                    self.var_ise_6th_semister_faculty_branch.set("")
                    self.var_ise_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame29)
                def ise_6th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame29)
                        else:
                            cur.execute("select * from add_ise_6th_semsiter_faculty where ise_6th_semister_faculty_name=%s",(self.var_ise_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame29)
                            else:
                                cur.execute("update add_ise_6th_semsiter_faculty set ise_6th_semister_faculty_branch=%s,ise_6th_semister_faculty_subject=%s where ise_6th_semister_faculty_name=%s",(
                                    
                                    self.var_ise_6th_semister_faculty_branch.get(),
                                    self.var_ise_6th_semister_faculty_subject.get(),
                                    self.var_ise_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame29)
                                fetch_ise_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame29)
                def ise_6th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame29)
                        else:
                            cur.execute("select * from add_ise_6th_semsiter_faculty where ise_6th_semister_faculty_name=%s",(self.var_ise_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame29)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame29)
                                if option==True:
                                    cur.execute('delete from add_ise_6th_semsiter_faculty where ise_6th_semister_faculty_name=%s',(self.var_ise_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame29)
                                    ise_6th_semister_faculty_data_clear()
                                    fetch_ise_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame29)
                
################################################################################################

                label11=Label(table_frame29,text='6th Semister ISE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame29,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame29,width=29,textvariable=self.var_ise_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame29,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame29,width=29,textvariable=self.var_ise_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame29,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame29,width=29,textvariable=self.var_ise_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame29,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ise_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ise_6th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ise_6th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ise_6th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ise_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ise_6th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ise_6th_semister_facuty_table_frame=Frame(table_frame29,width=800,height=200,relief=GROOVE)
                self.ise_6th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ise_6th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ise_6th_semister_facuty_table_frame,orient=VERTICAL)
                self.ise_6th_semister_faculty_data_table=ttk.Treeview(self.ise_6th_semister_facuty_table_frame,columns=('ise_6th_semister_faculty_name','ise_6th_semister_faculty_branch','ise_6th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ise_6th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ise_6th_semister_faculty_data_table.yview)

                #self.ise_6th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ise_6th_semister_faculty_data_table.heading('ise_6th_semister_faculty_name',text='Faculty Name ')
                self.ise_6th_semister_faculty_data_table.heading('ise_6th_semister_faculty_branch',text='Faculty Branch ')
                self.ise_6th_semister_faculty_data_table.heading('ise_6th_semister_faculty_subject',text='Faculty Subject ')

                #self.ise_6th_semister_faculty_data_table.column('cid',width=150)
                self.ise_6th_semister_faculty_data_table.column('ise_6th_semister_faculty_name',width=210)
                self.ise_6th_semister_faculty_data_table.column('ise_6th_semister_faculty_branch',width=300)
                self.ise_6th_semister_faculty_data_table.column('ise_6th_semister_faculty_subject',width=270)

                self.ise_6th_semister_faculty_data_table['show']='headings'

                self.ise_6th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ise_6th_semister_faculty_data()
                self.ise_6th_semister_faculty_data_table.bind('<ButtonRelease-1>',ise_6th_semister_faculty_data_get)
         ############################################# 6th semister ETE #########################################################################################################################
        if self.var_sem_select.get()=="6th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Telecommunication_Engineering":
                table_frame30=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame30.place(x=10,y=120) 

################################################################################################
                def add_ete_6th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                   # con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ete_6th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame30)
                    else:
                        if self.var_ete_6th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame30)
                        else:
                            if self.var_ete_6th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame30)
                            else:
                                cur.execute('insert into add_ete_6th_semsiter_faculty(ete_6th_semister_faculty_name,ete_6th_semister_faculty_branch,ete_6th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ete_6th_semister_faculty_name.get(),
                                self.var_ete_6th_semister_faculty_branch.get(),
                                self.var_ete_6th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ete_6th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame30)
                def fetch_ete_6th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ete_6th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ete_6th_semister_faculty_data_table.delete(*self.ete_6th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ete_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame30)

                def ete_6th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_6th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame30)
                        else:
                            cur.execute(f"select * from add_ete_6th_semsiter_faculty where ete_6th_semister_faculty_name LIKE '%{self.var_ete_6th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ete_6th_semister_faculty_data_table.delete(*self.ete_6th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ete_6th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame30)
                def ete_6th_semister_faculty_data_get(ev):
                    r1=self.ete_6th_semister_faculty_data_table.focus()
                    content1=self.ete_6th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ete_6th_semister_faculty_name.set(row1[0])
                    self.var_ete_6th_semister_faculty_branch.set(row1[1])
                    self.var_ete_6th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame30)

                def ete_6th_semister_faculty_data_clear():
                    fetch_ete_6th_semister_faculty_data()
                    self.var_ete_6th_semister_faculty_serch.set("")
                    self.var_ete_6th_semister_faculty_name.set("")
                    self.var_ete_6th_semister_faculty_branch.set("")
                    self.var_ete_6th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame30)
                def ete_6th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame30)
                        else:
                            cur.execute("select * from add_ete_6th_semsiter_faculty where ete_6th_semister_faculty_name=%s",(self.var_ete_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame30)
                            else:
                                cur.execute("update add_ete_6th_semsiter_faculty set ete_6th_semister_faculty_branch=%s,ete_6th_semister_faculty_subject=%s where ete_6th_semister_faculty_name=%s",(
                                    
                                    self.var_ete_6th_semister_faculty_branch.get(),
                                    self.var_ete_6th_semister_faculty_subject.get(),
                                    self.var_ete_6th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame30)
                                fetch_ete_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame30)
                def ete_6th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_6th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame30)
                        else:
                            cur.execute("select * from add_ete_6th_semsiter_faculty where ete_6th_semister_faculty_name=%s",(self.var_ete_6th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame30)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame30)
                                if option==True:
                                    cur.execute('delete from add_ete_6th_semsiter_faculty where ete_6th_semister_faculty_name=%s',(self.var_ete_6th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame30)
                                    ete_6th_semister_faculty_data_clear()
                                    fetch_ete_6th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame30)
                
################################################################################################

                label11=Label(table_frame30,text='6th Semister ETE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame30,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame30,width=29,textvariable=self.var_ete_6th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame30,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame30,width=29,textvariable=self.var_ete_6th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame30,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame30,width=29,textvariable=self.var_ete_6th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame30,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ete_6th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ete_6th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ete_6th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ete_6th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ete_6th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ete_6th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ete_6th_semister_facuty_table_frame=Frame(table_frame30,width=800,height=200,relief=GROOVE)
                self.ete_6th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ete_6th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ete_6th_semister_facuty_table_frame,orient=VERTICAL)
                self.ete_6th_semister_faculty_data_table=ttk.Treeview(self.ete_6th_semister_facuty_table_frame,columns=('ete_6th_semister_faculty_name','ete_6th_semister_faculty_branch','ete_6th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ete_6th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ete_6th_semister_faculty_data_table.yview)

                #self.ete_6th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ete_6th_semister_faculty_data_table.heading('ete_6th_semister_faculty_name',text='Faculty Name ')
                self.ete_6th_semister_faculty_data_table.heading('ete_6th_semister_faculty_branch',text='Faculty Branch ')
                self.ete_6th_semister_faculty_data_table.heading('ete_6th_semister_faculty_subject',text='Faculty Subject ')

                #self.ete_6th_semister_faculty_data_table.column('cid',width=150)
                self.ete_6th_semister_faculty_data_table.column('ete_6th_semister_faculty_name',width=210)
                self.ete_6th_semister_faculty_data_table.column('ete_6th_semister_faculty_branch',width=300)
                self.ete_6th_semister_faculty_data_table.column('ete_6th_semister_faculty_subject',width=270)

                self.ete_6th_semister_faculty_data_table['show']='headings'

                self.ete_6th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ete_6th_semister_faculty_data()
                self.ete_6th_semister_faculty_data_table.bind('<ButtonRelease-1>',ete_6th_semister_faculty_data_get)
        #################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
##########################################################  7th semister #########################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Civil_Engineering":
                table_frame31=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame31.place(x=10,y=120) 

################################################################################################
                def add_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame31)
                    else:
                        if self.var_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame31)
                        else:
                            if self.var_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame31)
                            else:
                                cur.execute('insert into add_7th_semsiter_faculty(rd7_semister_faculty_name,rd7_semister_faculty_branch,rd7_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_7th_semister_faculty_name.get(),
                                self.var_7th_semister_faculty_branch.get(),
                                self.var_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame31)
                def fetch_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.rd7_semister_faculty_data_table.delete(*self.rd7_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.rd7_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame31)

                def rd7_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame31)
                        else:
                            cur.execute(f"select * from add_7th_semsiter_faculty where rd7_semister_faculty_name LIKE '%{self.var_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.rd7_semister_faculty_data_table.delete(*self.rd7_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.rd7_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame31)
                def rd7_semister_faculty_data_get(ev):
                    r1=self.rd7_semister_faculty_data_table.focus()
                    content1=self.rd7_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_7th_semister_faculty_name.set(row1[0])
                    self.var_7th_semister_faculty_branch.set(row1[1])
                    self.var_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame31)

                def rd7_semister_faculty_data_clear():
                    fetch_7th_semister_faculty_data()
                    self.var_7th_semister_faculty_serch.set("")
                    self.var_7th_semister_faculty_name.set("")
                    self.var_7th_semister_faculty_branch.set("")
                    self.var_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame31)
                def rd7_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame31)
                        else:
                            cur.execute("select * from add_7th_semsiter_faculty where rd7_semister_faculty_name=%s",(self.var_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame31)
                            else:
                                cur.execute("update add_7th_semsiter_faculty set rd7_semister_faculty_branch=%s,rd7_semister_faculty_subject=%s where rd7_semister_faculty_name=%s",(
                                    
                                    self.var_7th_semister_faculty_branch.get(),
                                    self.var_7th_semister_faculty_subject.get(),
                                    self.var_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame31)
                                fetch_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame31)
                def rd7_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame31)
                        else:
                            cur.execute("select * from add_7th_semsiter_faculty where rd7_semister_faculty_name=%s",(self.var_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame31)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame31)
                                if option==True:
                                    cur.execute('delete from add_7th_semsiter_faculty where rd7_semister_faculty_name=%s',(self.var_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame31)
                                    rd7_semister_faculty_data_clear()
                                    fetch_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame31)
                
################################################################################################

                label11=Label(table_frame31,text='7th Semsiter civil:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame31,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame31,width=29,textvariable=self.var_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame31,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame31,width=29,textvariable=self.var_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame31,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame31,width=29,textvariable=self.var_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame31,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=rd7_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=rd7_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=rd7_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=rd7_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.rd7_semister_facuty_table_frame=Frame(table_frame31,width=800,height=200,relief=GROOVE)
                self.rd7_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.rd7_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.rd7_semister_facuty_table_frame,orient=VERTICAL)
                self.rd7_semister_faculty_data_table=ttk.Treeview(self.rd7_semister_facuty_table_frame,columns=('rd7_semister_faculty_name','rd7_semister_faculty_branch','rd7_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.rd7_semister_faculty_data_table.xview)
                scrolly.configure(command=self.rd7_semister_faculty_data_table.yview)

               # self.rd7_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.rd7_semister_faculty_data_table.heading('rd7_semister_faculty_name',text='Faculty Name ')
                self.rd7_semister_faculty_data_table.heading('rd7_semister_faculty_branch',text='Faculty Branch ')
                self.rd7_semister_faculty_data_table.heading('rd7_semister_faculty_subject',text='Faculty Subject ')

                #self.rd7_semister_faculty_data_table.column('cid',width=150)
                self.rd7_semister_faculty_data_table.column('rd7_semister_faculty_name',width=210)
                self.rd7_semister_faculty_data_table.column('rd7_semister_faculty_branch',width=300)
                self.rd7_semister_faculty_data_table.column('rd7_semister_faculty_subject',width=270)

                self.rd7_semister_faculty_data_table['show']='headings'

                self.rd7_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_7th_semister_faculty_data()
                self.rd7_semister_faculty_data_table.bind('<ButtonRelease-1>',rd7_semister_faculty_data_get)



        
############################################# 7th semister mech #########################################################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Mechanical_Engineering":
                table_frame32=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame32.place(x=10,y=120) 

################################################################################################
                def add_mech_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_mech_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame32)
                    else:
                        if self.var_mech_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame32)
                        else:
                            if self.var_mech_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame32)
                            else:
                                cur.execute('insert into add_mech_7th_semsiter_faculty(mech_7th_semister_faculty_name,mech_7th_semister_faculty_branch,mech_7th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_mech_7th_semister_faculty_name.get(),
                                self.var_mech_7th_semister_faculty_branch.get(),
                                self.var_mech_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_mech_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame32)
                def fetch_mech_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_mech_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.mech_7th_semister_faculty_data_table.delete(*self.mech_7th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.mech_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame32)

                def mech_7th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame32)
                        else:
                            cur.execute(f"select * from add_mech_7th_semsiter_faculty where mech_7th_semister_faculty_name LIKE '%{self.var_mech_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.mech_7th_semister_faculty_data_table.delete(*self.mech_7th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.mech_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame32)
                def mech_7th_semister_faculty_data_get(ev):
                    r1=self.mech_7th_semister_faculty_data_table.focus()
                    content1=self.mech_7th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_mech_7th_semister_faculty_name.set(row1[0])
                    self.var_mech_7th_semister_faculty_branch.set(row1[1])
                    self.var_mech_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame32)

                def mech_7th_semister_faculty_data_clear():
                    fetch_mech_7th_semister_faculty_data()
                    self.var_mech_7th_semister_faculty_serch.set("")
                    self.var_mech_7th_semister_faculty_name.set("")
                    self.var_mech_7th_semister_faculty_branch.set("")
                    self.var_mech_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame32)
                def mech_7th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame32)
                        else:
                            cur.execute("select * from add_mech_7th_semsiter_faculty where mech_7th_semister_faculty_name=%s",(self.var_mech_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame32)
                            else:
                                cur.execute("update add_mech_7th_semsiter_faculty set mech_7th_semister_faculty_branch=%s,mech_7th_semister_faculty_subject=%s where mech_7th_semister_faculty_name=%s",(
                                    
                                    self.var_mech_7th_semister_faculty_branch.get(),
                                    self.var_mech_7th_semister_faculty_subject.get(),
                                    self.var_mech_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame32)
                                fetch_mech_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame32)
                def mech_7th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame32)
                        else:
                            cur.execute("select * from add_mech_7th_semsiter_faculty where mech_7th_semister_faculty_name=5s",(self.var_mech_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame32)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame32)
                                if option==True:
                                    cur.execute('delete from add_mech_7th_semsiter_faculty where mech_7th_semister_faculty_name=%s',(self.var_mech_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame32)
                                    mech_7th_semister_faculty_data_clear()
                                    fetch_mech_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame32)
                
################################################################################################

                label11=Label(table_frame32,text='7th Semsiter MECH:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame32,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame32,width=29,textvariable=self.var_mech_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame32,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame32,width=29,textvariable=self.var_mech_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame32,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame32,width=29,textvariable=self.var_mech_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame32,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_mech_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=mech_7th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=mech_7th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=mech_7th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_mech_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=mech_7th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.mech_7th_semister_facuty_table_frame=Frame(table_frame32,width=800,height=200,relief=GROOVE)
                self.mech_7th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.mech_7th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.mech_7th_semister_facuty_table_frame,orient=VERTICAL)
                self.mech_7th_semister_faculty_data_table=ttk.Treeview(self.mech_7th_semister_facuty_table_frame,columns=('mech_7th_semister_faculty_name','mech_7th_semister_faculty_branch','mech_7th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.mech_7th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.mech_7th_semister_faculty_data_table.yview)

                #self.mech_7th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.mech_7th_semister_faculty_data_table.heading('mech_7th_semister_faculty_name',text='Faculty Name ')
                self.mech_7th_semister_faculty_data_table.heading('mech_7th_semister_faculty_branch',text='Faculty Branch ')
                self.mech_7th_semister_faculty_data_table.heading('mech_7th_semister_faculty_subject',text='Faculty Subject ')

                #self.mech_7th_semister_faculty_data_table.column('cid',width=150)
                self.mech_7th_semister_faculty_data_table.column('mech_7th_semister_faculty_name',width=210)
                self.mech_7th_semister_faculty_data_table.column('mech_7th_semister_faculty_branch',width=300)
                self.mech_7th_semister_faculty_data_table.column('mech_7th_semister_faculty_subject',width=270)

                self.mech_7th_semister_faculty_data_table['show']='headings'

                self.mech_7th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_mech_7th_semister_faculty_data()
                self.mech_7th_semister_faculty_data_table.bind('<ButtonRelease-1>',mech_7th_semister_faculty_data_get)
################################################################################ Electrical_And_Electronic_Engineering ############################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Electrical_And_Electronic_Engineering":
                table_frame33=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame33.place(x=10,y=120) 

################################################################################################
                def add_eee_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_eee_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame33)
                    else:
                        if self.var_eee_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame33)
                        else:
                            if self.var_eee_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame33)
                            else:
                                cur.execute('insert into add_eee_7th_semsiter_faculty(eee_7th_semister_faculty_name,eee_7th_semister_faculty_branch,eee_7th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_eee_7th_semister_faculty_name.get(),
                                self.var_eee_7th_semister_faculty_branch.get(),
                                self.var_eee_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_eee_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame33)
                def fetch_eee_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_eee_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.eee_7th_semister_faculty_data_table.delete(*self.eee_7th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.eee_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame33)

                def eee_7th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame33)
                        else:
                            cur.execute(f"select * from add_eee_7th_semsiter_faculty where eee_7th_semister_faculty_name LIKE '%{self.var_eee_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.eee_7th_semister_faculty_data_table.delete(*self.eee_7th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.eee_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame33)
                def eee_7th_semister_faculty_data_get(ev):
                    r1=self.eee_7th_semister_faculty_data_table.focus()
                    content1=self.eee_7th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_eee_7th_semister_faculty_name.set(row1[0])
                    self.var_eee_7th_semister_faculty_branch.set(row1[1])
                    self.var_eee_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame33)

                def eee_7th_semister_faculty_data_clear():
                    fetch_eee_7th_semister_faculty_data()
                    self.var_eee_7th_semister_faculty_serch.set("")
                    self.var_eee_7th_semister_faculty_name.set("")
                    self.var_eee_7th_semister_faculty_branch.set("")
                    self.var_eee_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame33)
                def eee_7th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame33)
                        else:
                            cur.execute("select * from add_eee_7th_semsiter_faculty where eee_7th_semister_faculty_name=%s",(self.var_eee_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame33)
                            else:
                                cur.execute("update add_eee_7th_semsiter_faculty set eee_7th_semister_faculty_branch=%s,eee_7th_semister_faculty_subject=%s where eee_7th_semister_faculty_name=%s",(
                                    
                                    self.var_eee_7th_semister_faculty_branch.get(),
                                    self.var_eee_7th_semister_faculty_subject.get(),
                                    self.var_eee_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame33)
                                fetch_eee_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame33)
                def eee_7th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame33)
                        else:
                            cur.execute("select * from add_eee_7th_semsiter_faculty where eee_7th_semister_faculty_name=%s",(self.var_eee_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame33)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame33)
                                if option==True:
                                    cur.execute('delete from add_eee_7th_semsiter_faculty where eee_7th_semister_faculty_name=%s',(self.var_eee_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame33)
                                    eee_7th_semister_faculty_data_clear()
                                    fetch_eee_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame33)
                
################################################################################################

                label11=Label(table_frame33,text='7th Semsiter EEE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame33,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame33,width=29,textvariable=self.var_eee_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame33,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame33,width=29,textvariable=self.var_eee_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame33,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame33,width=29,textvariable=self.var_eee_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame33,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_eee_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=eee_7th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=eee_7th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=eee_7th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_eee_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=eee_7th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.eee_7th_semister_facuty_table_frame=Frame(table_frame33,width=800,height=200,relief=GROOVE)
                self.eee_7th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.eee_7th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.eee_7th_semister_facuty_table_frame,orient=VERTICAL)
                self.eee_7th_semister_faculty_data_table=ttk.Treeview(self.eee_7th_semister_facuty_table_frame,columns=('eee_7th_semister_faculty_name','eee_7th_semister_faculty_branch','eee_7th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.eee_7th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.eee_7th_semister_faculty_data_table.yview)

                #self.eee_7th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.eee_7th_semister_faculty_data_table.heading('eee_7th_semister_faculty_name',text='Faculty Name ')
                self.eee_7th_semister_faculty_data_table.heading('eee_7th_semister_faculty_branch',text='Faculty Branch ')
                self.eee_7th_semister_faculty_data_table.heading('eee_7th_semister_faculty_subject',text='Faculty Subject ')

                #self.eee_7th_semister_faculty_data_table.column('cid',width=150)
                self.eee_7th_semister_faculty_data_table.column('eee_7th_semister_faculty_name',width=210)
                self.eee_7th_semister_faculty_data_table.column('eee_7th_semister_faculty_branch',width=300)
                self.eee_7th_semister_faculty_data_table.column('eee_7th_semister_faculty_subject',width=270)

                self.eee_7th_semister_faculty_data_table['show']='headings'

                self.eee_7th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_eee_7th_semister_faculty_data()
                self.eee_7th_semister_faculty_data_table.bind('<ButtonRelease-1>',eee_7th_semister_faculty_data_get)
        
############################################# 7th semister ece #########################################################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Communication_Engineering":
                table_frame34=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame34.place(x=10,y=120) 

################################################################################################
                def add_ece_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ece_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame34)
                    else:
                        if self.var_ece_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame34)
                        else:
                            if self.var_ece_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame34)
                            else:
                                cur.execute('insert into add_ece_7th_semsiter_faculty(ece_7th_semister_faculty_name,ece_7th_semister_faculty_branch,ece_7th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ece_7th_semister_faculty_name.get(),
                                self.var_ece_7th_semister_faculty_branch.get(),
                                self.var_ece_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ece_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame34)
                def fetch_ece_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ece_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ece_7th_semister_faculty_data_table.delete(*self.ece_7th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ece_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame34)

                def ece_7th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame34)
                        else:
                            cur.execute(f"select * from add_ece_7th_semsiter_faculty where ece_7th_semister_faculty_name LIKE '%{self.var_ece_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ece_7th_semister_faculty_data_table.delete(*self.ece_7th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ece_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame34)
                def ece_7th_semister_faculty_data_get(ev):
                    r1=self.ece_7th_semister_faculty_data_table.focus()
                    content1=self.ece_7th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ece_7th_semister_faculty_name.set(row1[0])
                    self.var_ece_7th_semister_faculty_branch.set(row1[1])
                    self.var_ece_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame34)

                def ece_7th_semister_faculty_data_clear():
                    fetch_ece_7th_semister_faculty_data()
                    self.var_ece_7th_semister_faculty_serch.set("")
                    self.var_ece_7th_semister_faculty_name.set("")
                    self.var_ece_7th_semister_faculty_branch.set("")
                    self.var_ece_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame34)
                def ece_7th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    cur=con.cursor()
                    try:
                        if self.var_ece_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame34)
                        else:
                            cur.execute("select * from add_ece_7th_semsiter_faculty where ece_7th_semister_faculty_name=%s",(self.var_ece_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame34)
                            else:
                                cur.execute("update add_ece_7th_semsiter_faculty set ece_7th_semister_faculty_branch=%s,ece_7th_semister_faculty_subject=%s where ece_7th_semister_faculty_name=%s",(
                                    
                                    self.var_ece_7th_semister_faculty_branch.get(),
                                    self.var_ece_7th_semister_faculty_subject.get(),
                                    self.var_ece_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame34)
                                fetch_ece_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame34)
                def ece_7th_semister_faculty_data_delete():
                   # con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame34)
                        else:
                            cur.execute("select * from add_ece_7th_semsiter_faculty where ece_7th_semister_faculty_name=%s",(self.var_ece_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame34)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame34)
                                if option==True:
                                    cur.execute('delete from add_ece_7th_semsiter_faculty where ece_7th_semister_faculty_name=%s',(self.var_ece_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame34)
                                    ece_7th_semister_faculty_data_clear()
                                    fetch_ece_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame34)
                
################################################################################################

                label11=Label(table_frame34,text='7th Semister ECE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame34,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame34,width=29,textvariable=self.var_ece_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame34,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame34,width=29,textvariable=self.var_ece_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame34,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame34,width=29,textvariable=self.var_ece_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame34,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ece_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ece_7th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ece_7th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ece_7th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ece_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ece_7th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ece_7th_semister_facuty_table_frame=Frame(table_frame34,width=800,height=200,relief=GROOVE)
                self.ece_7th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ece_7th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ece_7th_semister_facuty_table_frame,orient=VERTICAL)
                self.ece_7th_semister_faculty_data_table=ttk.Treeview(self.ece_7th_semister_facuty_table_frame,columns=('ece_7th_semister_faculty_name','ece_7th_semister_faculty_branch','ece_7th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ece_7th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ece_7th_semister_faculty_data_table.yview)

                #self.ece_7th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ece_7th_semister_faculty_data_table.heading('ece_7th_semister_faculty_name',text='Faculty Name ')
                self.ece_7th_semister_faculty_data_table.heading('ece_7th_semister_faculty_branch',text='Faculty Branch ')
                self.ece_7th_semister_faculty_data_table.heading('ece_7th_semister_faculty_subject',text='Faculty Subject ')

                #self.ece_7th_semister_faculty_data_table.column('cid',width=150)
                self.ece_7th_semister_faculty_data_table.column('ece_7th_semister_faculty_name',width=210)
                self.ece_7th_semister_faculty_data_table.column('ece_7th_semister_faculty_branch',width=300)
                self.ece_7th_semister_faculty_data_table.column('ece_7th_semister_faculty_subject',width=270)

                self.ece_7th_semister_faculty_data_table['show']='headings'

                self.ece_7th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ece_7th_semister_faculty_data()
                self.ece_7th_semister_faculty_data_table.bind('<ButtonRelease-1>',ece_7th_semister_faculty_data_get)
        ############################################# 7th semister CS #########################################################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Computer_Science_Engineering":
                table_frame35=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame35.place(x=10,y=120) 

################################################################################################
                def add_cs_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_cs_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame35)
                    else:
                        if self.var_cs_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame35)
                        else:
                            if self.var_cs_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame35)
                            else:
                                cur.execute('insert into add_cs_7th_semsiter_faculty(cs_7th_semister_faculty_name,cs_7th_semister_faculty_branch,cs_7th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_cs_7th_semister_faculty_name.get(),
                                self.var_cs_7th_semister_faculty_branch.get(),
                                self.var_cs_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_cs_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame35)
                def fetch_cs_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_cs_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.cs_7th_semister_faculty_data_table.delete(*self.cs_7th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.cs_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame35)

                def cs_7th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame35)
                        else:
                            cur.execute(f"select * from add_cs_7th_semsiter_faculty where cs_7th_semister_faculty_name LIKE '%{self.var_cs_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.cs_7th_semister_faculty_data_table.delete(*self.cs_7th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.cs_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame35)
                def cs_7th_semister_faculty_data_get(ev):
                    r1=self.cs_7th_semister_faculty_data_table.focus()
                    content1=self.cs_7th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_cs_7th_semister_faculty_name.set(row1[0])
                    self.var_cs_7th_semister_faculty_branch.set(row1[1])
                    self.var_cs_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame35)

                def cs_7th_semister_faculty_data_clear():
                    fetch_cs_7th_semister_faculty_data()
                    self.var_cs_7th_semister_faculty_serch.set("")
                    self.var_cs_7th_semister_faculty_name.set("")
                    self.var_cs_7th_semister_faculty_branch.set("")
                    self.var_cs_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame35)
                def cs_7th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame35)
                        else:
                            cur.execute("select * from add_cs_7th_semsiter_faculty where cs_7th_semister_faculty_name=%s",(self.var_cs_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame35)
                            else:
                                cur.execute("update add_cs_7th_semsiter_faculty set cs_7th_semister_faculty_branch=%s,cs_7th_semister_faculty_subject=%s where cs_7th_semister_faculty_name=%s",(
                                    
                                    self.var_cs_7th_semister_faculty_branch.get(),
                                    self.var_cs_7th_semister_faculty_subject.get(),
                                    self.var_cs_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame35)
                                fetch_cs_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame35)
                def cs_7th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame35)
                        else:
                            cur.execute("select * from add_cs_7th_semsiter_faculty where cs_7th_semister_faculty_name=%s",(self.var_cs_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame35)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame35)
                                if option==True:
                                    cur.execute('delete from add_cs_7th_semsiter_faculty where cs_7th_semister_faculty_name=%s',(self.var_cs_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame35)
                                    cs_7th_semister_faculty_data_clear()
                                    fetch_cs_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame35)
                
################################################################################################

                label11=Label(table_frame35,text='7th Semister CS:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame35,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame35,width=29,textvariable=self.var_cs_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame35,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame35,width=29,textvariable=self.var_cs_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame35,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame35,width=29,textvariable=self.var_cs_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame35,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_cs_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=cs_7th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=cs_7th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=cs_7th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_cs_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=cs_7th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.cs_7th_semister_facuty_table_frame=Frame(table_frame35,width=800,height=200,relief=GROOVE)
                self.cs_7th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.cs_7th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.cs_7th_semister_facuty_table_frame,orient=VERTICAL)
                self.cs_7th_semister_faculty_data_table=ttk.Treeview(self.cs_7th_semister_facuty_table_frame,columns=('cs_7th_semister_faculty_name','cs_7th_semister_faculty_branch','cs_7th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.cs_7th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.cs_7th_semister_faculty_data_table.yview)

                #self.cs_7th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.cs_7th_semister_faculty_data_table.heading('cs_7th_semister_faculty_name',text='Faculty Name ')
                self.cs_7th_semister_faculty_data_table.heading('cs_7th_semister_faculty_branch',text='Faculty Branch ')
                self.cs_7th_semister_faculty_data_table.heading('cs_7th_semister_faculty_subject',text='Faculty Subject ')

                #self.cs_7th_semister_faculty_data_table.column('cid',width=150)
                self.cs_7th_semister_faculty_data_table.column('cs_7th_semister_faculty_name',width=210)
                self.cs_7th_semister_faculty_data_table.column('cs_7th_semister_faculty_branch',width=300)
                self.cs_7th_semister_faculty_data_table.column('cs_7th_semister_faculty_subject',width=270)

                self.cs_7th_semister_faculty_data_table['show']='headings'

                self.cs_7th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_cs_7th_semister_faculty_data()
                self.cs_7th_semister_faculty_data_table.bind('<ButtonRelease-1>',cs_7th_semister_faculty_data_get)
 ############################################# 7th semister ISE #########################################################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Information_Science_and_Engineering":
                table_frame36=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame36.place(x=10,y=120) 

################################################################################################
                def add_ise_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ise_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame36)
                    else:
                        if self.var_ise_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame36)
                        else:
                            if self.var_ise_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame36)
                            else:
                            
                                cur.execute('insert into add_ise_7th_semsiter_faculty(ise_7th_semister_faculty_name,ise_7th_semister_faculty_branch,ise_7th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ise_7th_semister_faculty_name.get(),
                                self.var_ise_7th_semister_faculty_branch.get(),
                                self.var_ise_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ise_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame36)
                def fetch_ise_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ise_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ise_7th_semister_faculty_data_table.delete(*self.ise_7th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ise_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame36)

                def ise_7th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame36)
                        else:
                            cur.execute(f"select * from add_ise_7th_semsiter_faculty where ise_7th_semister_faculty_name LIKE '%{self.var_ise_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ise_7th_semister_faculty_data_table.delete(*self.ise_7th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ise_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame36)
                def ise_7th_semister_faculty_data_get(ev):
                    r1=self.ise_7th_semister_faculty_data_table.focus()
                    content1=self.ise_7th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ise_7th_semister_faculty_name.set(row1[0])
                    self.var_ise_7th_semister_faculty_branch.set(row1[1])
                    self.var_ise_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame36)

                def ise_7th_semister_faculty_data_clear():
                    fetch_ise_7th_semister_faculty_data()
                    self.var_ise_7th_semister_faculty_serch.set("")
                    self.var_ise_7th_semister_faculty_name.set("")
                    self.var_ise_7th_semister_faculty_branch.set("")
                    self.var_ise_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame36)
                def ise_7th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame36)
                        else:
                            cur.execute("select * from add_ise_7th_semsiter_faculty where ise_7th_semister_faculty_name=%s",(self.var_ise_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame36)
                            else:
                                cur.execute("update add_ise_7th_semsiter_faculty set ise_7th_semister_faculty_branch=%s,ise_7th_semister_faculty_subject=%s where ise_7th_semister_faculty_name=%s",(
                                    
                                    self.var_ise_7th_semister_faculty_branch.get(),
                                    self.var_ise_7th_semister_faculty_subject.get(),
                                    self.var_ise_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame36)
                                fetch_ise_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame36)
                def ise_7th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame36)
                        else:
                            cur.execute("select * from add_ise_7th_semsiter_faculty where ise_7th_semister_faculty_name=%s",(self.var_ise_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame36)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame36)
                                if option==True:
                                    cur.execute('delete from add_ise_7th_semsiter_faculty where ise_7th_semister_faculty_name=%s',(self.var_ise_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame36)
                                    ise_7th_semister_faculty_data_clear()
                                    fetch_ise_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame36)
                
################################################################################################

                label11=Label(table_frame36,text='7th Semister ISE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame36,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame36,width=29,textvariable=self.var_ise_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame36,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame36,width=29,textvariable=self.var_ise_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame36,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame36,width=29,textvariable=self.var_ise_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame36,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ise_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ise_7th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ise_7th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ise_7th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ise_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ise_7th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ise_7th_semister_facuty_table_frame=Frame(table_frame36,width=800,height=200,relief=GROOVE)
                self.ise_7th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ise_7th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ise_7th_semister_facuty_table_frame,orient=VERTICAL)
                self.ise_7th_semister_faculty_data_table=ttk.Treeview(self.ise_7th_semister_facuty_table_frame,columns=('ise_7th_semister_faculty_name','ise_7th_semister_faculty_branch','ise_7th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ise_7th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ise_7th_semister_faculty_data_table.yview)

                #self.ise_7th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ise_7th_semister_faculty_data_table.heading('ise_7th_semister_faculty_name',text='Faculty Name ')
                self.ise_7th_semister_faculty_data_table.heading('ise_7th_semister_faculty_branch',text='Faculty Branch ')
                self.ise_7th_semister_faculty_data_table.heading('ise_7th_semister_faculty_subject',text='Faculty Subject ')

                #self.ise_7th_semister_faculty_data_table.column('cid',width=150)
                self.ise_7th_semister_faculty_data_table.column('ise_7th_semister_faculty_name',width=210)
                self.ise_7th_semister_faculty_data_table.column('ise_7th_semister_faculty_branch',width=300)
                self.ise_7th_semister_faculty_data_table.column('ise_7th_semister_faculty_subject',width=270)

                self.ise_7th_semister_faculty_data_table['show']='headings'

                self.ise_7th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ise_7th_semister_faculty_data()
                self.ise_7th_semister_faculty_data_table.bind('<ButtonRelease-1>',ise_7th_semister_faculty_data_get)
         ############################################# 7th semister ETE #########################################################################################################################
        if self.var_sem_select.get()=="7th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Telecommunication_Engineering":
                table_frame37=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame37.place(x=10,y=120) 

################################################################################################
                def add_ete_7th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ete_7th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame37)
                    else:
                        if self.var_ete_7th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame37)
                        else:
                            if self.var_ete_7th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame37)
                            else:
                                cur.execute('insert into add_ete_7th_semsiter_faculty(ete_7th_semister_faculty_name,ete_7th_semister_faculty_branch,ete_7th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ete_7th_semister_faculty_name.get(),
                                self.var_ete_7th_semister_faculty_branch.get(),
                                self.var_ete_7th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ete_7th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame37)
                def fetch_ete_7th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ete_7th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ete_7th_semister_faculty_data_table.delete(*self.ete_7th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ete_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame37)

                def ete_7th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_7th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame37)
                        else:
                            cur.execute(f"select * from add_ete_7th_semsiter_faculty where ete_7th_semister_faculty_name LIKE '%{self.var_ete_7th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ete_7th_semister_faculty_data_table.delete(*self.ete_7th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ete_7th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame37)
                def ete_7th_semister_faculty_data_get(ev):
                    r1=self.ete_7th_semister_faculty_data_table.focus()
                    content1=self.ete_7th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ete_7th_semister_faculty_name.set(row1[0])
                    self.var_ete_7th_semister_faculty_branch.set(row1[1])
                    self.var_ete_7th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame37)

                def ete_7th_semister_faculty_data_clear():
                    fetch_ete_7th_semister_faculty_data()
                    self.var_ete_7th_semister_faculty_serch.set("")
                    self.var_ete_7th_semister_faculty_name.set("")
                    self.var_ete_7th_semister_faculty_branch.set("")
                    self.var_ete_7th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame37)
                def ete_7th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame37)
                        else:
                            cur.execute("select * from add_ete_7th_semsiter_faculty where ete_7th_semister_faculty_name=%s",(self.var_ete_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame37)
                            else:
                                cur.execute("update add_ete_7th_semsiter_faculty set ete_7th_semister_faculty_branch=%s,ete_7th_semister_faculty_subject=%s where ete_7th_semister_faculty_name=%s",(
                                    
                                    self.var_ete_7th_semister_faculty_branch.get(),
                                    self.var_ete_7th_semister_faculty_subject.get(),
                                    self.var_ete_7th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame37)
                                fetch_ete_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame37)
                def ete_7th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_7th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame37)
                        else:
                            cur.execute("select * from add_ete_7th_semsiter_faculty where ete_7th_semister_faculty_name=%s",(self.var_ete_7th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame37)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame37)
                                if option==True:
                                    cur.execute('delete from add_ete_7th_semsiter_faculty where ete_7th_semister_faculty_name=%s',(self.var_ete_7th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame37)
                                    ete_7th_semister_faculty_data_clear()
                                    fetch_ete_7th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame37)
                
################################################################################################

                label11=Label(table_frame37,text='7th Semister ETE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame37,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame37,width=29,textvariable=self.var_ete_7th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame37,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame37,width=29,textvariable=self.var_ete_7th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame37,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame37,width=29,textvariable=self.var_ete_7th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame37,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ete_7th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ete_7th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ete_7th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ete_7th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ete_7th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ete_7th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ete_7th_semister_facuty_table_frame=Frame(table_frame37,width=800,height=200,relief=GROOVE)
                self.ete_7th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ete_7th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ete_7th_semister_facuty_table_frame,orient=VERTICAL)
                self.ete_7th_semister_faculty_data_table=ttk.Treeview(self.ete_7th_semister_facuty_table_frame,columns=('ete_7th_semister_faculty_name','ete_7th_semister_faculty_branch','ete_7th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ete_7th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ete_7th_semister_faculty_data_table.yview)

                #self.ete_7th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ete_7th_semister_faculty_data_table.heading('ete_7th_semister_faculty_name',text='Faculty Name ')
                self.ete_7th_semister_faculty_data_table.heading('ete_7th_semister_faculty_branch',text='Faculty Branch ')
                self.ete_7th_semister_faculty_data_table.heading('ete_7th_semister_faculty_subject',text='Faculty Subject ')

                #self.ete_7th_semister_faculty_data_table.column('cid',width=150)
                self.ete_7th_semister_faculty_data_table.column('ete_7th_semister_faculty_name',width=210)
                self.ete_7th_semister_faculty_data_table.column('ete_7th_semister_faculty_branch',width=300)
                self.ete_7th_semister_faculty_data_table.column('ete_7th_semister_faculty_subject',width=270)

                self.ete_7th_semister_faculty_data_table['show']='headings'

                self.ete_7th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ete_7th_semister_faculty_data()
                self.ete_7th_semister_faculty_data_table.bind('<ButtonRelease-1>',ete_7th_semister_faculty_data_get)
          #################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
##########################################################  8th semister #########################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Civil_Engineering":
                table_frame38=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame38.place(x=10,y=120) 

################################################################################################
                def add_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame38)
                    else:
                        if self.var_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame38)
                        else:
                            if self.var_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame38)
                            else:
                                cur.execute('insert into add_8th_semsiter_faculty(rd8_semister_faculty_name,rd8_semister_faculty_branch,rd8_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_8th_semister_faculty_name.get(),
                                self.var_8th_semister_faculty_branch.get(),
                                self.var_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame38)
                def fetch_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.rd8_semister_faculty_data_table.delete(*self.rd8_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.rd8_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame38)

                def rd8_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame38)
                        else:
                            cur.execute(f"select * from add_8th_semsiter_faculty where rd8_semister_faculty_name LIKE '%{self.var_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.rd8_semister_faculty_data_table.delete(*self.rd8_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.rd8_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame38)
                def rd8_semister_faculty_data_get(ev):
                    r1=self.rd8_semister_faculty_data_table.focus()
                    content1=self.rd8_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_8th_semister_faculty_name.set(row1[0])
                    self.var_8th_semister_faculty_branch.set(row1[1])
                    self.var_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame38)

                def rd8_semister_faculty_data_clear():
                    fetch_8th_semister_faculty_data()
                    self.var_8th_semister_faculty_serch.set("")
                    self.var_8th_semister_faculty_name.set("")
                    self.var_8th_semister_faculty_branch.set("")
                    self.var_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame38)
                def rd8_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame38)
                        else:
                            cur.execute("select * from add_8th_semsiter_faculty where rd8_semister_faculty_name=%s",(self.var_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame38)
                            else:
                                cur.execute("update add_8th_semsiter_faculty set rd8_semister_faculty_branch=%s,rd8_semister_faculty_subject=%s where rd8_semister_faculty_name=%s",(
                                    
                                    self.var_8th_semister_faculty_branch.get(),
                                    self.var_8th_semister_faculty_subject.get(),
                                    self.var_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame38)
                                fetch_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame38)
                def rd8_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame38)
                        else:
                            cur.execute("select * from add_8th_semsiter_faculty where rd8_semister_faculty_name=%s",(self.var_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame38)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame38)
                                if option==True:
                                    cur.execute('delete from add_8th_semsiter_faculty where rd8_semister_faculty_name=%s',(self.var_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame38)
                                    rd8_semister_faculty_data_clear()
                                    fetch_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame38)
                
################################################################################################

                label11=Label(table_frame38,text='8th Semsiter civil:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame38,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame38,width=29,textvariable=self.var_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame38,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame38,width=29,textvariable=self.var_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame38,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame38,width=29,textvariable=self.var_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame38,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=rd8_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=rd8_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=rd8_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=rd8_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.rd8_semister_facuty_table_frame=Frame(table_frame38,width=800,height=200,relief=GROOVE)
                self.rd8_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.rd8_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.rd8_semister_facuty_table_frame,orient=VERTICAL)
                self.rd8_semister_faculty_data_table=ttk.Treeview(self.rd8_semister_facuty_table_frame,columns=('rd8_semister_faculty_name','rd8_semister_faculty_branch','rd8_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.rd8_semister_faculty_data_table.xview)
                scrolly.configure(command=self.rd8_semister_faculty_data_table.yview)

                #self.rd8_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.rd8_semister_faculty_data_table.heading('rd8_semister_faculty_name',text='Faculty Name ')
                self.rd8_semister_faculty_data_table.heading('rd8_semister_faculty_branch',text='Faculty Branch ')
                self.rd8_semister_faculty_data_table.heading('rd8_semister_faculty_subject',text='Faculty Subject ')

                #self.rd8_semister_faculty_data_table.column('cid',width=150)
                self.rd8_semister_faculty_data_table.column('rd8_semister_faculty_name',width=210)
                self.rd8_semister_faculty_data_table.column('rd8_semister_faculty_branch',width=220)
                self.rd8_semister_faculty_data_table.column('rd8_semister_faculty_subject',width=210)

                self.rd8_semister_faculty_data_table['show']='headings'

                self.rd8_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_8th_semister_faculty_data()
                self.rd8_semister_faculty_data_table.bind('<ButtonRelease-1>',rd8_semister_faculty_data_get)



        
############################################# 8th semister mech #########################################################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Mechanical_Engineering":
                table_frame39=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame39.place(x=10,y=120) 

################################################################################################
                def add_mech_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                   # con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_mech_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame39)
                    else:
                        if self.var_mech_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame39)
                        else:
                            if self.var_mech_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame39)
                            else:
                                cur.execute('insert into add_mech_8th_semsiter_faculty(mech_8th_semister_faculty_name,mech_8th_semister_faculty_branch,mech_8th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_mech_8th_semister_faculty_name.get(),
                                self.var_mech_8th_semister_faculty_branch.get(),
                                self.var_mech_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_mech_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame39)
                def fetch_mech_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_mech_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.mech_8th_semister_faculty_data_table.delete(*self.mech_8th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.mech_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame39)

                def mech_8th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame39)
                        else:
                            cur.execute(f"select * from add_mech_8th_semsiter_faculty where mech_8th_semister_faculty_name LIKE '%{self.var_mech_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.mech_8th_semister_faculty_data_table.delete(*self.mech_8th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.mech_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame39)
                def mech_8th_semister_faculty_data_get(ev):
                    r1=self.mech_8th_semister_faculty_data_table.focus()
                    content1=self.mech_8th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_mech_8th_semister_faculty_name.set(row1[0])
                    self.var_mech_8th_semister_faculty_branch.set(row1[1])
                    self.var_mech_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame39)

                def mech_8th_semister_faculty_data_clear():
                    fetch_mech_8th_semister_faculty_data()
                    self.var_mech_8th_semister_faculty_serch.set("")
                    self.var_mech_8th_semister_faculty_name.set("")
                    self.var_mech_8th_semister_faculty_branch.set("")
                    self.var_mech_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame39)
                def mech_8th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame39)
                        else:
                            cur.execute("select * from add_mech_8th_semsiter_faculty where mech_8th_semister_faculty_name=%s",(self.var_mech_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame39)
                            else:
                                cur.execute("update add_mech_8th_semsiter_faculty set mech_8th_semister_faculty_branch=%s,mech_8th_semister_faculty_subject=%s where mech_8th_semister_faculty_name=%s",(
                                    
                                    self.var_mech_8th_semister_faculty_branch.get(),
                                    self.var_mech_8th_semister_faculty_subject.get(),
                                    self.var_mech_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame39)
                                fetch_mech_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame39)
                def mech_8th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_mech_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame39)
                        else:
                            cur.execute("select * from add_mech_8th_semsiter_faculty where mech_8th_semister_faculty_name=%s",(self.var_mech_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame39)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame39)
                                if option==True:
                                    cur.execute('delete from add_mech_8th_semsiter_faculty where mech_8th_semister_faculty_name=%s',(self.var_mech_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame39)
                                    mech_8th_semister_faculty_data_clear()
                                    fetch_mech_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame39)
                
################################################################################################

                label11=Label(table_frame39,text='8th Semsiter MECH:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame39,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame39,width=29,textvariable=self.var_mech_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame39,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame39,width=29,textvariable=self.var_mech_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame39,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame39,width=29,textvariable=self.var_mech_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame39,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_mech_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=mech_8th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=mech_8th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=mech_8th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_mech_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=mech_8th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.mech_8th_semister_facuty_table_frame=Frame(table_frame39,width=800,height=200,relief=GROOVE)
                self.mech_8th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.mech_8th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.mech_8th_semister_facuty_table_frame,orient=VERTICAL)
                self.mech_8th_semister_faculty_data_table=ttk.Treeview(self.mech_8th_semister_facuty_table_frame,columns=('mech_8th_semister_faculty_name','mech_8th_semister_faculty_branch','mech_8th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.mech_8th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.mech_8th_semister_faculty_data_table.yview)

                #self.mech_8th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.mech_8th_semister_faculty_data_table.heading('mech_8th_semister_faculty_name',text='Faculty Name ')
                self.mech_8th_semister_faculty_data_table.heading('mech_8th_semister_faculty_branch',text='Faculty Branch ')
                self.mech_8th_semister_faculty_data_table.heading('mech_8th_semister_faculty_subject',text='Faculty Subject ')

                #self.mech_8th_semister_faculty_data_table.column('cid',width=150)
                self.mech_8th_semister_faculty_data_table.column('mech_8th_semister_faculty_name',width=210)
                self.mech_8th_semister_faculty_data_table.column('mech_8th_semister_faculty_branch',width=300)
                self.mech_8th_semister_faculty_data_table.column('mech_8th_semister_faculty_subject',width=270)

                self.mech_8th_semister_faculty_data_table['show']='headings'

                self.mech_8th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_mech_8th_semister_faculty_data()
                self.mech_8th_semister_faculty_data_table.bind('<ButtonRelease-1>',mech_8th_semister_faculty_data_get)
################################################################################ Electrical_And_Electronic_Engineering ############################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Electrical_And_Electronic_Engineering":
                table_frame40=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame40.place(x=10,y=120) 

################################################################################################
                def add_eee_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_eee_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame40)
                    else:
                        if self.var_eee_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame40)
                        else:
                            if self.var_eee_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame40)
                            else:
                                cur.execute('insert into add_eee_8th_semsiter_faculty(eee_8th_semister_faculty_name,eee_8th_semister_faculty_branch,eee_8th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_eee_8th_semister_faculty_name.get(),
                                self.var_eee_8th_semister_faculty_branch.get(),
                                self.var_eee_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_eee_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame40)
                def fetch_eee_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_eee_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.eee_8th_semister_faculty_data_table.delete(*self.eee_8th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.eee_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame40)

                def eee_8th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame40)
                        else:
                            cur.execute(f"select * from add_eee_8th_semsiter_faculty where eee_8th_semister_faculty_name LIKE '%{self.var_eee_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.eee_8th_semister_faculty_data_table.delete(*self.eee_8th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.eee_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame40)
                def eee_8th_semister_faculty_data_get(ev):
                    r1=self.eee_8th_semister_faculty_data_table.focus()
                    content1=self.eee_8th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_eee_8th_semister_faculty_name.set(row1[0])
                    self.var_eee_8th_semister_faculty_branch.set(row1[1])
                    self.var_eee_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame40)

                def eee_8th_semister_faculty_data_clear():
                    fetch_eee_8th_semister_faculty_data()
                    self.var_eee_8th_semister_faculty_serch.set("")
                    self.var_eee_8th_semister_faculty_name.set("")
                    self.var_eee_8th_semister_faculty_branch.set("")
                    self.var_eee_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame40)
                def eee_8th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame40)
                        else:
                            cur.execute("select * from add_eee_8th_semsiter_faculty where eee_8th_semister_faculty_name=%s",(self.var_eee_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame40)
                            else:
                                cur.execute("update add_eee_8th_semsiter_faculty set eee_8th_semister_faculty_branch=%s,eee_8th_semister_faculty_subject=%s where eee_8th_semister_faculty_name=%s",(
                                    
                                    self.var_eee_8th_semister_faculty_branch.get(),
                                    self.var_eee_8th_semister_faculty_subject.get(),
                                    self.var_eee_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame40)
                                fetch_eee_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame40)
                def eee_8th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_eee_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame40)
                        else:
                            cur.execute("select * from add_eee_8th_semsiter_faculty where eee_8th_semister_faculty_name=%s",(self.var_eee_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame40)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame40)
                                if option==True:
                                    cur.execute('delete from add_eee_8th_semsiter_faculty where eee_8th_semister_faculty_name=%s',(self.var_eee_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame40)
                                    eee_8th_semister_faculty_data_clear()
                                    fetch_eee_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame40)
                
################################################################################################

                label11=Label(table_frame40,text='8th Semsiter EEE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame40,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame40,width=29,textvariable=self.var_eee_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame40,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame40,width=29,textvariable=self.var_eee_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame40,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame40,width=29,textvariable=self.var_eee_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame40,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_eee_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=eee_8th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=eee_8th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=eee_8th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_eee_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=eee_8th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.eee_8th_semister_facuty_table_frame=Frame(table_frame40,width=800,height=200,relief=GROOVE)
                self.eee_8th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.eee_8th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.eee_8th_semister_facuty_table_frame,orient=VERTICAL)
                self.eee_8th_semister_faculty_data_table=ttk.Treeview(self.eee_8th_semister_facuty_table_frame,columns=('eee_8th_semister_faculty_name','eee_8th_semister_faculty_branch','eee_8th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.eee_8th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.eee_8th_semister_faculty_data_table.yview)

                #self.eee_8th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.eee_8th_semister_faculty_data_table.heading('eee_8th_semister_faculty_name',text='Faculty Name ')
                self.eee_8th_semister_faculty_data_table.heading('eee_8th_semister_faculty_branch',text='Faculty Branch ')
                self.eee_8th_semister_faculty_data_table.heading('eee_8th_semister_faculty_subject',text='Faculty Subject ')

                #self.eee_8th_semister_faculty_data_table.column('cid',width=150)
                self.eee_8th_semister_faculty_data_table.column('eee_8th_semister_faculty_name',width=210)
                self.eee_8th_semister_faculty_data_table.column('eee_8th_semister_faculty_branch',width=300)
                self.eee_8th_semister_faculty_data_table.column('eee_8th_semister_faculty_subject',width=270)

                self.eee_8th_semister_faculty_data_table['show']='headings'

                self.eee_8th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_eee_8th_semister_faculty_data()
                self.eee_8th_semister_faculty_data_table.bind('<ButtonRelease-1>',eee_8th_semister_faculty_data_get)
        
############################################# 8th semister ece #########################################################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Communication_Engineering":
                table_frame41=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame41.place(x=10,y=120) 

################################################################################################
                def add_ece_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ece_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame41)
                    else:
                        if self.var_ece_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame41)
                        else:
                            if self.var_ece_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame41)
                            else:
                                cur.execute('insert into add_ece_8th_semsiter_faculty(ece_8th_semister_faculty_name,ece_8th_semister_faculty_branch,ece_8th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ece_8th_semister_faculty_name.get(),
                                self.var_ece_8th_semister_faculty_branch.get(),
                                self.var_ece_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ece_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame41)
                def fetch_ece_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ece_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ece_8th_semister_faculty_data_table.delete(*self.ece_8th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ece_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame41)

                def ece_8th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame41)
                        else:
                            cur.execute(f"select * from add_ece_8th_semsiter_faculty where ece_8th_semister_faculty_name LIKE '%{self.var_ece_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ece_8th_semister_faculty_data_table.delete(*self.ece_8th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ece_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame41)
                def ece_8th_semister_faculty_data_get(ev):
                    r1=self.ece_8th_semister_faculty_data_table.focus()
                    content1=self.ece_8th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ece_8th_semister_faculty_name.set(row1[0])
                    self.var_ece_8th_semister_faculty_branch.set(row1[1])
                    self.var_ece_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame41)

                def ece_8th_semister_faculty_data_clear():
                    fetch_ece_8th_semister_faculty_data()
                    self.var_ece_8th_semister_faculty_serch.set("")
                    self.var_ece_8th_semister_faculty_name.set("")
                    self.var_ece_8th_semister_faculty_branch.set("")
                    self.var_ece_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame41)
                def ece_8th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame41)
                        else:
                            cur.execute("select * from add_ece_8th_semsiter_faculty where ece_8th_semister_faculty_name=%s",(self.var_ece_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame41)
                            else:
                                cur.execute("update add_ece_8th_semsiter_faculty set ece_8th_semister_faculty_branch=%s,ece_8th_semister_faculty_subject=%s where ece_8th_semister_faculty_name=%s",(
                                    
                                    self.var_ece_8th_semister_faculty_branch.get(),
                                    self.var_ece_8th_semister_faculty_subject.get(),
                                    self.var_ece_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame41)
                                fetch_ece_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame41)
                def ece_8th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ece_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame41)
                        else:
                            cur.execute("select * from add_ece_8th_semsiter_faculty where ece_8th_semister_faculty_name=%s",(self.var_ece_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame41)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame41)
                                if option==True:
                                    cur.execute('delete from add_ece_8th_semsiter_faculty where ece_8th_semister_faculty_name=%s',(self.var_ece_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame41)
                                    ece_8th_semister_faculty_data_clear()
                                    fetch_ece_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame41)
                
################################################################################################

                label11=Label(table_frame41,text='8th Semister ECE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame41,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame41,width=29,textvariable=self.var_ece_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame41,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame41,width=29,textvariable=self.var_ece_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame41,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame41,width=29,textvariable=self.var_ece_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame41,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ece_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ece_8th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ece_8th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ece_8th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ece_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ece_8th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ece_8th_semister_facuty_table_frame=Frame(table_frame41,width=800,height=200,relief=GROOVE)
                self.ece_8th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ece_8th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ece_8th_semister_facuty_table_frame,orient=VERTICAL)
                self.ece_8th_semister_faculty_data_table=ttk.Treeview(self.ece_8th_semister_facuty_table_frame,columns=('ece_8th_semister_faculty_name','ece_8th_semister_faculty_branch','ece_8th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ece_8th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ece_8th_semister_faculty_data_table.yview)

                #self.ece_8th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ece_8th_semister_faculty_data_table.heading('ece_8th_semister_faculty_name',text='Faculty Name ')
                self.ece_8th_semister_faculty_data_table.heading('ece_8th_semister_faculty_branch',text='Faculty Branch ')
                self.ece_8th_semister_faculty_data_table.heading('ece_8th_semister_faculty_subject',text='Faculty Subject ')

                #self.ece_8th_semister_faculty_data_table.column('cid',width=150)
                self.ece_8th_semister_faculty_data_table.column('ece_8th_semister_faculty_name',width=210)
                self.ece_8th_semister_faculty_data_table.column('ece_8th_semister_faculty_branch',width=300)
                self.ece_8th_semister_faculty_data_table.column('ece_8th_semister_faculty_subject',width=270)

                self.ece_8th_semister_faculty_data_table['show']='headings'

                self.ece_8th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ece_8th_semister_faculty_data()
                self.ece_8th_semister_faculty_data_table.bind('<ButtonRelease-1>',ece_8th_semister_faculty_data_get)
        ############################################# 8th semister CS #########################################################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Computer_Science_Engineering":
                table_frame42=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame42.place(x=10,y=120) 

################################################################################################
                def add_cs_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                   # con=sqlite3.connect(database='StudentDataBase.db')
                   
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_cs_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame42)
                    else:
                        if self.var_cs_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame42)
                        else:
                            if self.var_cs_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame42)
                            else:
                                cur.execute('insert into add_cs_8th_semsiter_faculty(cs_8th_semister_faculty_name,cs_8th_semister_faculty_branch,cs_8th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_cs_8th_semister_faculty_name.get(),
                                self.var_cs_8th_semister_faculty_branch.get(),
                                self.var_cs_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_cs_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame42)
                def fetch_cs_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_cs_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.cs_8th_semister_faculty_data_table.delete(*self.cs_8th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.cs_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame42)

                def cs_8th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame42)
                        else:
                            cur.execute(f"select * from add_cs_8th_semsiter_faculty where cs_8th_semister_faculty_name LIKE '%{self.var_cs_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.cs_8th_semister_faculty_data_table.delete(*self.cs_8th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.cs_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame42)
                def cs_8th_semister_faculty_data_get(ev):
                    r1=self.cs_8th_semister_faculty_data_table.focus()
                    content1=self.cs_8th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_cs_8th_semister_faculty_name.set(row1[0])
                    self.var_cs_8th_semister_faculty_branch.set(row1[1])
                    self.var_cs_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame42)

                def cs_8th_semister_faculty_data_clear():
                    fetch_cs_8th_semister_faculty_data()
                    self.var_cs_8th_semister_faculty_serch.set("")
                    self.var_cs_8th_semister_faculty_name.set("")
                    self.var_cs_8th_semister_faculty_branch.set("")
                    self.var_cs_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame42)
                def cs_8th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame42)
                        else:
                            cur.execute("select * from add_cs_8th_semsiter_faculty where cs_8th_semister_faculty_name=?",(self.var_cs_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame42)
                            else:
                                cur.execute("update add_cs_8th_semsiter_faculty set cs_8th_semister_faculty_branch=?,cs_8th_semister_faculty_subject=? where cs_8th_semister_faculty_name=?",(
                                    
                                    self.var_cs_8th_semister_faculty_branch.get(),
                                    self.var_cs_8th_semister_faculty_subject.get(),
                                    self.var_cs_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame42)
                                fetch_cs_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame42)
                def cs_8th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_cs_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame42)
                        else:
                            cur.execute("select * from add_cs_8th_semsiter_faculty where cs_8th_semister_faculty_name=%s",(self.var_cs_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame42)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame42)
                                if option==True:
                                    cur.execute('delete from add_cs_8th_semsiter_faculty where cs_8th_semister_faculty_name=%s',(self.var_cs_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame42)
                                    cs_8th_semister_faculty_data_clear()
                                    fetch_cs_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame42)
                
################################################################################################

                label11=Label(table_frame42,text='8th Semister CS:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame42,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame42,width=29,textvariable=self.var_cs_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame42,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame42,width=29,textvariable=self.var_cs_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame42,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame42,width=29,textvariable=self.var_cs_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame42,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_cs_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=cs_8th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=cs_8th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=cs_8th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_cs_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=cs_8th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.cs_8th_semister_facuty_table_frame=Frame(table_frame42,width=800,height=200,relief=GROOVE)
                self.cs_8th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.cs_8th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.cs_8th_semister_facuty_table_frame,orient=VERTICAL)
                self.cs_8th_semister_faculty_data_table=ttk.Treeview(self.cs_8th_semister_facuty_table_frame,columns=('cs_8th_semister_faculty_name','cs_8th_semister_faculty_branch','cs_8th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.cs_8th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.cs_8th_semister_faculty_data_table.yview)

                #self.cs_8th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.cs_8th_semister_faculty_data_table.heading('cs_8th_semister_faculty_name',text='Faculty Name ')
                self.cs_8th_semister_faculty_data_table.heading('cs_8th_semister_faculty_branch',text='Faculty Branch ')
                self.cs_8th_semister_faculty_data_table.heading('cs_8th_semister_faculty_subject',text='Faculty Subject ')

                #self.cs_8th_semister_faculty_data_table.column('cid',width=150)
                self.cs_8th_semister_faculty_data_table.column('cs_8th_semister_faculty_name',width=210)
                self.cs_8th_semister_faculty_data_table.column('cs_8th_semister_faculty_branch',width=300)
                self.cs_8th_semister_faculty_data_table.column('cs_8th_semister_faculty_subject',width=270)

                self.cs_8th_semister_faculty_data_table['show']='headings'

                self.cs_8th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_cs_8th_semister_faculty_data()
                self.cs_8th_semister_faculty_data_table.bind('<ButtonRelease-1>',cs_8th_semister_faculty_data_get)
 ############################################# 8th semister ISE #########################################################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Information_Science_and_Engineering":
                table_frame43=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame43.place(x=10,y=120) 

################################################################################################
                def add_ise_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ise_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame43)
                    else:
                        if self.var_ise_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame43)
                        else:
                            if self.var_ise_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame43)
                            else:
                                cur.execute('insert into add_ise_8th_semsiter_faculty(ise_8th_semister_faculty_name,ise_8th_semister_faculty_branch,ise_8th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ise_8th_semister_faculty_name.get(),
                                self.var_ise_8th_semister_faculty_branch.get(),
                                self.var_ise_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ise_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame43)
                def fetch_ise_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ise_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ise_8th_semister_faculty_data_table.delete(*self.ise_8th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ise_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame43)

                def ise_8th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame43)
                        else:
                            cur.execute(f"select * from add_ise_8th_semsiter_faculty where ise_8th_semister_faculty_name LIKE '%{self.var_ise_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ise_8th_semister_faculty_data_table.delete(*self.ise_8th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ise_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame43)
                def ise_8th_semister_faculty_data_get(ev):
                    r1=self.ise_8th_semister_faculty_data_table.focus()
                    content1=self.ise_8th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ise_8th_semister_faculty_name.set(row1[0])
                    self.var_ise_8th_semister_faculty_branch.set(row1[1])
                    self.var_ise_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame43)

                def ise_8th_semister_faculty_data_clear():
                    fetch_ise_8th_semister_faculty_data()
                    self.var_ise_8th_semister_faculty_serch.set("")
                    self.var_ise_8th_semister_faculty_name.set("")
                    self.var_ise_8th_semister_faculty_branch.set("")
                    self.var_ise_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame43)
                def ise_8th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame43)
                        else:
                            cur.execute("select * from add_ise_8th_semsiter_faculty where ise_8th_semister_faculty_name=%s",(self.var_ise_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame43)
                            else:
                                cur.execute("update add_ise_8th_semsiter_faculty set ise_8th_semister_faculty_branch=%s,ise_8th_semister_faculty_subject=%s where ise_8th_semister_faculty_name=%s",(
                                    
                                    self.var_ise_8th_semister_faculty_branch.get(),
                                    self.var_ise_8th_semister_faculty_subject.get(),
                                    self.var_ise_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame43)
                                fetch_ise_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame43)
                def ise_8th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ise_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame43)
                        else:
                            cur.execute("select * from add_ise_8th_semsiter_faculty where ise_8th_semister_faculty_name=%s",(self.var_ise_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame43)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame43)
                                if option==True:
                                    cur.execute('delete from add_ise_8th_semsiter_faculty where ise_8th_semister_faculty_name=%s',(self.var_ise_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame43)
                                    ise_8th_semister_faculty_data_clear()
                                    fetch_ise_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame43)
                
################################################################################################

                label11=Label(table_frame43,text='8th Semister ISE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame43,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame43,width=29,textvariable=self.var_ise_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame43,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame43,width=29,textvariable=self.var_ise_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame43,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame43,width=29,textvariable=self.var_ise_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame43,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ise_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ise_8th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ise_8th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ise_8th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ise_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ise_8th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ise_8th_semister_facuty_table_frame=Frame(table_frame43,width=800,height=200,relief=GROOVE)
                self.ise_8th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ise_8th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ise_8th_semister_facuty_table_frame,orient=VERTICAL)
                self.ise_8th_semister_faculty_data_table=ttk.Treeview(self.ise_8th_semister_facuty_table_frame,columns=('ise_8th_semister_faculty_name','ise_8th_semister_faculty_branch','ise_8th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ise_8th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ise_8th_semister_faculty_data_table.yview)

                #self.ise_8th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ise_8th_semister_faculty_data_table.heading('ise_8th_semister_faculty_name',text='Faculty Name ')
                self.ise_8th_semister_faculty_data_table.heading('ise_8th_semister_faculty_branch',text='Faculty Branch ')
                self.ise_8th_semister_faculty_data_table.heading('ise_8th_semister_faculty_subject',text='Faculty Subject ')

                #self.ise_8th_semister_faculty_data_table.column('cid',width=150)
                self.ise_8th_semister_faculty_data_table.column('ise_8th_semister_faculty_name',width=210)
                self.ise_8th_semister_faculty_data_table.column('ise_8th_semister_faculty_branch',width=300)
                self.ise_8th_semister_faculty_data_table.column('ise_8th_semister_faculty_subject',width=270)

                self.ise_8th_semister_faculty_data_table['show']='headings'

                self.ise_8th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ise_8th_semister_faculty_data()
                self.ise_8th_semister_faculty_data_table.bind('<ButtonRelease-1>',ise_8th_semister_faculty_data_get)
         ############################################# 8th semister ETE #########################################################################################################################
        if self.var_sem_select.get()=="8th_Semister":
            if self.var_branch_select.get() == "Electronic_And_Telecommunication_Engineering":
                table_frame44=Frame(self.root,width=1035,height=300,relief=GROOVE,bd=2,bg='white')
                table_frame44.place(x=10,y=120) 

################################################################################################
                def add_ete_8th_semister_faculty_into_database():


                    ##################################
                    
                    ######################################
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    
                    if self.var_ete_8th_semister_faculty_name.get()=='':
                        messagebox.showerror('Error','The faculty name must be required',parent=table_frame44)
                    else:
                        if self.var_ete_8th_semister_faculty_branch.get()=='':
                            messagebox.showerror('Error','The faclty branch mest be required',parent=table_frame44)
                        else:
                            if self.var_ete_8th_semister_faculty_subject.get()=='':
                                messagebox.showerror('Error','The faculty subject must be rquired',parent=table_frame44)
                            else:
                                cur.execute('insert into add_ete_8th_semsiter_faculty(ete_8th_semister_faculty_name,ete_8th_semister_faculty_branch,ete_8th_semister_faculty_subject) values(%s,%s,%s)',(
                                self.var_ete_8th_semister_faculty_name.get(),
                                self.var_ete_8th_semister_faculty_branch.get(),
                                self.var_ete_8th_semister_faculty_subject.get()
                            ))
                            con.commit()
                            fetch_ete_8th_semister_faculty_data()
                            con.close()
                            messagebox.showinfo('Info','The data added successfulty...',parent=table_frame44)
                def fetch_ete_8th_semister_faculty_data():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from add_ete_8th_semsiter_faculty')
                        rows=cur.fetchall()
                        self.ete_8th_semister_faculty_data_table.delete(*self.ete_8th_semister_faculty_data_table.get_children())
                        for row in rows:
                            self.ete_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame44)

                def ete_8th_semister_faculty_serch():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_8th_semister_faculty_serch.get()=='':
                            messagebox.showerror('Error','The faculty name must be required must be required',parent=table_frame44)
                        else:
                            cur.execute(f"select * from add_ete_8th_semsiter_faculty where ete_8th_semister_faculty_name LIKE '%{self.var_ete_8th_semister_faculty_serch.get()}%' ")
                            rows=cur.fetchall()
                            self.ete_8th_semister_faculty_data_table.delete(*self.ete_8th_semister_faculty_data_table.get_children())
                            for row in rows:
                                self.ete_8th_semister_faculty_data_table.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f"Error due to {str(ex)}",parent=table_frame44)
                def ete_8th_semister_faculty_data_get(ev):
                    r1=self.ete_8th_semister_faculty_data_table.focus()
                    content1=self.ete_8th_semister_faculty_data_table.item(r1)
                    row1=content1["values"]

                    self.var_ete_8th_semister_faculty_name.set(row1[0])
                    self.var_ete_8th_semister_faculty_branch.set(row1[1])
                    self.var_ete_8th_semister_faculty_subject.set(row1[2])
                    messagebox.showinfo('Info','The all data fetch successfully ',parent=table_frame44)

                def ete_8th_semister_faculty_data_clear():
                    fetch_ete_8th_semister_faculty_data()
                    self.var_ete_8th_semister_faculty_serch.set("")
                    self.var_ete_8th_semister_faculty_name.set("")
                    self.var_ete_8th_semister_faculty_branch.set("")
                    self.var_ete_8th_semister_faculty_subject.set("")
                    messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=table_frame44)
                def ete_8th_semister_faculty_data_update():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required?',parent=table_frame44)
                        else:
                            cur.execute("select * from add_ete_8th_semsiter_faculty where ete_8th_semister_faculty_name=%s",(self.var_ete_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Select a Faculty name from the  table:",parent=table_frame44)
                            else:
                                cur.execute("update add_ete_8th_semsiter_faculty set ete_8th_semister_faculty_branch=%s,ete_8th_semister_faculty_subject=%s where ete_8th_semister_faculty_name=%s",(
                                    
                                    self.var_ete_8th_semister_faculty_branch.get(),
                                    self.var_ete_8th_semister_faculty_subject.get(),
                                    self.var_ete_8th_semister_faculty_name.get()
                                                                                                            
                                ))
                                con.commit()
                                messagebox.showinfo('Success','Faculty details is updated successfuly..........',parent=table_frame44)
                                fetch_ete_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f'error due to{str(ex)}',parent=table_frame44)
                def ete_8th_semister_faculty_data_delete():
                    #con=sqlite3.connect(database='StudentDataBase.db')
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_ete_8th_semister_faculty_name.get()=="":
                            messagebox.showerror('Error','Faculty name  must be required',parent=table_frame44)
                        else:
                            cur.execute("select * from add_ete_8th_semsiter_faculty where ete_8th_semister_faculty_name=%s",(self.var_ete_8th_semister_faculty_name.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','select the Faculty name from the table',parent=table_frame44)
                            else:
                                option=messagebox.askyesno('confirm','do you want to delete the faculty detail from the database',parent=table_frame44)
                                if option==True:
                                    cur.execute('delete from add_ete_8th_semsiter_faculty where ete_8th_semister_faculty_name=%s',(self.var_ete_8th_semister_faculty_name.get(),))
                                    con.commit()
                                    messagebox.showinfo('Info','The student data deleted successfully.......',parent=table_frame44)
                                    ete_8th_semister_faculty_data_clear()
                                    fetch_ete_8th_semister_faculty_data()
                    except Exception as ex:
                        messagebox.showerror('Error',f"The error due to {str(ex)}",parent=table_frame44)
                
################################################################################################

                label11=Label(table_frame44,text='8th Semister ETE:',font=('times new roman',13,'bold'),bg='white',bd=2).place(x=10,y=10,width=180,height=20)

                faculty_label=Label(table_frame44,text='Enter the Faculty name:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=40)

                faculty_entry=ttk.Entry(table_frame44,width=29,textvariable=self.var_ete_8th_semister_faculty_name)
                faculty_entry.place(x=10,y=80)
                
                #add_database_chemistry_faculty=ttk.Button(table_frame,text='Add Database',width=15)
                #add_database_chemistry_faculty.place(x=200,y=78)

                faculty_barnch_label=Label(table_frame44,text='Enter the Faculty Branch:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=120)

                faculty_branch_entry=ttk.Combobox(table_frame44,width=29,textvariable=self.var_ete_8th_semister_faculty_branch)
                faculty_branch_entry.place(x=10,y=160)
                faculty_branch_entry['values']=(
                                    'Civil_Engineering',
                                    'Mechanical_Engineering',
                                    'Electrical_And_Electronic_Engineering',
                                    'Electronic_And_Communication_Engineering',
                                    'Computer_Science_Engineering',
                                    'Information_Science_and_Engineering',
                                    'Electronic_And_Telecommunication_Engineering',
                                    'Master_of_Businee_ Administration',
                                    'Master_of_Computer_Application'
                    
                )
                faculty_subject_label=Label(table_frame44,text='Enter the Faculty Subject:',font=('times new roman',13,'bold'),bg='white').place(x=10,y=200)

                faculty_subject_entry=ttk.Combobox(table_frame44,width=29,textvariable=self.var_ete_8th_semister_faculty_subject)
                faculty_subject_entry.place(x=10,y=240)
                faculty_subject_entry['values']=(
                                    'kannada',
                                    'english',
                                    'samaja',
                                    'scinces',
                                    'social',
                                    'hindi',
                                    'maths',
                                    'ss',
                                    'ed'
         
                )

                menu_frame1=tk.LabelFrame(table_frame44,bg='white',fg='#262626')
                menu_frame1.place(x=220,y=2,width=784,height=55)

                
                update_faculty=ttk.Button(menu_frame1,text='Add to Data Base',width=20,command=add_ete_8th_semister_faculty_into_database).grid(row=0,column=0,padx=4,pady=9)
                clear_faculty=ttk.Button(menu_frame1,text='Update',width=15,command=ete_8th_semister_faculty_data_update).grid(row=0,column=1,padx=4,pady=9)
                delete_faculty=ttk.Button(menu_frame1,text='Delete',width=15,command=ete_8th_semister_faculty_data_delete).grid(row=0,column=2,padx=4,pady=9)
                clear_all=ttk.Button(menu_frame1,text='Clear',width=15,command=ete_8th_semister_faculty_data_clear).grid(row=0,column=3,padx=4,pady=9)
                
                faculty_serch=ttk.Entry(menu_frame1,width=31,textvariable=self.var_ete_8th_semister_faculty_serch)
                faculty_serch.grid(row=0,column=4,padx=4,pady=9)
                add_faculty=ttk.Button(menu_frame1,text='Search',width=15,command=ete_8th_semister_faculty_serch).grid(row=0,column=5,padx=4,pady=9)

                self.ete_8th_semister_facuty_table_frame=Frame(table_frame44,width=800,height=200,relief=GROOVE)
                self.ete_8th_semister_facuty_table_frame.place(x=220,y=50)

                scrollx=Scrollbar(self.ete_8th_semister_facuty_table_frame,orient=HORIZONTAL)
                scrolly=Scrollbar(self.ete_8th_semister_facuty_table_frame,orient=VERTICAL)
                self.ete_8th_semister_faculty_data_table=ttk.Treeview(self.ete_8th_semister_facuty_table_frame,columns=('ete_8th_semister_faculty_name','ete_8th_semister_faculty_branch','ete_8th_semister_faculty_subject'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=self.ete_8th_semister_faculty_data_table.xview)
                scrolly.configure(command=self.ete_8th_semister_faculty_data_table.yview)

                #self.ete_8th_semister_faculty_data_table.heading('cid',text='Serial Number')
                self.ete_8th_semister_faculty_data_table.heading('ete_8th_semister_faculty_name',text='Faculty Name ')
                self.ete_8th_semister_faculty_data_table.heading('ete_8th_semister_faculty_branch',text='Faculty Branch ')
                self.ete_8th_semister_faculty_data_table.heading('ete_8th_semister_faculty_subject',text='Faculty Subject ')

                #self.ete_8th_semister_faculty_data_table.column('cid',width=150)
                self.ete_8th_semister_faculty_data_table.column('ete_8th_semister_faculty_name',width=210)
                self.ete_8th_semister_faculty_data_table.column('ete_8th_semister_faculty_branch',width=300)
                self.ete_8th_semister_faculty_data_table.column('ete_8th_semister_faculty_subject',width=270)

                self.ete_8th_semister_faculty_data_table['show']='headings'

                self.ete_8th_semister_faculty_data_table.pack(fill=BOTH,expand=1)
                fetch_ete_8th_semister_faculty_data()
                self.ete_8th_semister_faculty_data_table.bind('<ButtonRelease-1>',ete_8th_semister_faculty_data_get)

if __name__=='__main__':
    root=tk.Tk()
    ob=AddFaculty(root)
    root.mainloop()