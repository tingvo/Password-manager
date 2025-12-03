import sqlite3
from tkinter import *

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

root = Tk()
root.geometry("400x210")
root.title("Password Manager")

def show():
    cursor.execute("SELECT * FROM passwords")
    details = cursor.fetchall()
    for x in details:
        account = x[0]
        if account == acc_sel.get(ACTIVE):
            username = x[1]
            password = x[2]
    userLabel.config(text="Username: " + username)
    passLabel.config(text="Password: " + password)

cursor.execute("SELECT account FROM passwords")
accounts = cursor.fetchall()

acc_sel = Listbox(root)
for item in accounts:
    acc_sel.insert(END, item)
acc_sel.grid(row=0, column=1, rowspan=6)

acc_entry = Entry(root)
acc_entry.grid(row=3, column=0)
acc_entry.insert(0, "Add Website")

user_entry = Entry(root)
user_entry.grid(row=4, column=0)
user_entry.insert(0, "Add Username")

pass_entry = Entry(root)
pass_entry.grid(row=5, column=0)
pass_entry.insert(0, "Add Password")

conf_entry = Entry(root, text="Confirm Password")
conf_entry.grid(row=6, column=0)
conf_entry.insert(0, "Confirm Password")

show_button = Button(root, padx=37, text="Show Details", command=show)
show_button.grid(row=6, column=1)
userLabel = Label(root, text="Username: ", anchor="w")
userLabel.grid(row=0, column=0)
passLabel = Label(root, text="Password: ", anchor="w")
passLabel.grid(row=1, column=0)

root.mainloop()
conn.close()