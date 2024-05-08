                     # hospital menagment system.
# tkinter is using to grafical user interface (GUI).
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

win = Tk()# to farform tkinter 
win.state('zoomed')#click a  run button for open a full screen. 
win.config(bg='black')#usng congig are set in background color.

#-----------------button funcation-----------------------#
# get method are used in fatch an info.
################################################
def pdb():
    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error","all fields are required")
    else:
        # mysql.connector.connect(host,username,password,database)under for peramiter
        con = mysql.connector.connect(host='localhost',username='root',password='4011', database='mydata')    
        #my courser
        my_cursor = con.cursor()
        # thier will using query in insert a table of connect sqldata base.
        my_cursor.execute("insert into alldata values(%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)",(
            nameoftablet.get(),
            Ref.get(),
            date.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dalydose.get(),
            sideeffact.get(),
            bloodpresure.get(),
            StoregeDevice.get(),
            medcation.get(),
            Patientid.get(),
            PatientName.get(),
            PerientAddress.get(),
        ))
        con.commit()
        # fetch_data()
        con.close()
        messagebox.showinfo("success","Data has been inserted")
####################################################
########


#fatch data.
# def fetch_data():
#         con = mysql.connector.connect(host='localhost',username='root',password='4011', database='mysql1')    
# # #         #my courser
#         my_cursor = con.cursor()
# # #         # thier will using query in insert a table of connect sqldata base.
#         my_cursor.execute('select* from hospital')
#         rows = my_cursor.fetchall()
#         if len(rows) != 0:
#           table.delete(* table.get_children())
#           for item in rows:
#               table.insert(' ',END,values=item)
#         con.commit()
#         con.close() 
########################################


