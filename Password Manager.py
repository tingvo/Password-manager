import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

root = Tk()
root.geometry("300x200")
root.title("Password Manager")

def show():
    cursor.execute("SELECT * FROM passwords")
    details = cursor.fetchall()
    for x in details:
        account = x[0]
        if account == acc_sel.get():
            username = x[1]
            password = x[2]
    userLabel = Label(root, text="Username: " + username).pack()
    passLabel = Label(root, text="Password: " + password).pack()

cursor.execute("SELECT account FROM passwords")
accounts = cursor.fetchall()

clicked = StringVar()

acc_sel = ttk.Combobox(root, values = accounts)
acc_sel.set("Select an account")
acc_sel.pack()

show_button = Button(root, text="Enter", command=show()).pack()

conn.commit()
conn.close()
root.mainloop()