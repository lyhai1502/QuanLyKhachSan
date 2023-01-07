from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.font import Font
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from connectdata import Connect

HOST = Connect().HOST
USERNAME = Connect().USERNAME
PASSWORD = Connect().PASSWORD
DATABASE = Connect().DATABASE

class ReportRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #        =================== title ===========================
        lbl_title=Label(self.root,text="REPORT",font=("arial",22,"bold"),bg="white",fg="orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        #        =================== logo ==========================
        img2=Image.open(r"D:\Desktop\hotel\Documents\image\hotel_logo.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)
        #         ================= label Frame ======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Report", font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        btnreport1=Button(labelframeleft,command=self.revenue_by_room_type,text="Revenue by room type",font=("arial",11,"bold"),bg="gray77",fg="black",width=20)
        btnreport1.grid(row=0,column=0,padx=1)

        btnreport2=Button(labelframeleft,command=self.room_occupancy_density,text="Room occupancy density",font=("arial",11,"bold"),bg="gray77",fg="black",width=20)
        btnreport2.grid(row=1,column=0,padx=1,pady=10)


        #         ======================= table frame =====================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details", font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_Frame,column=("room","noofdays","revenue"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("room",text="Room")
        self.room_table.heading("noofdays",text="NoOfDays")
        self.room_table.heading("revenue",text="Revenue")

        self.room_table["show"]="headings"

        self.room_table.column("room",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.column("revenue",width=100)


        self.room_table.pack(fill=BOTH,expand=1)

    def revenue_by_room_type(self):
        self.room_table.heading("room",text="Room Type")
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()
        query=("select roomtype,sum(noofdays),sum(totalcost) from room group by roomtype")
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,value=i)
            conn.commit()
        conn.close()
        #SELECT roomtype,sum(noofdays),sum(totalcost)
        #FROM room
        #GROUP BY roomtype


    def room_occupancy_density(self):
        self.room_table.heading("room",text="Room")
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()
        query=("select Room,sum(noofdays),sum(totalcost) from room group by Room")
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,value=i)
            conn.commit()
        conn.close()   
        #SELECT roomname,sum(noofdays),sum(totalcost)
        #FROM room
        #GROUP BY roomname



if __name__ == "__main__":
    root=Tk()
    obj=ReportRoom(root)
    root.mainloop()