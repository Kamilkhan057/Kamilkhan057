from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Python GUI ")
win.config(bg='blue')
win.state('zoomed')
# frame1
frame1 = Frame(win,bd=15, relief= RIDGE)
frame1.place(x=500,y=70,width=600,height=600) 
# Frame Label
lf =LabelFrame(frame1,text='Software Registration ',font='arial 18 bold',bd=10)
lf.place(x=0,y=4,width=570,height=570)
#regitration
Label(lf,text=" Registration ",font='impate 17 bold' ,bg='lightgreen').pack(fill=X)
# regitration info
Label(lf,text="FIRST NAME",font='impate 12 bold').place(x=70,y=50,width=100) 
Label(lf,text="LAST NAME",font='impate 12 bold').place(x=345,y=50,width=150)
Label(lf,text="EMAIL ADDRESS",font='impate 12 bold').place(x=50,y=150,width=150)  
Label(lf,text="PHYSICAL ADDRESS",font='impate 12 bold').place(x=300,y=150,width=250)
Label(lf,text="PHONE NUMBER",font='impate 12 bold').place(x=150,y=250,width=250)

# entry
fn = Entry(lf,bd=4)
fn.place(x=50,y=80,width=150,height=30)
ln = Entry(lf,bd=4)
ln.place(x=350,y=80,width=150,height=30)
ea = Entry(lf,bd=4)
ea.place(x=50,y=180,width=150,height=30)
pa = Entry(lf,bd=4)
pa.place(x=350,y=180,width=150,height=30)
pn = Entry(lf,bd=4)
pn.place(x=200,y=280,width=150,height=35)
# Button
btn = Button(lf,text='Registration',font='impate 15 bold',bg='red',fg='white',bd=7,cursor='hand2')
btn.place(x=150,y=340,width=250,height=50)
mainloop()