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


class AddStudent():
    def __init__(self,root):
        self.root=root
        self.root.title("Add Student")
        self.root.geometry('1055x440+213+145')
        self.root.resizable(False,False)
        self.root.configure(bg='white')

     

        ############################# variables
        #self.var_state=StringVar()
        self.var_serch_roll_number=StringVar()
        self.var_student_image_path=StringVar()
        self.var_roll_number=StringVar()
        self.var_student_name=StringVar()
        self.var_email=StringVar()
        self.var_state=StringVar()  
        self.var_distic=StringVar()
        self.var_gender=StringVar()
        self.var_date_of_birth=StringVar()
        self.var_contact_number=StringVar()
        self.var_cource=StringVar()
        self.var_addimision_date=StringVar()
        self.var_city=StringVar()
        self.var_pin_code=StringVar()
        self.var_color_chooser=StringVar()
        self.var_roll_number_from_database=StringVar()
        self.var_student_name_entry_from_database=StringVar()
        self.var_student_father_name=StringVar()
        self.var_student_mather_name=StringVar()
        self.var_father_mobile_number=StringVar()
        self.var_mather_mobile_number=StringVar()
        self.var_student_roll_number_from_database=StringVar()
        self.var_serch_student_personal_data=StringVar()
        self.var_student_semister=StringVar()
        ######################3###############
        top_label=tk.Label(self.root,text='Add Students',font=('Bahnschrift',20),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=40)

        menu_frame=tk.LabelFrame(self.root,text='Menu',font=('times now roman',10,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=10,y=45,width=1035,height=55)

        entry=ttk.Entry(menu_frame,width=50,textvariable=self.var_serch_roll_number).grid(row=0,column=0,padx=15,pady=3)

        button1=ttk.Button(menu_frame,text='Search',width=20,command=self.serch).grid(row=0,column=1,padx=4,pady=3)
        button2=ttk.Button(menu_frame,text='Show Database',width=20,command=self.add_student_details).grid(row=0,column=2,padx=4,pady=3)
        button3=ttk.Button(menu_frame,text='Update',width=20,command=self.update).grid(row=0,column=3,padx=4,pady=3)
        button4=ttk.Button(menu_frame,text='Delete',width=20,command=self.delete).grid(row=0,column=4,padx=4,pady=3)
        button4=ttk.Button(menu_frame,text='Clear',width=20,command=self.clear).grid(row=0,column=5,padx=4,pady=3)
        
        ######################student frame
        self.add_student_frame=Frame(self.root,width=1035,height=286,bg='black',relief=RIDGE)
        self.add_student_frame.place(x=10,y=110)

        button=ttk.Button(self.root,text='Show the data.',command=self.show)
        button.place(x=0,y=50)
        
        button1=ttk.Button(self.root,text='Show  data.',command=self.personal_data)
        button1.place(x=0,y=80)
        
        addStudentNoteBook=ttk.Notebook(self.add_student_frame)
        addStudentNoteBook.place(x=0,y=0)
        
        frame1=ttk.Frame(addStudentNoteBook,width=1035,height=260)
        frame3=ttk.Frame(addStudentNoteBook,width=1035,height=260)

        frame1.pack(fill='both')
        frame3.pack(fill='both')
    
        addStudentNoteBook.add(frame1,text='       Add Student          ')
        addStudentNoteBook.add(frame3,text='     Dara Base of Additional Details of Student   ')
        roll_no_label=tk.Label(frame1,text='Roll Number:',font=('times new roman',13,'bold')).place(x=10,y=10)
        roll_no_entry=ttk.Entry(frame1,width=33,textvariable=self.var_roll_number).place(x=125,y=12)
        student_name_label=tk.Label(frame1,text='Student Name:',font=('times new roman',13,'bold')).place(x=10,y=50)
        student_name_entry=ttk.Entry(frame1,width=33,textvariable=self.var_student_name).place(x=125,y=54)
        student_email_label=tk.Label(frame1,text="Student Email:",font=('times new roman',13,'bold')).place(x=10,y=90)
        student_email_entry=ttk.Entry(frame1,width=33,textvariable=self.var_email).place(x=125,y=94)
        select_state_label=tk.Label(frame1,text='Select State:',font=('times new roman',13,'bold')).place(x=10,y=130)
        select_state=ttk.Combobox(frame1,width=30,textvariable=self.var_state,state='readonly')
        select_state['values']=(
                            'Andhra Pradesh',
                            'Arunachal Pradesh',
                            'Assam',
                            'Bihar',
                            'Chhattisgarh',
                            'Goa',
                            'Gujarat',
                            'Haryana',
                            'Himachal Pradesh',
                            'Jharkhand',
                            'Karnataka',
                            'Kerala',
                            'Madhya Pradesh',
                            'Maharashtra',
                            'Manipur',
                            'Meghalaya',
                            'Mizoram',
                            'Nagaland',
                            'Odisha',
                            'Punjab',
                            'Rajasthan',
                            'Sikkim',
                            'Tamil Nadu',
                            'Telangana',
                            'Tripura',
                            'Uttar Pradesh',
                            'Uttarakhand',
                            'Uttarakhand'
                            
                               )
        select_state.place(x=125,y=134)

        select_distic_label=tk.Label(frame1,text='Select Distic:',font=('times new roman',13,'bold')).place(x=10,y=170)
        
        
        select_distic=ttk.Combobox(frame1,width=30,state='readonly',textvariable=self.var_distic)
        select_distic['values']=(
                                'Bagalkot',
                                'Bangalore urban',
                                'Bangalore Rural',
                                'Belgaum',
                                'Bellary',
                                'Bidar',
                                'Bijapur',
                                'Chamarajanagar',
                                'Chikballapur',
                                'Chikmaglur',
                                'Chitradurga',
                                'Dakshina Kannada',
                                'Davanagere',
                                'Dharwad',
                                'Gadag',
                                'Gulbarga',
                                'Hassan',
                                'Haveri',
                                'Kodagu',
                                'Kolar',
                                'Koppal',
                                'Mandya',
                                'Mysore',
                                'Raichur',
                                'Ramanagara',
                                'Shimoga',
                                'Tumkur',
                                'Udupi',
                                'Uttara kannada',
                                'Vijayanagara',
                                'Yadgir'
                                )
        select_distic.place(x=125,y=174)

        gender_lebal=tk.Label(frame1,text='Select Gender:',font=('times new roman',13,'bold')).place(x=10,y=210)
        select_gender=ttk.Combobox(frame1,width=30,state='readonly',textvariable=self.var_gender)
        select_gender['values']=(
                            'male',
                            'female',
                            'Not defined'
                             )
        select_gender.place(x=125,y=214)

        birth_label=tk.Label(frame1,text='Date of Birth       :',font=('times new roman',13,'bold')).place(x=360,y=12)

        select_birth_date=DateEntry(frame1,dateformat=3,width=30,foreground='white', borderwidth=1,Calendar =2021,textvariable=self.var_date_of_birth,state='readonly')
        select_birth_date.place(x=500,y=12)
        
        enter_contact_number_label=tk.Label(frame1,text='Contact Number:',font=('times new roman',13,'bold')).place(x=360,y=50)
        enter_contact_number=ttk.Entry(frame1,width=33,textvariable=self.var_contact_number).place(x=500,y=54)

        select_cource_label=tk.Label(frame1,text='Select Cource     :',font=('times new roman',13,'bold')).place(x=360,y=90)
        select_cource=ttk.Combobox(frame1,width=30,textvariable=self.var_cource)
        select_cource['values']=(
                                'Civil Engineering',
                                'Mechanical Engineering',
                                'Electrical And Electronic Engineering',
                                'Electronic And Communication Engineering',
                                'Computer Science Engineering',
                                'Information Science and Engineering',
                                'Electronic And Telecommunication Engineering',
                                'Master of Businees Administration',
                                'Master of Computer Application'


                                 )
        select_cource.place(x=500,y=94)

        addmision_date_label=tk.Label(frame1,text='Addmision Date :',font=('times new roman',13,'bold')).place(x=360,y=130)
        addmision_date=DateEntry(frame1,dataformat=3,width=30,bd=0,Calender=2021,textvariable=self.var_addimision_date,state='readonly')
        addmision_date.place(x=500,y=134)

        select_city_label=tk.Label(frame1,text='Select City          :',font=('times new roman',13,'bold')).place(x=360,y=170)
        select_city=ttk.Entry(frame1,width=33,textvariable=self.var_city)
        select_city.place(x=500,y=174)

        city_pin_code_label=tk.Label(frame1,text='City Pin Code   :',font=('times new roman',13,'bold')).place(x=360,y=210)
        city_pin_code=ttk.Entry(frame1,width=33,textvariable=self.var_pin_code)
        city_pin_code.place(x=500,y=214)
        select_semister=ttk.Combobox(frame1,width=30,textvariable=self.var_student_semister)
        select_semister.place(x=730,y=59)

        select_semister['values']=(
            '1st semister',
            '2nd semister',
            '3rd semister',
            '4th semister',
            '5th semister',
            '6th semister',
            '7th semister',
            '8th semister'
        )
        

        #select_image_label=tk.Label(frame1,text='Select Student Image:',font=('times new roman',13,'bold')).place(x=730,y=12)
        #select_image_button=ttk.Button(frame1,text='Select Image',width=20,command=select_student_image).place(x=900,y=12)

        
        #self.student_table.bind("<ButtonRelease-1>",self.get_data)
        #self.fetch_student_data_from_database()

        bottom_label=tk.Label(self.root,bg="#0A0715",text="JAMS - JJNCE SHIVAMOGGA  \nfor any qution ar inproment and contect onformation are contect number is:934934xxxx3",font=('times new roman',10,'bold'),fg='white',bd=1,width=1230,height=2,relief='raised').place(relwidth=1,x=0,y=407)
        serch_student_personal_data=ttk.Entry(self.root,width=28,textvariable=self.var_serch_student_personal_data)
        style=ttk.Style()
        style.map('Treeview',
                  background=[('selected','#347083')]
                  
                  )
        
        serch_student_personal_data.place(x=722,y=110)
        color_change_button=ttk.Button(self.root,text='Serach name.',width=20,command=self.serach_student)
        color_change_button.place(x=900,y=108)  

##################################################frame 3 starts
        self.roll_number_list=[]
        self.fetch_roll_numbber()
        roll_number_combobox=ttk.Combobox(frame3,width=30,textvariable=self.var_roll_number_from_database,values=self.roll_number_list,state='readonly')
        roll_number_combobox.place(x=15,y=15)

        fetch_button=ttk.Button(frame3,width=20,text='Fetch Data.',command=self.fetch_name)
        fetch_button.place(x=230,y=13)

        student_name_from_database=tk.Label(frame3,text='Student Name       :',font=('times new roman',13,'bold')).place(x=15,y=50)
        student_name_entry_from_database=ttk.Entry(frame3,width=33,textvariable=self.var_student_name_entry_from_database,state='readonly')
        student_name_entry_from_database.place(x=155,y=53)
        student_father_name=tk.Label(frame3,text='Father Name        :',font=('times new roman',13,'bold')).place(x=15,y=90)
        student_father_name_entry=ttk.Entry(frame3,width=33,textvariable=self.var_student_father_name)
        student_father_name_entry.place(x=155,y=93)
        student_mather_name=tk.Label(frame3,text='Mather Name       :',font=('times new roman',13,'bold')).place(x=15,y=130)
        student_mather_name_entry=ttk.Entry(frame3,width=33,textvariable=self.var_student_mather_name)
        student_mather_name_entry.place(x=155,y=133)
        father_mobile_number=tk.Label(frame3,text='Father Mobile No. :',font=('times new roman',12,'bold')).place(x=15,y=170)
        father_mobile_number_entry=ttk.Entry(frame3,width=33,textvariable=self.var_father_mobile_number)
        father_mobile_number_entry.place(x=155,y=173)
        mather_mobile_number=tk.Label(frame3,text='Mather Mobile No.:',font=('times new roman',12,'bold')).place(x=15,y=210)
        mather_mobile_number_entry=ttk.Entry(frame3,width=33,textvariable=self.var_mather_mobile_number)
        mather_mobile_number_entry.place(x=155,y=213)
        student_parmanet_address_label=tk.Label(frame3,text='Parmenat Address :',font=('times new roman',13,'bold')).place(x=380,y=15)
        #######
        self.text_frame=Frame(frame3,bd=0,relief=RIDGE)
        self.text_frame.place(x=380,y=50,width=300,height=80)
        #######
        scrolly=ttk.Scrollbar(self.text_frame,orient=VERTICAL)
        ##########
        self.student_parmanet_address_entry=Text(self.text_frame,width=20,height=20,yscrollcommand=scrolly.set,bg='lightyellow',bd=1,relief=GROOVE)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.student_parmanet_address_entry.yview)
        self.student_parmanet_address_entry.pack(fill=BOTH,expand=1)

        student_parmanet_contact_address_label=tk.Label(frame3,text='Contact Address :',font=('times new roman',13,'bold')).place(x=380,y=140)
        #########
        self.text_frame1=Frame(frame3,bd=0,relief=RIDGE)
        self.text_frame1.place(x=380,y=170,width=300,height=80)
        #######
        Cscrolly=ttk.Scrollbar(self.text_frame1,orient=VERTICAL)
        ##########
        self.student_contcat_address_entry=Text(self.text_frame1,width=20,height=20,yscrollcommand=Cscrolly.set,bg='lightyellow',bd=1,relief=GROOVE)
        Cscrolly.pack(side=RIGHT,fill=Y)
        Cscrolly.config(command=self.student_contcat_address_entry.yview)
        self.student_contcat_address_entry.pack(fill=BOTH,expand=1)

        frame3_framelabel=tk.LabelFrame(frame3,text='All Button Menu',font=('times new roman',10,'bold'),width=330,height=100,relief=RIDGE,bd=2)
        frame3_framelabel.place(x=700,y=150)

        frame3_frame=Frame(frame3,relief=RIDGE)
        frame3_frame.place(x=710,y=170,width=310,height=70)
        frame3_add_button=ttk.Button(frame3_frame,text='Add to Database',width=23,command=self.student_personal_details_add)
        frame3_add_button.grid(row=0,column=0,padx=5,pady=5)
        frame3_update_button=ttk.Button(frame3_frame,text='Update.',width=22,command=self.update_student_parsonal_data)
        frame3_update_button.grid(row=0,column=1,padx=7,pady=5)

        frame3_delete_button=ttk.Button(frame3_frame,text='Delete',width=23,command=self.delete_student_parsonal_data)
        frame3_delete_button.grid(row=1,column=0,padx=5,pady=5)
        frame3_clear_button=ttk.Button(frame3_frame,text='Clear.',width=22,command=self.clear_student_parsonal_data)
        frame3_clear_button.grid(row=1,column=1,padx=7,pady=5)
    def serach_student(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_serch_student_personal_data.get()=='':
                messagebox.showerror('Error','The student Roll Number must be required',parent=self.root)
            else:
                cur.execute(f"select * from student_personal_database where roll_number_personal=%s",(self.var_serch_student_personal_data.get(),))
                rows=cur.fetchall()
                self.student_personal_table.delete(*self.student_personal_table.get_children())
                for row in rows:
                    self.student_personal_table.insert('',END,values=row)
            
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=self.root)
        #self.fetch_student_personal_data()
    def student_personal_details_add(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        if self.var_roll_number_from_database.get()=='':
            messagebox.showinfo('Info','Student Roll Number must be select.',parent=self.root)
        else:
            if self.var_student_father_name.get()=='':
                messagebox.showinfo('Info','The student Father name must be required.',parent=self.root)
            else:
                if self.var_student_mather_name.get()=='':
                    messagebox.showinfo('Info','The student mather name must be required',parent=self.root)
                else:
                    if self.var_father_mobile_number.get()=='':
                        messagebox.showinfo('Info','The student Father mobile number must be required.',parent=self.root)
                    else:
                        if self.student_parmanet_address_entry.get('1.0',END)==None:
                            messagebox.showinfo('Info','The student Parmanet Address must be reqired',parent=self.root) 
                        else:
                            
                            cur.execute("insert into student_personal_database (roll_number_personal,student_name_personal,father_name,mather_name,father_mobile_number,mather_mobile_number,parmanet_address,contact_address) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_roll_number_from_database.get(),
                                self.var_student_name_entry_from_database.get(),
                                self.var_student_father_name.get(),
                                self.var_student_mather_name.get(),
                                self.var_father_mobile_number.get(),
                                self.var_mather_mobile_number.get(),
                                self.student_parmanet_address_entry.get('1.0',END),
                                self.student_contcat_address_entry.get('1.0',END),
                                
                            ))
                            con.commit()
                            messagebox.showinfo('Info','The data Add successefuly........',parent=self.root)
                            self.fetch_student_personal_data()
                            self.clear_student_parsonal_data()
                            con.close()
    
 
    def clear_student_parsonal_data(self):
        self.fetch_student_personal_data()
        self.var_roll_number_from_database.set("")
        self.var_student_name_entry_from_database.set('')
        self.var_student_father_name.set("")
        self.var_student_mather_name.set("")
        self.var_father_mobile_number.set("")
        self.var_mather_mobile_number.set("")
        self.student_parmanet_address_entry.delete('1.0',END)
        self.student_contcat_address_entry.delete('1.0',END)
        
        messagebox.showinfo('Info','The data clear successfuly.....',parent=self.root)
    def update_student_parsonal_data(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_student_name_entry_from_database.get()=='':
                messagebox.showinfo('Info','The student Roll Number must be required',parent=self.root)
            else:
                cur.execute('select * from student_personal_database where student_name_personal=%s',(self.var_student_name_entry_from_database.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Select the rollnumber from the student personal list',parent=self.root)
                else:
                    cur.execute('update student_personal_database set father_name=%s,mather_name=%s,father_mobile_number=%s,mather_mobile_number=%s,parmanet_address=%s,contact_address=%s,student_image=%s where student_name_personal=%s',(
                        self.var_student_father_name.get(),
                        self.var_student_mather_name.get(),
                        self.var_father_mobile_number.get(),
                        self.var_mather_mobile_number.get(),
                        self.student_parmanet_address_entry.get('1.0',END),
                        self.student_contcat_address_entry.get('1.0',END),
                        self.var_student_semister.get(),
                        self.var_student_name_entry_from_database.get()
                        
                    ))
                    con.commit()
                    messagebox.showinfo('Info','The data updated successfuly........',parent=self.root)
                    self.fetch_student_personal_data()
                    self.clear_student_parsonal_data()
        except Exception as ex:
            messagebox.showerror('Error',f'The error due to  {str(ex)}',parent=self.root)

   
    def delete_student_parsonal_data(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_student_name_entry_from_database.get()=="":
                messagebox.showerror('Error','Student name must be required',parent=self.root)
            else:
                cur.execute("select * from student_personal_database where student_name_personal=%s",(self.var_student_name_entry_from_database.get(),))
                row1=cur.fetchone()
                if row1==None:
                    messagebox.showerror('Error','select the roll number from the student table',parent=self.root)
                else:
                    option1=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                    if option1==True:
                        cur.execute('delete from student_personal_database where student_name_personal=%s',(self.var_student_name_entry_from_database.get(),))
                        con.commit()
                        messagebox.showinfo('Info','The student data deleted successfully.......',parent=self.root)
                        self.clear_student_parsonal_data()
                        self.fetch_student_personal_data()
        except Exception as ex:
            messagebox.showerror('Error',f"The error due to {str(ex)}",parent=self.root)
 ##################################3#############################frame3 end
    def fetch_name(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_roll_number_from_database.get()=='':
                messagebox.showinfo('Info','Student Roll Number must be required',parent=self.root)
            else:
                cur.execute('select student_name from StudentDetailsdatabase where roll_number=%s',(self.var_roll_number_from_database.get(),))
                row=cur.fetchone()
                self.var_student_name_entry_from_database.set(row[0])
                con.commit()
                con.close()
        except Exception as ex:
            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=self.root)
        


    def student_table_color_change(self):
        if self.var_color_chooser.get()=='Primary_Color':
            Primary_Color=colorchooser.askcolor(parent=self.root)[1]
            if Primary_Color:
                #self.student_table.tag_configure('oddrow',background='white')
                
                self.student_table.tag_configure('evenrow',background=Primary_Color)
        if self.var_color_chooser.get()=='Secondry Color':
            secondary_color=colorchooser.askcolor()[1]
            if primary_color:
                self.student_table.tag_configure('oddrow',background=secondary_color)
                #self.student_table.tag_configure('evenrow',background=secondary_color)
    
    def add_student_details(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_roll_number.get()=='':
                messagebox.showerror('Error','Student rollnnumber must be required',parent=self.root)
            else:
                if self.var_student_name.get()=="":
                    messagebox.showerror('Error','Student Name must be required',parent=self.root)
                else:
                    if self.var_state.get()=="":
                        messagebox.showerror('Error','Student state must be required',parent=self.root)
                    else:
                        if self.var_distic.get()=='':
                            messagebox.showerror('Error','Student distic must be required',parent=self.root)
                        else:
                            if self.var_gender.get()=='':
                                messagebox.showerror('Error','Student Gender must ne select',parent=self.root)
                            else:
                                if self.var_date_of_birth.get()=="":
                                    messagebox.showerror('Error','Student Date Of Brirth must be required',parent=self.root)
                                else:
                                    if self.var_contact_number.get()=='':
                                        messagebox.showerror('Error','Student Contact Number Must be required',parent=self.root)
                                    else:
                                        if self.var_cource.get()=='':
                                            messagebox.showerror('Error','Select the Cource from the list',parent=self.root)
                                        else:
                                            if self.var_addimision_date.get()=='':
                                                messagebox.showerror('Error','Enter the addimision date.',parent=self.root)
                                            else:
                                                if self.var_city.get()=='':
                                                    messagebox.showerror('Error','Enter the city',parent=self.root)
                                                else:
                                                    if self.var_pin_code.get()=='':
                                                        messagebox.showerror('Error','Enter the city pincode',parent=self.root)
                                                    else:
                                                        if self.var_student_semister.get()=='':
                                                            messagebox.showerror('Error','Select the student semsiter',parent=self.root)
                                                        else:
                                                            cur.execute("insert into StudentDetailsdatabase(roll_number,student_name,email,state1,distic,gender,date_of_birth,contact_number,cource,addimision_date,city,pin_code,student_image) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                                                                                self.var_roll_number.get(), 
                                                                                                                                                                                                                                self.var_student_name.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_state.get(),
                                                                                                                                                                                                                                self.var_distic.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_date_of_birth.get(),
                                                                                                                                                                                                                                self.var_contact_number.get(),
                                                                                                                                                                                                                                self.var_cource.get(),
                                                                                                                                                                                                                                self.var_addimision_date.get(),
                                                                                                                                                                                                                                self.var_city.get(),
                                                                                                                                                                                                                                self.var_pin_code.get(),
                                                                                                                                                                                                                                self.var_student_semister.get()
                                                                                                                                                                                                                                
                                                            )) 
                                                            

                                                            con.commit()
                                                            self.fetch_student_data_from_database() 
                                                            messagebox.showinfo('Info','The data added successfully..',parent=self.root)
                                                            con.close()
        except Exception as ex:
            messagebox.showerror('Error',f'The error due to {str(ex)}',parent=self.root)    
    
    def serch(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_serch_roll_number.get()=='':
                messagebox.showerror('Error','The student Roll Number must be required',parent=self.root)
            else:
                cur.execute(f"select * from StudentDetailsdatabase where roll_number LIKE '%{self.var_serch_roll_number.get()}%' ")
                rows=cur.fetchall()
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to {str(ex)}",parent=self.root)

    def update(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_roll_number.get()=="":
                messagebox.showerror('Error','Student Roll Number must be required%s',parent=self.root)
            else:
                cur.execute("select * from StudentDetailsdatabase where roll_number=%s",(self.var_roll_number.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select a Roll Number from the student table:",parent=self.root)
                else:
                    cur.execute("update StudentDetailsdatabase set student_name=%s,email=%s,state1=%s,distic=%s,gender=%s,date_of_birth=%s,contact_number=%s,cource=%s,addimision_date=%s,city=%s,pin_code=%s,student_image=%s where roll_number=%s",(
                                                                                                self.var_student_name.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_state.get(),
                                                                                                self.var_distic.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_date_of_birth.get(),
                                                                                                self.var_contact_number.get(),
                                                                                                self.var_cource.get(),
                                                                                                self.var_addimision_date.get(),
                                                                                                self.var_city.get(),
                                                                                                self.var_pin_code.get(),
                                                                                                self.var_student_semister.get(),
                                                                                                self.var_roll_number.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Student details is updated successfuly..........',parent=self.root)
                    self.fetch_student_data_from_database()
        except Exception as ex:
            messagebox.showerror('Error',f'error due to{str(ex)}',parent=self.root)
   
    def clear(self):
        self.fetch_student_data_from_database()
        self.var_roll_number.set("")
        self.var_student_name.set("")
        self.var_email.set("")
        self.var_state.set("")
        self.var_distic.set("")
        self.var_gender.set("")
        self.var_date_of_birth.set("")
        self.var_contact_number.set("")
        self.var_cource.set("")
        self.var_addimision_date.set("")
        self.var_city.set("")
        self.var_pin_code.set("")
        self.var_student_semister.set("")
        messagebox.showinfo('Info','All data are cleared but not deleted from the data base....',parent=self.root)

    def delete(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            if self.var_roll_number.get()=="":
                messagebox.showerror('Error','Student roll number must be required',parent=self.root)
            else:
                cur.execute("select * from StudentDetailsdatabase where roll_number=%s",(self.var_roll_number.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','select the roll number from the student table',parent=self.root)
                else:
                    option=messagebox.askyesno('confirm','do you want to delete the student detail from the database\nonece the data is deleted cannot be recovered...',parent=self.root)
                    if option==True:
                        cur.execute('delete from StudentDetailsdatabase where roll_number=%s',(self.var_roll_number.get(),))
                        con.commit()
                        messagebox.showinfo('Info','The student data deleted successfully.......',parent=self.root)
                        self.clear()
                        self.fetch_student_data_from_database()
        except Exception as ex:
            messagebox.showerror('Error',f"The error due to {str(ex)}",parent=self.root)
    def fetch_roll_numbber(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        cur.execute('select roll_number from StudentDetailsdatabase ')
        rows=cur.fetchall()
        if len(rows)>0:
            for row in rows:
                self.roll_number_list.append(row[0])
            con.commit()
            con.close()
    def personal_data(self):
        
        personal_toplevel=Toplevel(self.root)

        self.treeview_frame=Frame(personal_toplevel,bg='black')
        self.treeview_frame.pack(fill='both',expand=1)

        newscrollx=Scrollbar(self.treeview_frame,orient=HORIZONTAL)
        newscrolly=Scrollbar(self.treeview_frame,orient=VERTICAL)
        self.student_personal_table=ttk.Treeview(self.treeview_frame,columns=('roll_number_personal','student_name_personal','father_name','mather_name','father_mobile_number','mather_mobile_number','parmanet_address','contact_address'),xscrollcommand=newscrollx.set,yscrollcommand=newscrolly.set)
        
        newscrollx.pack(side=BOTTOM,fill=X)
        newscrolly.pack(side=RIGHT,fill=Y)

        newscrollx.config(command=self.student_personal_table.xview)
        newscrolly.config(command=self.student_personal_table.yview)

        self.student_personal_table.heading('roll_number_personal',text='Roll Number') 
        self.student_personal_table.heading('student_name_personal',text='Student Nmae')
        self.student_personal_table.heading('father_name',text='Father Name ')
        self.student_personal_table.heading('mather_name',text='Mather Name')
        self.student_personal_table.heading('father_mobile_number',text='Father Mobile Number')
        self.student_personal_table.heading('mather_mobile_number',text='Mather Mobile Number')
        self.student_personal_table.heading('parmanet_address',text='Pesonal Details')
        self.student_personal_table.heading('contact_address',text='Contact Details')

        self.student_personal_table.column('roll_number_personal',width=130) 
        self.student_personal_table.column('student_name_personal',width=180)
        self.student_personal_table.column('father_name',width=180)
        self.student_personal_table.column('mather_name',width=180)
        self.student_personal_table.column('father_mobile_number',width=140)
        self.student_personal_table.column('mather_mobile_number',width=140)
        self.student_personal_table.column('parmanet_address',width=200)
        self.student_personal_table.column('contact_address',width=200)
        self.student_personal_table['show']='headings'

        
        self.student_personal_table.pack(fill='both',expand=1)
        self.student_personal_table.bind('<ButtonRelease-1>',self.get_student_personal_data)
        self.fetch_student_personal_data()
    def fetch_student_personal_data(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        try:
            cur.execute('select * from student_personal_database')
            rows=cur.fetchall()
            self.student_personal_table.delete(*self.student_personal_table.get_children())
            for row in rows:
                self.student_personal_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',f"The error due to {str(ex)}",parent=self.root)
    def get_student_personal_data(self,ev):
        read=self.student_personal_table.focus()
        content=self.student_personal_table.item(read)
        row=content['values']
            #print(content)
        self.var_roll_number_from_database.set([row[0]])
        self.var_student_name_entry_from_database.set(row[1])
        self.var_student_father_name.set(row[2])
        self.var_student_mather_name.set(row[3])
        self.var_father_mobile_number.set(row[4])
        self.var_mather_mobile_number.set(row[5])
        self.student_parmanet_address_entry.delete('1.0',END)
        self.student_parmanet_address_entry.insert(END,row[6])
        self.student_contcat_address_entry.delete('1.0',END)
        self.student_contcat_address_entry.insert(END,row[7])
 
    def show(self):
        toplevel=Toplevel(self.root)
        toplevel.geometry('1280x658+0+0')
        frame=Frame(toplevel,bg='black')
        frame.pack(fill=BOTH,expand=1)

        dumy_image_label=tk.Label(frame,relief=GROOVE,width=42,height=10)
        dumy_image_label.pack(fill=BOTH,expand=1)


        self.student_table_frame=Frame(dumy_image_label,bd=2,relief=FLAT)
        self.student_table_frame.pack(fill=BOTH,expand=1)
        
        #####################scroll bar of x axis and y axis
        scrollx=Scrollbar(self.student_table_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(self.student_table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(self.student_table_frame,columns=('roll_number','student_name','email','state1','distic','gender','date_of_birth','contact_number','cource','addimision_date','city','pin_code','student_image'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)

        self.student_table.heading('roll_number',text='Roll Number')
        self.student_table.heading('student_name',text='Student Name')
        self.student_table.heading('email',text='Email')
        self.student_table.heading('state1',text='State')
        self.student_table.heading('distic',text='Distic')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('date_of_birth',text='Date Of Birth')
        self.student_table.heading('contact_number',text='Contact Number')
        self.student_table.heading('cource',text='Cource')
        self.student_table.heading('addimision_date',text='Addimision Number')
        self.student_table.heading('city',text='City')
        self.student_table.heading('pin_code',text='Pin Code')
        self.student_table.heading('student_image',text='Student Semsiter')

        self.student_table.column('roll_number',width=100)
        self.student_table.column('student_name',width=150)
        self.student_table.column('email',width=210)
        self.student_table.column('state1',width=150)
        self.student_table.column('distic',width=150)
        self.student_table.column('gender',width=80)
        self.student_table.column('date_of_birth',width=80)
        self.student_table.column('contact_number',width=100)
        self.student_table.column('cource',width=250)
        self.student_table.column('addimision_date',width=80)
        self.student_table.column('city',width=100)
        self.student_table.column('pin_code',width=100)
        self.student_table.column('student_image',width=300)

        self.student_table['show']='headings'

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_student_data_from_database()
        self.student_table.bind('<ButtonRelease-1>',self.get_data)
    
    def fetch_student_data_from_database(self):
        con=psycopg2.connect(
                    host="ec2-23-21-4-7.compute-1.amazonaws.com",
                    database="d3cgb3tsbur7dj",
                    user="huzavcwsvfccit",
                    password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",
                    port="5432",
                    )
        cur=con.cursor()
        cur.execute('select * from StudentDetailsdatabase')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
            con.close()

        
    def get_data(self,ev):
        r=self.student_table.focus()
        content=self.student_table.item(r)
        row=content["values"]
        
        self.var_roll_number.set(row[0])
        self.var_student_name.set(row[1])
        self.var_email.set(row[2])
        self.var_state.set(row[3])
        self.var_distic.set(row[4])
        self.var_gender.set(row[5])
        self.var_date_of_birth.set(row[6])
        self.var_contact_number.set(row[7])
        self.var_cource.set(row[8])
        self.var_addimision_date.set(row[9])
        self.var_city.set(row[10])
        self.var_pin_code.set(row[11])
        self.var_student_semister.set(row[12])
        messagebox.showinfo('Info','The all data fetch successfully goto the Add Student Menu ',parent=self.root)



if __name__=='__main__':
    root=tk.Tk()
    ob1=AddStudent(root)
    root.mainloop()