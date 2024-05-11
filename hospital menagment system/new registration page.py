from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



def main():
    win = Tk()
    app=login_window(win)
    win.mainloop()


class Register_user:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration page of Hospital Menagment System")
        self.root.geometry("1350x700+0+0")
######################veriable############
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_chack=IntVar()
    ######################veriable############
        #image
        self.bg =ImageTk.PhotoImage(file=r"E:\basic html code4\hospital menagment system\hospital img.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0)
        #left image#
        self.bg1 =ImageTk.PhotoImage(file=r"E:\basic html code4\hospital menagment system\astrazeneca.png")
        lft_bg = Label(self.root,image=self.bg1)
        lft_bg.place(x=300,y=100,width=470,height=550)

        # Frame
        Frame1 = Frame(self.root,bg="white")
        Frame1.place(x=770,y=100,width=470,height=550)
        #
        #register lable frame
        lf1 = LabelFrame(Frame1,font='arial 15 bold',bd=6,bg='white')
        lf1.place(x=8,y=5,width=460,height=540)
        #label
        reg_lbl = Label(Frame1,text="REGISTRATION HERE",font="impate 19 bold",fg="green",bg="white")
        reg_lbl.place(x=20,y=20)
        #label and name of user 
        #first name
        fname_lbl = Label(Frame1,text="First Name",font="impate 15 bold",fg="black",bg="white")
        fname_lbl.place(x=30,y=80)
        self.fname_entry = ttk.Entry(Frame1,textvariable=self.var_fname,font="impate 12 bold")
        self.fname_entry.place(x=30,y=110,width=170)
        #LAST NAME
        lname_lbl = Label(Frame1,text="Last Name",font="impate 15 bold",fg="black",bg="white")
        lname_lbl.place(x=250,y=80)
        self.lname_entry = ttk.Entry(Frame1,textvariable=self.var_lname,font="impate 12 bold")
        self.lname_entry.place(x=250,y=110,width=170)
        #contact no.
        contact_lbl = Label(Frame1,text="Contact No.",font="impate 15 bold",fg="black",bg="white")
        contact_lbl.place(x=30,y=150)
        # entery
        self.contact_entry = ttk.Entry(Frame1,textvariable=self.var_contact,font="impate 12 bold")
        self.contact_entry.place(x=30,y=180,width=170)
        # email
        email_lbl = Label(Frame1,text="Email",font="impate 15 bold",fg="black",bg="white")
        email_lbl.place(x=250,y=150)
        # entry.
        self.email_entry = ttk.Entry(Frame1,textvariable=self.var_email,font="impate 12 bold")
        self.email_entry.place(x=250,y=180,width=170)
        # select security quation.
        security_quation = Label(Frame1,text="Select Security Quation",font="impate 15 bold",fg="black",bg="white")
        security_quation.place(x=30,y=220)
        #select choice
        self.security_quation_combo = ttk.Combobox(Frame1,textvariable=self.var_securityQ,font="impate 12 bold",state="readonly")
        self.security_quation_combo["values"] = ("Select","Your Birth Place","Your Nick Name","Your Pet Name")
        self.security_quation_combo.place(x=30,y=250,width=240)
        self.security_quation_combo.current(0)
        #selct answer
        answer_lbl = Label(Frame1,text=" Security Answer",font="impate 15 bold",fg="black",bg="white")
        answer_lbl.place(x=30,y=280)
        # entry.
        self.answer_entry = ttk.Entry(Frame1,textvariable=self.var_securityA,font="impate 12 bold")
        self.answer_entry.place(x=30,y=310,width=240)
        #password
        password_lbl = Label(Frame1,text="Password",font="impate 15 bold",fg="black",bg="white")
        password_lbl.place(x=30,y=340)
        #entry
        self.password_entry = ttk.Entry(Frame1,textvariable=self.var_pass,font="impate 12 bold",show="*")
        self.password_entry.place(x=30,y=370,width=240)
        #confirm password
        confirm_password_lbl = Label(Frame1,text="Confirm Password",font="impate 15 bold",fg="black",bg="white")
        confirm_password_lbl.place(x=30,y=400)
        #entry
        self.confirm_password_entry = ttk.Entry(Frame1,textvariable=self.var_confpass,font="impate 12 bold")
        self.confirm_password_entry.place(x=30,y=430,width=240)
        # chack Button. 
        Checkbutton1 =Checkbutton(Frame1,variable=self.var_chack,text="I am agree the term & condition",font="impate 10 bold" ,bg="white",onvalue=1,offvalue=0)
        Checkbutton1.place(x=30,y=460)
        # register Button. 
        Button1 = Button(Frame1,text="Register",command=self.register_data,font="impate 15 bold",bg="red",fg="white")
        Button1.place(x=30,y=490,width=240)
        #login btn
        Button2 = Button(Frame1,text="Login",font="impate 15 bold",bg="red",fg="white")
        Button2.place(x=300,y=490,width=150)

        # creat image button .
        # Img1 =Image.open(r"E:\basic html code4\hospital menagment system\images (2).jpg")
        # Img1 = Img1.resize((100,50),Image.ANTIALIZE)
        # self.photoimg1 = ImageTk.PhotoImage(Img1)
        # b1 = Button(Frame1,image=self.photoimg1,cursor="hand2",borderwidth=0)
        # b1.place(x=30,y=490,width=240,height=50)
################function###################
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
           messagebox.showerror("Error","plz fill all entry")
        elif self.var_pass.get()!=self.var_confpass.get():
           messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_chack.get()==0:
            messagebox.showerror("Error","plz agree our term and condition")
        else:
            con =mysql.connector.connect(host="localhost",user="root",password="4011",database="mydata")
            cur =con.cursor()
            Query("select * from reg1 where email=%s")
            value=(self.var_email.get(),)
            cur.execute(Query,value)
            row = cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","user alredy valid,plz try another email")
            else:
                cur.execute("insert into reg1 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                              self.var_fname.get(),
                                                                              self.var_lname.get(),
                                                                              self.var_contact.get(),
                                                                              self.var_email.get(),
                                                                              self.var_securityQ.get(),
                                                                              self.var_securityA.get(),
                                                                              self.var_pass.get()
                                                                             ))
            con.commit()
            con.close()
            messagebox.showinfo("success","Register Successfully")    

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login page of Hospital Menagment System")
        self.root.geometry("1350x700+0+0")
        ###image using some background####
        self.bg =ImageTk.PhotoImage(file=r"E:\basic html code4\hospital menagment system\hospital img.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0)
#########frame#####
        Frame1 = Frame(self.root,bg="black")
        Frame1.place(x=610,y=170,width=340,height=450)
# imgae in logo.
        img1 = Image.open(r"E:\basic html code4\hospital menagment system\images.png")
        img1=img1.resize((100,70)) #using antilias to hard level image to convert low level image.
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)
# get started.
        get_str = Label(Frame1,text="Get started",font="arial 20 bold",fg='white',bg='black')
        get_str.place(x=95,y=100)
