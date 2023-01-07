from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.font import Font
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem
from register import Register
from connectdata import Connect

HOST = Connect().HOST
USERNAME = Connect().USERNAME
PASSWORD = Connect().PASSWORD
DATABASE = Connect().DATABASE

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
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

        login_str=Label(frame,text="LOGIN",font=("arial",20,"bold"),fg="white",bg="black")
        login_str.place(x=120,y=65)

        #label
        username=lbl=Label(frame,text="Username",font=("arial",12,"bold"),fg="white",bg="black")
        username.place(x=30,y=125)

        self.txtuser=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtuser.place(x=30,y=155,width=270)

        password=lbl=Label(frame,text="Password",font=("arial",12,"bold"),fg="white",bg="black")
        password.place(x=30,y=195)

        self.txtpass=ttk.Entry(frame,font=("arial",15,"bold"))
        self.txtpass.place(x=30,y=225,width=270)

        # Login Button
        btn_login=Button(frame,command=self.login,text="Login",borderwidth=3,relief=RAISED,font=("arial",12,"bold"),bg="white",fg="black", activebackground="gray")
        btn_login.place(x=110,y=290,width=120,height=35)
        # Register Button
        btn_register=Button(frame,command=self.register_window,text="Register",borderwidth=3,relief=RAISED,font=("arial",12,"bold"),bg="white",fg="black",activebackground="gray")
        btn_register.place(x=110,y=340,width=120,height=35)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        else:
            conn=mysql.connector.connect(host=HOST,username=USERNAME,password=PASSWORD,database=DATABASE)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from account where username=%s and password=%s",(
                                                        self.txtuser.get(),
                                                        self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("Login","Success")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()





main()
