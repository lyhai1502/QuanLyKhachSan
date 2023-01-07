from tkinter import*
from PIL import Image, ImageTk
from customer import Cust_Win
from tkinter.font import Font
from room import Roombooking
from details import DetailsRoom

from report import ReportRoom
from connectdata import Connect

HOST = Connect().HOST
USERNAME = Connect().USERNAME
PASSWORD = Connect().PASSWORD
DATABASE = Connect().DATABASE


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #       =================== background ====================
        img1=Image.open(r"D:\Desktop\hotel\Documents\image\background_signin.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        #        =================== logo ==========================
        img2=Image.open(r"D:\Desktop\hotel\Documents\image\hotel_logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
        #        =================== title ===========================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Big Caslon",40,"bold"),bg="white",fg="orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #        =================== main frame ======================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #        =================== menu ============================
        lbl_menu=Label(main_frame,text="MENU",font=("Big Caslon",20,"bold"),bg="gray",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        #        =================== button frame ======================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=230,height=190)

        # customer button
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,anchor=CENTER,width=18,font=("Big Caslon",14,"bold"),bg="white",fg="black",activebackground="gray",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        # room button
        room_btn=Button(btn_frame,text="BOOKING",command=self.roombooking,anchor=CENTER,width=18,font=("Big Caslon",14,"bold"),bg="white",fg="black",activebackground="gray",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        # details button
        details_btn=Button(btn_frame,text="ROOM",command=self.details_room,anchor=CENTER,width=18,font=("Big Caslon",14,"bold"),bg="white",activebackground="gray",fg="black",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        # report button
        report_btn=Button(btn_frame,command=self.report,text="REPORT",anchor=CENTER,width=18,font=("Big Caslon",14,"bold"),bg="white",activebackground="gray",fg="black",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        # logout button
        logout_btn=Button(btn_frame,command=root.destroy,text="LOGOUT",anchor=CENTER,width=18,font=("Big Caslon",14,"bold"),bg="white",activebackground="gray",fg="black",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #        =================== right side image ==========================
        img3=Image.open(r"D:\Desktop\hotel\Documents\image\right_side.jpg")
        img3=img3.resize((1310,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=600)
        
        #        =================== image under menu ==========================
        img4=Image.open(r"D:\Desktop\hotel\Documents\image\under_menu.jpg")
        img4=img4.resize((225,400),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=225,height=400)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=ReportRoom(self.new_window)



        
        



if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()


