from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.font import Font
import random
import time
import datetime
import mysql.connector
from connectdata import Connect

HOST = Connect().HOST
USERNAME = Connect().USERNAME
PASSWORD = Connect().PASSWORD
DATABASE = Connect().DATABASE

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        #       =================== background ====================
        img1=Image.open(r"D:\Desktop\hotel\Documents\image\background_signin.jpg")
        img1=img1.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1920,height=1080)

        #         ================= label Frame ======================
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=430)

        login_str=Label(frame,text="REGISTER",font=("arial",20,"bold"),fg="white",bg="black")
        login_str.place(x=100,y=65)

        #label
        username=lbl=Label(frame,text="Username",font=("arial",12,"bold"),fg="white",bg="black")
        username.place(x=30,y=125)

        self.txtuser=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtuser.place(x=30,y=155,width=270)

        password=lbl=Label(frame,text="Password",font=("arial",12,"bold"),fg="white",bg="black")
        password.place(x=30,y=195)

        self.txtpass=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtpass.place(x=30,y=225,width=270)

        btn_register=Button(frame,command=self.register,text="Register",borderwidth=3,relief=RAISED,font=("arial",12,"bold"),bg="white",fg="black",activebackground="gray")
        btn_register.place(x=110,y=270,width=120,height=35)

    def register(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        else:
            try:
                conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into account values(%s,%s)",(
                                                                            self.txtuser.get(),
                                                                            self.txtpass.get()
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "account has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()