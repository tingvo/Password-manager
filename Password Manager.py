import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS passwords ('account' TEXT, 'username' TEXT, 'password' TEXT)")

root = Tk()
root.geometry("380x230")
root.title("Password Manager")

def set_listbox():
    global accounts
    global acc_sel
    cursor.execute("SELECT account FROM passwords")
    accounts = cursor.fetchall()
    acc_sel = Listbox(root)
    for item in accounts:
        acc_sel.insert(END, item)
        acc_sel.grid(row=0, column=1, rowspan=9)
    Scrollbar(acc_sel, orient="vertical")

def display_details():
    cursor.execute("SELECT * FROM passwords")
    details = cursor.fetchall()
    for x in details:
        account = x[0]
        if account == acc_sel.get(ACTIVE)[0]:
            username = x[1]
            password = x[2]    
    userLabel.config(text = username)
    passLabel.config(text = password)

def send_details():
    account = acc_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    confirmed = conf_entry.get()
    if password != confirmed:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        details = account, username, password
        cursor.execute("INSERT INTO passwords VALUES (?,?,?)", details)
        set_listbox()

set_listbox()

## Widgets ##
acc_entry = Entry(root)
acc_entry.grid(row=4, column=0)
acc_entry.insert(0, "Add Website")

user_entry = Entry(root)
user_entry.grid(row=5, column=0)
user_entry.insert(0, "Add Username")

pass_entry = Entry(root, show="*")
pass_entry.grid(row=6, column=0)
pass_entry.insert(0, "Add Password")

conf_entry = Entry(root, show="*")
conf_entry.grid(row=7, column=0)
conf_entry.insert(0, "Confirm Password")

show_button = Button(root, padx=37, text="Show Details", command=display_details)
show_button.grid(row=9, column=1)

enter_button = Button(root, padx=63, text="Enter", command=send_details)
enter_button.grid(row=9, column=0)

userTitle = Label(root, text="Username:").grid(row=0, column=0)
passTitle = Label(root, text="Password:").grid(row=2, column=0)

userLabel = Label(root, text=" ")
userLabel.grid(row=1, column=0)

passLabel = Label(root, text=" ")
passLabel.grid(row=3, column=0)
## End of Widgets ##

root.mainloop()
conn.close()