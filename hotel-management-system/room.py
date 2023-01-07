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



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #        =================== variable ===========================
        self.var_mobile=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_totalcustomer=StringVar()
        self.var_isexistforeigner=StringVar()
        self.var_noofdays=StringVar()
        self.var_subtotal=StringVar()
        self.var_coefficient=StringVar()
        self.var_totalcost=StringVar()

        #        =================== title ===========================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("arial",22,"bold"),bg="white",fg="orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        #        =================== logo ==========================
        img2=Image.open(r"D:\Desktop\hotel\Documents\image\hotel_logo.jpg")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)
        #         ================= label Frame ======================
        self.labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details", font=("arial",12,"bold"),padx=2)
        self.labelframeleft.place(x=5,y=50,width=425,height=490)
        #         ================= labels and entry ======================
        # Customer mobile
        lbl_cust_mobile=Label(self.labelframeleft,text="Customer Mobile",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mobile.grid(row=0,column=0,sticky=W)

        entry_mobile=ttk.Entry(self.labelframeleft,textvariable=self.var_mobile,width=20,font=("arial",13,"bold"))
        entry_mobile.grid(row=0,column=1,sticky=W)

        #Fetch data button
        btnFetchData=Button(self.labelframeleft,command=self.Fetch_mobile,text="Fetch Data",font=("arial",8,"bold"),bg="gray77",fg="black",width=10)
        btnFetchData.place(x=340,y=4)
        
        # Check_in
        check_in_date=Label(self.labelframeleft,font=("arial",12,"bold"),text="Check in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(self.labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        # Check_out
        check_out_date=Label(self.labelframeleft,font=("arial",12,"bold"),text="Check out Date:",padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(self.labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        # room Type
        label_RoomType=Label(self.labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()
        my_cursor.execute("select distinct roomtype from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(self.labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Room
        #lblRoomAvailable=Button(self.labelframeleft,command=self.available_room,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        #lblRoomAvailable.grid(row=4,column=0,sticky=W)

        btnRoomAvailable=Button(self.labelframeleft,command=self.available_room,text="Available Room",font=("arial",11,"bold"),bg="gray77",fg="black",width=15)
        btnRoomAvailable.grid(row=4,column=0,padx=1,sticky=W)

        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)

        

        # Total Customer
        lblTotalCustomer=Label(self.labelframeleft,font=("arial",12,"bold"),text="Total Customer:",padx=2,pady=6)
        lblTotalCustomer.grid(row=5,column=0,sticky=W)

        txtTotalCustomer=ttk.Entry(self.labelframeleft,textvariable=self.var_totalcustomer,width=29,font=("arial",13,"bold"))
        txtTotalCustomer.grid(row=5,column=1)

        # is exist foreigner
        lblIsExistForeigner=Label(self.labelframeleft,font=("arial",12,"bold"),text="Is Exists Foreigner:",padx=2,pady=6)
        lblIsExistForeigner.grid(row=6,column=0,sticky=W)

        combo_IsExistForeigner=ttk.Combobox(self.labelframeleft,textvariable=self.var_isexistforeigner,font=("arial",12,"bold"),width=27,state="readonly")
        combo_IsExistForeigner["value"]=("NO","YES")
        combo_IsExistForeigner.current(0)
        combo_IsExistForeigner.grid(row=6,column=1)

        # No of Days
        lblNoOfDays=Label(self.labelframeleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(self.labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=7,column=1)

        # Sub Total
        lblSubTotal=Label(self.labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)

        txtSubTotal=ttk.Entry(self.labelframeleft,textvariable=self.var_subtotal,width=29,font=("arial",13,"bold"))
        txtSubTotal.grid(row=8,column=1)

        # Coefficient
        lblCoefficient=Label(self.labelframeleft,font=("arial",12,"bold"),text="Coefficient:",padx=2,pady=6)
        lblCoefficient.grid(row=9,column=0,sticky=W)

        txtCoefficient=ttk.Entry(self.labelframeleft,textvariable=self.var_coefficient,width=29,font=("arial",13,"bold"))
        txtCoefficient.grid(row=9,column=1)

        # Total Cost
        lblTotalCost=Label(self.labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblTotalCost.grid(row=10,column=0,sticky=W)

        txtTotalCost=ttk.Entry(self.labelframeleft,textvariable=self.var_totalcost,width=29,font=("arial",13,"bold"))
        txtTotalCost.grid(row=10,column=1)

        #        ====================== Bill button =====================
        btnBill=Button(self.labelframeleft,command=self.total,text="Bill",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnBill.grid(row=11,column=0,padx=1,sticky=W)

        #         ====================== btns ===========================
        btn_frame=Frame(self.labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=425,width=412,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,command=self.update,text="Update",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,command=self.mDelete,text="Delete",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnReset.grid(row=0,column=3,padx=1)


        #         ======================= table frame =====================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System", font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="orange",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",12,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="gray77",fg="black",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #         ======================= Show data table =====================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,column=("mobile","checkin","checkout","roomtype","Room","totalcustomer","isexistsForeigner","noOfdays","totalCost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("mobile",text="Mobile")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("Room",text="Room No")
        self.room_table.heading("totalcustomer",text="Total Customer")
        self.room_table.heading("isexistsForeigner",text="Foreigner")
        self.room_table.heading("noOfdays",text="NoOfDays")
        self.room_table.heading("totalCost",text="Total Cost")

        self.room_table["show"]="headings"

        self.room_table.column("mobile",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("Room",width=100)
        self.room_table.column("totalcustomer",width=100)
        self.room_table.column("isexistsForeigner",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.column("totalCost",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    #add data
    def add_data(self):
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()
        query=("select max_customer from details where roomname=%s")
        value=(self.var_roomavailable.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        max_cus=row[0]


        if self.var_mobile.get()=="" or self.var_checkin.get()=="" or self.var_checkout.get()=="" or self.var_roomtype.get()=="" or self.var_roomavailable.get()=="" or self.var_totalcustomer.get()=="" or self.var_isexistforeigner.get()=="" or self.var_noofdays.get()=="" or self.var_totalcost.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif float(self.var_totalcustomer.get()) > float(max_cus):
            messagebox.showerror("Error",f"max customer in "+str(self.var_roomavailable.get())+": "+str(max_cus),parent=self.root)
        else:
            try:
                
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_mobile.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_totalcustomer.get(),
                                                                            self.var_isexistforeigner.get(),
                                                                            self.var_noofdays.get(),
                                                                            self.var_totalcost.get()
                ))

                my_cursor.execute("update details set status=%s where roomname=%s",(
                                                            "Not Ready",
                                                            self.var_roomavailable.get()
                ))
                                                

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


#available room
    def available_room(self):
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()

        
        query="select roomname from details where roomtype=%s and status=%s"
        value=(self.var_roomtype.get(),"Ready",)
        my_cursor.execute(query,value)
        rows=my_cursor.fetchall()

        combo_RoomName=ttk.Combobox(self.labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomName["value"]=rows
        combo_RoomName.current(0)
        combo_RoomName.grid(row=4,column=1)


# fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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
        self.var_mobile.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_totalcustomer.set(row[5])
        self.var_isexistforeigner.set(row[6])
        self.var_noofdays.set(row[7])
        #self.var_totalcost.set(row[11])

    # update
    def update(self):
        if self.var_mobile.get()=="" or self.var_checkin.get()=="" or self.var_checkout.get()=="" or self.var_roomtype.get()=="" or self.var_roomavailable.get()=="" or self.var_totalcustomer.get()=="" or self.var_isexistforeigner.get()=="" or self.var_noofdays.get()=="" or self.var_totalcost.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s, check_out=%s,roomtype=%s,Room=%s,totalcustomer=%s,foreigner=%s,noofdays=%s,totalcost=%s where Mobile=%s",(                                                                          
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_roomavailable.get(),
                                                                                self.var_totalcustomer.get(),
                                                                                self.var_isexistforeigner.get(),
                                                                                self.var_noofdays.get(),
                                                                                self.var_totalcost.get(),
                                                                                self.var_mobile.get()
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
            query="delete from room where Mobile=%s"
            value=(self.var_mobile.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # reset
    def reset(self):
        self.var_mobile.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        #self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_totalcustomer.set("")
        #self.var_isexistforeigner.set("")
        self.var_noofdays.set("")
        self.var_subtotal.set("")
        self.var_coefficient.set("")
        self.var_totalcost.set("")
#        ===========================ALL data fetch ======================
    def Fetch_mobile(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
            my_cursor=conn.cursor()
            query=("select HotenKH from customer where Mobile=%s")
            value=(self.var_mobile.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                # Name
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455,y=55,width=600,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                # Gender
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                query=("select GioiTinh from customer where Mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                # Email
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

                # Nationality
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                query=("select QuocTich from customer where Mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

                # ID Proof
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                query=("select LoaiThe from customer where Mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=0,y=120)

                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                query=("select SoThe from customer where Mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)

                # Address
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                query=("select DiaChi from customer where Mobile=%s")
                value=(self.var_mobile.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=150)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=150)

    # search
    def search(self):
        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # total 

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
        my_cursor=conn.cursor()

        my_cursor.execute("select * from details where "+str(self.var_roomavailable.get())+" LIKE '%"+str(self.var_roomavailable.get())+"%'")
        rows=my_cursor.fetchone()

        roomcost = rows[3]
        subtotal = rows[5]
        coefficient = rows[6]

        if(self.var_isexistforeigner.get()=="YES"):
            self.var_coefficient.set(coefficient)  
        else:
            self.var_coefficient.set(1)
        if(float(self.var_totalcustomer.get())==3):
            self.var_subtotal.set(float(self.var_noofdays.get())*roomcost*subtotal/100)
        else:
            self.var_subtotal.set(0)          

        self.var_totalcost.set(((float(self.var_noofdays.get())*roomcost)+float(self.var_subtotal.get()))*float(self.var_coefficient.get()))






if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()