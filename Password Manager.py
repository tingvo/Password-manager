import sqlite3 as sql
from tkinter import *
from tkinter import ttk

conn = sql.connect('passwords.db')
cursor = conn.cursor()

root = Tk()
title = Label(root, text="Password Manager").pack()

cursor.execute("SELECT account FROM passwords")
accounts = cursor.fetchall()

acc_sel = ttk.Combobox(root, values = accounts)
acc_sel.set("Select an account")
acc_sel.pack()


root.mainloop()