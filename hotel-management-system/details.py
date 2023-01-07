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


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #        =================== title ===========================
        lbl_title=Label(self.root,text="ROOM DETAILS",font=("arial",22,"bold"),bg="white",fg="orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        #        =================== logo ==========================
        img2=Image.open(r"D:\Desktop\hotel\Documents\image\hotel_logo.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)
        #         ================= label Frame ======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add", font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # Floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room No
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        self.var_roomname=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomname,width=20,font=("arial",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

         # room Type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=2,column=0,sticky=W)
        self.var_roomtype=StringVar()
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=18,state="readonly")
        combo_RoomType["value"]=("A","B","C")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=2,column=1)

        # Price
        lbl_price=Label(labelframeleft,text="Price",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_price.grid(row=3,column=0,sticky=W)
        self.var_price=StringVar()
        entry_price=ttk.Entry(labelframeleft,textvariable=self.var_price,width=20,font=("arial",13,"bold"))
        entry_price.grid(row=3,column=1,sticky=W)

        # max_customer
        lbl_max_customer=Label(labelframeleft,text="Max Customer",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_max_customer.grid(row=4,column=0,sticky=W)
        self.var_max_customer=StringVar()
        entry_max_customer=ttk.Entry(labelframeleft,textvariable=self.var_max_customer,width=20,font=("arial",13,"bold"))
        entry_max_customer.grid(row=4,column=1,sticky=W)

        # subtotal
        lbl_subtotal=Label(labelframeleft,text="Sub total(%)",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_subtotal.grid(row=5,column=0,sticky=W)
        self.var_subtotal=StringVar()
        entry_subtotal=ttk.Entry(labelframeleft,textvariable=self.var_subtotal,width=20,font=("arial",13,"bold"))
        entry_subtotal.grid(row=5,column=1,sticky=W)

        # coefficient
        lbl_coefficient=Label(labelframeleft,text="Coefficient",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_coefficient.grid(row=6,column=0,sticky=W)
        self.var_coefficient=StringVar()
        entry_coefficient=ttk.Entry(labelframeleft,textvariable=self.var_coefficient,width=20,font=("arial",13,"bold"))
        entry_coefficient.grid(row=6,column=1,sticky=W)

        # Status
        label_status=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_status.grid(row=7,column=0,sticky=W)
        self.var_status=StringVar()
        combo_status=ttk.Combobox(labelframeleft,textvariable=self.var_status,font=("arial",12,"bold"),width=18,state="readonly")
        combo_status["value"]=("Ready","Not Ready")
        combo_status.current(0)
        combo_status.grid(row=7,column=1)

        

        #         ====================== btns ===========================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=290,width=412,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,command=self.update,text="Update",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,command=self.mDelete,text="Delete",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #         ======================= table frame =====================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details", font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="orange",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=12,state="readonly")
        combo_Search["value"]=("roomname","roomtype")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",12,"bold"),width=18)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("arial",11,"bold"),bg="gray77",fg="black",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="gray77",fg="black",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)

         #         ======================= Show data table =====================
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=600,height=280)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,column=("floor","roomname","roomtype","price","max_customer","subtotal","coefficient","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomname",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("price",text="Price")
        self.room_table.heading("max_customer",text="Max Customer")
        self.room_table.heading("subtotal",text="Sub total(%)")
        self.room_table.heading("coefficient",text="Coefficient")
        self.room_table.heading("status",text="Status")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomname",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("price",width=100)
        self.room_table.column("max_customer",width=100)
        self.room_table.column("subtotal",width=100)
        self.room_table.column("coefficient",width=100)
        self.room_table.column("status",width=100)


        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomname.get()=="" or self.var_roomtype.get()=="" or self.var_price.get()=="" or self.var_max_customer.get()=="" or self.var_status.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomname.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_price.get(),
                                                                            self.var_max_customer.get(),
                                                                            self.var_subtotal.get(),
                                                                            self.var_coefficient.get(),
                                                                            self.var_status.get()
                ))
                                                

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "room has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,value=i)
            conn.commit()
        conn.close()

    #getcursor

    def get_cuersor(self,event=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]
        self.var_floor.set(row[0])
        self.var_roomname.set(row[1])
        self.var_roomtype.set(row[2])
        self.var_price.set(row[3])
        self.var_max_customer.set(row[4])
        self.var_subtotal.set(row[5])
        self.var_coefficient.set(row[6])
        self.var_status.set(row[7])

    # update
    def update(self):
        if self.var_floor.get()=="" or self.var_roomname.get()=="" or self.var_roomtype.get()=="" or self.var_price.get()=="" or self.var_max_customer.get()=="" or self.var_status.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
            my_cursor=conn.cursor()
            my_cursor.execute("update details set roomtype=%s, price=%s,max_customer=%s,subtotal=%s,coefficient=%s,status=%s where floor=%s and roomname=%s",(                                                                          
                                                                                self.var_roomtype.get(),
                                                                                self.var_price.get(),
                                                                                self.var_max_customer.get(),
                                                                                self.var_subtotal.get(),
                                                                                self.var_coefficient.get(),
                                                                                self.var_status.get(),
                                                                                self.var_floor.get(),
                                                                                self.var_roomname.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    # delete
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
            my_cursor=conn.cursor()
            query="delete from details where floor=%s and roomname=%s"
            value=(self.var_floor.get(),self.var_roomname.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # reset
    def reset(self):
        self.var_floor.set("")
        self.var_roomname.set("")
        #self.var_roomtype.set("")
        self.var_price.set("")
        self.var_max_customer.set("")
        #self.var_status.set("")

    def search(self):
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()

        my_cursor.execute("select * from details where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()







if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()