
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry('1280x704+0+0')
bg=ImageTk.PhotoImage(file='student_login_page_bg2.png')
bg1=ImageTk.PhotoImage(file='images/moon.png')
bg2=ImageTk.PhotoImage(file='images/mountains_behind.png')
bg3=ImageTk.PhotoImage(file='images/mountains_front.png')
frame=Frame(root,width=1280,height=704,bg='black')
frame.pack(side=TOP)

label=Label(frame,width=1284,height=704,image=bg,bg='black')
label.pack(fill=BOTH)







root.mainloop()


        
