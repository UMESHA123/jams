from tkinter import Tk
from tkinter import *
from time import sleep

class load():
    def __init__(self,root):
        self.root=root
        self.root.config(bg='black')
        self.root.title("loader")
        self.root.geometry('1000x600')

        Label(self.root,text='Loading..........',font='Bahnschrift 15',bg='black',fg='#ffbd09').place(x=490,y=320)

        for i in range(16):
            label=Label(self.root,bg='#1f2732',width=2,height=1).place(x=(i+22)*22,y=350)    
        self.root.update()
        self.play()

        

    def play(self):
        for i in range(200):
            for j in range(16):
                Label(self.root,bg='#ffbd09',width=2,height=1).place(x=(j+22)*22,y=350)
                sleep(1)
                self.root.update_idletasks()
                Label(self.root,bg='#1f2732',width=2,height=1).place(x=(j+22)*22,y=350)
        
        else:
            self.root.destroy()
            exit(0)
if __name__=='__main__':
    root=Tk()
    ob=load(root)
    root.mainloop()     
        