# user name.
        username_lbl = Label(Frame1,text="User-Name",font="arial 15 bold",bg="black",fg="white")
        username_lbl.place(x=70,y=155)
# user entey filld.
        self.e1 = Entry(Frame1,font="arial 15 bold",bg="white",fg="black")
        self.e1.place(x=40,y=180,width=270)
# password.
        password_lbl = Label(Frame1,text="Password",font="arial 15 bold",bg="black",fg="white")
        password_lbl.place(x=75,y=225)
# user entey filld.
        self.e2 = Entry(Frame1,font="arial 15 bold",bg="white",fg="black" ,show="*")
        self.e2.place(x=40,y=250,width=270)

###########icon images user and password interface##########
#user email
        img2 = Image.open(r"E:\basic html code4\hospital menagment system\images.png")
        img2=img2.resize((50,50)) #using antilias to hard level image to convert low level image.
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=310,width=25,height=35)
#password
        img3 = Image.open(r"E:\basic html code4\hospital menagment system\pngtree-vector-key-icon-png-image_1028662.jpg")
        img3=img3.resize((50,50)) #using antilias to hard level image to convert low level image.
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=380,width=35,height=35)
        
########################################################
# login btn.
        btn_button = Button(Frame1,command=self.login,text="LOGIN",font="arial 15 bold",bg="red",fg="white",bd=3,relief=RIDGE,activeforeground="white",activebackground="red")
        btn_button.place(x=110,y=300,width=120,height=35)  
#registration btn
        reg_button = Button(Frame1,text="New User Register",command=self.ref_window,font="arial 11 bold underline",bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
        reg_button.place(x=20,y=350,width=160) 
#forget btn
        fog_button2 = Button(Frame1,text="Forget Password",font="arial 11 bold underline",bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
        fog_button2.place(x=12,y=375,width=160) 

# connect the login file and registration file .
    def ref_window(self):
       self.New_window=Toplevel(self.root)
       self.app=Register_user( self.New_window )
    
#creat login funtion #                
    def login(self):
        if self.e1.get()=="" or self.e2.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.e1.get()=="kapu" and  self.e2.get()=="ashu":
            messagebox.showinfo("Success","Welcome to hospital managment system")
        else:
            con =mysql.connector.connect(host="localhost",user="root",password="4011",database="mydata")
            cur =con.cursor()   
            cur.execute("select * from reg1 where email=%s and password=%s",(self.var_emial.get(),self.var_pass.get()))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("error","invalid user name and password")
            else:
                open_main=messagebox.askyesno("yesno","Access only admin")
                if open_main>0:
                    self.New_window=Toplevel(self.New_window)
                    self.app=Register_user( self.New_window )
                else:
                    if not open_main:
                        return    
            con.commit()
            con.close()



        




if __name__=="__main__":
   main()