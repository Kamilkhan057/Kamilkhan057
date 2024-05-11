import tkinter as tk
from tkinter import messagebox
import sqlite3

# create a connection to the database
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

def forgot_password():
    username = entry_username.get()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    if row:
        new_password = entry_new_password.get()
        confirm_new_password = entry_confirm_new_password.get()
        if new_password == confirm_new_password:
            cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
            conn.commit()
            messagebox.showinfo("Forgot Password", "Password updated successfully!")
        else:
            messagebox.showerror("Forgot Password", "New passwords do not match")
    else:
        messagebox.showerror("Forgot Password", "Username not found")

# create a forgot password window
forgot_password_window = tk.Tk()
forgot_password_window.title("Forgot Password")

label_username = tk.Label(forgot_password_window, text="Username:")
label_username.pack()
entry_username = tk.Entry(forgot_password_window)
entry_username.pack()

label_new_password = tk.Label(forgot_password_window, text="New Password:")
label_new_password.pack()
entry_new_password = tk.Entry(forgot_password_window, show="*")
entry_new_password.pack()

label_confirm_new_password = tk.Label(forgot_password_window, text="Confirm New Password:")
label_confirm_new_password.pack()
entry_confirm_new_password = tk.Entry(forgot_password_window, show="*")
entry_confirm_new_password.pack()

button_forgot_password = tk.Button(forgot_password_window, text="Update Password", command=forgot_password)
button_forgot_password.pack()

forgot_password_window.mainloop()