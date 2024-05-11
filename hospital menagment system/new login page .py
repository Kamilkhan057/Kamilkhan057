###################HOSPITAL MENAGMENT SYSTEM CREAT FOR LOGIN PAGE###########
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk      #command in install in python (pip install pillow)
from tkinter import messagebox

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
        reg_button = Button(Frame1,text="New User Register",font="arial 11 bold underline",bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
        reg_button.place(x=20,y=350,width=160) 
#forget btn
        fog_button2 = Button(Frame1,text="Forget Password",font="arial 11 bold underline",bg="black",fg="white",borderwidth=0,activeforeground="white",activebackground="black")
        fog_button2.place(x=12,y=375,width=160) 

#creat login funtion #                
    def login(self):
        if self.e1.get()=="" or self.e2.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.e1.get()=="kapu" and  self.e2.get()=="ashu":
            messagebox.showinfo("Success","Welcome to hospital managment system")
        else:
            messagebox.showerror("Invalid","invalid user name  password")              

if __name__=="__main__":
    root = Tk()
    app = login_window(root)
    root.mainloop()