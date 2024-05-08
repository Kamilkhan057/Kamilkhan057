import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def creat_n_w():
   pass
def creat_window():
   extra = tk.Toplevel() 
    

   
#r
win = tk.Tk()
win.title("my first gui")
win.geometry('300x400')

#button 
button = ttk.Button(win,text='open new window',command= creat_window)
button.pack(expand = True)
button.place(x=70,y=20,width=150)
#button1 
button1 = ttk.Button(win,text='close main window')
button1.pack(expand = True)
button1.place(x=70,y=50,width=150)
#button2
button2 = ttk.Button(win,text='creat new window',command = creat_n_w)
button2.pack(expand = True)
button2.place(x=70,y=80,width=150)
win.mainloop()

# root.mainloop()