#heading
#font using change a style and hight of font.
#bg using set background color.
#fg using set font color.
#pack method are using under multiple work 
#fill=x are work in horizantal diraction.
# there module are work in without verible  
Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
###################################
#frame1
# bd are used for boder in Frame.
Frame1 = Frame(win,bd=15,relief=RIDGE)
Frame1.place(x=0,y=54,width=1537,height=400)
#frame patiant information.
lf1 = LabelFrame(Frame1,text='PATIENT INFORMATION',font='arial 10 bold',bd=10,bg='pink')
lf1.place(x=8,y=0,width=900,height=370)
#lable pationt information
#left
#name
Label(Frame1,text='Name of Tablet',bg='pink',font='arial 10 bold').place(x=30,y=25)
#Ref.no
Label(Frame1,text='Refrence.NO.',bg='pink',font='arial 10 bold').place(x=30,y=70)
#dose
Label(Frame1,text='Does',bg='pink',font='arial 10 bold').place(x=30,y=115)
#No.of Tablets
Label(Frame1,text='No.of Tablets',bg='pink',font='arial 10 bold').place(x=30,y=160)
#issue Date
Label(Frame1,text='Issue',bg='pink',font='arial 10 bold').place(x=30,y=215)
#Expiry Date
Label(Frame1,text='Expiry Date',bg='pink',font='arial 10 bold').place(x=30,y=265)
#Daly Dose
Label(Frame1,text='Daly Dose',bg='pink',font='arial 10 bold').place(x=30,y=310)
#Side Effect
Label(Frame1,text='Side Effect',bg='pink',font='arial 10 bold').place(x=30,y=435)
#
#right
#blood preseure
Label(Frame1,text='Blood Prasure',bg='pink',font='arial 10 bold').place(x=450,y=25)
#storege device
Label(Frame1,text='Storege Device',bg='pink',font='arial 10 bold').place(x=450,y=70)
#medcation
Label(Frame1,text='Medcation',bg='pink',font='arial 10 bold').place(x=450,y=115)
#patient id.
Label(Frame1,text='Patient id',bg='pink',font='arial 10 bold').place(x=450,y=160)
#patient Name.
Label(Frame1,text='Patient Name',bg='pink',font='arial 10 bold').place(x=450,y=215)
#DOB
Label(Frame1,text='DOB',bg='pink',font='arial 10 bold').place(x=450,y=265)
#petient addr.
Label(Frame1,text='Perient Address.',bg='pink',font='arial 10 bold').place(x=450,y=310)
#entry Field for all labels.
#TEXT veriabal for all lables
nameoftablet = StringVar()
Ref = StringVar()
date = StringVar
nooftablets= StringVar()
issuedate =StringVar()
expdate = StringVar()
dalydose = StringVar()
sideeffact = StringVar()
bloodpresure = StringVar()
StoregeDevice = StringVar()
medcation = StringVar()
Patientid = StringVar()
PatientName = StringVar()
DOB = StringVar()
PerientAddress = StringVar()
#left
e1 = Entry(lf1,bd=4,textvariable=nameoftablet)
e1.place(x=150,y=8,width=210)
e2 = Entry(lf1,bd=4, textvariable=Ref)
e2.place(x=150,y=50,width=210)
e3 = Entry(lf1,bd=4, textvariable=nooftablets)
e3.place(x=150,y=90,width=210)
e4 = Entry(lf1,bd=4, textvariable=issuedate)
e4.place(x=150,y=140,width=210)
e5 = Entry(lf1,bd=4, textvariable=expdate)
e5.place(x=150,y=190,width=210)
e6 = Entry(lf1,bd=4, textvariable=dalydose)
e6.place(x=150,y=240,width=210)
e7 = Entry(lf1,bd=4, textvariable=sideeffact)
e7.place(x=150,y=290,width=210)
#right
e8 = Entry(lf1,bd=4, textvariable=bloodpresure)
e8.place(x=600,y=8,width=210)
e9 = Entry(lf1,bd=4, textvariable=StoregeDevice)
e9.place(x=600,y=50,width=210)
e10 = Entry(lf1,bd=4, textvariable=medcation)
e10.place(x=600,y=90,width=210)
e11 = Entry(lf1,bd=4, textvariable=Patientid)
e11.place(x=600,y=140,width=210)
e12 = Entry(lf1,bd=4, textvariable=PatientName)
e12.place(x=600,y=190,width=210)
e13 = Entry(lf1,bd=4, textvariable=DOB)
e13.place(x=600,y=245,width=210)
e14 = Entry(lf1,bd=4, textvariable=PerientAddress)
e14.place(x=600,y=290,width=210)
#
# frame priscription
lf2 = LabelFrame(Frame1,text='PRISCIPTION',font='arial 10 bold',bd=10)
lf2.place(x=920,y=0,width=580,height=370)
#text box for  peisciption
txt_frame = Text(lf2,bg='yellow',font='impack 10 bold',width=80,height=400)
txt_frame.pack(fill=BOTH)
###############################################
#frame2
Frame2 = Frame(win,bd=15,relief=RIDGE)
Frame2.place(x=0,y=449,width=1537,height=290)
#######################################
#button delete
d_btn = Button(win,text='Delete',font='ariel 16 bold',bg='red',fg='white',bd=7,cursor='hand2')
d_btn.place(x=0,y=740,width=270)
#button prescription 
P_btn = Button(win,text='Prescription',font='ariel 16 bold',bg='purple',fg='white',bd=7,cursor='hand2')
P_btn.place(x=270,y=740,width=460)
#button save prescription data
S_btn = Button(win,text='Save Prescription Data',font='ariel 16 bold',bg='green',fg='white',bd=7,cursor='hand2',command=pdb)
S_btn.place(x=730,y=740,width=400) 
#button  clear270
C_btn = Button(win,text='CLEAR',font='ariel 16 bold',bg='Darkblue',fg='white',bd=7,cursor='hand2')
C_btn.place(x=1130,y=740,width=200) 
#button exit
E_btn = Button(win,text='EXIT',font='ariel 16 bold',bg='gold',fg='white',bd=7,cursor='hand2')
E_btn.place(x=1330,y=740,width=210)
#########################################
#Scroll  bar for prescription DATA in fill entery.
# using scroll bar are define  TKINTER module of secound line.
#using x axis to used in scroll bAR.
scroll_x = ttk.Scrollbar(Frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill=X)
#USING Y Axis to used in scroll bar.
scroll_y = ttk.Scrollbar(Frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill=Y)
#table
table = ttk.Treeview(Frame2,columns=('NOT','REN','DATE','ISD','ED','DD','SE','BP','SD','M','PI','PN','DOB','PA'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x =ttk.Scrollbar(command=table.xview)
scroll_y =ttk.Scrollbar(command=table.yview)
#hading for pricaption Data.
table.heading('NOT',text='Name of tablet')
table.heading('REN',text='Ref.no')
table.heading('DATE',text='DATE')
table.heading('ISD',text='ISSUE DATE')
table.heading('ED',text='EXP.DATE')
table.heading('DD',text='DALY DOSE')
table.heading('SE',text='SIDE EFFACT')
table.heading('BP',text='BLOOP PRE..R')
table.heading('SD',text='STOREGE')
table.heading('M',text='MEDICATION')
table.heading('PI',text='PATIENT ID')
table.heading('PN',text='PATIANT NAME')
table.heading('DOB',text='DATE OF BIRTH')
table.heading('PA',text='PATIANT ADDRESS')
table['show'] ='headings'
table.pack(fill=BOTH,expand=1)
###
table.column('NOT',width=100)
table.column('REN',width=100)
table.column('DATE',width=100)
table.column('ISD',width=100)
table.column('ED',width=100)
table.column('DD',width=100)
table.column('SE',width=100)
table.column('BP',width=100)
table.column('SD',width=100)
table.column('M',width=100)
table.column('PI',width=100)
table.column('PN',width=100)
table.column('DOB',width=100)
table.column('PA',width=100)
mainloop()