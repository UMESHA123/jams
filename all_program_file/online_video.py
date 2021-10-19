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

class OnlineVideo():
    def __init__(self,root):
        self.root=root
        self.root.title("Video class")
        self.root.geometry('1055x440+213+145')
        self.root.resizable(False,False)
        self.root.configure(bg='white')
        #########################################################
        self.var_student_semister_select=StringVar()
        self.var_student_branch_select=StringVar()
        
        self.che_subjects_entry=StringVar()
        self.che_faculyt_entry=StringVar()
        self.var_che_watch_video=StringVar()
        self.var_serach_che_faculty=StringVar()

        self.phy_subjects_entry=StringVar()
        self.phy_faculyt_entry=StringVar()
        self.var_phy_watch_video=StringVar()
        self.var_serach_phy_faculty=StringVar()

        self.civil_3rd_subjects_entry=StringVar()
        self.civil_3rd_faculyt_entry=StringVar()
        self.var_civil_3rd_watch_video=StringVar()
        self.var_serach_civil_3rd_faculty=StringVar()

        self.civil_4th_subjects_entry=StringVar()
        self.civil_4th_faculyt_entry=StringVar()
        self.var_civil_4th_watch_video=StringVar()
        self.var_serach_civil_4th_faculty=StringVar()


        self.civil_5th_subjects_entry=StringVar()
        self.civil_5th_faculyt_entry=StringVar()
        self.var_civil_5th_watch_video=StringVar()
        self.var_serach_civil_5th_faculty=StringVar()


        self.civil_6th_subjects_entry=StringVar()
        self.civil_6th_faculyt_entry=StringVar()
        self.var_civil_6th_watch_video=StringVar()
        self.var_serach_civil_6th_faculty=StringVar()


        self.civil_7th_subjects_entry=StringVar()
        self.civil_7th_faculyt_entry=StringVar()
        self.var_civil_7th_watch_video=StringVar()
        self.var_serach_civil_7th_faculty=StringVar()


        self.civil_8th_subjects_entry=StringVar()
        self.civil_8th_faculyt_entry=StringVar()
        self.var_civil_8th_watch_video=StringVar()
        self.var_serach_civil_8th_faculty=StringVar()


        ########################################################################
        self.mech_3rd_subjects_entry=StringVar()
        self.mech_3rd_faculyt_entry=StringVar()
        self.var_mech_3rd_watch_video=StringVar()
        self.var_serach_mech_3rd_faculty=StringVar()

        self.mech_4th_subjects_entry=StringVar()
        self.mech_4th_faculyt_entry=StringVar()
        self.var_mech_4th_watch_video=StringVar()
        self.var_serach_mech_4th_faculty=StringVar()


        self.mech_5th_subjects_entry=StringVar()
        self.mech_5th_faculyt_entry=StringVar()
        self.var_mech_5th_watch_video=StringVar()
        self.var_serach_mech_5th_faculty=StringVar()


        self.mech_6th_subjects_entry=StringVar()
        self.mech_6th_faculyt_entry=StringVar()
        self.var_mech_6th_watch_video=StringVar()
        self.var_serach_mech_6th_faculty=StringVar()


        self.mech_7th_subjects_entry=StringVar()
        self.mech_7th_faculyt_entry=StringVar()
        self.var_mech_7th_watch_video=StringVar()
        self.var_serach_mech_7th_faculty=StringVar()


        self.mech_8th_subjects_entry=StringVar()
        self.mech_8th_faculyt_entry=StringVar()
        self.var_mech_8th_watch_video=StringVar()
        self.var_serach_mech_8th_faculty=StringVar()

        ###########################################################
        self.eee_3rd_subjects_entry=StringVar()
        self.eee_3rd_faculyt_entry=StringVar()
        self.var_eee_3rd_watch_video=StringVar()
        self.var_serach_eee_3rd_faculty=StringVar()

        self.eee_4th_subjects_entry=StringVar()
        self.eee_4th_faculyt_entry=StringVar()
        self.var_eee_4th_watch_video=StringVar()
        self.var_serach_eee_4th_faculty=StringVar()


        self.eee_5th_subjects_entry=StringVar()
        self.eee_5th_faculyt_entry=StringVar()
        self.var_eee_5th_watch_video=StringVar()
        self.var_serach_eee_5th_faculty=StringVar()


        self.eee_6th_subjects_entry=StringVar()
        self.eee_6th_faculyt_entry=StringVar()
        self.var_eee_6th_watch_video=StringVar()
        self.var_serach_eee_6th_faculty=StringVar()


        self.eee_7th_subjects_entry=StringVar()
        self.eee_7th_faculyt_entry=StringVar()
        self.var_eee_7th_watch_video=StringVar()
        self.var_serach_eee_7th_faculty=StringVar()


        self.eee_8th_subjects_entry=StringVar()
        self.eee_8th_faculyt_entry=StringVar()
        self.var_eee_8th_watch_video=StringVar()
        self.var_serach_eee_8th_faculty=StringVar()

        ######################################################
        self.ece_3rd_subjects_entry=StringVar()
        self.ece_3rd_faculyt_entry=StringVar()
        self.var_ece_3rd_watch_video=StringVar()
        self.var_serach_ece_3rd_faculty=StringVar()

        self.ece_4th_subjects_entry=StringVar()
        self.ece_4th_faculyt_entry=StringVar()
        self.var_ece_4th_watch_video=StringVar()
        self.var_serach_ece_4th_faculty=StringVar()


        self.ece_5th_subjects_entry=StringVar()
        self.ece_5th_faculyt_entry=StringVar()
        self.var_ece_5th_watch_video=StringVar()
        self.var_serach_ece_5th_faculty=StringVar()


        self.ece_6th_subjects_entry=StringVar()
        self.ece_6th_faculyt_entry=StringVar()
        self.var_ece_6th_watch_video=StringVar()
        self.var_serach_ece_6th_faculty=StringVar()


        self.ece_7th_subjects_entry=StringVar()
        self.ece_7th_faculyt_entry=StringVar()
        self.var_ece_7th_watch_video=StringVar()
        self.var_serach_ece_7th_faculty=StringVar()


        self.ece_8th_subjects_entry=StringVar()
        self.ece_8th_faculyt_entry=StringVar()
        self.var_ece_8th_watch_video=StringVar()
        self.var_serach_ece_8th_faculty=StringVar()

        ##############################################################
        self.ise_3rd_subjects_entry=StringVar()
        self.ise_3rd_faculyt_entry=StringVar()
        self.var_ise_3rd_watch_video=StringVar()
        self.var_serach_ise_3rd_faculty=StringVar()

        self.ise_4th_subjects_entry=StringVar()
        self.ise_4th_faculyt_entry=StringVar()
        self.var_ise_4th_watch_video=StringVar()
        self.var_serach_ise_4th_faculty=StringVar()


        self.ise_5th_subjects_entry=StringVar()
        self.ise_5th_faculyt_entry=StringVar()
        self.var_ise_5th_watch_video=StringVar()
        self.var_serach_ise_5th_faculty=StringVar()


        self.ise_6th_subjects_entry=StringVar()
        self.ise_6th_faculyt_entry=StringVar()
        self.var_ise_6th_watch_video=StringVar()
        self.var_serach_ise_6th_faculty=StringVar()


        self.ise_7th_subjects_entry=StringVar()
        self.ise_7th_faculyt_entry=StringVar()
        self.var_ise_7th_watch_video=StringVar()
        self.var_serach_ise_7th_faculty=StringVar()


        self.ise_8th_subjects_entry=StringVar()
        self.ise_8th_faculyt_entry=StringVar()
        self.var_ise_8th_watch_video=StringVar()
        self.var_serach_ise_8th_faculty=StringVar()
        ##########################################################
        self.ete_3rd_subjects_entry=StringVar()
        self.ete_3rd_faculyt_entry=StringVar()
        self.var_ete_3rd_watch_video=StringVar()
        self.var_serach_ete_3rd_faculty=StringVar()

        self.ete_4th_subjects_entry=StringVar()
        self.ete_4th_faculyt_entry=StringVar()
        self.var_ete_4th_watch_video=StringVar()
        self.var_serach_ete_4th_faculty=StringVar()


        self.ete_5th_subjects_entry=StringVar()
        self.ete_5th_faculyt_entry=StringVar()
        self.var_ete_5th_watch_video=StringVar()
        self.var_serach_ete_5th_faculty=StringVar()


        self.ete_6th_subjects_entry=StringVar()
        self.ete_6th_faculyt_entry=StringVar()
        self.var_ete_6th_watch_video=StringVar()
        self.var_serach_ete_6th_faculty=StringVar()


        self.ete_7th_subjects_entry=StringVar()
        self.ete_7th_faculyt_entry=StringVar()
        self.var_ete_7th_watch_video=StringVar()
        self.var_serach_ete_7th_faculty=StringVar()


        self.ete_8th_subjects_entry=StringVar()
        self.ete_8th_faculyt_entry=StringVar()
        self.var_ete_8th_watch_video=StringVar()
        self.var_serach_ete_8th_faculty=StringVar()
        ################################################################
        self.cs_3rd_subjects_entry=StringVar()
        self.cs_3rd_faculyt_entry=StringVar()
        self.var_cs_3rd_watch_video=StringVar()
        self.var_serach_cs_3rd_faculty=StringVar()

        self.cs_4th_subjects_entry=StringVar()
        self.cs_4th_faculyt_entry=StringVar()
        self.var_cs_4th_watch_video=StringVar()
        self.var_serach_cs_4th_faculty=StringVar()


        self.cs_5th_subjects_entry=StringVar()
        self.cs_5th_faculyt_entry=StringVar()
        self.var_cs_5th_watch_video=StringVar()
        self.var_serach_cs_5th_faculty=StringVar()


        self.cs_6th_subjects_entry=StringVar()
        self.cs_6th_faculyt_entry=StringVar()
        self.var_cs_6th_watch_video=StringVar()
        self.var_serach_cs_6th_faculty=StringVar()


        self.cs_7th_subjects_entry=StringVar()
        self.cs_7th_faculyt_entry=StringVar()
        self.var_cs_7th_watch_video=StringVar()
        self.var_serach_cs_7th_faculty=StringVar()


        self.cs_8th_subjects_entry=StringVar()
        self.cs_8th_faculyt_entry=StringVar()
        self.var_cs_8th_watch_video=StringVar()
        self.var_serach_cs_8th_faculty=StringVar()
        
        #########################################################
        
        top_label=tk.Label(self.root,text='Video calss',font=('Bahnschrift',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)

        menu_frame=tk.LabelFrame(self.root,text='Menu',font=('times now roman',10,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=10,y=40,width=1035,height=55)

        self.semister_entry=ttk.Combobox(menu_frame,width=43,textvariable=self.var_student_semister_select)
        self.semister_entry.grid(row=0,column=1,padx=5,pady=3)
        self.semister_entry['values']=(
            'CHEMISTRY_cycle',
            'PHYSICS_cycle',
            '3rd_Semister',
            '4th_Semister',
            '5th_Semister',
            '6th_Semister',
            '7th_Semister',
            '8th_Semister'
        )
        branch_entry=ttk.Combobox(menu_frame,width=45,textvariable=self.var_student_branch_select)
        branch_entry.grid(row=0,column=2,padx=5,pady=3)
        branch_entry['values']=(
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
        button2=ttk.Button(menu_frame,text='Search',width=20,command=self.serach_student).grid(row=0,column=4,padx=4,pady=3)

        bottom_label=tk.Label(self.root,text='for anr lsssfnsdskfjniieiicfjwefjj ferfhndfslidghsd\nugefwe76xve7tgxv7ebrtbxetkgxnsfkgkepnfbeogfwce',font=('times new roman',10),fg='white',bg='#363636')
        bottom_label.place(x=0,y=410,width=1060,height=30)
        
    def serach_student(self):
        if self.var_student_semister_select.get()=="CHEMISTRY_cycle":
            if self.var_student_branch_select.get()=='1st_semister':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                che_faculty_list=[]
                def che_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                che_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_che_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.che_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from che_watch_video where faculty=%s",(self.che_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_che_treeview.delete(*tree_che_treeview.get_children())
                            for row in rows:
                                tree_che_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_che_watch_video():
                    fetch_che_watch_video()
                    self.che_subjects_entry.set("")
                    self.che_faculyt_entry.set('')
                    self.var_che_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_che_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.che_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from che_watch_video where faculty=%s',(self.che_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from che_watch_video where faculty=%s ',(self.che_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_che_watch_video()
                                fetch_che_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_che_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.che_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update che_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.che_subjects_entry.get(),
                               
                                self.var_che_watch_video.get(),
                                self.che_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_che_watch_video()
                            fetch_che_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_che_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.che_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.che_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_che_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'phy_subjects','phy_date','phy_time','phy_code','semisters','branch'
                                cur.execute('insert into che_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.che_subjects_entry.get(),
                                self.che_faculyt_entry.get(),
                                self.var_che_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_che_watch_video()
                                con.close()
                def fetch_che_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from che_watch_video')
                        rows=cur.fetchall()
                        tree_che_treeview.delete(*tree_che_treeview.get_children())
                        for row in rows:
                            tree_che_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_che_watch_video(ev):
                    read=tree_che_treeview.focus()
                    content=tree_che_treeview.item(read)
                    row=content['values']
                    self.che_subjects_entry.set(row[0])
                    self.che_faculyt_entry.set(row[1])
                    self.var_che_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,heigh=300)
                fetch_che_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                che_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.che_subjects_entry,values=che_subjects_list)
                che_subjects_entry.grid(row=0,column=1)

                che_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                che_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.che_faculyt_entry,values=che_faculty_list)
                che_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                che_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_che_watch_video,width=44)
                che_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_che_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_che_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_che_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_che_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_che_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_che_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_che_treeview.xview)
                scrolly.configure(command=tree_che_treeview.yview)

                
                tree_che_treeview.heading('subject_name',text="Subject Name")
                tree_che_treeview.heading('faculty',text="Faculty")
                tree_che_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_che_treeview.column('subject_name',width=200)
                tree_che_treeview.column('faculty',width=100)
                tree_che_treeview.column('you_tube_link',width=250)

                tree_che_treeview['show']='headings'
                
                tree_che_treeview.pack(fill=BOTH,expand=1)
                fetch_che_watch_video()
                tree_che_treeview.bind('<ButtonRelease-1>',get_che_watch_video)
        if self.var_student_semister_select.get()=="PHYSICS_cycle":
            if self.var_student_branch_select.get()=='2nd_semister':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                phy_faculty_list=[]
                def phy_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                phy_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_phy_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.phy_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from phy_watch_video where faculty=%s",(self.phy_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_phy_treeview.delete(*tree_phy_treeview.get_children())
                            for row in rows:
                                tree_phy_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_phy_watch_video():
                    fetch_phy_watch_video()
                    self.phy_subjects_entry.set("")
                    self.phy_faculyt_entry.set('')
                    self.var_phy_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_phy_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.phy_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from phy_watch_video where faculty=%s',(self.phy_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from phy_watch_video where faculty=%s ',(self.phy_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_phy_watch_video()
                                fetch_phy_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_phy_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.phy_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update phy_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.phy_subjects_entry.get(),
                               
                                self.var_phy_watch_video.get(),
                                self.phy_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_phy_watch_video()
                            fetch_phy_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_phy_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.phy_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.phy_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_phy_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'phy_subjects','phy_date','phy_time','phy_code','semisters','branch'
                                cur.execute('insert into phy_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.phy_subjects_entry.get(),
                                self.phy_faculyt_entry.get(),
                                self.var_phy_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_phy_watch_video()
                                con.close()
                def fetch_phy_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from phy_watch_video')
                        rows=cur.fetchall()
                        tree_phy_treeview.delete(*tree_phy_treeview.get_children())
                        for row in rows:
                            tree_phy_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_phy_watch_video(ev):
                    read=tree_phy_treeview.focus()
                    content=tree_phy_treeview.item(read)
                    row=content['values']
                    self.phy_subjects_entry.set(row[0])
                    self.phy_faculyt_entry.set(row[1])
                    self.var_phy_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_phy_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                phy_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.phy_subjects_entry,values=phy_subjects_list)
                phy_subjects_entry.grid(row=0,column=1)

                phy_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                phy_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.phy_faculyt_entry,values=phy_faculty_list)
                phy_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                phy_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_phy_watch_video,width=44)
                phy_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_phy_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_phy_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_phy_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_phy_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_phy_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_phy_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_phy_treeview.xview)
                scrolly.configure(command=tree_phy_treeview.yview)

                
                tree_phy_treeview.heading('subject_name',text="Subject Name")
                tree_phy_treeview.heading('faculty',text="Faculty")
                tree_phy_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_phy_treeview.column('subject_name',width=200)
                tree_phy_treeview.column('faculty',width=100)
                tree_phy_treeview.column('you_tube_link',width=250)

                tree_phy_treeview['show']='headings'
                
                tree_phy_treeview.pack(fill=BOTH,expand=1)
                fetch_phy_watch_video()
                tree_phy_treeview.bind('<ButtonRelease-1>',get_phy_watch_video)
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                civil_3rd_faculty_list=[]
                def civil_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                civil_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_civil_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from civil_3rd_watch_video where faculty=%s",(self.civil_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_civil_3rd_treeview.delete(*tree_civil_3rd_treeview.get_children())
                            for row in rows:
                                tree_civil_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_civil_3rd_watch_video():
                    fetch_civil_3rd_watch_video()
                    self.civil_3rd_subjects_entry.set("")
                    self.civil_3rd_faculyt_entry.set('')
                    self.var_civil_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_civil_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from civil_3rd_watch_video where faculty=%s',(self.civil_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from civil_3rd_watch_video where faculty=%s ',(self.civil_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_civil_3rd_watch_video()
                                fetch_civil_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_civil_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update civil_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.civil_3rd_subjects_entry.get(),
                               
                                self.var_civil_3rd_watch_video.get(),
                                self.civil_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_civil_3rd_watch_video()
                            fetch_civil_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_civil_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.civil_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.civil_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_civil_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'civil_3rd_subjects','civil_3rd_date','civil_3rd_time','civil_3rd_code','semisters','branch'
                                cur.execute('insert into civil_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.civil_3rd_subjects_entry.get(),
                                self.civil_3rd_faculyt_entry.get(),
                                self.var_civil_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_civil_3rd_watch_video()
                                con.close()
                def fetch_civil_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from civil_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_civil_3rd_treeview.delete(*tree_civil_3rd_treeview.get_children())
                        for row in rows:
                            tree_civil_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_civil_3rd_watch_video(ev):
                    read=tree_civil_3rd_treeview.focus()
                    content=tree_civil_3rd_treeview.item(read)
                    row=content['values']
                    self.civil_3rd_subjects_entry.set(row[0])
                    self.civil_3rd_faculyt_entry.set(row[1])
                    self.var_civil_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_civil_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                civil_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.civil_3rd_subjects_entry,values=civil_3rd_subjects_list)
                civil_3rd_subjects_entry.grid(row=0,column=1)

                civil_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                civil_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.civil_3rd_faculyt_entry,values=civil_3rd_faculty_list)
                civil_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                civil_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_civil_3rd_watch_video,width=44)
                civil_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_civil_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_civil_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_civil_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_civil_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_civil_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_civil_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_civil_3rd_treeview.xview)
                scrolly.configure(command=tree_civil_3rd_treeview.yview)

                
                tree_civil_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_civil_3rd_treeview.heading('faculty',text="Faculty")
                tree_civil_3rd_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_civil_3rd_treeview.column('subject_name',width=200)
                tree_civil_3rd_treeview.column('faculty',width=100)
                tree_civil_3rd_treeview.column('you_tube_link',width=250)

                tree_civil_3rd_treeview['show']='headings'
                
                tree_civil_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_civil_3rd_watch_video()
                tree_civil_3rd_treeview.bind('<ButtonRelease-1>',get_civil_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                civil_4th_faculty_list=[]
                def civil_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                civil_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_civil_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from civil_4th_watch_video where faculty=%s",(self.civil_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_civil_4th_treeview.delete(*tree_civil_4th_treeview.get_children())
                            for row in rows:
                                tree_civil_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_civil_4th_watch_video():
                    fetch_civil_4th_watch_video()
                    self.civil_4th_subjects_entry.set("")
                    self.civil_4th_faculyt_entry.set('')
                    self.var_civil_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_civil_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from civil_4th_watch_video where faculty=%s',(self.civil_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from civil_4th_watch_video where faculty=%s ',(self.civil_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_civil_4th_watch_video()
                                fetch_civil_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_civil_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update civil_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.civil_4th_subjects_entry.get(),
                               
                                self.var_civil_4th_watch_video.get(),
                                self.civil_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_civil_4th_watch_video()
                            fetch_civil_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_civil_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.civil_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.civil_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_civil_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'civil_4th_subjects','civil_4th_date','civil_4th_time','civil_4th_code','semisters','branch'
                                cur.execute('insert into civil_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.civil_4th_subjects_entry.get(),
                                self.civil_4th_faculyt_entry.get(),
                                self.var_civil_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_civil_4th_watch_video()
                                con.close()
                def fetch_civil_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from civil_4th_watch_video')
                        rows=cur.fetchall()
                        tree_civil_4th_treeview.delete(*tree_civil_4th_treeview.get_children())
                        for row in rows:
                            tree_civil_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_civil_4th_watch_video(ev):
                    read=tree_civil_4th_treeview.focus()
                    content=tree_civil_4th_treeview.item(read)
                    row=content['values']
                    self.civil_4th_subjects_entry.set(row[0])
                    self.civil_4th_faculyt_entry.set(row[1])
                    self.var_civil_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_civil_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                civil_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.civil_4th_subjects_entry,values=civil_4th_subjects_list)
                civil_4th_subjects_entry.grid(row=0,column=1)

                civil_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                civil_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.civil_4th_faculyt_entry,values=civil_4th_faculty_list)
                civil_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                civil_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_civil_4th_watch_video,width=44)
                civil_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_civil_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_civil_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_civil_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_civil_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_civil_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_civil_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_civil_4th_treeview.xview)
                scrolly.configure(command=tree_civil_4th_treeview.yview)

                
                tree_civil_4th_treeview.heading('subject_name',text="Subject Name")
                tree_civil_4th_treeview.heading('faculty',text="Faculty")
                tree_civil_4th_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_civil_4th_treeview.column('subject_name',width=200)
                tree_civil_4th_treeview.column('faculty',width=100)
                tree_civil_4th_treeview.column('you_tube_link',width=250)

                tree_civil_4th_treeview['show']='headings'
                
                tree_civil_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_civil_4th_watch_video()
                tree_civil_4th_treeview.bind('<ButtonRelease-1>',get_civil_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                civil_5th_faculty_list=[]
                def civil_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                civil_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_civil_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from civil_5th_watch_video where faculty=%s",(self.civil_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_civil_5th_treeview.delete(*tree_civil_5th_treeview.get_children())
                            for row in rows:
                                tree_civil_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_civil_5th_watch_video():
                    fetch_civil_5th_watch_video()
                    self.civil_5th_subjects_entry.set("")
                    self.civil_5th_faculyt_entry.set('')
                    self.var_civil_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_civil_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from civil_5th_watch_video where faculty=%s',(self.civil_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from civil_5th_watch_video where faculty=%s ',(self.civil_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_civil_5th_watch_video()
                                fetch_civil_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_civil_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update civil_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.civil_5th_subjects_entry.get(),
                               
                                self.var_civil_5th_watch_video.get(),
                                self.civil_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_civil_5th_watch_video()
                            fetch_civil_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_civil_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.civil_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.civil_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_civil_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'civil_5th_subjects','civil_5th_date','civil_5th_time','civil_5th_code','semisters','branch'
                                cur.execute('insert into civil_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.civil_5th_subjects_entry.get(),
                                self.civil_5th_faculyt_entry.get(),
                                self.var_civil_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_civil_5th_watch_video()
                                con.close()
                def fetch_civil_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from civil_5th_watch_video')
                        rows=cur.fetchall()
                        tree_civil_5th_treeview.delete(*tree_civil_5th_treeview.get_children())
                        for row in rows:
                            tree_civil_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_civil_5th_watch_video(ev):
                    read=tree_civil_5th_treeview.focus()
                    content=tree_civil_5th_treeview.item(read)
                    row=content['values']
                    self.civil_5th_subjects_entry.set(row[0])
                    self.civil_5th_faculyt_entry.set(row[1])
                    self.var_civil_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_civil_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                civil_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.civil_5th_subjects_entry,values=civil_5th_subjects_list)
                civil_5th_subjects_entry.grid(row=0,column=1)

                civil_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                civil_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.civil_5th_faculyt_entry,values=civil_5th_faculty_list)
                civil_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                civil_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_civil_5th_watch_video,width=44)
                civil_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_civil_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_civil_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_civil_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_civil_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_civil_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_civil_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_civil_5th_treeview.xview)
                scrolly.configure(command=tree_civil_5th_treeview.yview)

               
                tree_civil_5th_treeview.heading('subject_name',text="Subject Name")
                tree_civil_5th_treeview.heading('faculty',text="Faculty")
                tree_civil_5th_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_civil_5th_treeview.column('subject_name',width=200)
                tree_civil_5th_treeview.column('faculty',width=100)
                tree_civil_5th_treeview.column('you_tube_link',width=250)

                tree_civil_5th_treeview['show']='headings'
                
                tree_civil_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_civil_5th_watch_video()
                tree_civil_5th_treeview.bind('<ButtonRelease-1>',get_civil_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                civil_6th_faculty_list=[]
                def civil_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                civil_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_civil_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from civil_6th_watch_video where faculty=%s",(self.civil_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_civil_6th_treeview.delete(*tree_civil_6th_treeview.get_children())
                            for row in rows:
                                tree_civil_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_civil_6th_watch_video():
                    fetch_civil_6th_watch_video()
                    self.civil_6th_subjects_entry.set("")
                    self.civil_6th_faculyt_entry.set('')
                    self.var_civil_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_civil_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from civil_6th_watch_video where faculty=%s',(self.civil_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from civil_6th_watch_video where faculty=%s ',(self.civil_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_civil_6th_watch_video()
                                fetch_civil_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_civil_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update civil_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.civil_6th_subjects_entry.get(),
                               
                                self.var_civil_6th_watch_video.get(),
                                self.civil_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_civil_6th_watch_video()
                            fetch_civil_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_civil_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.civil_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.civil_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_civil_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'civil_6th_subjects','civil_6th_date','civil_6th_time','civil_6th_code','semisters','branch'
                                cur.execute('insert into civil_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.civil_6th_subjects_entry.get(),
                                self.civil_6th_faculyt_entry.get(),
                                self.var_civil_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_civil_6th_watch_video()
                                con.close()
                def fetch_civil_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from civil_6th_watch_video')
                        rows=cur.fetchall()
                        tree_civil_6th_treeview.delete(*tree_civil_6th_treeview.get_children())
                        for row in rows:
                            tree_civil_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_civil_6th_watch_video(ev):
                    read=tree_civil_6th_treeview.focus()
                    content=tree_civil_6th_treeview.item(read)
                    row=content['values']
                    self.civil_6th_subjects_entry.set(row[0])
                    self.civil_6th_faculyt_entry.set(row[1])
                    self.var_civil_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_civil_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                civil_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.civil_6th_subjects_entry,values=civil_6th_subjects_list)
                civil_6th_subjects_entry.grid(row=0,column=1)

                civil_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                civil_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.civil_6th_faculyt_entry,values=civil_6th_faculty_list)
                civil_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                civil_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_civil_6th_watch_video,width=44)
                civil_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_civil_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_civil_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_civil_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_civil_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_civil_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_civil_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_civil_6th_treeview.xview)
                scrolly.configure(command=tree_civil_6th_treeview.yview)

                
                tree_civil_6th_treeview.heading('subject_name',text="Subject Name")
                tree_civil_6th_treeview.heading('faculty',text="Faculty")
                tree_civil_6th_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_civil_6th_treeview.column('subject_name',width=200)
                tree_civil_6th_treeview.column('faculty',width=100)
                tree_civil_6th_treeview.column('you_tube_link',width=250)

                tree_civil_6th_treeview['show']='headings'
                
                tree_civil_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_civil_6th_watch_video()
                tree_civil_6th_treeview.bind('<ButtonRelease-1>',get_civil_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                civil_7th_faculty_list=[]
                def civil_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                civil_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_civil_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from civil_7th_watch_video where faculty=%s",(self.civil_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_civil_7th_treeview.delete(*tree_civil_7th_treeview.get_children())
                            for row in rows:
                                tree_civil_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_civil_7th_watch_video():
                    fetch_civil_7th_watch_video()
                    self.civil_7th_subjects_entry.set("")
                    self.civil_7th_faculyt_entry.set('')
                    self.var_civil_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_civil_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from civil_7th_watch_video where faculty=%s',(self.civil_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from civil_7th_watch_video where faculty=%s ',(self.civil_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_civil_7th_watch_video()
                                fetch_civil_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_civil_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update civil_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.civil_7th_subjects_entry.get(),
                               
                                self.var_civil_7th_watch_video.get(),
                                self.civil_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_civil_7th_watch_video()
                            fetch_civil_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_civil_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.civil_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.civil_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_civil_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'civil_7th_subjects','civil_7th_date','civil_7th_time','civil_7th_code','semisters','branch'
                                cur.execute('insert into civil_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.civil_7th_subjects_entry.get(),
                                self.civil_7th_faculyt_entry.get(),
                                self.var_civil_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_civil_7th_watch_video()
                                con.close()
                def fetch_civil_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from civil_7th_watch_video')
                        rows=cur.fetchall()
                        tree_civil_7th_treeview.delete(*tree_civil_7th_treeview.get_children())
                        for row in rows:
                            tree_civil_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_civil_7th_watch_video(ev):
                    read=tree_civil_7th_treeview.focus()
                    content=tree_civil_7th_treeview.item(read)
                    row=content['values']
                    self.civil_7th_subjects_entry.set(row[0])
                    self.civil_7th_faculyt_entry.set(row[1])
                    self.var_civil_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_civil_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                civil_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.civil_7th_subjects_entry,values=civil_7th_subjects_list)
                civil_7th_subjects_entry.grid(row=0,column=1)

                civil_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                civil_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.civil_7th_faculyt_entry,values=civil_7th_faculty_list)
                civil_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                civil_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_civil_7th_watch_video,width=44)
                civil_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_civil_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_civil_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_civil_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_civil_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_civil_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_civil_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_civil_7th_treeview.xview)
                scrolly.configure(command=tree_civil_7th_treeview.yview)

                
                tree_civil_7th_treeview.heading('subject_name',text="Subject Name")
                tree_civil_7th_treeview.heading('faculty',text="Faculty")
                tree_civil_7th_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_civil_7th_treeview.column('subject_name',width=200)
                tree_civil_7th_treeview.column('faculty',width=100)
                tree_civil_7th_treeview.column('you_tube_link',width=250)

                tree_civil_7th_treeview['show']='headings'
                
                tree_civil_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_civil_7th_watch_video()
                tree_civil_7th_treeview.bind('<ButtonRelease-1>',get_civil_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                civil_8th_faculty_list=[]
                def civil_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                civil_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_civil_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from civil_8th_watch_video where faculty=%s",(self.civil_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_civil_8th_treeview.delete(*tree_civil_8th_treeview.get_children())
                            for row in rows:
                                tree_civil_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_civil_8th_watch_video():
                    fetch_civil_8th_watch_video()
                    self.civil_8th_subjects_entry.set("")
                    self.civil_8th_faculyt_entry.set('')
                    self.var_civil_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_civil_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from civil_8th_watch_video where faculty=%s',(self.civil_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from civil_8th_watch_video where faculty=%s ',(self.civil_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_civil_8th_watch_video()
                                fetch_civil_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_civil_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.civil_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update civil_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.civil_8th_subjects_entry.get(),
                               
                                self.var_civil_8th_watch_video.get(),
                                self.civil_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_civil_8th_watch_video()
                            fetch_civil_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_civil_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.civil_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.civil_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_civil_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'civil_8th_subjects','civil_8th_date','civil_8th_time','civil_8th_code','semisters','branch'
                                cur.execute('insert into civil_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.civil_8th_subjects_entry.get(),
                                self.civil_8th_faculyt_entry.get(),
                                self.var_civil_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_civil_8th_watch_video()
                                con.close()
                def fetch_civil_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from civil_8th_watch_video')
                        rows=cur.fetchall()
                        tree_civil_8th_treeview.delete(*tree_civil_8th_treeview.get_children())
                        for row in rows:
                            tree_civil_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_civil_8th_watch_video(ev):
                    read=tree_civil_8th_treeview.focus()
                    content=tree_civil_8th_treeview.item(read)
                    row=content['values']
                    self.civil_8th_subjects_entry.set(row[0])
                    self.civil_8th_faculyt_entry.set(row[1])
                    self.var_civil_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_civil_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                civil_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.civil_8th_subjects_entry,values=civil_8th_subjects_list)
                civil_8th_subjects_entry.grid(row=0,column=1)

                civil_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                civil_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.civil_8th_faculyt_entry,values=civil_8th_faculty_list)
                civil_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                civil_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_civil_8th_watch_video,width=44)
                civil_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_civil_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_civil_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_civil_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_civil_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_civil_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_civil_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_civil_8th_treeview.xview)
                scrolly.configure(command=tree_civil_8th_treeview.yview)

              
                tree_civil_8th_treeview.heading('subject_name',text="Subject Name")
                tree_civil_8th_treeview.heading('faculty',text="Faculty")
                tree_civil_8th_treeview.heading('you_tube_link',text="Watch")
                

          
                tree_civil_8th_treeview.column('subject_name',width=200)
                tree_civil_8th_treeview.column('faculty',width=100)
                tree_civil_8th_treeview.column('you_tube_link',width=250)

                tree_civil_8th_treeview['show']='headings'
                
                tree_civil_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_civil_8th_watch_video()
                tree_civil_8th_treeview.bind('<ButtonRelease-1>',get_civil_8th_watch_video)
        ################################################################################################################
        ######################################################################################################################3
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                mech_3rd_faculty_list=[]
                def mech_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                mech_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_mech_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from mech_3rd_watch_video where faculty=%s",(self.mech_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_mech_3rd_treeview.delete(*tree_mech_3rd_treeview.get_children())
                            for row in rows:
                                tree_mech_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_mech_3rd_watch_video():
                    fetch_mech_3rd_watch_video()
                    self.mech_3rd_subjects_entry.set("")
                    self.mech_3rd_faculyt_entry.set('')
                    self.var_mech_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_mech_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from mech_3rd_watch_video where faculty=%s',(self.mech_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from mech_3rd_watch_video where faculty=%s ',(self.mech_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_mech_3rd_watch_video()
                                fetch_mech_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_mech_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update mech_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.mech_3rd_subjects_entry.get(),
                               
                                self.var_mech_3rd_watch_video.get(),
                                self.mech_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_mech_3rd_watch_video()
                            fetch_mech_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_mech_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.mech_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.mech_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_mech_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'mech_3rd_subjects','mech_3rd_date','mech_3rd_time','mech_3rd_code','semisters','branch'
                                cur.execute('insert into mech_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.mech_3rd_subjects_entry.get(),
                                self.mech_3rd_faculyt_entry.get(),
                                self.var_mech_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_mech_3rd_watch_video()
                                con.close()
                def fetch_mech_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from mech_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_mech_3rd_treeview.delete(*tree_mech_3rd_treeview.get_children())
                        for row in rows:
                            tree_mech_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_mech_3rd_watch_video(ev):
                    read=tree_mech_3rd_treeview.focus()
                    content=tree_mech_3rd_treeview.item(read)
                    row=content['values']
                    self.mech_3rd_subjects_entry.set(row[0])
                    self.mech_3rd_faculyt_entry.set(row[1])
                    self.var_mech_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_mech_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                mech_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.mech_3rd_subjects_entry,values=mech_3rd_subjects_list)
                mech_3rd_subjects_entry.grid(row=0,column=1)

                mech_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                mech_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.mech_3rd_faculyt_entry,values=mech_3rd_faculty_list)
                mech_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                mech_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_mech_3rd_watch_video,width=44)
                mech_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_mech_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_mech_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_mech_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_mech_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_mech_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_mech_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_mech_3rd_treeview.xview)
                scrolly.configure(command=tree_mech_3rd_treeview.yview)

          
                tree_mech_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_mech_3rd_treeview.heading('faculty',text="Faculty")
                tree_mech_3rd_treeview.heading('you_tube_link',text="Watch")
                

              
                tree_mech_3rd_treeview.column('subject_name',width=200)
                tree_mech_3rd_treeview.column('faculty',width=100)
                tree_mech_3rd_treeview.column('you_tube_link',width=250)

                tree_mech_3rd_treeview['show']='headings'
                
                tree_mech_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_mech_3rd_watch_video()
                tree_mech_3rd_treeview.bind('<ButtonRelease-1>',get_mech_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                mech_4th_faculty_list=[]
                def mech_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                mech_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_mech_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from mech_4th_watch_video where faculty=%s",(self.mech_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_mech_4th_treeview.delete(*tree_mech_4th_treeview.get_children())
                            for row in rows:
                                tree_mech_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_mech_4th_watch_video():
                    fetch_mech_4th_watch_video()
                    self.mech_4th_subjects_entry.set("")
                    self.mech_4th_faculyt_entry.set('')
                    self.var_mech_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_mech_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from mech_4th_watch_video where faculty=%s',(self.mech_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from mech_4th_watch_video where faculty=%s ',(self.mech_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_mech_4th_watch_video()
                                fetch_mech_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_mech_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update mech_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.mech_4th_subjects_entry.get(),
                               
                                self.var_mech_4th_watch_video.get(),
                                self.mech_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_mech_4th_watch_video()
                            fetch_mech_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_mech_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.mech_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.mech_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_mech_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'mech_4th_subjects','mech_4th_date','mech_4th_time','mech_4th_code','semisters','branch'
                                cur.execute('insert into mech_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.mech_4th_subjects_entry.get(),
                                self.mech_4th_faculyt_entry.get(),
                                self.var_mech_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_mech_4th_watch_video()
                                con.close()
                def fetch_mech_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from mech_4th_watch_video')
                        rows=cur.fetchall()
                        tree_mech_4th_treeview.delete(*tree_mech_4th_treeview.get_children())
                        for row in rows:
                            tree_mech_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_mech_4th_watch_video(ev):
                    read=tree_mech_4th_treeview.focus()
                    content=tree_mech_4th_treeview.item(read)
                    row=content['values']
                    self.mech_4th_subjects_entry.set(row[0])
                    self.mech_4th_faculyt_entry.set(row[1])
                    self.var_mech_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_mech_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                mech_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.mech_4th_subjects_entry,values=mech_4th_subjects_list)
                mech_4th_subjects_entry.grid(row=0,column=1)

                mech_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                mech_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.mech_4th_faculyt_entry,values=mech_4th_faculty_list)
                mech_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                mech_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_mech_4th_watch_video,width=44)
                mech_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_mech_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_mech_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_mech_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_mech_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_mech_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_mech_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_mech_4th_treeview.xview)
                scrolly.configure(command=tree_mech_4th_treeview.yview)

             
                tree_mech_4th_treeview.heading('subject_name',text="Subject Name")
                tree_mech_4th_treeview.heading('faculty',text="Faculty")
                tree_mech_4th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_mech_4th_treeview.column('subject_name',width=200)
                tree_mech_4th_treeview.column('faculty',width=100)
                tree_mech_4th_treeview.column('you_tube_link',width=250)

                tree_mech_4th_treeview['show']='headings'
                
                tree_mech_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_mech_4th_watch_video()
                tree_mech_4th_treeview.bind('<ButtonRelease-1>',get_mech_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                mech_5th_faculty_list=[]
                def mech_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                mech_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_mech_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from mech_5th_watch_video where faculty=%s",(self.mech_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_mech_5th_treeview.delete(*tree_mech_5th_treeview.get_children())
                            for row in rows:
                                tree_mech_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_mech_5th_watch_video():
                    fetch_mech_5th_watch_video()
                    self.mech_5th_subjects_entry.set("")
                    self.mech_5th_faculyt_entry.set('')
                    self.var_mech_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_mech_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from mech_5th_watch_video where faculty=%s',(self.mech_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from mech_5th_watch_video where faculty=%s ',(self.mech_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_mech_5th_watch_video()
                                fetch_mech_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_mech_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update mech_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.mech_5th_subjects_entry.get(),
                               
                                self.var_mech_5th_watch_video.get(),
                                self.mech_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_mech_5th_watch_video()
                            fetch_mech_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_mech_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.mech_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.mech_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_mech_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'mech_5th_subjects','mech_5th_date','mech_5th_time','mech_5th_code','semisters','branch'
                                cur.execute('insert into mech_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.mech_5th_subjects_entry.get(),
                                self.mech_5th_faculyt_entry.get(),
                                self.var_mech_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_mech_5th_watch_video()
                                con.close()
                def fetch_mech_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from mech_5th_watch_video')
                        rows=cur.fetchall()
                        tree_mech_5th_treeview.delete(*tree_mech_5th_treeview.get_children())
                        for row in rows:
                            tree_mech_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_mech_5th_watch_video(ev):
                    read=tree_mech_5th_treeview.focus()
                    content=tree_mech_5th_treeview.item(read)
                    row=content['values']
                    self.mech_5th_subjects_entry.set(row[0])
                    self.mech_5th_faculyt_entry.set(row[1])
                    self.var_mech_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_mech_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                mech_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.mech_5th_subjects_entry,values=mech_5th_subjects_list)
                mech_5th_subjects_entry.grid(row=0,column=1)

                mech_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                mech_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.mech_5th_faculyt_entry,values=mech_5th_faculty_list)
                mech_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                mech_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_mech_5th_watch_video,width=44)
                mech_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_mech_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_mech_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_mech_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_mech_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_mech_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_mech_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_mech_5th_treeview.xview)
                scrolly.configure(command=tree_mech_5th_treeview.yview)

               
                tree_mech_5th_treeview.heading('subject_name',text="Subject Name")
                tree_mech_5th_treeview.heading('faculty',text="Faculty")
                tree_mech_5th_treeview.heading('you_tube_link',text="Watch")
 
                tree_mech_5th_treeview.column('subject_name',width=200)
                tree_mech_5th_treeview.column('faculty',width=100)
                tree_mech_5th_treeview.column('you_tube_link',width=250)

                tree_mech_5th_treeview['show']='headings'
                
                tree_mech_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_mech_5th_watch_video()
                tree_mech_5th_treeview.bind('<ButtonRelease-1>',get_mech_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                mech_6th_faculty_list=[]
                def mech_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                mech_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_mech_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from mech_6th_watch_video where faculty=%s",(self.mech_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_mech_6th_treeview.delete(*tree_mech_6th_treeview.get_children())
                            for row in rows:
                                tree_mech_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_mech_6th_watch_video():
                    fetch_mech_6th_watch_video()
                    self.mech_6th_subjects_entry.set("")
                    self.mech_6th_faculyt_entry.set('')
                    self.var_mech_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_mech_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from mech_6th_watch_video where faculty=%s',(self.mech_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from mech_6th_watch_video where faculty=%s ',(self.mech_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_mech_6th_watch_video()
                                fetch_mech_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_mech_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update mech_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.mech_6th_subjects_entry.get(),
                               
                                self.var_mech_6th_watch_video.get(),
                                self.mech_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_mech_6th_watch_video()
                            fetch_mech_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_mech_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.mech_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.mech_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_mech_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'mech_6th_subjects','mech_6th_date','mech_6th_time','mech_6th_code','semisters','branch'
                                cur.execute('insert into mech_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.mech_6th_subjects_entry.get(),
                                self.mech_6th_faculyt_entry.get(),
                                self.var_mech_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_mech_6th_watch_video()
                                con.close()
                def fetch_mech_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from mech_6th_watch_video')
                        rows=cur.fetchall()
                        tree_mech_6th_treeview.delete(*tree_mech_6th_treeview.get_children())
                        for row in rows:
                            tree_mech_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_mech_6th_watch_video(ev):
                    read=tree_mech_6th_treeview.focus()
                    content=tree_mech_6th_treeview.item(read)
                    row=content['values']
                    self.mech_6th_subjects_entry.set(row[0])
                    self.mech_6th_faculyt_entry.set(row[1])
                    self.var_mech_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_mech_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                mech_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.mech_6th_subjects_entry,values=mech_6th_subjects_list)
                mech_6th_subjects_entry.grid(row=0,column=1)

                mech_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                mech_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.mech_6th_faculyt_entry,values=mech_6th_faculty_list)
                mech_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                mech_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_mech_6th_watch_video,width=44)
                mech_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_mech_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_mech_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_mech_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_mech_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_mech_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_mech_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_mech_6th_treeview.xview)
                scrolly.configure(command=tree_mech_6th_treeview.yview)

                tree_mech_6th_treeview.heading('subject_name',text="Subject Name")
                tree_mech_6th_treeview.heading('faculty',text="Faculty")
                tree_mech_6th_treeview.heading('you_tube_link',text="Watch")
                

                tree_mech_6th_treeview.column('subject_name',width=200)
                tree_mech_6th_treeview.column('faculty',width=100)
                tree_mech_6th_treeview.column('you_tube_link',width=250)

                tree_mech_6th_treeview['show']='headings'
                
                tree_mech_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_mech_6th_watch_video()
                tree_mech_6th_treeview.bind('<ButtonRelease-1>',get_mech_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                mech_7th_faculty_list=[]
                def mech_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                mech_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_mech_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from mech_7th_watch_video where faculty=%s",(self.mech_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_mech_7th_treeview.delete(*tree_mech_7th_treeview.get_children())
                            for row in rows:
                                tree_mech_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_mech_7th_watch_video():
                    fetch_mech_7th_watch_video()
                    self.mech_7th_subjects_entry.set("")
                    self.mech_7th_faculyt_entry.set('')
                    self.var_mech_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_mech_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from mech_7th_watch_video where faculty=%s',(self.mech_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from mech_7th_watch_video where faculty=%s ',(self.mech_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_mech_7th_watch_video()
                                fetch_mech_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_mech_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update mech_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.mech_7th_subjects_entry.get(),
                               
                                self.var_mech_7th_watch_video.get(),
                                self.mech_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_mech_7th_watch_video()
                            fetch_mech_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_mech_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.mech_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.mech_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_mech_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'mech_7th_subjects','mech_7th_date','mech_7th_time','mech_7th_code','semisters','branch'
                                cur.execute('insert into mech_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.mech_7th_subjects_entry.get(),
                                self.mech_7th_faculyt_entry.get(),
                                self.var_mech_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_mech_7th_watch_video()
                                con.close()
                def fetch_mech_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from mech_7th_watch_video')
                        rows=cur.fetchall()
                        tree_mech_7th_treeview.delete(*tree_mech_7th_treeview.get_children())
                        for row in rows:
                            tree_mech_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_mech_7th_watch_video(ev):
                    read=tree_mech_7th_treeview.focus()
                    content=tree_mech_7th_treeview.item(read)
                    row=content['values']
                    self.mech_7th_subjects_entry.set(row[0])
                    self.mech_7th_faculyt_entry.set(row[1])
                    self.var_mech_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_mech_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                mech_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.mech_7th_subjects_entry,values=mech_7th_subjects_list)
                mech_7th_subjects_entry.grid(row=0,column=1)

                mech_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                mech_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.mech_7th_faculyt_entry,values=mech_7th_faculty_list)
                mech_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                mech_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_mech_7th_watch_video,width=44)
                mech_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_mech_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_mech_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_mech_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_mech_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_mech_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_mech_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_mech_7th_treeview.xview)
                scrolly.configure(command=tree_mech_7th_treeview.yview)

                tree_mech_7th_treeview.heading('subject_name',text="Subject Name")
                tree_mech_7th_treeview.heading('faculty',text="Faculty")
                tree_mech_7th_treeview.heading('you_tube_link',text="Watch")
                

                tree_mech_7th_treeview.column('subject_name',width=200)
                tree_mech_7th_treeview.column('faculty',width=100)
                tree_mech_7th_treeview.column('you_tube_link',width=250)

                tree_mech_7th_treeview['show']='headings'
                
                tree_mech_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_mech_7th_watch_video()
                tree_mech_7th_treeview.bind('<ButtonRelease-1>',get_mech_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                mech_8th_faculty_list=[]
                def mech_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                mech_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_mech_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from mech_8th_watch_video where faculty=%s",(self.mech_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_mech_8th_treeview.delete(*tree_mech_8th_treeview.get_children())
                            for row in rows:
                                tree_mech_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_mech_8th_watch_video():
                    fetch_mech_8th_watch_video()
                    self.mech_8th_subjects_entry.set("")
                    self.mech_8th_faculyt_entry.set('')
                    self.var_mech_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_mech_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from mech_8th_watch_video where faculty=%s',(self.mech_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from mech_8th_watch_video where faculty=%s ',(self.mech_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_mech_8th_watch_video()
                                fetch_mech_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_mech_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.mech_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update mech_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.mech_8th_subjects_entry.get(),
                               
                                self.var_mech_8th_watch_video.get(),
                                self.mech_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_mech_8th_watch_video()
                            fetch_mech_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_mech_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.mech_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.mech_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_mech_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'mech_8th_subjects','mech_8th_date','mech_8th_time','mech_8th_code','semisters','branch'
                                cur.execute('insert into mech_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.mech_8th_subjects_entry.get(),
                                self.mech_8th_faculyt_entry.get(),
                                self.var_mech_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_mech_8th_watch_video()
                                con.close()
                def fetch_mech_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from mech_8th_watch_video')
                        rows=cur.fetchall()
                        tree_mech_8th_treeview.delete(*tree_mech_8th_treeview.get_children())
                        for row in rows:
                            tree_mech_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_mech_8th_watch_video(ev):
                    read=tree_mech_8th_treeview.focus()
                    content=tree_mech_8th_treeview.item(read)
                    row=content['values']
                    self.mech_8th_subjects_entry.set(row[0])
                    self.mech_8th_faculyt_entry.set(row[1])
                    self.var_mech_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_mech_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                mech_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.mech_8th_subjects_entry,values=mech_8th_subjects_list)
                mech_8th_subjects_entry.grid(row=0,column=1)

                mech_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                mech_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.mech_8th_faculyt_entry,values=mech_8th_faculty_list)
                mech_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                mech_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_mech_8th_watch_video,width=44)
                mech_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_mech_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_mech_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_mech_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_mech_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_mech_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_mech_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_mech_8th_treeview.xview)
                scrolly.configure(command=tree_mech_8th_treeview.yview)

                tree_mech_8th_treeview.heading('subject_name',text="Subject Name")
                tree_mech_8th_treeview.heading('faculty',text="Faculty")
                tree_mech_8th_treeview.heading('you_tube_link',text="Watch")
                

                tree_mech_8th_treeview.column('subject_name',width=200)
                tree_mech_8th_treeview.column('faculty',width=100)
                tree_mech_8th_treeview.column('you_tube_link',width=250)

                tree_mech_8th_treeview['show']='headings'
                
                tree_mech_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_mech_8th_watch_video()
                tree_mech_8th_treeview.bind('<ButtonRelease-1>',get_mech_8th_watch_video)
        ####################################################################################################################################
        ########################################################################################################################################
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                eee_3rd_faculty_list=[]
                def eee_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                eee_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_eee_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from eee_3rd_watch_video where faculty=%s",(self.eee_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_eee_3rd_treeview.delete(*tree_eee_3rd_treeview.get_children())
                            for row in rows:
                                tree_eee_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_eee_3rd_watch_video():
                    fetch_eee_3rd_watch_video()
                    self.eee_3rd_subjects_entry.set("")
                    self.eee_3rd_faculyt_entry.set('')
                    self.var_eee_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_eee_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from eee_3rd_watch_video where faculty=%s',(self.eee_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from eee_3rd_watch_video where faculty=%s ',(self.eee_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_eee_3rd_watch_video()
                                fetch_eee_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_eee_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update eee_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.eee_3rd_subjects_entry.get(),
                               
                                self.var_eee_3rd_watch_video.get(),
                                self.eee_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_eee_3rd_watch_video()
                            fetch_eee_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_eee_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.eee_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.eee_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_eee_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'eee_3rd_subjects','eee_3rd_date','eee_3rd_time','eee_3rd_code','semisters','branch'
                                cur.execute('insert into eee_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.eee_3rd_subjects_entry.get(),
                                self.eee_3rd_faculyt_entry.get(),
                                self.var_eee_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_eee_3rd_watch_video()
                                con.close()
                def fetch_eee_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from eee_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_eee_3rd_treeview.delete(*tree_eee_3rd_treeview.get_children())
                        for row in rows:
                            tree_eee_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_eee_3rd_watch_video(ev):
                    read=tree_eee_3rd_treeview.focus()
                    content=tree_eee_3rd_treeview.item(read)
                    row=content['values']
                    self.eee_3rd_subjects_entry.set(row[0])
                    self.eee_3rd_faculyt_entry.set(row[1])
                    self.var_eee_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_eee_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                eee_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.eee_3rd_subjects_entry,values=eee_3rd_subjects_list)
                eee_3rd_subjects_entry.grid(row=0,column=1)

                eee_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                eee_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.eee_3rd_faculyt_entry,values=eee_3rd_faculty_list)
                eee_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                eee_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_eee_3rd_watch_video,width=44)
                eee_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_eee_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_eee_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_eee_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_eee_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_eee_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_eee_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_eee_3rd_treeview.xview)
                scrolly.configure(command=tree_eee_3rd_treeview.yview)

                
                tree_eee_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_eee_3rd_treeview.heading('faculty',text="Faculty")
                tree_eee_3rd_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_eee_3rd_treeview.column('subject_name',width=200)
                tree_eee_3rd_treeview.column('faculty',width=100)
                tree_eee_3rd_treeview.column('you_tube_link',width=250)

                tree_eee_3rd_treeview['show']='headings'
                
                tree_eee_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_eee_3rd_watch_video()
                tree_eee_3rd_treeview.bind('<ButtonRelease-1>',get_eee_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                eee_4th_faculty_list=[]
                def eee_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                eee_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_eee_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from eee_4th_watch_video where faculty=%s",(self.eee_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_eee_4th_treeview.delete(*tree_eee_4th_treeview.get_children())
                            for row in rows:
                                tree_eee_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_eee_4th_watch_video():
                    fetch_eee_4th_watch_video()
                    self.eee_4th_subjects_entry.set("")
                    self.eee_4th_faculyt_entry.set('')
                    self.var_eee_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_eee_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from eee_4th_watch_video where faculty=%s',(self.eee_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from eee_4th_watch_video where faculty=%s ',(self.eee_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_eee_4th_watch_video()
                                fetch_eee_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_eee_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update eee_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.eee_4th_subjects_entry.get(),
                               
                                self.var_eee_4th_watch_video.get(),
                                self.eee_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_eee_4th_watch_video()
                            fetch_eee_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_eee_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.eee_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.eee_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_eee_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'eee_4th_subjects','eee_4th_date','eee_4th_time','eee_4th_code','semisters','branch'
                                cur.execute('insert into eee_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.eee_4th_subjects_entry.get(),
                                self.eee_4th_faculyt_entry.get(),
                                self.var_eee_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_eee_4th_watch_video()
                                con.close()
                def fetch_eee_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from eee_4th_watch_video')
                        rows=cur.fetchall()
                        tree_eee_4th_treeview.delete(*tree_eee_4th_treeview.get_children())
                        for row in rows:
                            tree_eee_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_eee_4th_watch_video(ev):
                    read=tree_eee_4th_treeview.focus()
                    content=tree_eee_4th_treeview.item(read)
                    row=content['values']
                    self.eee_4th_subjects_entry.set(row[0])
                    self.eee_4th_faculyt_entry.set(row[1])
                    self.var_eee_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_eee_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                eee_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.eee_4th_subjects_entry,values=eee_4th_subjects_list)
                eee_4th_subjects_entry.grid(row=0,column=1)

                eee_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                eee_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.eee_4th_faculyt_entry,values=eee_4th_faculty_list)
                eee_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                eee_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_eee_4th_watch_video,width=44)
                eee_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_eee_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_eee_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_eee_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_eee_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_eee_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_eee_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_eee_4th_treeview.xview)
                scrolly.configure(command=tree_eee_4th_treeview.yview)

                
                tree_eee_4th_treeview.heading('subject_name',text="Subject Name")
                tree_eee_4th_treeview.heading('faculty',text="Faculty")
                tree_eee_4th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_eee_4th_treeview.column('subject_name',width=200)
                tree_eee_4th_treeview.column('faculty',width=100)
                tree_eee_4th_treeview.column('you_tube_link',width=250)

                tree_eee_4th_treeview['show']='headings'
                
                tree_eee_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_eee_4th_watch_video()
                tree_eee_4th_treeview.bind('<ButtonRelease-1>',get_eee_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                eee_5th_faculty_list=[]
                def eee_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                eee_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_eee_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from eee_5th_watch_video where faculty=%s",(self.eee_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_eee_5th_treeview.delete(*tree_eee_5th_treeview.get_children())
                            for row in rows:
                                tree_eee_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_eee_5th_watch_video():
                    fetch_eee_5th_watch_video()
                    self.eee_5th_subjects_entry.set("")
                    self.eee_5th_faculyt_entry.set('')
                    self.var_eee_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_eee_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from eee_5th_watch_video where faculty=%s',(self.eee_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from eee_5th_watch_video where faculty=%s ',(self.eee_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_eee_5th_watch_video()
                                fetch_eee_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_eee_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update eee_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.eee_5th_subjects_entry.get(),
                               
                                self.var_eee_5th_watch_video.get(),
                                self.eee_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_eee_5th_watch_video()
                            fetch_eee_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_eee_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.eee_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.eee_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_eee_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'eee_5th_subjects','eee_5th_date','eee_5th_time','eee_5th_code','semisters','branch'
                                cur.execute('insert into eee_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.eee_5th_subjects_entry.get(),
                                self.eee_5th_faculyt_entry.get(),
                                self.var_eee_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_eee_5th_watch_video()
                                con.close()
                def fetch_eee_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from eee_5th_watch_video')
                        rows=cur.fetchall()
                        tree_eee_5th_treeview.delete(*tree_eee_5th_treeview.get_children())
                        for row in rows:
                            tree_eee_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_eee_5th_watch_video(ev):
                    read=tree_eee_5th_treeview.focus()
                    content=tree_eee_5th_treeview.item(read)
                    row=content['values']
                    self.eee_5th_subjects_entry.set(row[0])
                    self.eee_5th_faculyt_entry.set(row[1])
                    self.var_eee_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_eee_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                eee_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.eee_5th_subjects_entry,values=eee_5th_subjects_list)
                eee_5th_subjects_entry.grid(row=0,column=1)

                eee_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                eee_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.eee_5th_faculyt_entry,values=eee_5th_faculty_list)
                eee_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                eee_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_eee_5th_watch_video,width=44)
                eee_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_eee_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_eee_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_eee_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_eee_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_eee_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_eee_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_eee_5th_treeview.xview)
                scrolly.configure(command=tree_eee_5th_treeview.yview)

              
                tree_eee_5th_treeview.heading('subject_name',text="Subject Name")
                tree_eee_5th_treeview.heading('faculty',text="Faculty")
                tree_eee_5th_treeview.heading('you_tube_link',text="Watch")
                

                tree_eee_5th_treeview.column('subject_name',width=200)
                tree_eee_5th_treeview.column('faculty',width=100)
                tree_eee_5th_treeview.column('you_tube_link',width=250)

                tree_eee_5th_treeview['show']='headings'
                
                tree_eee_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_eee_5th_watch_video()
                tree_eee_5th_treeview.bind('<ButtonRelease-1>',get_eee_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                eee_6th_faculty_list=[]
                def eee_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                eee_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_eee_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from eee_6th_watch_video where faculty=%s",(self.eee_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_eee_6th_treeview.delete(*tree_eee_6th_treeview.get_children())
                            for row in rows:
                                tree_eee_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_eee_6th_watch_video():
                    fetch_eee_6th_watch_video()
                    self.eee_6th_subjects_entry.set("")
                    self.eee_6th_faculyt_entry.set('')
                    self.var_eee_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_eee_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from eee_6th_watch_video where faculty=%s',(self.eee_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from eee_6th_watch_video where faculty=%s ',(self.eee_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_eee_6th_watch_video()
                                fetch_eee_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_eee_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update eee_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.eee_6th_subjects_entry.get(),
                               
                                self.var_eee_6th_watch_video.get(),
                                self.eee_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_eee_6th_watch_video()
                            fetch_eee_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_eee_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.eee_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.eee_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_eee_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'eee_6th_subjects','eee_6th_date','eee_6th_time','eee_6th_code','semisters','branch'
                                cur.execute('insert into eee_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.eee_6th_subjects_entry.get(),
                                self.eee_6th_faculyt_entry.get(),
                                self.var_eee_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_eee_6th_watch_video()
                                con.close()
                def fetch_eee_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from eee_6th_watch_video')
                        rows=cur.fetchall()
                        tree_eee_6th_treeview.delete(*tree_eee_6th_treeview.get_children())
                        for row in rows:
                            tree_eee_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_eee_6th_watch_video(ev):
                    read=tree_eee_6th_treeview.focus()
                    content=tree_eee_6th_treeview.item(read)
                    row=content['values']
                    self.eee_6th_subjects_entry.set(row[0])
                    self.eee_6th_faculyt_entry.set(row[1])
                    self.var_eee_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_eee_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                eee_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.eee_6th_subjects_entry,values=eee_6th_subjects_list)
                eee_6th_subjects_entry.grid(row=0,column=1)

                eee_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                eee_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.eee_6th_faculyt_entry,values=eee_6th_faculty_list)
                eee_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                eee_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_eee_6th_watch_video,width=44)
                eee_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_eee_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_eee_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_eee_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_eee_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_eee_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_eee_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_eee_6th_treeview.xview)
                scrolly.configure(command=tree_eee_6th_treeview.yview)

                
                tree_eee_6th_treeview.heading('subject_name',text="Subject Name")
                tree_eee_6th_treeview.heading('faculty',text="Faculty")
                tree_eee_6th_treeview.heading('you_tube_link',text="Watch")
                

                tree_eee_6th_treeview.column('subject_name',width=200)
                tree_eee_6th_treeview.column('faculty',width=100)
                tree_eee_6th_treeview.column('you_tube_link',width=250)

                tree_eee_6th_treeview['show']='headings'
                
                tree_eee_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_eee_6th_watch_video()
                tree_eee_6th_treeview.bind('<ButtonRelease-1>',get_eee_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                eee_7th_faculty_list=[]
                def eee_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                eee_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_eee_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from eee_7th_watch_video where faculty=%s",(self.eee_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_eee_7th_treeview.delete(*tree_eee_7th_treeview.get_children())
                            for row in rows:
                                tree_eee_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_eee_7th_watch_video():
                    fetch_eee_7th_watch_video()
                    self.eee_7th_subjects_entry.set("")
                    self.eee_7th_faculyt_entry.set('')
                    self.var_eee_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_eee_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from eee_7th_watch_video where faculty=%s',(self.eee_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from eee_7th_watch_video where faculty=%s ',(self.eee_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_eee_7th_watch_video()
                                fetch_eee_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_eee_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update eee_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.eee_7th_subjects_entry.get(),
                               
                                self.var_eee_7th_watch_video.get(),
                                self.eee_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_eee_7th_watch_video()
                            fetch_eee_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_eee_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.eee_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.eee_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_eee_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'eee_7th_subjects','eee_7th_date','eee_7th_time','eee_7th_code','semisters','branch'
                                cur.execute('insert into eee_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.eee_7th_subjects_entry.get(),
                                self.eee_7th_faculyt_entry.get(),
                                self.var_eee_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_eee_7th_watch_video()
                                con.close()
                def fetch_eee_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from eee_7th_watch_video')
                        rows=cur.fetchall()
                        tree_eee_7th_treeview.delete(*tree_eee_7th_treeview.get_children())
                        for row in rows:
                            tree_eee_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_eee_7th_watch_video(ev):
                    read=tree_eee_7th_treeview.focus()
                    content=tree_eee_7th_treeview.item(read)
                    row=content['values']
                    self.eee_7th_subjects_entry.set(row[0])
                    self.eee_7th_faculyt_entry.set(row[1])
                    self.var_eee_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_eee_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                eee_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.eee_7th_subjects_entry,values=eee_7th_subjects_list)
                eee_7th_subjects_entry.grid(row=0,column=1)

                eee_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                eee_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.eee_7th_faculyt_entry,values=eee_7th_faculty_list)
                eee_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                eee_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_eee_7th_watch_video,width=44)
                eee_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_eee_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_eee_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_eee_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_eee_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_eee_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_eee_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_eee_7th_treeview.xview)
                scrolly.configure(command=tree_eee_7th_treeview.yview)

              
                tree_eee_7th_treeview.heading('subject_name',text="Subject Name")
                tree_eee_7th_treeview.heading('faculty',text="Faculty")
                tree_eee_7th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_eee_7th_treeview.column('subject_name',width=200)
                tree_eee_7th_treeview.column('faculty',width=100)
                tree_eee_7th_treeview.column('you_tube_link',width=250)

                tree_eee_7th_treeview['show']='headings'
                
                tree_eee_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_eee_7th_watch_video()
                tree_eee_7th_treeview.bind('<ButtonRelease-1>',get_eee_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                eee_8th_faculty_list=[]
                def eee_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                eee_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_eee_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from eee_8th_watch_video where faculty=%s",(self.eee_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_eee_8th_treeview.delete(*tree_eee_8th_treeview.get_children())
                            for row in rows:
                                tree_eee_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_eee_8th_watch_video():
                    fetch_eee_8th_watch_video()
                    self.eee_8th_subjects_entry.set("")
                    self.eee_8th_faculyt_entry.set('')
                    self.var_eee_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_eee_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from eee_8th_watch_video where faculty=%s',(self.eee_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from eee_8th_watch_video where faculty=%s ',(self.eee_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_eee_8th_watch_video()
                                fetch_eee_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_eee_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.eee_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update eee_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.eee_8th_subjects_entry.get(),
                               
                                self.var_eee_8th_watch_video.get(),
                                self.eee_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_eee_8th_watch_video()
                            fetch_eee_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_eee_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.eee_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.eee_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_eee_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'eee_8th_subjects','eee_8th_date','eee_8th_time','eee_8th_code','semisters','branch'
                                cur.execute('insert into eee_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.eee_8th_subjects_entry.get(),
                                self.eee_8th_faculyt_entry.get(),
                                self.var_eee_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_eee_8th_watch_video()
                                con.close()
                def fetch_eee_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from eee_8th_watch_video')
                        rows=cur.fetchall()
                        tree_eee_8th_treeview.delete(*tree_eee_8th_treeview.get_children())
                        for row in rows:
                            tree_eee_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_eee_8th_watch_video(ev):
                    read=tree_eee_8th_treeview.focus()
                    content=tree_eee_8th_treeview.item(read)
                    row=content['values']
                    self.eee_8th_subjects_entry.set(row[0])
                    self.eee_8th_faculyt_entry.set(row[1])
                    self.var_eee_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_eee_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                eee_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.eee_8th_subjects_entry,values=eee_8th_subjects_list)
                eee_8th_subjects_entry.grid(row=0,column=1)

                eee_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                eee_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.eee_8th_faculyt_entry,values=eee_8th_faculty_list)
                eee_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                eee_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_eee_8th_watch_video,width=44)
                eee_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_eee_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_eee_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_eee_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_eee_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_eee_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_eee_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_eee_8th_treeview.xview)
                scrolly.configure(command=tree_eee_8th_treeview.yview)

               
                tree_eee_8th_treeview.heading('subject_name',text="Subject Name")
                tree_eee_8th_treeview.heading('faculty',text="Faculty")
                tree_eee_8th_treeview.heading('you_tube_link',text="Watch")
                

        
                tree_eee_8th_treeview.column('subject_name',width=200)
                tree_eee_8th_treeview.column('faculty',width=100)
                tree_eee_8th_treeview.column('you_tube_link',width=250)

                tree_eee_8th_treeview['show']='headings'
                
                tree_eee_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_eee_8th_watch_video()
                tree_eee_8th_treeview.bind('<ButtonRelease-1>',get_eee_8th_watch_video)
        ####################################################################################################################################
        #################################################################################################################################
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ece_3rd_faculty_list=[]
                def ece_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ece_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ece_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ece_3rd_watch_video where faculty=%s",(self.ece_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ece_3rd_treeview.delete(*tree_ece_3rd_treeview.get_children())
                            for row in rows:
                                tree_ece_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ece_3rd_watch_video():
                    fetch_ece_3rd_watch_video()
                    self.ece_3rd_subjects_entry.set("")
                    self.ece_3rd_faculyt_entry.set('')
                    self.var_ece_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ece_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ece_3rd_watch_video where faculty=%s',(self.ece_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ece_3rd_watch_video where faculty=%s ',(self.ece_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ece_3rd_watch_video()
                                fetch_ece_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ece_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ece_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ece_3rd_subjects_entry.get(),
                               
                                self.var_ece_3rd_watch_video.get(),
                                self.ece_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ece_3rd_watch_video()
                            fetch_ece_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ece_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ece_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ece_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ece_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ece_3rd_subjects','ece_3rd_date','ece_3rd_time','ece_3rd_code','semisters','branch'
                                cur.execute('insert into ece_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ece_3rd_subjects_entry.get(),
                                self.ece_3rd_faculyt_entry.get(),
                                self.var_ece_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ece_3rd_watch_video()
                                con.close()
                def fetch_ece_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ece_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_ece_3rd_treeview.delete(*tree_ece_3rd_treeview.get_children())
                        for row in rows:
                            tree_ece_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ece_3rd_watch_video(ev):
                    read=tree_ece_3rd_treeview.focus()
                    content=tree_ece_3rd_treeview.item(read)
                    row=content['values']
                    self.ece_3rd_subjects_entry.set(row[0])
                    self.ece_3rd_faculyt_entry.set(row[1])
                    self.var_ece_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ece_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ece_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ece_3rd_subjects_entry,values=ece_3rd_subjects_list)
                ece_3rd_subjects_entry.grid(row=0,column=1)

                ece_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ece_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ece_3rd_faculyt_entry,values=ece_3rd_faculty_list)
                ece_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ece_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ece_3rd_watch_video,width=44)
                ece_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ece_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ece_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ece_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ece_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ece_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ece_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ece_3rd_treeview.xview)
                scrolly.configure(command=tree_ece_3rd_treeview.yview)

                
                tree_ece_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_ece_3rd_treeview.heading('faculty',text="Faculty")
                tree_ece_3rd_treeview.heading('you_tube_link',text="Watch")
                

                tree_ece_3rd_treeview.column('subject_name',width=200)
                tree_ece_3rd_treeview.column('faculty',width=100)
                tree_ece_3rd_treeview.column('you_tube_link',width=250)

                tree_ece_3rd_treeview['show']='headings'
                
                tree_ece_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_ece_3rd_watch_video()
                tree_ece_3rd_treeview.bind('<ButtonRelease-1>',get_ece_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ece_4th_faculty_list=[]
                def ece_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ece_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ece_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ece_4th_watch_video where faculty=%s",(self.ece_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ece_4th_treeview.delete(*tree_ece_4th_treeview.get_children())
                            for row in rows:
                                tree_ece_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ece_4th_watch_video():
                    fetch_ece_4th_watch_video()
                    self.ece_4th_subjects_entry.set("")
                    self.ece_4th_faculyt_entry.set('')
                    self.var_ece_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ece_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ece_4th_watch_video where faculty=%s',(self.ece_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ece_4th_watch_video where faculty=%s ',(self.ece_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ece_4th_watch_video()
                                fetch_ece_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ece_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ece_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ece_4th_subjects_entry.get(),
                               
                                self.var_ece_4th_watch_video.get(),
                                self.ece_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ece_4th_watch_video()
                            fetch_ece_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ece_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ece_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ece_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ece_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ece_4th_subjects','ece_4th_date','ece_4th_time','ece_4th_code','semisters','branch'
                                cur.execute('insert into ece_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ece_4th_subjects_entry.get(),
                                self.ece_4th_faculyt_entry.get(),
                                self.var_ece_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ece_4th_watch_video()
                                con.close()
                def fetch_ece_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ece_4th_watch_video')
                        rows=cur.fetchall()
                        tree_ece_4th_treeview.delete(*tree_ece_4th_treeview.get_children())
                        for row in rows:
                            tree_ece_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ece_4th_watch_video(ev):
                    read=tree_ece_4th_treeview.focus()
                    content=tree_ece_4th_treeview.item(read)
                    row=content['values']
                    self.ece_4th_subjects_entry.set(row[0])
                    self.ece_4th_faculyt_entry.set(row[1])
                    self.var_ece_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ece_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ece_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ece_4th_subjects_entry,values=ece_4th_subjects_list)
                ece_4th_subjects_entry.grid(row=0,column=1)

                ece_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ece_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ece_4th_faculyt_entry,values=ece_4th_faculty_list)
                ece_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ece_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ece_4th_watch_video,width=44)
                ece_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ece_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ece_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ece_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ece_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ece_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ece_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ece_4th_treeview.xview)
                scrolly.configure(command=tree_ece_4th_treeview.yview)

           
                tree_ece_4th_treeview.heading('subject_name',text="Subject Name")
                tree_ece_4th_treeview.heading('faculty',text="Faculty")
                tree_ece_4th_treeview.heading('you_tube_link',text="Watch")
                

         
                tree_ece_4th_treeview.column('subject_name',width=200)
                tree_ece_4th_treeview.column('faculty',width=100)
                tree_ece_4th_treeview.column('you_tube_link',width=250)

                tree_ece_4th_treeview['show']='headings'
                
                tree_ece_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_ece_4th_watch_video()
                tree_ece_4th_treeview.bind('<ButtonRelease-1>',get_ece_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ece_5th_faculty_list=[]
                def ece_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ece_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ece_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ece_5th_watch_video where faculty=%s",(self.ece_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ece_5th_treeview.delete(*tree_ece_5th_treeview.get_children())
                            for row in rows:
                                tree_ece_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ece_5th_watch_video():
                    fetch_ece_5th_watch_video()
                    self.ece_5th_subjects_entry.set("")
                    self.ece_5th_faculyt_entry.set('')
                    self.var_ece_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ece_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ece_5th_watch_video where faculty=%s',(self.ece_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ece_5th_watch_video where faculty=%s ',(self.ece_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ece_5th_watch_video()
                                fetch_ece_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ece_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ece_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ece_5th_subjects_entry.get(),
                               
                                self.var_ece_5th_watch_video.get(),
                                self.ece_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ece_5th_watch_video()
                            fetch_ece_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ece_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ece_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ece_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ece_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ece_5th_subjects','ece_5th_date','ece_5th_time','ece_5th_code','semisters','branch'
                                cur.execute('insert into ece_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ece_5th_subjects_entry.get(),
                                self.ece_5th_faculyt_entry.get(),
                                self.var_ece_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ece_5th_watch_video()
                                con.close()
                def fetch_ece_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ece_5th_watch_video')
                        rows=cur.fetchall()
                        tree_ece_5th_treeview.delete(*tree_ece_5th_treeview.get_children())
                        for row in rows:
                            tree_ece_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ece_5th_watch_video(ev):
                    read=tree_ece_5th_treeview.focus()
                    content=tree_ece_5th_treeview.item(read)
                    row=content['values']
                    self.ece_5th_subjects_entry.set(row[0])
                    self.ece_5th_faculyt_entry.set(row[1])
                    self.var_ece_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ece_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ece_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ece_5th_subjects_entry,values=ece_5th_subjects_list)
                ece_5th_subjects_entry.grid(row=0,column=1)

                ece_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ece_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ece_5th_faculyt_entry,values=ece_5th_faculty_list)
                ece_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ece_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ece_5th_watch_video,width=44)
                ece_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ece_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ece_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ece_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ece_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ece_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ece_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ece_5th_treeview.xview)
                scrolly.configure(command=tree_ece_5th_treeview.yview)

                tree_ece_5th_treeview.heading('subject_name',text="Subject Name")
                tree_ece_5th_treeview.heading('faculty',text="Faculty")
                tree_ece_5th_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_ece_5th_treeview.column('subject_name',width=200)
                tree_ece_5th_treeview.column('faculty',width=100)
                tree_ece_5th_treeview.column('you_tube_link',width=250)

                tree_ece_5th_treeview['show']='headings'
                
                tree_ece_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_ece_5th_watch_video()
                tree_ece_5th_treeview.bind('<ButtonRelease-1>',get_ece_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ece_6th_faculty_list=[]
                def ece_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ece_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ece_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ece_6th_watch_video where faculty=%s",(self.ece_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ece_6th_treeview.delete(*tree_ece_6th_treeview.get_children())
                            for row in rows:
                                tree_ece_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ece_6th_watch_video():
                    fetch_ece_6th_watch_video()
                    self.ece_6th_subjects_entry.set("")
                    self.ece_6th_faculyt_entry.set('')
                    self.var_ece_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ece_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ece_6th_watch_video where faculty=%s',(self.ece_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ece_6th_watch_video where faculty=%s ',(self.ece_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ece_6th_watch_video()
                                fetch_ece_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ece_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ece_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ece_6th_subjects_entry.get(),
                               
                                self.var_ece_6th_watch_video.get(),
                                self.ece_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ece_6th_watch_video()
                            fetch_ece_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ece_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ece_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ece_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ece_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ece_6th_subjects','ece_6th_date','ece_6th_time','ece_6th_code','semisters','branch'
                                cur.execute('insert into ece_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ece_6th_subjects_entry.get(),
                                self.ece_6th_faculyt_entry.get(),
                                self.var_ece_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ece_6th_watch_video()
                                con.close()
                def fetch_ece_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ece_6th_watch_video')
                        rows=cur.fetchall()
                        tree_ece_6th_treeview.delete(*tree_ece_6th_treeview.get_children())
                        for row in rows:
                            tree_ece_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ece_6th_watch_video(ev):
                    read=tree_ece_6th_treeview.focus()
                    content=tree_ece_6th_treeview.item(read)
                    row=content['values']
                    self.ece_6th_subjects_entry.set(row[0])
                    self.ece_6th_faculyt_entry.set(row[1])
                    self.var_ece_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ece_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ece_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ece_6th_subjects_entry,values=ece_6th_subjects_list)
                ece_6th_subjects_entry.grid(row=0,column=1)

                ece_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ece_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ece_6th_faculyt_entry,values=ece_6th_faculty_list)
                ece_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ece_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ece_6th_watch_video,width=44)
                ece_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ece_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ece_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ece_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ece_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ece_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ece_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ece_6th_treeview.xview)
                scrolly.configure(command=tree_ece_6th_treeview.yview)

             
                tree_ece_6th_treeview.heading('subject_name',text="Subject Name")
                tree_ece_6th_treeview.heading('faculty',text="Faculty")
                tree_ece_6th_treeview.heading('you_tube_link',text="Watch")
                

                
                tree_ece_6th_treeview.column('subject_name',width=200)
                tree_ece_6th_treeview.column('faculty',width=100)
                tree_ece_6th_treeview.column('you_tube_link',width=250)

                tree_ece_6th_treeview['show']='headings'
                
                tree_ece_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_ece_6th_watch_video()
                tree_ece_6th_treeview.bind('<ButtonRelease-1>',get_ece_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ece_7th_faculty_list=[]
                def ece_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ece_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ece_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ece_7th_watch_video where faculty=%s",(self.ece_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ece_7th_treeview.delete(*tree_ece_7th_treeview.get_children())
                            for row in rows:
                                tree_ece_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ece_7th_watch_video():
                    fetch_ece_7th_watch_video()
                    self.ece_7th_subjects_entry.set("")
                    self.ece_7th_faculyt_entry.set('')
                    self.var_ece_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ece_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ece_7th_watch_video where faculty=%s',(self.ece_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ece_7th_watch_video where faculty=%s ',(self.ece_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ece_7th_watch_video()
                                fetch_ece_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ece_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ece_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ece_7th_subjects_entry.get(),
                               
                                self.var_ece_7th_watch_video.get(),
                                self.ece_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ece_7th_watch_video()
                            fetch_ece_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ece_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ece_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ece_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ece_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ece_7th_subjects','ece_7th_date','ece_7th_time','ece_7th_code','semisters','branch'
                                cur.execute('insert into ece_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ece_7th_subjects_entry.get(),
                                self.ece_7th_faculyt_entry.get(),
                                self.var_ece_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ece_7th_watch_video()
                                con.close()
                def fetch_ece_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ece_7th_watch_video')
                        rows=cur.fetchall()
                        tree_ece_7th_treeview.delete(*tree_ece_7th_treeview.get_children())
                        for row in rows:
                            tree_ece_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ece_7th_watch_video(ev):
                    read=tree_ece_7th_treeview.focus()
                    content=tree_ece_7th_treeview.item(read)
                    row=content['values']
                    self.ece_7th_subjects_entry.set(row[0])
                    self.ece_7th_faculyt_entry.set(row[1])
                    self.var_ece_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ece_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ece_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ece_7th_subjects_entry,values=ece_7th_subjects_list)
                ece_7th_subjects_entry.grid(row=0,column=1)

                ece_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ece_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ece_7th_faculyt_entry,values=ece_7th_faculty_list)
                ece_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ece_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ece_7th_watch_video,width=44)
                ece_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ece_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ece_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ece_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ece_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ece_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ece_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ece_7th_treeview.xview)
                scrolly.configure(command=tree_ece_7th_treeview.yview)

                
                tree_ece_7th_treeview.heading('subject_name',text="Subject Name")
                tree_ece_7th_treeview.heading('faculty',text="Faculty")
                tree_ece_7th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_ece_7th_treeview.column('subject_name',width=200)
                tree_ece_7th_treeview.column('faculty',width=100)
                tree_ece_7th_treeview.column('you_tube_link',width=250)

                tree_ece_7th_treeview['show']='headings'
                
                tree_ece_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_ece_7th_watch_video()
                tree_ece_7th_treeview.bind('<ButtonRelease-1>',get_ece_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ece_8th_faculty_list=[]
                def ece_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ece_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ece_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ece_8th_watch_video where faculty=%s",(self.ece_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ece_8th_treeview.delete(*tree_ece_8th_treeview.get_children())
                            for row in rows:
                                tree_ece_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ece_8th_watch_video():
                    fetch_ece_8th_watch_video()
                    self.ece_8th_subjects_entry.set("")
                    self.ece_8th_faculyt_entry.set('')
                    self.var_ece_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ece_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ece_8th_watch_video where faculty=%s',(self.ece_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ece_8th_watch_video where faculty=%s ',(self.ece_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ece_8th_watch_video()
                                fetch_ece_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ece_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ece_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ece_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ece_8th_subjects_entry.get(),
                               
                                self.var_ece_8th_watch_video.get(),
                                self.ece_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ece_8th_watch_video()
                            fetch_ece_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ece_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ece_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ece_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ece_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ece_8th_subjects','ece_8th_date','ece_8th_time','ece_8th_code','semisters','branch'
                                cur.execute('insert into ece_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ece_8th_subjects_entry.get(),
                                self.ece_8th_faculyt_entry.get(),
                                self.var_ece_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ece_8th_watch_video()
                                con.close()
                def fetch_ece_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ece_8th_watch_video')
                        rows=cur.fetchall()
                        tree_ece_8th_treeview.delete(*tree_ece_8th_treeview.get_children())
                        for row in rows:
                            tree_ece_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ece_8th_watch_video(ev):
                    read=tree_ece_8th_treeview.focus()
                    content=tree_ece_8th_treeview.item(read)
                    row=content['values']
                    self.ece_8th_subjects_entry.set(row[0])
                    self.ece_8th_faculyt_entry.set(row[1])
                    self.var_ece_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ece_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ece_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ece_8th_subjects_entry,values=ece_8th_subjects_list)
                ece_8th_subjects_entry.grid(row=0,column=1)

                ece_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ece_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ece_8th_faculyt_entry,values=ece_8th_faculty_list)
                ece_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ece_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ece_8th_watch_video,width=44)
                ece_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ece_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ece_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ece_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ece_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ece_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ece_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ece_8th_treeview.xview)
                scrolly.configure(command=tree_ece_8th_treeview.yview)

                
                tree_ece_8th_treeview.heading('subject_name',text="Subject Name")
                tree_ece_8th_treeview.heading('faculty',text="Faculty")
                tree_ece_8th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_ece_8th_treeview.column('subject_name',width=200)
                tree_ece_8th_treeview.column('faculty',width=100)
                tree_ece_8th_treeview.column('you_tube_link',width=250)

                tree_ece_8th_treeview['show']='headings'
                
                tree_ece_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_ece_8th_watch_video()
                tree_ece_8th_treeview.bind('<ButtonRelease-1>',get_ece_8th_watch_video)
        ############################################################################################################################################
        #################################################################################################################################################
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                cs_3rd_faculty_list=[]
                def cs_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                cs_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_cs_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from cs_3rd_watch_video where faculty=%s",(self.cs_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_cs_3rd_treeview.delete(*tree_cs_3rd_treeview.get_children())
                            for row in rows:
                                tree_cs_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_cs_3rd_watch_video():
                    fetch_cs_3rd_watch_video()
                    self.cs_3rd_subjects_entry.set("")
                    self.cs_3rd_faculyt_entry.set('')
                    self.var_cs_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_cs_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from cs_3rd_watch_video where faculty=%s',(self.cs_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from cs_3rd_watch_video where faculty=%s ',(self.cs_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_cs_3rd_watch_video()
                                fetch_cs_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_cs_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update cs_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.cs_3rd_subjects_entry.get(),
                               
                                self.var_cs_3rd_watch_video.get(),
                                self.cs_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_cs_3rd_watch_video()
                            fetch_cs_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_cs_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.cs_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.cs_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_cs_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'cs_3rd_subjects','cs_3rd_date','cs_3rd_time','cs_3rd_code','semisters','branch'
                                cur.execute('insert into cs_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.cs_3rd_subjects_entry.get(),
                                self.cs_3rd_faculyt_entry.get(),
                                self.var_cs_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_cs_3rd_watch_video()
                                con.close()
                def fetch_cs_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from cs_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_cs_3rd_treeview.delete(*tree_cs_3rd_treeview.get_children())
                        for row in rows:
                            tree_cs_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_cs_3rd_watch_video(ev):
                    read=tree_cs_3rd_treeview.focus()
                    content=tree_cs_3rd_treeview.item(read)
                    row=content['values']
                    self.cs_3rd_subjects_entry.set(row[0])
                    self.cs_3rd_faculyt_entry.set(row[1])
                    self.var_cs_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_cs_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                cs_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.cs_3rd_subjects_entry,values=cs_3rd_subjects_list)
                cs_3rd_subjects_entry.grid(row=0,column=1)

                cs_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                cs_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.cs_3rd_faculyt_entry,values=cs_3rd_faculty_list)
                cs_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                cs_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_cs_3rd_watch_video,width=44)
                cs_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_cs_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_cs_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_cs_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_cs_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_cs_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_cs_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_cs_3rd_treeview.xview)
                scrolly.configure(command=tree_cs_3rd_treeview.yview)

                
                tree_cs_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_cs_3rd_treeview.heading('faculty',text="Faculty")
                tree_cs_3rd_treeview.heading('you_tube_link',text="Watch")
                

              
                tree_cs_3rd_treeview.column('subject_name',width=200)
                tree_cs_3rd_treeview.column('faculty',width=100)
                tree_cs_3rd_treeview.column('you_tube_link',width=250)

                tree_cs_3rd_treeview['show']='headings'
                
                tree_cs_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_cs_3rd_watch_video()
                tree_cs_3rd_treeview.bind('<ButtonRelease-1>',get_cs_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                cs_4th_faculty_list=[]
                def cs_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                cs_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_cs_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from cs_4th_watch_video where faculty=%s",(self.cs_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_cs_4th_treeview.delete(*tree_cs_4th_treeview.get_children())
                            for row in rows:
                                tree_cs_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_cs_4th_watch_video():
                    fetch_cs_4th_watch_video()
                    self.cs_4th_subjects_entry.set("")
                    self.cs_4th_faculyt_entry.set('')
                    self.var_cs_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_cs_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from cs_4th_watch_video where faculty=%s',(self.cs_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from cs_4th_watch_video where faculty=%s ',(self.cs_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_cs_4th_watch_video()
                                fetch_cs_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_cs_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update cs_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.cs_4th_subjects_entry.get(),
                               
                                self.var_cs_4th_watch_video.get(),
                                self.cs_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_cs_4th_watch_video()
                            fetch_cs_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_cs_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.cs_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.cs_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_cs_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'cs_4th_subjects','cs_4th_date','cs_4th_time','cs_4th_code','semisters','branch'
                                cur.execute('insert into cs_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.cs_4th_subjects_entry.get(),
                                self.cs_4th_faculyt_entry.get(),
                                self.var_cs_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_cs_4th_watch_video()
                                con.close()
                def fetch_cs_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from cs_4th_watch_video')
                        rows=cur.fetchall()
                        tree_cs_4th_treeview.delete(*tree_cs_4th_treeview.get_children())
                        for row in rows:
                            tree_cs_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_cs_4th_watch_video(ev):
                    read=tree_cs_4th_treeview.focus()
                    content=tree_cs_4th_treeview.item(read)
                    row=content['values']
                    self.cs_4th_subjects_entry.set(row[0])
                    self.cs_4th_faculyt_entry.set(row[1])
                    self.var_cs_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_cs_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                cs_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.cs_4th_subjects_entry,values=cs_4th_subjects_list)
                cs_4th_subjects_entry.grid(row=0,column=1)

                cs_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                cs_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.cs_4th_faculyt_entry,values=cs_4th_faculty_list)
                cs_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                cs_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_cs_4th_watch_video,width=44)
                cs_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_cs_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_cs_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_cs_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_cs_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_cs_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_cs_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_cs_4th_treeview.xview)
                scrolly.configure(command=tree_cs_4th_treeview.yview)

                
                tree_cs_4th_treeview.heading('subject_name',text="Subject Name")
                tree_cs_4th_treeview.heading('faculty',text="Faculty")
                tree_cs_4th_treeview.heading('you_tube_link',text="Watch")
                

             
                tree_cs_4th_treeview.column('subject_name',width=200)
                tree_cs_4th_treeview.column('faculty',width=100)
                tree_cs_4th_treeview.column('you_tube_link',width=250)

                tree_cs_4th_treeview['show']='headings'
                
                tree_cs_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_cs_4th_watch_video()
                tree_cs_4th_treeview.bind('<ButtonRelease-1>',get_cs_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                cs_5th_faculty_list=[]
                def cs_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                cs_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_cs_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from cs_5th_watch_video where faculty=%s",(self.cs_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_cs_5th_treeview.delete(*tree_cs_5th_treeview.get_children())
                            for row in rows:
                                tree_cs_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_cs_5th_watch_video():
                    fetch_cs_5th_watch_video()
                    self.cs_5th_subjects_entry.set("")
                    self.cs_5th_faculyt_entry.set('')
                    self.var_cs_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_cs_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from cs_5th_watch_video where faculty=%s',(self.cs_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from cs_5th_watch_video where faculty=%s ',(self.cs_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_cs_5th_watch_video()
                                fetch_cs_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_cs_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update cs_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.cs_5th_subjects_entry.get(),
                               
                                self.var_cs_5th_watch_video.get(),
                                self.cs_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_cs_5th_watch_video()
                            fetch_cs_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_cs_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.cs_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.cs_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_cs_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'cs_5th_subjects','cs_5th_date','cs_5th_time','cs_5th_code','semisters','branch'
                                cur.execute('insert into cs_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.cs_5th_subjects_entry.get(),
                                self.cs_5th_faculyt_entry.get(),
                                self.var_cs_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_cs_5th_watch_video()
                                con.close()
                def fetch_cs_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from cs_5th_watch_video')
                        rows=cur.fetchall()
                        tree_cs_5th_treeview.delete(*tree_cs_5th_treeview.get_children())
                        for row in rows:
                            tree_cs_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_cs_5th_watch_video(ev):
                    read=tree_cs_5th_treeview.focus()
                    content=tree_cs_5th_treeview.item(read)
                    row=content['values']
                    self.cs_5th_subjects_entry.set(row[0])
                    self.cs_5th_faculyt_entry.set(row[1])
                    self.var_cs_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_cs_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                cs_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.cs_5th_subjects_entry,values=cs_5th_subjects_list)
                cs_5th_subjects_entry.grid(row=0,column=1)

                cs_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                cs_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.cs_5th_faculyt_entry,values=cs_5th_faculty_list)
                cs_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                cs_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_cs_5th_watch_video,width=44)
                cs_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_cs_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_cs_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_cs_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_cs_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_cs_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_cs_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_cs_5th_treeview.xview)
                scrolly.configure(command=tree_cs_5th_treeview.yview)

         
                tree_cs_5th_treeview.heading('subject_name',text="Subject Name")
                tree_cs_5th_treeview.heading('faculty',text="Faculty")
                tree_cs_5th_treeview.heading('you_tube_link',text="Watch")
                

             
                tree_cs_5th_treeview.column('subject_name',width=200)
                tree_cs_5th_treeview.column('faculty',width=100)
                tree_cs_5th_treeview.column('you_tube_link',width=250)

                tree_cs_5th_treeview['show']='headings'
                
                tree_cs_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_cs_5th_watch_video()
                tree_cs_5th_treeview.bind('<ButtonRelease-1>',get_cs_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                cs_6th_faculty_list=[]
                def cs_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                cs_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_cs_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from cs_6th_watch_video where faculty=%s",(self.cs_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_cs_6th_treeview.delete(*tree_cs_6th_treeview.get_children())
                            for row in rows:
                                tree_cs_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_cs_6th_watch_video():
                    fetch_cs_6th_watch_video()
                    self.cs_6th_subjects_entry.set("")
                    self.cs_6th_faculyt_entry.set('')
                    self.var_cs_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_cs_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from cs_6th_watch_video where faculty=%s',(self.cs_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from cs_6th_watch_video where faculty=%s ',(self.cs_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_cs_6th_watch_video()
                                fetch_cs_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_cs_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update cs_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.cs_6th_subjects_entry.get(),
                               
                                self.var_cs_6th_watch_video.get(),
                                self.cs_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_cs_6th_watch_video()
                            fetch_cs_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_cs_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.cs_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.cs_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_cs_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'cs_6th_subjects','cs_6th_date','cs_6th_time','cs_6th_code','semisters','branch'
                                cur.execute('insert into cs_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.cs_6th_subjects_entry.get(),
                                self.cs_6th_faculyt_entry.get(),
                                self.var_cs_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_cs_6th_watch_video()
                                con.close()
                def fetch_cs_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from cs_6th_watch_video')
                        rows=cur.fetchall()
                        tree_cs_6th_treeview.delete(*tree_cs_6th_treeview.get_children())
                        for row in rows:
                            tree_cs_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_cs_6th_watch_video(ev):
                    read=tree_cs_6th_treeview.focus()
                    content=tree_cs_6th_treeview.item(read)
                    row=content['values']
                    self.cs_6th_subjects_entry.set(row[0])
                    self.cs_6th_faculyt_entry.set(row[1])
                    self.var_cs_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_cs_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                cs_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.cs_6th_subjects_entry,values=cs_6th_subjects_list)
                cs_6th_subjects_entry.grid(row=0,column=1)

                cs_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                cs_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.cs_6th_faculyt_entry,values=cs_6th_faculty_list)
                cs_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                cs_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_cs_6th_watch_video,width=44)
                cs_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_cs_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_cs_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_cs_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_cs_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_cs_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_cs_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_cs_6th_treeview.xview)
                scrolly.configure(command=tree_cs_6th_treeview.yview)

               
                tree_cs_6th_treeview.heading('subject_name',text="Subject Name")
                tree_cs_6th_treeview.heading('faculty',text="Faculty")
                tree_cs_6th_treeview.heading('you_tube_link',text="Watch")
                

             
                tree_cs_6th_treeview.column('subject_name',width=200)
                tree_cs_6th_treeview.column('faculty',width=100)
                tree_cs_6th_treeview.column('you_tube_link',width=250)

                tree_cs_6th_treeview['show']='headings'
                
                tree_cs_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_cs_6th_watch_video()
                tree_cs_6th_treeview.bind('<ButtonRelease-1>',get_cs_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                cs_7th_faculty_list=[]
                def cs_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                cs_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_cs_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from cs_7th_watch_video where faculty=%s",(self.cs_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_cs_7th_treeview.delete(*tree_cs_7th_treeview.get_children())
                            for row in rows:
                                tree_cs_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_cs_7th_watch_video():
                    fetch_cs_7th_watch_video()
                    self.cs_7th_subjects_entry.set("")
                    self.cs_7th_faculyt_entry.set('')
                    self.var_cs_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_cs_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from cs_7th_watch_video where faculty=%s',(self.cs_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from cs_7th_watch_video where faculty=%s ',(self.cs_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_cs_7th_watch_video()
                                fetch_cs_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_cs_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update cs_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.cs_7th_subjects_entry.get(),
                               
                                self.var_cs_7th_watch_video.get(),
                                self.cs_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_cs_7th_watch_video()
                            fetch_cs_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_cs_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.cs_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.cs_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_cs_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'cs_7th_subjects','cs_7th_date','cs_7th_time','cs_7th_code','semisters','branch'
                                cur.execute('insert into cs_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.cs_7th_subjects_entry.get(),
                                self.cs_7th_faculyt_entry.get(),
                                self.var_cs_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_cs_7th_watch_video()
                                con.close()
                def fetch_cs_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from cs_7th_watch_video')
                        rows=cur.fetchall()
                        tree_cs_7th_treeview.delete(*tree_cs_7th_treeview.get_children())
                        for row in rows:
                            tree_cs_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_cs_7th_watch_video(ev):
                    read=tree_cs_7th_treeview.focus()
                    content=tree_cs_7th_treeview.item(read)
                    row=content['values']
                    self.cs_7th_subjects_entry.set(row[0])
                    self.cs_7th_faculyt_entry.set(row[1])
                    self.var_cs_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_cs_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                cs_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.cs_7th_subjects_entry,values=cs_7th_subjects_list)
                cs_7th_subjects_entry.grid(row=0,column=1)

                cs_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                cs_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.cs_7th_faculyt_entry,values=cs_7th_faculty_list)
                cs_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                cs_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_cs_7th_watch_video,width=44)
                cs_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_cs_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_cs_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_cs_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_cs_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_cs_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_cs_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_cs_7th_treeview.xview)
                scrolly.configure(command=tree_cs_7th_treeview.yview)

               
                tree_cs_7th_treeview.heading('subject_name',text="Subject Name")
                tree_cs_7th_treeview.heading('faculty',text="Faculty")
                tree_cs_7th_treeview.heading('you_tube_link',text="Watch")
                

                tree_cs_7th_treeview.column('subject_name',width=200)
                tree_cs_7th_treeview.column('faculty',width=100)
                tree_cs_7th_treeview.column('you_tube_link',width=250)

                tree_cs_7th_treeview['show']='headings'
                
                tree_cs_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_cs_7th_watch_video()
                tree_cs_7th_treeview.bind('<ButtonRelease-1>',get_cs_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                cs_8th_faculty_list=[]
                def cs_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                cs_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_cs_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from cs_8th_watch_video where faculty=%s",(self.cs_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_cs_8th_treeview.delete(*tree_cs_8th_treeview.get_children())
                            for row in rows:
                                tree_cs_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_cs_8th_watch_video():
                    fetch_cs_8th_watch_video()
                    self.cs_8th_subjects_entry.set("")
                    self.cs_8th_faculyt_entry.set('')
                    self.var_cs_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_cs_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from cs_8th_watch_video where faculty=%s',(self.cs_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from cs_8th_watch_video where faculty=%s ',(self.cs_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_cs_8th_watch_video()
                                fetch_cs_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_cs_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.cs_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update cs_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.cs_8th_subjects_entry.get(),
                               
                                self.var_cs_8th_watch_video.get(),
                                self.cs_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_cs_8th_watch_video()
                            fetch_cs_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_cs_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.cs_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.cs_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_cs_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'cs_8th_subjects','cs_8th_date','cs_8th_time','cs_8th_code','semisters','branch'
                                cur.execute('insert into cs_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.cs_8th_subjects_entry.get(),
                                self.cs_8th_faculyt_entry.get(),
                                self.var_cs_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_cs_8th_watch_video()
                                con.close()
                def fetch_cs_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from cs_8th_watch_video')
                        rows=cur.fetchall()
                        tree_cs_8th_treeview.delete(*tree_cs_8th_treeview.get_children())
                        for row in rows:
                            tree_cs_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_cs_8th_watch_video(ev):
                    read=tree_cs_8th_treeview.focus()
                    content=tree_cs_8th_treeview.item(read)
                    row=content['values']
                    self.cs_8th_subjects_entry.set(row[0])
                    self.cs_8th_faculyt_entry.set(row[1])
                    self.var_cs_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_cs_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                cs_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.cs_8th_subjects_entry,values=cs_8th_subjects_list)
                cs_8th_subjects_entry.grid(row=0,column=1)

                cs_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                cs_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.cs_8th_faculyt_entry,values=cs_8th_faculty_list)
                cs_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                cs_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_cs_8th_watch_video,width=44)
                cs_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_cs_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_cs_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_cs_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_cs_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_cs_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_cs_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_cs_8th_treeview.xview)
                scrolly.configure(command=tree_cs_8th_treeview.yview)

                tree_cs_8th_treeview.heading('subject_name',text="Subject Name")
                tree_cs_8th_treeview.heading('faculty',text="Faculty")
                tree_cs_8th_treeview.heading('you_tube_link',text="Watch")
                

                tree_cs_8th_treeview.column('subject_name',width=200)
                tree_cs_8th_treeview.column('faculty',width=100)
                tree_cs_8th_treeview.column('you_tube_link',width=250)

                tree_cs_8th_treeview['show']='headings'
                
                tree_cs_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_cs_8th_watch_video()
                tree_cs_8th_treeview.bind('<ButtonRelease-1>',get_cs_8th_watch_video)
        #####################################################################################################################################################
        #########################################################################################################################################################
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ise_3rd_faculty_list=[]
                def ise_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ise_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ise_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ise_3rd_watch_video where faculty=%s",(self.ise_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ise_3rd_treeview.delete(*tree_ise_3rd_treeview.get_children())
                            for row in rows:
                                tree_ise_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ise_3rd_watch_video():
                    fetch_ise_3rd_watch_video()
                    self.ise_3rd_subjects_entry.set("")
                    self.ise_3rd_faculyt_entry.set('')
                    self.var_ise_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ise_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ise_3rd_watch_video where faculty=%s',(self.ise_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ise_3rd_watch_video where faculty=%s ',(self.ise_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ise_3rd_watch_video()
                                fetch_ise_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ise_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ise_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ise_3rd_subjects_entry.get(),
                               
                                self.var_ise_3rd_watch_video.get(),
                                self.ise_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ise_3rd_watch_video()
                            fetch_ise_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ise_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ise_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ise_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ise_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ise_3rd_subjects','ise_3rd_date','ise_3rd_time','ise_3rd_code','semisters','branch'
                                cur.execute('insert into ise_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ise_3rd_subjects_entry.get(),
                                self.ise_3rd_faculyt_entry.get(),
                                self.var_ise_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ise_3rd_watch_video()
                                con.close()
                def fetch_ise_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ise_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_ise_3rd_treeview.delete(*tree_ise_3rd_treeview.get_children())
                        for row in rows:
                            tree_ise_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ise_3rd_watch_video(ev):
                    read=tree_ise_3rd_treeview.focus()
                    content=tree_ise_3rd_treeview.item(read)
                    row=content['values']
                    self.ise_3rd_subjects_entry.set(row[0])
                    self.ise_3rd_faculyt_entry.set(row[1])
                    self.var_ise_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ise_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ise_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ise_3rd_subjects_entry,values=ise_3rd_subjects_list)
                ise_3rd_subjects_entry.grid(row=0,column=1)

                ise_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ise_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ise_3rd_faculyt_entry,values=ise_3rd_faculty_list)
                ise_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ise_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ise_3rd_watch_video,width=44)
                ise_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ise_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ise_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ise_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ise_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ise_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ise_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ise_3rd_treeview.xview)
                scrolly.configure(command=tree_ise_3rd_treeview.yview)

           
                tree_ise_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_ise_3rd_treeview.heading('faculty',text="Faculty")
                tree_ise_3rd_treeview.heading('you_tube_link',text="Watch")
                

          
                tree_ise_3rd_treeview.column('subject_name',width=200)
                tree_ise_3rd_treeview.column('faculty',width=100)
                tree_ise_3rd_treeview.column('you_tube_link',width=250)

                tree_ise_3rd_treeview['show']='headings'
                
                tree_ise_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_ise_3rd_watch_video()
                tree_ise_3rd_treeview.bind('<ButtonRelease-1>',get_ise_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ise_4th_faculty_list=[]
                def ise_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ise_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ise_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ise_4th_watch_video where faculty=%s",(self.ise_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ise_4th_treeview.delete(*tree_ise_4th_treeview.get_children())
                            for row in rows:
                                tree_ise_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ise_4th_watch_video():
                    fetch_ise_4th_watch_video()
                    self.ise_4th_subjects_entry.set("")
                    self.ise_4th_faculyt_entry.set('')
                    self.var_ise_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ise_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ise_4th_watch_video where faculty=%s',(self.ise_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ise_4th_watch_video where faculty=%s ',(self.ise_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ise_4th_watch_video()
                                fetch_ise_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ise_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ise_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ise_4th_subjects_entry.get(),
                               
                                self.var_ise_4th_watch_video.get(),
                                self.ise_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ise_4th_watch_video()
                            fetch_ise_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ise_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ise_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ise_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ise_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ise_4th_subjects','ise_4th_date','ise_4th_time','ise_4th_code','semisters','branch'
                                cur.execute('insert into ise_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ise_4th_subjects_entry.get(),
                                self.ise_4th_faculyt_entry.get(),
                                self.var_ise_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ise_4th_watch_video()
                                con.close()
                def fetch_ise_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ise_4th_watch_video')
                        rows=cur.fetchall()
                        tree_ise_4th_treeview.delete(*tree_ise_4th_treeview.get_children())
                        for row in rows:
                            tree_ise_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ise_4th_watch_video(ev):
                    read=tree_ise_4th_treeview.focus()
                    content=tree_ise_4th_treeview.item(read)
                    row=content['values']
                    self.ise_4th_subjects_entry.set(row[0])
                    self.ise_4th_faculyt_entry.set(row[1])
                    self.var_ise_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ise_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ise_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ise_4th_subjects_entry,values=ise_4th_subjects_list)
                ise_4th_subjects_entry.grid(row=0,column=1)

                ise_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ise_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ise_4th_faculyt_entry,values=ise_4th_faculty_list)
                ise_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ise_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ise_4th_watch_video,width=44)
                ise_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ise_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ise_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ise_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ise_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ise_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ise_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ise_4th_treeview.xview)
                scrolly.configure(command=tree_ise_4th_treeview.yview)

            
                tree_ise_4th_treeview.heading('subject_name',text="Subject Name")
                tree_ise_4th_treeview.heading('faculty',text="Faculty")
                tree_ise_4th_treeview.heading('you_tube_link',text="Watch")
         
                tree_ise_4th_treeview.column('subject_name',width=200)
                tree_ise_4th_treeview.column('faculty',width=100)
                tree_ise_4th_treeview.column('you_tube_link',width=250)

                tree_ise_4th_treeview['show']='headings'
                
                tree_ise_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_ise_4th_watch_video()
                tree_ise_4th_treeview.bind('<ButtonRelease-1>',get_ise_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ise_5th_faculty_list=[]
                def ise_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ise_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ise_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ise_5th_watch_video where faculty=%s",(self.ise_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ise_5th_treeview.delete(*tree_ise_5th_treeview.get_children())
                            for row in rows:
                                tree_ise_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ise_5th_watch_video():
                    fetch_ise_5th_watch_video()
                    self.ise_5th_subjects_entry.set("")
                    self.ise_5th_faculyt_entry.set('')
                    self.var_ise_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ise_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ise_5th_watch_video where faculty=%s',(self.ise_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ise_5th_watch_video where faculty=%s ',(self.ise_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ise_5th_watch_video()
                                fetch_ise_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ise_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ise_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ise_5th_subjects_entry.get(),
                               
                                self.var_ise_5th_watch_video.get(),
                                self.ise_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ise_5th_watch_video()
                            fetch_ise_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ise_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ise_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ise_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ise_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ise_5th_subjects','ise_5th_date','ise_5th_time','ise_5th_code','semisters','branch'
                                cur.execute('insert into ise_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ise_5th_subjects_entry.get(),
                                self.ise_5th_faculyt_entry.get(),
                                self.var_ise_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ise_5th_watch_video()
                                con.close()
                def fetch_ise_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ise_5th_watch_video')
                        rows=cur.fetchall()
                        tree_ise_5th_treeview.delete(*tree_ise_5th_treeview.get_children())
                        for row in rows:
                            tree_ise_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ise_5th_watch_video(ev):
                    read=tree_ise_5th_treeview.focus()
                    content=tree_ise_5th_treeview.item(read)
                    row=content['values']
                    self.ise_5th_subjects_entry.set(row[0])
                    self.ise_5th_faculyt_entry.set(row[1])
                    self.var_ise_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ise_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ise_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ise_5th_subjects_entry,values=ise_5th_subjects_list)
                ise_5th_subjects_entry.grid(row=0,column=1)

                ise_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ise_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ise_5th_faculyt_entry,values=ise_5th_faculty_list)
                ise_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ise_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ise_5th_watch_video,width=44)
                ise_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ise_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ise_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ise_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ise_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ise_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ise_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ise_5th_treeview.xview)
                scrolly.configure(command=tree_ise_5th_treeview.yview)

                
                tree_ise_5th_treeview.heading('subject_name',text="Subject Name")
                tree_ise_5th_treeview.heading('faculty',text="Faculty")
                tree_ise_5th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_ise_5th_treeview.column('subject_name',width=200)
                tree_ise_5th_treeview.column('faculty',width=100)
                tree_ise_5th_treeview.column('you_tube_link',width=250)

                tree_ise_5th_treeview['show']='headings'
                
                tree_ise_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_ise_5th_watch_video()
                tree_ise_5th_treeview.bind('<ButtonRelease-1>',get_ise_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ise_6th_faculty_list=[]
                def ise_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ise_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ise_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ise_6th_watch_video where faculty=%s",(self.ise_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ise_6th_treeview.delete(*tree_ise_6th_treeview.get_children())
                            for row in rows:
                                tree_ise_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ise_6th_watch_video():
                    fetch_ise_6th_watch_video()
                    self.ise_6th_subjects_entry.set("")
                    self.ise_6th_faculyt_entry.set('')
                    self.var_ise_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ise_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ise_6th_watch_video where faculty=%s',(self.ise_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ise_6th_watch_video where faculty=%s ',(self.ise_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ise_6th_watch_video()
                                fetch_ise_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ise_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ise_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ise_6th_subjects_entry.get(),
                               
                                self.var_ise_6th_watch_video.get(),
                                self.ise_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ise_6th_watch_video()
                            fetch_ise_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ise_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ise_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ise_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ise_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ise_6th_subjects','ise_6th_date','ise_6th_time','ise_6th_code','semisters','branch'
                                cur.execute('insert into ise_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ise_6th_subjects_entry.get(),
                                self.ise_6th_faculyt_entry.get(),
                                self.var_ise_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ise_6th_watch_video()
                                con.close()
                def fetch_ise_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ise_6th_watch_video')
                        rows=cur.fetchall()
                        tree_ise_6th_treeview.delete(*tree_ise_6th_treeview.get_children())
                        for row in rows:
                            tree_ise_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ise_6th_watch_video(ev):
                    read=tree_ise_6th_treeview.focus()
                    content=tree_ise_6th_treeview.item(read)
                    row=content['values']
                    self.ise_6th_subjects_entry.set(row[0])
                    self.ise_6th_faculyt_entry.set(row[1])
                    self.var_ise_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ise_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ise_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ise_6th_subjects_entry,values=ise_6th_subjects_list)
                ise_6th_subjects_entry.grid(row=0,column=1)

                ise_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ise_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ise_6th_faculyt_entry,values=ise_6th_faculty_list)
                ise_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ise_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ise_6th_watch_video,width=44)
                ise_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ise_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ise_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ise_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ise_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ise_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ise_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ise_6th_treeview.xview)
                scrolly.configure(command=tree_ise_6th_treeview.yview)

           
                tree_ise_6th_treeview.heading('subject_name',text="Subject Name")
                tree_ise_6th_treeview.heading('faculty',text="Faculty")
                tree_ise_6th_treeview.heading('you_tube_link',text="Watch")
                

            
                tree_ise_6th_treeview.column('subject_name',width=200)
                tree_ise_6th_treeview.column('faculty',width=100)
                tree_ise_6th_treeview.column('you_tube_link',width=250)

                tree_ise_6th_treeview['show']='headings'
                
                tree_ise_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_ise_6th_watch_video()
                tree_ise_6th_treeview.bind('<ButtonRelease-1>',get_ise_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ise_7th_faculty_list=[]
                def ise_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ise_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ise_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ise_7th_watch_video where faculty=%s",(self.ise_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ise_7th_treeview.delete(*tree_ise_7th_treeview.get_children())
                            for row in rows:
                                tree_ise_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ise_7th_watch_video():
                    fetch_ise_7th_watch_video()
                    self.ise_7th_subjects_entry.set("")
                    self.ise_7th_faculyt_entry.set('')
                    self.var_ise_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ise_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ise_7th_watch_video where faculty=%s',(self.ise_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ise_7th_watch_video where faculty=%s ',(self.ise_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ise_7th_watch_video()
                                fetch_ise_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ise_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ise_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ise_7th_subjects_entry.get(),
                               
                                self.var_ise_7th_watch_video.get(),
                                self.ise_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ise_7th_watch_video()
                            fetch_ise_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ise_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ise_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ise_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ise_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ise_7th_subjects','ise_7th_date','ise_7th_time','ise_7th_code','semisters','branch'
                                cur.execute('insert into ise_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ise_7th_subjects_entry.get(),
                                self.ise_7th_faculyt_entry.get(),
                                self.var_ise_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ise_7th_watch_video()
                                con.close()
                def fetch_ise_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ise_7th_watch_video')
                        rows=cur.fetchall()
                        tree_ise_7th_treeview.delete(*tree_ise_7th_treeview.get_children())
                        for row in rows:
                            tree_ise_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ise_7th_watch_video(ev):
                    read=tree_ise_7th_treeview.focus()
                    content=tree_ise_7th_treeview.item(read)
                    row=content['values']
                    self.ise_7th_subjects_entry.set(row[0])
                    self.ise_7th_faculyt_entry.set(row[1])
                    self.var_ise_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ise_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ise_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ise_7th_subjects_entry,values=ise_7th_subjects_list)
                ise_7th_subjects_entry.grid(row=0,column=1)

                ise_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ise_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ise_7th_faculyt_entry,values=ise_7th_faculty_list)
                ise_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ise_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ise_7th_watch_video,width=44)
                ise_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ise_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ise_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ise_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ise_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ise_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ise_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ise_7th_treeview.xview)
                scrolly.configure(command=tree_ise_7th_treeview.yview)

               
                tree_ise_7th_treeview.heading('subject_name',text="Subject Name")
                tree_ise_7th_treeview.heading('faculty',text="Faculty")
                tree_ise_7th_treeview.heading('you_tube_link',text="Watch")
                

               
                tree_ise_7th_treeview.column('subject_name',width=200)
                tree_ise_7th_treeview.column('faculty',width=100)
                tree_ise_7th_treeview.column('you_tube_link',width=250)

                tree_ise_7th_treeview['show']='headings'
                
                tree_ise_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_ise_7th_watch_video()
                tree_ise_7th_treeview.bind('<ButtonRelease-1>',get_ise_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ise_8th_faculty_list=[]
                def ise_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ise_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ise_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ise_8th_watch_video where faculty=%s",(self.ise_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ise_8th_treeview.delete(*tree_ise_8th_treeview.get_children())
                            for row in rows:
                                tree_ise_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ise_8th_watch_video():
                    fetch_ise_8th_watch_video()
                    self.ise_8th_subjects_entry.set("")
                    self.ise_8th_faculyt_entry.set('')
                    self.var_ise_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ise_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ise_8th_watch_video where faculty=%s',(self.ise_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ise_8th_watch_video where faculty=%s ',(self.ise_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ise_8th_watch_video()
                                fetch_ise_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ise_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ise_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ise_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ise_8th_subjects_entry.get(),
                               
                                self.var_ise_8th_watch_video.get(),
                                self.ise_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ise_8th_watch_video()
                            fetch_ise_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ise_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ise_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ise_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ise_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ise_8th_subjects','ise_8th_date','ise_8th_time','ise_8th_code','semisters','branch'
                                cur.execute('insert into ise_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ise_8th_subjects_entry.get(),
                                self.ise_8th_faculyt_entry.get(),
                                self.var_ise_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ise_8th_watch_video()
                                con.close()
                def fetch_ise_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ise_8th_watch_video')
                        rows=cur.fetchall()
                        tree_ise_8th_treeview.delete(*tree_ise_8th_treeview.get_children())
                        for row in rows:
                            tree_ise_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ise_8th_watch_video(ev):
                    read=tree_ise_8th_treeview.focus()
                    content=tree_ise_8th_treeview.item(read)
                    row=content['values']
                    self.ise_8th_subjects_entry.set(row[0])
                    self.ise_8th_faculyt_entry.set(row[1])
                    self.var_ise_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ise_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ise_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ise_8th_subjects_entry,values=ise_8th_subjects_list)
                ise_8th_subjects_entry.grid(row=0,column=1)

                ise_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ise_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ise_8th_faculyt_entry,values=ise_8th_faculty_list)
                ise_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ise_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ise_8th_watch_video,width=44)
                ise_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ise_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ise_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ise_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ise_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ise_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ise_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ise_8th_treeview.xview)
                scrolly.configure(command=tree_ise_8th_treeview.yview)

            
                tree_ise_8th_treeview.heading('subject_name',text="Subject Name")
                tree_ise_8th_treeview.heading('faculty',text="Faculty")
                tree_ise_8th_treeview.heading('you_tube_link',text="Watch")
                

                tree_ise_8th_treeview.column('subject_name',width=200)
                tree_ise_8th_treeview.column('faculty',width=100)
                tree_ise_8th_treeview.column('you_tube_link',width=250)

                tree_ise_8th_treeview['show']='headings'
                
                tree_ise_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_ise_8th_watch_video()
                tree_ise_8th_treeview.bind('<ButtonRelease-1>',get_ise_8th_watch_video)
        ###################################################################################################################################################
        ##################################################################################################################################################
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ete_3rd_faculty_list=[]
                def ete_3rd_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ete_3rd_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ete_3rd_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ete_3rd_watch_video where faculty=%s",(self.ete_3rd_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ete_3rd_treeview.delete(*tree_ete_3rd_treeview.get_children())
                            for row in rows:
                                tree_ete_3rd_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ete_3rd_watch_video():
                    fetch_ete_3rd_watch_video()
                    self.ete_3rd_subjects_entry.set("")
                    self.ete_3rd_faculyt_entry.set('')
                    self.var_ete_3rd_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ete_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ete_3rd_watch_video where faculty=%s',(self.ete_3rd_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ete_3rd_watch_video where faculty=%s ',(self.ete_3rd_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ete_3rd_watch_video()
                                fetch_ete_3rd_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ete_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ete_3rd_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ete_3rd_subjects_entry.get(),
                               
                                self.var_ete_3rd_watch_video.get(),
                                self.ete_3rd_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ete_3rd_watch_video()
                            fetch_ete_3rd_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ete_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ete_3rd_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ete_3rd_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ete_3rd_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ete_3rd_subjects','ete_3rd_date','ete_3rd_time','ete_3rd_code','semisters','branch'
                                cur.execute('insert into ete_3rd_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ete_3rd_subjects_entry.get(),
                                self.ete_3rd_faculyt_entry.get(),
                                self.var_ete_3rd_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ete_3rd_watch_video()
                                con.close()
                def fetch_ete_3rd_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ete_3rd_watch_video')
                        rows=cur.fetchall()
                        tree_ete_3rd_treeview.delete(*tree_ete_3rd_treeview.get_children())
                        for row in rows:
                            tree_ete_3rd_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ete_3rd_watch_video(ev):
                    read=tree_ete_3rd_treeview.focus()
                    content=tree_ete_3rd_treeview.item(read)
                    row=content['values']
                    self.ete_3rd_subjects_entry.set(row[0])
                    self.ete_3rd_faculyt_entry.set(row[1])
                    self.var_ete_3rd_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ete_3rd_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ete_3rd_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ete_3rd_subjects_entry,values=ete_3rd_subjects_list)
                ete_3rd_subjects_entry.grid(row=0,column=1)

                ete_3rd_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ete_3rd_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ete_3rd_faculyt_entry,values=ete_3rd_faculty_list)
                ete_3rd_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ete_3rd_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ete_3rd_watch_video,width=44)
                ete_3rd_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ete_3rd_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ete_3rd_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ete_3rd_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ete_3rd_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ete_3rd_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ete_3rd_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ete_3rd_treeview.xview)
                scrolly.configure(command=tree_ete_3rd_treeview.yview)

                tree_ete_3rd_treeview.heading('subject_name',text="Subject Name")
                tree_ete_3rd_treeview.heading('faculty',text="Faculty")
                tree_ete_3rd_treeview.heading('you_tube_link',text="Watch")
                

                tree_ete_3rd_treeview.column('subject_name',width=200)
                tree_ete_3rd_treeview.column('faculty',width=100)
                tree_ete_3rd_treeview.column('you_tube_link',width=250)

                tree_ete_3rd_treeview['show']='headings'
                
                tree_ete_3rd_treeview.pack(fill=BOTH,expand=1)
                fetch_ete_3rd_watch_video()
                tree_ete_3rd_treeview.bind('<ButtonRelease-1>',get_ete_3rd_watch_video)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ete_4th_faculty_list=[]
                def ete_4th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ete_4th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ete_4th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ete_4th_watch_video where faculty=%s",(self.ete_4th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ete_4th_treeview.delete(*tree_ete_4th_treeview.get_children())
                            for row in rows:
                                tree_ete_4th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ete_4th_watch_video():
                    fetch_ete_4th_watch_video()
                    self.ete_4th_subjects_entry.set("")
                    self.ete_4th_faculyt_entry.set('')
                    self.var_ete_4th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ete_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ete_4th_watch_video where faculty=%s',(self.ete_4th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ete_4th_watch_video where faculty=%s ',(self.ete_4th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ete_4th_watch_video()
                                fetch_ete_4th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ete_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ete_4th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ete_4th_subjects_entry.get(),
                               
                                self.var_ete_4th_watch_video.get(),
                                self.ete_4th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ete_4th_watch_video()
                            fetch_ete_4th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ete_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ete_4th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ete_4th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ete_4th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ete_4th_subjects','ete_4th_date','ete_4th_time','ete_4th_code','semisters','branch'
                                cur.execute('insert into ete_4th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ete_4th_subjects_entry.get(),
                                self.ete_4th_faculyt_entry.get(),
                                self.var_ete_4th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ete_4th_watch_video()
                                con.close()
                def fetch_ete_4th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ete_4th_watch_video')
                        rows=cur.fetchall()
                        tree_ete_4th_treeview.delete(*tree_ete_4th_treeview.get_children())
                        for row in rows:
                            tree_ete_4th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ete_4th_watch_video(ev):
                    read=tree_ete_4th_treeview.focus()
                    content=tree_ete_4th_treeview.item(read)
                    row=content['values']
                    self.ete_4th_subjects_entry.set(row[0])
                    self.ete_4th_faculyt_entry.set(row[1])
                    self.var_ete_4th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ete_4th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ete_4th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ete_4th_subjects_entry,values=ete_4th_subjects_list)
                ete_4th_subjects_entry.grid(row=0,column=1)

                ete_4th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ete_4th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ete_4th_faculyt_entry,values=ete_4th_faculty_list)
                ete_4th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ete_4th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ete_4th_watch_video,width=44)
                ete_4th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ete_4th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ete_4th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ete_4th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ete_4th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ete_4th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ete_4th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ete_4th_treeview.xview)
                scrolly.configure(command=tree_ete_4th_treeview.yview)

                tree_ete_4th_treeview.heading('subject_name',text="Subject Name")
                tree_ete_4th_treeview.heading('faculty',text="Faculty")
                tree_ete_4th_treeview.heading('you_tube_link',text="Watch")
                

                tree_ete_4th_treeview.column('subject_name',width=200)
                tree_ete_4th_treeview.column('faculty',width=100)
                tree_ete_4th_treeview.column('you_tube_link',width=250)

                tree_ete_4th_treeview['show']='headings'
                
                tree_ete_4th_treeview.pack(fill=BOTH,expand=1)
                fetch_ete_4th_watch_video()
                tree_ete_4th_treeview.bind('<ButtonRelease-1>',get_ete_4th_watch_video)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ete_5th_faculty_list=[]
                def ete_5th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ete_5th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ete_5th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ete_5th_watch_video where faculty=%s",(self.ete_5th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ete_5th_treeview.delete(*tree_ete_5th_treeview.get_children())
                            for row in rows:
                                tree_ete_5th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ete_5th_watch_video():
                    fetch_ete_5th_watch_video()
                    self.ete_5th_subjects_entry.set("")
                    self.ete_5th_faculyt_entry.set('')
                    self.var_ete_5th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ete_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ete_5th_watch_video where faculty=%s',(self.ete_5th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ete_5th_watch_video where faculty=%s ',(self.ete_5th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ete_5th_watch_video()
                                fetch_ete_5th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ete_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ete_5th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ete_5th_subjects_entry.get(),
                               
                                self.var_ete_5th_watch_video.get(),
                                self.ete_5th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ete_5th_watch_video()
                            fetch_ete_5th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ete_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ete_5th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ete_5th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ete_5th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ete_5th_subjects','ete_5th_date','ete_5th_time','ete_5th_code','semisters','branch'
                                cur.execute('insert into ete_5th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ete_5th_subjects_entry.get(),
                                self.ete_5th_faculyt_entry.get(),
                                self.var_ete_5th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ete_5th_watch_video()
                                con.close()
                def fetch_ete_5th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ete_5th_watch_video')
                        rows=cur.fetchall()
                        tree_ete_5th_treeview.delete(*tree_ete_5th_treeview.get_children())
                        for row in rows:
                            tree_ete_5th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ete_5th_watch_video(ev):
                    read=tree_ete_5th_treeview.focus()
                    content=tree_ete_5th_treeview.item(read)
                    row=content['values']
                    self.ete_5th_subjects_entry.set(row[0])
                    self.ete_5th_faculyt_entry.set(row[1])
                    self.var_ete_5th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ete_5th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ete_5th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ete_5th_subjects_entry,values=ete_5th_subjects_list)
                ete_5th_subjects_entry.grid(row=0,column=1)

                ete_5th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ete_5th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ete_5th_faculyt_entry,values=ete_5th_faculty_list)
                ete_5th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ete_5th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ete_5th_watch_video,width=44)
                ete_5th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ete_5th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ete_5th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ete_5th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ete_5th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ete_5th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ete_5th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ete_5th_treeview.xview)
                scrolly.configure(command=tree_ete_5th_treeview.yview)

            
                tree_ete_5th_treeview.heading('subject_name',text="Subject Name")
                tree_ete_5th_treeview.heading('faculty',text="Faculty")
                tree_ete_5th_treeview.heading('you_tube_link',text="Watch")
                

                tree_ete_5th_treeview.column('subject_name',width=200)
                tree_ete_5th_treeview.column('faculty',width=100)
                tree_ete_5th_treeview.column('you_tube_link',width=250)

                tree_ete_5th_treeview['show']='headings'
                
                tree_ete_5th_treeview.pack(fill=BOTH,expand=1)
                fetch_ete_5th_watch_video()
                tree_ete_5th_treeview.bind('<ButtonRelease-1>',get_ete_5th_watch_video)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ete_6th_faculty_list=[]
                def ete_6th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ete_6th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ete_6th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ete_6th_watch_video where faculty=%s",(self.ete_6th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ete_6th_treeview.delete(*tree_ete_6th_treeview.get_children())
                            for row in rows:
                                tree_ete_6th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ete_6th_watch_video():
                    fetch_ete_6th_watch_video()
                    self.ete_6th_subjects_entry.set("")
                    self.ete_6th_faculyt_entry.set('')
                    self.var_ete_6th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ete_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ete_6th_watch_video where faculty=%s',(self.ete_6th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ete_6th_watch_video where faculty=%s ',(self.ete_6th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ete_6th_watch_video()
                                fetch_ete_6th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ete_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ete_6th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ete_6th_subjects_entry.get(),
                               
                                self.var_ete_6th_watch_video.get(),
                                self.ete_6th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ete_6th_watch_video()
                            fetch_ete_6th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ete_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ete_6th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ete_6th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ete_6th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ete_6th_subjects','ete_6th_date','ete_6th_time','ete_6th_code','semisters','branch'
                                cur.execute('insert into ete_6th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ete_6th_subjects_entry.get(),
                                self.ete_6th_faculyt_entry.get(),
                                self.var_ete_6th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ete_6th_watch_video()
                                con.close()
                def fetch_ete_6th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ete_6th_watch_video')
                        rows=cur.fetchall()
                        tree_ete_6th_treeview.delete(*tree_ete_6th_treeview.get_children())
                        for row in rows:
                            tree_ete_6th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ete_6th_watch_video(ev):
                    read=tree_ete_6th_treeview.focus()
                    content=tree_ete_6th_treeview.item(read)
                    row=content['values']
                    self.ete_6th_subjects_entry.set(row[0])
                    self.ete_6th_faculyt_entry.set(row[1])
                    self.var_ete_6th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ete_6th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ete_6th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ete_6th_subjects_entry,values=ete_6th_subjects_list)
                ete_6th_subjects_entry.grid(row=0,column=1)

                ete_6th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ete_6th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ete_6th_faculyt_entry,values=ete_6th_faculty_list)
                ete_6th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ete_6th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ete_6th_watch_video,width=44)
                ete_6th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ete_6th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ete_6th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ete_6th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ete_6th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ete_6th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ete_6th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ete_6th_treeview.xview)
                scrolly.configure(command=tree_ete_6th_treeview.yview)

               
                tree_ete_6th_treeview.heading('subject_name',text="Subject Name")
                tree_ete_6th_treeview.heading('faculty',text="Faculty")
                tree_ete_6th_treeview.heading('you_tube_link',text="Watch")
                

           
                tree_ete_6th_treeview.column('subject_name',width=200)
                tree_ete_6th_treeview.column('faculty',width=100)
                tree_ete_6th_treeview.column('you_tube_link',width=250)

                tree_ete_6th_treeview['show']='headings'
                
                tree_ete_6th_treeview.pack(fill=BOTH,expand=1)
                fetch_ete_6th_watch_video()
                tree_ete_6th_treeview.bind('<ButtonRelease-1>',get_ete_6th_watch_video)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ete_7th_faculty_list=[]
                def ete_7th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ete_7th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ete_7th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ete_7th_watch_video where faculty=%s",(self.ete_7th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ete_7th_treeview.delete(*tree_ete_7th_treeview.get_children())
                            for row in rows:
                                tree_ete_7th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ete_7th_watch_video():
                    fetch_ete_7th_watch_video()
                    self.ete_7th_subjects_entry.set("")
                    self.ete_7th_faculyt_entry.set('')
                    self.var_ete_7th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ete_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ete_7th_watch_video where faculty=%s',(self.ete_7th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ete_7th_watch_video where faculty=%s ',(self.ete_7th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ete_7th_watch_video()
                                fetch_ete_7th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ete_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ete_7th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ete_7th_subjects_entry.get(),
                               
                                self.var_ete_7th_watch_video.get(),
                                self.ete_7th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ete_7th_watch_video()
                            fetch_ete_7th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ete_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ete_7th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ete_7th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ete_7th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ete_7th_subjects','ete_7th_date','ete_7th_time','ete_7th_code','semisters','branch'
                                cur.execute('insert into ete_7th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ete_7th_subjects_entry.get(),
                                self.ete_7th_faculyt_entry.get(),
                                self.var_ete_7th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ete_7th_watch_video()
                                con.close()
                def fetch_ete_7th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ete_7th_watch_video')
                        rows=cur.fetchall()
                        tree_ete_7th_treeview.delete(*tree_ete_7th_treeview.get_children())
                        for row in rows:
                            tree_ete_7th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ete_7th_watch_video(ev):
                    read=tree_ete_7th_treeview.focus()
                    content=tree_ete_7th_treeview.item(read)
                    row=content['values']
                    self.ete_7th_subjects_entry.set(row[0])
                    self.ete_7th_faculyt_entry.set(row[1])
                    self.var_ete_7th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ete_7th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ete_7th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ete_7th_subjects_entry,values=ete_7th_subjects_list)
                ete_7th_subjects_entry.grid(row=0,column=1)

                ete_7th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ete_7th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ete_7th_faculyt_entry,values=ete_7th_faculty_list)
                ete_7th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ete_7th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ete_7th_watch_video,width=44)
                ete_7th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ete_7th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ete_7th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ete_7th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ete_7th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ete_7th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ete_7th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ete_7th_treeview.xview)
                scrolly.configure(command=tree_ete_7th_treeview.yview)

         
                tree_ete_7th_treeview.heading('subject_name',text="Subject Name")
                tree_ete_7th_treeview.heading('faculty',text="Faculty")
                tree_ete_7th_treeview.heading('you_tube_link',text="Watch")
                

                tree_ete_7th_treeview.column('subject_name',width=200)
                tree_ete_7th_treeview.column('faculty',width=100)
                tree_ete_7th_treeview.column('you_tube_link',width=250)

                tree_ete_7th_treeview['show']='headings'
                
                tree_ete_7th_treeview.pack(fill=BOTH,expand=1)
                fetch_ete_7th_watch_video()
                tree_ete_7th_treeview.bind('<ButtonRelease-1>',get_ete_7th_watch_video)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':

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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                ete_8th_faculty_list=[]
                def ete_8th_faculty_fetch():
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
                        cur.execute('select faculty_name from add_faculty1')
                        rows=cur.fetchall()
                        if len(rows)>0:
                            for row in rows:
                                ete_8th_faculty_list.append(row[0])
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                def var_serach_ete_8th_faculty():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name  must be required',parent=frame)
                        else:
                            cur.execute(f"select * from ete_8th_watch_video where faculty=%s",(self.ete_8th_faculyt_entry.get(),))
                            rows=cur.fetchall()
                            tree_ete_8th_treeview.delete(*tree_ete_8th_treeview.get_children())
                            for row in rows:
                                tree_ete_8th_treeview.insert('',END,values=row)
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def clear_ete_8th_watch_video():
                    fetch_ete_8th_watch_video()
                    self.ete_8th_subjects_entry.set("")
                    self.ete_8th_faculyt_entry.set('')
                    self.var_ete_8th_watch_video.set('') 
                    
                    messagebox.showinfo('Info','The data clear is succssfuly.....',parent=frame)

                def delete_ete_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('select * from ete_8th_watch_video where faculty=%s',(self.ete_8th_faculyt_entry.get(),))
                            row=cur.fetchone()
                            if row==None:
                                messagebox.showerror('Error','Select the faculty name from the table',parennt=frame)
                            else:
                                option=messagebox.askyesno('confirm','Do you wont to delet the data from the table.',parent=frame)
                                if option==True:
                                    cur.execute('delete from ete_8th_watch_video where faculty=%s ',(self.ete_8th_faculyt_entry.get(),))
                                con.commit()
                                messagebox.showinfo('Info','the data is deleted successflly....',parent=frame)
                                clear_ete_8th_watch_video()
                                fetch_ete_8th_watch_video()
                                con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def update_ete_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.ete_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be reuired',parent=frame)
                        else:
                            cur.execute('update ete_8th_watch_video set subject_name=%s,you_tube_link=%s where faculty=%s',(
                                self.ete_8th_subjects_entry.get(),
                               
                                self.var_ete_8th_watch_video.get(),
                                self.ete_8th_faculyt_entry.get(),
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data updated succssflly....',parent=frame)
                            clear_ete_8th_watch_video()
                            fetch_ete_8th_watch_video()
                            con.close()
                                    
                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)
                    
                def add_ete_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    if self.ete_8th_subjects_entry.get()=='':
                        messagebox.showerror('Error','The  subjects must be requered.',parent=frame)
                    else:
                        if self.ete_8th_faculyt_entry.get()=='':
                            messagebox.showerror('Error','The faculty name must be required',parent=frame)
                        else:
                            if self.var_ete_8th_watch_video.get()=='':
                                messagebox.showerror('Error','The you tube video link  must be required',parent=frame)
                            else:
                                   #'ete_8th_subjects','ete_8th_date','ete_8th_time','ete_8th_code','semisters','branch'
                                cur.execute('insert into ete_8th_watch_video(subject_name,faculty,you_tube_link) values(%s,%s,%s)',(
                                self.ete_8th_subjects_entry.get(),
                                self.ete_8th_faculyt_entry.get(),
                                self.var_ete_8th_watch_video.get()
                                ))
                                con.commit()
                                messagebox.showinfo('info','The data add succssfuly....',parent=frame)
                                fetch_ete_8th_watch_video()
                                con.close()
                def fetch_ete_8th_watch_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        cur.execute('select * from ete_8th_watch_video')
                        rows=cur.fetchall()
                        tree_ete_8th_treeview.delete(*tree_ete_8th_treeview.get_children())
                        for row in rows:
                            tree_ete_8th_treeview.insert('',END,values=row)

                    except Exception as ex:
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=frame)

                def get_ete_8th_watch_video(ev):
                    read=tree_ete_8th_treeview.focus()
                    content=tree_ete_8th_treeview.item(read)
                    row=content['values']
                    self.ete_8th_subjects_entry.set(row[0])
                    self.ete_8th_faculyt_entry.set(row[1])
                    self.var_ete_8th_watch_video.set(row[2])
                    messagebox.showinfo('Info','The data get is succssfuly.....',parent=frame)                    
                    
                    
                frame=Frame(self.root,bg='white')
                frame.place(x=0,y=100,width=1064,height=300)
                fetch_ete_8th_subjects()
                label_frame_entry=LabelFrame(frame,width=1039,height=40)
                label_frame_entry.place(x=10,y=0)
                
                label_subjects=Label(label_frame_entry,text='Subject Name:',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=0)
                ete_8th_subjects_entry=ttk.Combobox(label_frame_entry,width=45,textvariable=self.ete_8th_subjects_entry,values=ete_8th_subjects_list)
                ete_8th_subjects_entry.grid(row=0,column=1)

                ete_8th_faculty_fetch()
                label_faculty=Label(label_frame_entry,text='Faculty',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=2,padx=5)
                ete_8th_Faculty_entry=ttk.Combobox(label_frame_entry,width=30,textvariable=self.ete_8th_faculyt_entry,values=ete_8th_faculty_list)
                ete_8th_Faculty_entry.grid(row=0,column=3,padx=5)

                label_link=Label(label_frame_entry,text='Watch',font=('times new roman',13,'bold'),bg='white').grid(row=0,column=4,padx=5)
                ete_8th_watch_video_entry=ttk.Entry(label_frame_entry,textvariable=self.var_ete_8th_watch_video,width=44)
                ete_8th_watch_video_entry.grid(row=0,column=5,padx=5)


                label_frame2=LabelFrame(frame,bg='white')
                label_frame2.place(x=10,y=46,width=200,height=227)

                add_database_button=ttk.Button(label_frame2,text='Add database',width=31,command=add_ete_8th_watch_video).grid(row=0,column=0)
                update_button=ttk.Button(label_frame2,text='Update',width=31,command=update_ete_8th_watch_video).grid(row=1,column=0)
                delete_button=ttk.Button(label_frame2,text='Delete',width=31,command=delete_ete_8th_watch_video).grid(row=2,column=0)
                clear_button=ttk.Button(label_frame2,text='Clear',width=31,command=clear_ete_8th_watch_video).grid(row=3,column=0)
                subjects_label=Label(label_frame2,text='Serach Marks:',font=('times new roman',13,'bold'),bg='white').grid(row=4,column=0)
                serch_entry=ttk.Entry(label_frame2,width=31,textvariable=self.var_serach_ete_8th_faculty).grid(row=5,column=0)
                serach_button=ttk.Button(label_frame2,text='Serach',width=31).grid(row=6,column=0)

                label_frame3=LabelFrame(frame)
                label_frame3.place(x=220,y=46,width=801,height=227)

                tree_frame1=Frame(label_frame3)
                tree_frame1.pack(fill=BOTH,expand=1)

                scrollx=Scrollbar(tree_frame1,orient=HORIZONTAL)
                scrolly=Scrollbar(tree_frame1,orient=VERTICAL)

                tree_ete_8th_treeview=ttk.Treeview(tree_frame1,columns=('subject_name','faculty','you_tube_link'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)

                scrollx.configure(command=tree_ete_8th_treeview.xview)
                scrolly.configure(command=tree_ete_8th_treeview.yview)

            
                tree_ete_8th_treeview.heading('subject_name',text="Subject Name")
                tree_ete_8th_treeview.heading('faculty',text="Faculty")
                tree_ete_8th_treeview.heading('you_tube_link',text="Watch")
                

                tree_ete_8th_treeview.column('subject_name',width=200)
                tree_ete_8th_treeview.column('faculty',width=100)
                tree_ete_8th_treeview.column('you_tube_link',width=250)

                tree_ete_8th_treeview['show']='headings'
                
                tree_ete_8th_treeview.pack(fill=BOTH,expand=1)
                fetch_ete_8th_watch_video()
                tree_ete_8th_treeview.bind('<ButtonRelease-1>',get_ete_8th_watch_video)












if __name__=='__main__':
    root=tk.Tk()
    ob1=OnlineVideo(root)
    root.mainloop()