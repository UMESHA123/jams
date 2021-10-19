import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#from attendence import Attendance
from add_student import AddStudent
from student_class_video import OnlineVideoWatch
from profile import StudentProfile
from show_stuudent_result import ShowStudentResult
import subprocess
class StudentMainPage():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Main Page")
        self.root.geometry('1280x658+0+0')
        self.root.config(bg='white')

        top_label=tk.Label(self.root,text='JAMS  - JNCE SHIVAMOGGA',font=('goudy old style',25,'bold'),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=50)
        
        menu_frame=tk.LabelFrame(self.root,text='Menu',font=('times now roman',15,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=213,y=50,width=1053,height=60)
        
        row_1_frame=Frame(self.root,bg='white')
        row_1_frame.place(x=218,y=73,width=1040,height=30)
        button1=ttk.Button(row_1_frame,text='Time Table',width=20).grid(row=0,column=0,padx=10)
        button2=ttk.Button(row_1_frame,text='Profile',width=20,command=self.StudentProfile).grid(row=0,column=1,padx=10)
        button3=ttk.Button(row_1_frame,text='Class Videos',width=20,command=self.OnlineVideoWatch).grid(row=0,column=2,padx=10)
        button4=ttk.Button(row_1_frame,text='Pyqt5',width=20,command=self.Ui_Form).grid(row=0,column=3,padx=10)
        button5=ttk.Button(row_1_frame,text='IA Schedule',width=20).grid(row=0,column=4,padx=10)
        button4=ttk.Button(row_1_frame,text='IA Marks',width=20).grid(row=0,column=5,padx=10)
        button5=ttk.Button(row_1_frame,text='Result',width=20,command=self.ShowStudentResult).grid(row=0,column=6,padx=10)

        self.tree_frame=Frame(self.root,width=210,height=530,bg='black',relief=GROOVE)
        self.tree_frame.place(x=4,y=57)
        
        self.treeview=ttk.Treeview(self.tree_frame,height=25)

        self.treeview.insert('', '1', 'item1',text ='Login')
        self.treeview.insert('', '2', 'item2',text ='Profile')
        self.treeview.insert('', '3', 'item3',text ='Academic')
        self.treeview.insert('', '4', 'item4',text ='Feedbacks')
        self.treeview.insert('', '5', 'item5',text ='Notice & Circulars')
        self.treeview.insert('', '6', 'item6',text ='University Results')
        self.treeview.insert('', '7', 'item7',text ='Exams')
        self.treeview.insert('','end','item8',text ='Electievs')

        ##ITEM 1
        self.treeview.insert('item1', 'end', 'Login',text ='Login') 
        self.treeview.insert('item1', 'end', 'Logout', text ='Logout')
        ##item2
        self.treeview.insert('item2', 'end', 'Personal', text ='Personal') 
        self.treeview.insert('item2', 'end', 'Vaccinations',text ='Vaccinations')
        ###item3
        self.treeview.insert('item3', 'end', 'Mentoring', text ='Mentoring')
        self.treeview.insert('item3', 'end', 'Time_Table', text ='Time Table')
        self.treeview.insert('item3', 'end', 'Attendance', text ='Attendance')
        
        self.treeview.insert('item3', 'end', 'Class_Videos', text ='Class Videos')
        self.treeview.insert('item3', 'end', 'Lesson_Plan', text ='Lesson Plane')
        self.treeview.insert('item3', 'end', 'IA_Schedule', text ='IA Schedule')
        self.treeview.insert('item3', 'end', 'IA_Marks', text ='IA Marks')
        self.treeview.insert('item3', 'end', 'Notes_Download', text ='Notes Download')
        ##item4
        self.treeview.insert('item4', 'end', 'Teaching_Learing', text ='Teaching Learing')
        self.treeview.insert('item4', 'end', 'Course_End_Survey', text ='Course End Survey')
        self.treeview.insert('item4', 'end', 'Program_Exit_Survey',text ='Program Exit Survey') 
        ##item5
        self.treeview.insert('item5', 'end', 'Department',text ='Department') 
        self.treeview.insert('item5', 'end', 'Collage', text ='Collage')
        self.treeview.insert('item5', 'end', 'Others',text ='Others') 
        ##item6
        self.treeview.insert('item6', 'end', 'Results',text ='Results') 
        #item7
        self.treeview.insert('item7', 'end', 'Exam_Registration',text ='Exam Registration') 
        #item8
        self.treeview.insert('item8', 'end', 'Elective_Management',text ='Elective Management') 

        #################################################################################################
        
        ##################################################################################################

        self.treeview.pack(fill=BOTH,expand=1)
        self.treeview.bind('<ButtonRelease>',self.get_data)

        bottom_label=tk.Label(self.root,bg="#0A0715",text="JAMS - JJNCE SHIVAMOGGA  \nfor any qution ar inproment and contect onformation\nare contect number is:934934xxxx3",font=('times new roman',10,'bold'),fg='white',bd=1,width=1230,height=4,relief='raised').place(relwidth=1,x=0,y=591)
    #def Attendance(self):
     #   self.attendance_windows=Toplevel(self.root)
      ##  self.ob1=Attendance(self.attendance_windows)


          ##background image 1
        self.img_bg1=Image.open('All_Program_Photos/bg1.jpg')
        self.img_bg1=self.img_bg1.resize((1150,550))
        self.img_bg1=ImageTk.PhotoImage(self.img_bg1)

        ##background image 2
        self.img_bg2=Image.open('All_Program_Photos/bg2.png')
        self.img_bg2=self.img_bg2.resize((1150,550))
        self.img_bg2=ImageTk.PhotoImage(self.img_bg2)

        ##background image 3
        self.img_bg3=Image.open('All_Program_Photos/bg3.png')
        self.img_bg3=self.img_bg3.resize((1150,550))
        self.img_bg3=ImageTk.PhotoImage(self.img_bg3)

        ##background image 4
        self.img_bg4=Image.open('All_Program_Photos/bg4.png')
        self.img_bg4=self.img_bg4.resize((1150,550))
        self.img_bg4=ImageTk.PhotoImage(self.img_bg4)

        ##background image 5
        self.img_bg5=Image.open('All_Program_Photos/bg5.png')
        self.img_bg5=self.img_bg5.resize((1150,550))
        self.img_bg5=ImageTk.PhotoImage(self.img_bg5)

        ##background image 6
        self.img_bg6=Image.open('All_Program_Photos/bg6.png')
        self.img_bg6=self.img_bg6.resize((1150,550))
        self.img_bg6=ImageTk.PhotoImage(self.img_bg6)

        ##background image 7
        self.img_bg7=Image.open('All_Program_Photos/bg7.png')
        self.img_bg7=self.img_bg7.resize((1150,550))
        self.img_bg7=ImageTk.PhotoImage(self.img_bg7)

        ##background image 8
        self.img_bg8=Image.open('All_Program_Photos/bg8.png')
        self.img_bg8=self.img_bg8.resize((1150,550))
        self.img_bg8=ImageTk.PhotoImage(self.img_bg8)

        ##background image 9
        self.img_bg9=Image.open('All_Program_Photos/bg9.png')
        self.img_bg9=self.img_bg9.resize((1150,550))
        self.img_bg9=ImageTk.PhotoImage(self.img_bg9)

        ##background image 10
        self.img_bg10=Image.open('All_Program_Photos/bg10.png')
        self.img_bg10=self.img_bg10.resize((1150,550))
        self.img_bg10=ImageTk.PhotoImage(self.img_bg10)

        ##background image 11
        self.img_bg11=Image.open('All_Program_Photos/bg11.png')
        self.img_bg11=self.img_bg11.resize((1150,550))
        self.img_bg11=ImageTk.PhotoImage(self.img_bg11)



        self.img_bg_label=Label(self.root,bg='red')
        self.img_bg_label.place(x=215,y=114,width=1055,height=470)
        self.animate()
    
    def animate(self):
        self.img=self.img_bg1
        self.img_bg1=self.img_bg2
        self.img_bg2=self.img_bg3
        self.img_bg3=self.img_bg4
        self.img_bg4=self.img_bg5
        self.img_bg5=self.img_bg6
        self.img_bg6=self.img_bg7
        self.img_bg7=self.img_bg8
        self.img_bg8=self.img_bg9
        self.img_bg9=self.img_bg10
        self.img_bg10=self.img_bg11
        self.img_bg11=self.img

        self.img_bg_label.config(image=self.img)

        self.img_bg_label.after(2000,self.animate)
    def OnlineVideoWatch(self):
        self.add_OnlineVideoWatch=Toplevel(self.root)
        self.ob1=OnlineVideoWatch(self.add_OnlineVideoWatch)
    def StudentProfile(self):
        self.add_Profile=Toplevel(self.root)
        self.ob1=StudentProfile(self.add_Profile)
    def ShowStudentResult(self):
        self.add_ShowStudentResult=Toplevel(self.root)
        self.ob1=ShowStudentResult(self.add_ShowStudentResult)
    def Ui_Form(self): #function before bind
        subprocess.Popen(['python' , 'ex1.py'])
    def get_data(self,ev):
        read=self.treeview.focus()

        if 'Class_Videos'==read:
            self.add_OnlineVideoWatch=Toplevel(self.root)
            self.ob1=OnlineVideoWatch(self.add_OnlineVideoWatch)

        if 'Personal'==read:
            self.add_Profile=Toplevel(self.root)
            self.ob1=StudentProfile(self.add_Profile)
        if 'Results'==read:
            self.add_ShowStudentResult=Toplevel(self.root)
            self.ob1=ShowStudentResult(self.add_ShowStudentResult)
    
    
        
if __name__=='__main__':
    root=tk.Tk()
    ob=StudentMainPage(root)
    root.mainloop()
        
        