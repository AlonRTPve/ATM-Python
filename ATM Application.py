from tkinter import *
import Database

root = Tk()

label = Label(root, text="Enter username:")
label.pack()

username_entry = Entry(root, width=40)
username_entry.pack()

label2 = Label(root, text="Enter password")
label2.pack()

password_entry = Entry(root, width=40, show='*')
password_entry.pack()

def login():
    username = username_entry.get()  # Getting the username from the entry box
    password = password_entry.get()  # Getting the password from the entry box
    clear()
    if len(password) == 0 or len(username) == 0:
        print('Must enter a password or a username')
    else:
        if Database.login(username, password):
            label2 = Label(root, text="Succesfully logged in")
            label2.pack()
            clear_widgets()
            passcode_window()
            return
        print("The user name or password is incorrect")

def register():
    username = username_entry.get()  # Getting the username from the entry box
    password = password_entry.get()  # Getting the password from the entry box
    clear()
    if len(password) == 0 or len(username) == 0:
        print('Must enter a password or a username')
    else:
        if Database.register(username,password):
         print("Created user successfully")
        else:
         print("User already exists")

def clear():
    password_entry.delete(0, END)
    username_entry.delete(0, END)

def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def button_click(number):
    print(e.get())
    e.insert(0, number)

def passcode_window():
    Label(root, text="Enter passcode").grid(row=0, column=2)
    global e
    e = Entry(root, show = "*")
    e.grid(row=1, column=2)
    Label(root, text="").grid(row=2, column=2)
    Button(root, text='1', width=15, height=1, command=lambda : button_click(1)).grid(row=3, column=1)
    Button(root, text='2', width=15, height=1, command=lambda : button_click(2)).grid(row=3, column=2)
    Button(root, text='3', width=15, height=1, command=lambda : button_click(3)).grid(row=3, column=3)
    Button(root, text='4', width=15, height=1, command=lambda : button_click(4)).grid(row=4, column=1)
    Button(root, text='5', width=15, height=1, command=lambda : button_click(5)).grid(row=4, column=2)
    Button(root, text='6', width=15, height=1, command=lambda : button_click(6)).grid(row=4, column=3)
    Button(root, text='7', width=15, height=1, command=lambda : button_click(7)).grid(row=5, column=1)
    Button(root, text='8', width=15, height=1, command=lambda : button_click(8)).grid(row=5, column=2)
    Button(root, text='9', width=15, height=1, command=lambda : button_click(9)).grid(row=5, column=3)




button1 = Button(root, text='Login', width=15, height=1, command=login)
button1.pack(side='left', anchor='e', expand=True)
button2 = Button(root, text='Register', width=15, height=1, command=register)
button2.pack(side='right', anchor='w', expand=True)

root.mainloop()


