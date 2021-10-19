import sqlite3

def attendences_data_base():
    con=sqlite3.connect(database='Attendences.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS attendences(id INTEGER PRIMARY KEY AUTOINCREMENT,umesha text,gokul text,suhail text,sunil text,ramesh text,ram text,ramakur text,shivaraj text,shivakumar text,shivu text,kiran text,induther text,raj text)")

   # self.attendence_table=ttk.Treeview(self.attendence_frame,columns=('umesha','gokul','suhail','sunil','ramesh','ram','ramakur','shivaraj','shivakumar','shivu','kiran','indu','induther','raj'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


    con.commit()
attendences_data_base()