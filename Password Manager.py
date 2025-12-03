import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

root = Tk()
root.geometry("210x110")
root.title("Password Manager")

def show():
    cursor.execute("SELECT * FROM passwords")
    details = cursor.fetchall()
    for x in details:
        account = x[0]
        if account == acc_sel.get():
            username = x[1]
            password = x[2]
    userLabel.config(text="Username: " + username)
    passLabel.config(text="Password: " + password)

cursor.execute("SELECT account FROM passwords")
accounts = cursor.fetchall()

acc_sel = ttk.Combobox(root, values = accounts)
acc_sel.set("Select an account")
acc_sel.grid(row=0, column=0)

show_button = Button(root, padx=70, text="Enter", command=show).grid(row=1, column=0)
userLabel = Label(root, text=" ")
userLabel.grid(row=2, column=0)
passLabel = Label(root, text=" ")
passLabel.grid(row=3, column=0)

root.mainloop()
conn.close()