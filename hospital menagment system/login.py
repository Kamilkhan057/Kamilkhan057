from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox\

def login():
    if e1 == "" or e2 == "":
        messagebox.showerror("error","error ")
    else:
       messagebox.showinfo("sucsses"," detial this filled ") 
        
def new_win(): 
       extra = Toplevel()
       extra.state('zoomed')
       extra.config(bg="balck",fg='white')
          

win = Tk()
win.state('zoomed')
win.config(bg='blue')

    
#frame
Frame1 = Frame(win,bd=15,bg='black',relief=RIDGE)
Frame1.place(x=570,y=100,width=400,height=500)
#Heading 
Label(win,text='Login Page',bg='black',fg='white',font='imapte 31 bold').place(x=660,y=120)
####################
#ubder frame 1
Frame2 = Frame(win,bd=5,bg='black',relief=RIDGE)
Frame2.place(x=620,y=180,width=300,height=360)
#ubder frame 2
Frame2 = Frame(win,bd=5,bg='black',relief=RIDGE)
Frame2.place(x=630,y=190,width=280,height=340)
#user email
Label(win,text='USER EMAil-ID ',bg='black',font='arial 12 bold',fg='white' ).place(x=715,y=218)
#user text
e1 = Entry(Frame2,bd=4)
e1.place(x=50,y=60,width=180,height=30)
#user password
Label(win,text='Password',bg='black',font='arial 12 bold',fg='white' ).place(x=728,y=287 )
#user password
e2 = Entry(Frame2,bd=4)
e2.place(x=50,y=120,width=180,height=30)
#login button
l_btn = Button(Frame2,text='Login',font='arial 15 bold',bg='gold',fg='white',bd=7,cursor='hand2',command=login)
l_btn.place(x=50,y=170,width=180)
#register button
R_btn = Button(Frame2,text='Register',font='arial 12 bold ',bg='black',bd=0,fg='white',cursor='hand2',command=new_win)
R_btn.place(x=50,y=230,width=80)
#
# registresion indigeter.

#forgot password
f_btn = Button(Frame2,text='forget',font='arial 12 bold ',bg='black',bd=0,fg='white',cursor='hand2')
f_btn.place(x=150,y=230,width=80)
#user text hospital
Label(win,text='Hospital Menagment System Login Page.',bg='black',font='arial 12 bold',fg='white' ).place(x=615,y=550)
##########################
mainloop()