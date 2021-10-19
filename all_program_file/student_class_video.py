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
import webbrowser
import psycopg2

class OnlineVideoWatch():
    def __init__(self,root):
        self.root=root
        self.root.title("Video class")
        self.root.geometry('1055x440+213+145')
        self.root.resizable(False,False)
        self.root.configure(bg='white')

        ################################################################

        self.var_student_branch_select=StringVar()
        self.var_student_semister_select=StringVar()
        self.var_select_subjects=StringVar()
        self.var_link_you_tube_video=StringVar()

        
#################################################################################

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
                def get_select_che_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from che_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_che_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=che_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        
        if self.var_student_semister_select.get()=="PHYSICS_cycle":
            if self.var_student_branch_select.get()=='2nd_semister':
                phy_subjects_list=[]
                def get_select_phy_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from phy_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_phy_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=phy_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':
                civil_3rd_subjects_list=[]
                def get_select_civil_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from civil_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_civil_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=civil_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':
                civil_4th_subjects_list=[]
                def get_select_civil_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from civil_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_civil_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=civil_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':
                civil_5th_subjects_list=[]
                def get_select_civil_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from civil_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_civil_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=civil_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':
                civil_6th_subjects_list=[]
                def get_select_civil_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from civil_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_civil_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=civil_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':
                civil_7th_subjects_list=[]
                def get_select_civil_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from civil_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_civil_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=civil_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Civil_Engineering':
                civil_8th_subjects_list=[]
                def get_select_civil_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from civil_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_civil_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=civil_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':
                mech_3rd_subjects_list=[]
                def get_select_mech_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from mech_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_mech_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=mech_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':
                mech_4th_subjects_list=[]
                def get_select_mech_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from mech_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_mech_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=mech_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':
                mech_5th_subjects_list=[]
                def get_select_mech_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from mech_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_mech_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=mech_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':
                mech_6th_subjects_list=[]
                def get_select_mech_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from mech_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_mech_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=mech_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':
                mech_7th_subjects_list=[]
                def get_select_mech_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from mech_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_mech_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=mech_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Mechanical_Engineering':
                mech_8th_subjects_list=[]
                def get_select_mech_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from mech_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_mech_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=mech_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)

        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':
                eee_3rd_subjects_list=[]
                def get_select_eee_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from eee_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_eee_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=eee_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':
                eee_4th_subjects_list=[]
                def get_select_eee_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from eee_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_eee_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=eee_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':
                eee_5th_subjects_list=[]
                def get_select_eee_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from eee_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_eee_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=eee_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':
                eee_6th_subjects_list=[]
                def get_select_eee_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from eee_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_eee_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=eee_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':
                eee_7th_subjects_list=[]
                def get_select_eee_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from eee_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_eee_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=eee_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Electrical_And_Electronic_Engineering':
                eee_8th_subjects_list=[]
                def get_select_eee_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from eee_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_eee_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=eee_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)

        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':
                ece_3rd_subjects_list=[]
                def get_select_ece_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ece_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ece_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ece_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':
                ece_4th_subjects_list=[]
                def get_select_ece_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ece_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ece_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ece_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':
                ece_5th_subjects_list=[]
                def get_select_ece_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ece_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ece_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ece_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':
                ece_6th_subjects_list=[]
                def get_select_ece_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ece_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ece_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ece_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':
                ece_7th_subjects_list=[]
                def get_select_ece_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ece_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ece_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ece_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Communication_Engineering':
                ece_8th_subjects_list=[]
                def get_select_ece_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ece_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ece_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ece_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':
                cs_3rd_subjects_list=[]
                def get_select_cs_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from cs_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_cs_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=cs_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':
                cs_4th_subjects_list=[]
                def get_select_cs_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from cs_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_cs_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=cs_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':
                cs_5th_subjects_list=[]
                def get_select_cs_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from cs_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_cs_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=cs_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':
                cs_6th_subjects_list=[]
                def get_select_cs_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from cs_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_cs_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=cs_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':
                cs_7th_subjects_list=[]
                def get_select_cs_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from cs_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_cs_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=cs_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Computer_Science_Engineering':
                cs_8th_subjects_list=[]
                def get_select_cs_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from cs_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_cs_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=cs_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':
                ise_3rd_subjects_list=[]
                def get_select_ise_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ise_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ise_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ise_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':
                ise_4th_subjects_list=[]
                def get_select_ise_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ise_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ise_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ise_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':
                ise_5th_subjects_list=[]
                def get_select_ise_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ise_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ise_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ise_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':
                ise_6th_subjects_list=[]
                def get_select_ise_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ise_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ise_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ise_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':
                ise_7th_subjects_list=[]
                def get_select_ise_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ise_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ise_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ise_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Information_Science_and_Engineering':
                ise_8th_subjects_list=[]
                def get_select_ise_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ise_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ise_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ise_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="3rd_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                ete_3rd_subjects_list=[]
                def get_select_ete_3rd_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ete_3rd_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ete_3rd_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ete_3rd_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="4th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                ete_4th_subjects_list=[]
                def get_select_ete_4th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ete_4th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ete_4th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ete_4th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="5th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                ete_5th_subjects_list=[]
                def get_select_ete_5th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ete_5th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ete_5th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ete_5th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="6th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                ete_6th_subjects_list=[]
                def get_select_ete_6th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ete_6th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ete_6th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ete_6th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="7th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                ete_7th_subjects_list=[]
                def get_select_ete_7th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ete_7th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ete_7th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ete_7th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
        if self.var_student_semister_select.get()=="8th_Semister":
            if self.var_student_branch_select.get()=='Electronic_And_Telecommunication_Engineering':
                ete_8th_subjects_list=[]
                def get_select_ete_8th_subjects():
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
                        messagebox.showerror('Error',f'The error due to {str(ex)}',parent=viedo_frame)
                
                def serach_youtube_video():
                    con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
                    cur=con.cursor()
                    try:
                        if self.var_select_subjects.get()=="":
                            messagebox.showerror('Error','The subjects must be required',parent=video_frame)
                        else:
                            cur.execute('select you_tube_link from ete_8th_watch_video where subject_name=%s',(self.var_select_subjects.get(),))
                            rows=cur.fetchone()
                            if len(rows)>0:
                                self.var_link_you_tube_video.set(rows[0])
                            con.commit()
                            messagebox.showinfo('Info','The link fetch successfluy..',parent=video_frame)
                            con.close()   
                    except Exception as ex:
                        messagebox.showerror('Error',f'the Error due to {str(ex)}',parent=video_frame)

                    #webbrowser.open_new_tab(url)
                def watch_youtube_video():
                    webbrowser.open_new_tab(self.var_link_you_tube_video.get())
                video_frame=Frame(self.root,bg='white')
                video_frame.place(x=0,y=100,width=1060,height=300)

                select_subject_label=Label(video_frame,text='Select Subjects:',font=('times new roman',19,'bold'),bg='white').place(x=100,y=30)
                get_select_ete_8th_subjects()
                select_subjects_entry=ttk.Combobox(video_frame,textvariable=self.var_select_subjects,values=ete_8th_subjects_list,width=50)
                select_subjects_entry.place(x=280,y=39)

                button_serch=ttk.Button(video_frame,text='Serach the link.',command=serach_youtube_video)
                button_serch.place(x=620,y=37,width=150)

                link_show_entry_box=ttk.Entry(video_frame,textvariable=self.var_link_you_tube_video,width=113,state='readonly')
                link_show_entry_box.place(x=100,y=90)

                button_watch=ttk.Button(video_frame,text='Watch video.',command=watch_youtube_video,width=100)
                button_watch.place(x=790,y=88,width=100)
if __name__=='__main__':
    root=tk.Tk()
    ob1=OnlineVideoWatch(root)
    root.mainloop()