import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#from attendence import Attendance
from add_student import AddStudent
from add_time_table import AddTimeTable
from add_subjects import AddSubjects
from student_IA import StudentIA
from IA_schedule import IAScheduleEntry
from online_video import OnlineVideo
from add_student_result import AddStudentResult
class Jams():
    def __init__(self,root):
        self.root=root
        self.root.title("Jams")
        self.root.geometry('1280x658+0+0')
        self.root.config(bg='white')



        top_label=tk.Label(self.root,text='JAMS  - JJNCE SHIVAMOGGA',font=('goudy old style',25,'bold'),fg='white',bg='#033054')
        top_label.place(x=0,y=0,relwidth=1,height=50)
        
        menu_frame=tk.LabelFrame(self.root,text='Menu',font=('times now roman',15,'bold'),fg='#262626',bg='white')
        menu_frame.place(x=215,y=50,width=1053,height=60)

        button1=ttk.Button(menu_frame,text='Add Student',width=20,command=self.AddStudent).grid(row=0,column=0,padx=10)
        button2=ttk.Button(menu_frame,text='Add Student Result ',width=20,command=self.AddStudentResult).grid(row=0,column=1,padx=10)
        button3=ttk.Button(menu_frame,text='Video calss',width=20,command=self.OnlineVideo).grid(row=0,column=2,padx=10)
        button4=ttk.Button(menu_frame,text='IA Schedule',width=20,command=self.IAScheduleEntry).grid(row=0,column=3,padx=10)
        button5=ttk.Button(menu_frame,text='Add Student IA',width=20,command=self.StudentIA).grid(row=0,column=4,padx=10)
        button4=ttk.Button(menu_frame,text='Add Subjects',width=20,command=self.AddSubjects).grid(row=0,column=5,padx=10)
        button5=ttk.Button(menu_frame,text='Add Time Table',width=20,command=self.AddTimeTable).grid(row=0,column=6,padx=10)

        self.tree_frame=Frame(self.root,width=210,height=530,bg='black',relief=GROOVE)
        self.tree_frame.place(x=4,y=57)
        
        self.treeview=ttk.Treeview(self.tree_frame,height=25)

        self.treeview.insert('', '1', 'item1',text ='Login')
        self.treeview.insert('', '2', 'item2',text ='Profile')
        self.treeview.insert('', '3', 'item3',text ='Academic')
        self.treeview.insert('', '4', 'item4',text ='Feedbacks')
        self.treeview.insert('', '5', 'item5',text ='Deparment')
        self.treeview.insert('', '6', 'item6',text ='Result')
        self.treeview.insert('', '7', 'item7',text ='Exam_Registration')
        self.treeview.insert('', 'end', 'item8',text ='Elective_Management')
        

        ##ITEM 1
        self.treeview.insert('item1', 'end', 'Logout', text ='Logout')
        ##item2
        self.treeview.insert('item2', 'end', 'Personal', text ='Personal') 
        self.treeview.insert('item2', 'end', 'Vaccinations',text ='Vaccinations')
        ###item3
        self.treeview.insert('item3', 'end', 'Add_Student',text='Add Student')
        self.treeview.insert('item3', 'end', 'Mentoring', text ='Mentoring')
        self.treeview.insert('item3', 'end', 'Time_Table', text ='Time Table')
        self.treeview.insert('item3', 'end', 'Attendance', text ='Attendance')
        
        self.treeview.insert('item3', 'end', 'Class_Videos', text ='Class Videos')
        self.treeview.insert('item3', 'end', 'Lesson_Plan', text ='Lesson Plane')
        self.treeview.insert('item3', 'end', 'IA_Schedule', text ='IA Schedule')
        self.treeview.insert('item3', 'end', 'IA_Marks', text ='IA Marks')
        self.treeview.insert('item3', 'end', 'Notes_Download', text ='Notes Download')
        self.treeview.insert('item3', 'end', 'Add_Subjects', text='Add Subjects')
        ##item4
        self.treeview.insert('item4', 'end', 'Teaching_Learing', text ='Teaching Learing')
        self.treeview.insert('item4', 'end', 'Course_End_Survey', text ='Course End Survey')
        self.treeview.insert('item4', 'end', 'Program_Exit_Survey',text ='Program Exit Survey') 
        ##item5
        self.treeview.insert('item5', 'end', 'Department',text ='Department') 
        self.treeview.insert('item5', 'end', 'Collage', text ='Collage')
        self.treeview.insert('item5', 'end', 'Others',text ='Others') 
        ##item6
        self.treeview.insert('item6', 'end', 'Result',text='Result')
        #item7
        self.treeview.insert('item7', 'end', 'Exam_Registration',text ='Exam Registration') 
        #item8
        self.treeview.insert('item8', 'end', 'Elective_Management',text ='Elective Management') 

        #################################################################################################
        
        ##################################################################################################

        self.treeview.pack(fill=BOTH,expand=1)
        self.treeview.bind('<ButtonRelease-1>',self.get)

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
    def AddStudent(self):
        self.add_student_window=Toplevel(self.root)
        self.ob1=AddStudent(self.add_student_window)
    def AddTimeTable(self):
        self.add_time_table_window=Toplevel(self.root)
        self.ob1=AddTimeTable(self.add_time_table_window)
    def AddSubjects(self):
        self.add_AddSubjects=Toplevel(self.root)
        self.ob1=AddSubjects(self.add_AddSubjects)
    def StudentIA(self):
        self.add_StudentIA=Toplevel(self.root)
        self.ob1=StudentIA(self.add_StudentIA)
    def IAScheduleEntry(self):
        self.add_IAScheduleEntry=Toplevel(self.root)
        self.ob1=IAScheduleEntry(self.add_IAScheduleEntry)
    def OnlineVideo(self):
        self.add_OnlineVideo=Toplevel(self.root)
        self.ob1=OnlineVideo(self.add_OnlineVideo)
    def AddStudentResult(self):
        self.add_AddStudentResult=Toplevel(self.root)
        self.ob1=AddStudentResult(self.add_AddStudentResult)
    def get(self,ev):
        read=self.treeview.focus()
        if 'IA_Schedule'==read:
            print('ia executed')
            self.add_IAScheduleEntry=Toplevel(self.root)
            self.ob1=IAScheduleEntry(self.add_IAScheduleEntry)
        if 'IA_Marks'==read:
            print('ia executed')
            self.add_StudentIA=Toplevel(self.root)
            self.ob1=StudentIA(self.add_StudentIA)
        if 'Time_Table'==read:
            print('ia executed')
            self.add_time_table_window=Toplevel(self.root)
            self.ob1=AddTimeTable(self.add_time_table_window)
        if 'Add_Student'==read:
            print('ia executed')
            self.add_student_window=Toplevel(self.root)
            self.ob1=AddStudent(self.add_student_window)
        if 'Add_Subjects'==read:
            self.add_AddSubjects=Toplevel(self.root)
            self.ob1=AddSubjects(self.add_AddSubjects)
        if 'Class_Videos'==read:
            self.add_OnlineVideo=Toplevel(self.root)
            self.ob1=OnlineVideo(self.add_OnlineVideo)
        if 'Result'==read:
            self.add_AddStudentResult=Toplevel(self.root)
            self.ob1=AddStudentResult(self.add_AddStudentResult)

         

if __name__=='__main__':
    root=tk.Tk()
    ob=Jams(root)
    root.mainloop()
        
        