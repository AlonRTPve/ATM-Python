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
    global username
    username = username_entry.get()  # Getting the username from the entry box
    password = password_entry.get()  # Getting the password from the entry box
    clear_entry()
    if len(password) == 0 or len(username) == 0:
        print('Must enter a password or a username')
    else:
        if Database.login(username, password):
            label2 = Label(root, text="Succesfully logged in")
            label2.pack()
            passcode_window()
            return
        print("The user name or password is incorrect")

def register():
    username = username_entry.get()  # Getting the username from the entry box
    password = password_entry.get()  # Getting the password from the entry box
    clear_entry()
    if len(password) == 0 or len(username) == 0:
        print('Must enter a password or a username')
    else:
        if Database.register(username,password):
         print("Created user successfully")
        else:
         print("User already exists")

def clear_entry():
    password_entry.delete(0, END)
    username_entry.delete(0, END)

def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def button_click(arr):
    number, entry = arr[0], arr[1]
    try:
        if len(entry.get()) <= 3:
            entry.insert(0, number)
    except AttributeError:
        entry.insert(0, number)

def submit(entry):
    if len(entry.get()) == 4:
        passcode = entry.get()
        if Database.fetch_passcode(username, passcode) == "first time":
            Database.insert_passcode(username, passcode)
            passcode_window()
        if Database.fetch_passcode(username, passcode):
            options_window()
        else:
            print("Login failed")

def submit_btn_deposit(entry, balancelabel):
    amt_to_deposit = entry.get()
    if amt_to_deposit != '':
        Database.deposit(username, amt_to_deposit)
        balancelabel.configure(text=f"balance is {Database.get_balance(username)}")

def submit_btn_withdraw(entry, balancelabel):
    amt_to_withdraw = entry.get()
    if amt_to_withdraw != '':
        Database.withdraw(username, amt_to_withdraw)
        balancelabel.configure(text=f"balance is {Database.get_balance(username)}")


def clear(entry):
    entry.delete(0, END)


def Return():
    options_window()

def passcode_window():
    global e
    clear_widgets() # Cleaning the window
    Label(root, text="ENTER PASSCODE: ").grid(row=0, column=2)
    if Database.fetch_passcode(username, 0) == "first time":
        Label(root, text="first time? ,choose passcode").grid(row=0, column=2)
    e = Entry(root, show = "*", width=15)
    e.grid(row=1, column=2)
    Label(root, text="").grid(row=2, column=2)
    Button(root, text='1', width=15, height=1, command=lambda: button_click([1, e])).grid(row=3, column=1)
    Button(root, text='2', width=15, height=1, command=lambda: button_click([2, e])).grid(row=3, column=2)
    Button(root, text='3', width=15, height=1, command=lambda: button_click([3, e])).grid(row=3, column=3)
    Button(root, text='4', width=15, height=1, command=lambda: button_click([4, e])).grid(row=4, column=1)
    Button(root, text='5', width=15, height=1, command=lambda: button_click([5, e])).grid(row=4, column=2)
    Button(root, text='6', width=15, height=1, command=lambda: button_click([6, e])).grid(row=4, column=3)
    Button(root, text='7', width=15, height=1, command=lambda: button_click([7, e])).grid(row=5, column=1)
    Button(root, text='8', width=15, height=1, command=lambda: button_click([8, e])).grid(row=5, column=2)
    Button(root, text='9', width=15, height=1, command=lambda: button_click([9, e])).grid(row=5, column=3)
    Button(root, text='CLEAR', width=15, height=1, bg='yellow', command=lambda: clear(e)).grid(row=6, column=2)
    Button(root, text='CANCEL', width=15, height=1, bg='red', command=root.destroy).grid(row=6, column=1)
    Button(root, text='SUBMIT', width=15, height=1, bg='green', command=lambda: submit(e)).grid(row=6, column=3)


def options_window():
    clear_widgets()
    Label(root, text="SELECT AN OPTION", font = 15, fg='blue').grid(row=5, column=5)
    Label(root, text='WITHDRAW', width=17, height=1, bg='bisque').grid(row=7, column=4) #WITHDRAW BUTTON
    Label(root, text="", font = 15).grid(row=8, column=4)
    Label(root, text='VIEW BALANCE', width=17, height=1, bg='bisque').grid(row=9, column=4) # View balance

    Label(root, text='DEPOSIT', width=17, height=1, bg='DarkSeaGreen').grid(row=7,column=6)  # DEPOSIT
    Label(root, text="", font = 15).grid(row=8, column=6)
    Label(root, text='CHANGE PASSCODE', width=17, height=1, bg='DarkSeaGreen').grid(row=9, column=6) # Change passcode
    Label(root, text="", font = 15).grid(row=10, column=6)

    Label(root, text='MAKE TRANSACTION', width=17, height=1, bg='DarkSeaGreen').grid(row=11, column=6)  # DEPOSIT
    Label(root, text="", font = 15).grid(row=10, column=6)
    Label(root, text='VIEW TRANSACTIONS', width=17, height=1, bg='bisque').grid(row=11, column=4)
    Button(root, text='>', font=15, command=withdraw_window).grid(row=7, column=3) # WITHDRAW BUTTON
    Button(root, text='>', font=15).grid(row=9, column=3) # VIEW BALANCE BUTTON
    Button(root, text='>', font=15).grid(row=11, column=3) # PLACEHOLDER LEFT SIDE BUTTON
    Button(root, text='<', font=15, command=deposit_window).grid(row=7, column=7) # DEPOSIT BUTTON
    Button(root, text='<', font=15, command=change_passcode_window).grid(row=9, column=7) # CHANGE PASSCODE BUTTON
    Button(root, text='<', font=15).grid(row=11, column=7) # PLACEHOLDER RIGHT SIDE BUTTON

def deposit_window():
    clear_widgets()
    balance = Database.get_balance(username)
    balancelabel = Label(root, text=f"balance is: {balance}", width=15, height = 1, fg = 'black')
    balancelabel.grid(row=4, column=5)
    Label(root, text='Amount to deposit:', width=15, height=1).grid(row=5, column=5)
    Label(root, text='',).grid(row=6, column=5)
    deposit_entry = Entry(root, width=15)
    deposit_entry.grid(row=7, column=5)
    Label(root, text = '').grid(row=8, column=5)
    Button(root, text='1', width=15, height=1, command=lambda: button_click([1, deposit_entry])).grid(row=9, column=4)
    Button(root, text='2', width=15, height=1, command=lambda: button_click([2, deposit_entry])).grid(row=9, column=5)
    Button(root, text='3', width=15, height=1, command=lambda: button_click([3, deposit_entry])).grid(row=9, column=6)
    Button(root, text='4', width=15, height=1, command=lambda: button_click([4, deposit_entry])).grid(row=10, column=4)
    Button(root, text='5', width=15, height=1, command=lambda: button_click([5, deposit_entry])).grid(row=10, column=5)
    Button(root, text='6', width=15, height=1, command=lambda: button_click([6, deposit_entry])).grid(row=10, column=6)
    Button(root, text='7', width=15, height=1, command=lambda: button_click([7, deposit_entry])).grid(row=11, column=4)
    Button(root, text='8', width=15, height=1, command=lambda: button_click([8, deposit_entry])).grid(row=11, column=5)
    Button(root, text='9', width=15, height=1, command=lambda: button_click([9, deposit_entry])).grid(row=11, column=6)
    Button(root, text='CLEAR', width=15, height=1, bg='yellow', command=lambda: clear(deposit_entry)).grid(row=10, column=7)
    Button(root, text='0', width=15, height=1, command=lambda: button_click([0,deposit_entry])).grid(row=12, column=5)
    Button(root, text='SUBMIT', width=15, height=1, bg='green', command= lambda: submit_btn_deposit(deposit_entry, balancelabel)).grid(row=9, column=7)
    Button(root, text='RETURN', width=15, height=1, bg='red', command=Return).grid(row=11, column=7)


def withdraw_window():
    clear_widgets()
    balance = Database.get_balance(username)
    balancelabel = Label(root, text=f"balance is: {balance}", width=15, height=1, fg='black')
    balancelabel.grid(row=4, column=5)
    Label(root, text='Amount to withdraw:', width=15, height=1).grid(row=5, column=5)
    Label(root, text='', ).grid(row=6, column=5)
    withdraw_entry = Entry(root, width=15)
    withdraw_entry.grid(row=7, column=5)
    Label(root, text='').grid(row=8, column=5)
    Button(root, text='1', width=15, height=1, command=lambda: button_click([1, withdraw_entry])).grid(row=9, column=4)
    Button(root, text='2', width=15, height=1, command=lambda: button_click([2, withdraw_entry])).grid(row=9, column=5)
    Button(root, text='3', width=15, height=1, command=lambda: button_click([3, withdraw_entry])).grid(row=9, column=6)
    Button(root, text='4', width=15, height=1, command=lambda: button_click([4, withdraw_entry])).grid(row=10, column=4)
    Button(root, text='5', width=15, height=1, command=lambda: button_click([5, withdraw_entry])).grid(row=10, column=5)
    Button(root, text='6', width=15, height=1, command=lambda: button_click([6, withdraw_entry])).grid(row=10, column=6)
    Button(root, text='7', width=15, height=1, command=lambda: button_click([7, withdraw_entry])).grid(row=11, column=4)
    Button(root, text='8', width=15, height=1, command=lambda: button_click([8, withdraw_entry])).grid(row=11, column=5)
    Button(root, text='9', width=15, height=1, command=lambda: button_click([9, withdraw_entry])).grid(row=11, column=6)
    Button(root, text='CLEAR', width=15, height=1, bg='yellow', command=lambda: clear(withdraw_entry)).grid(row=10,column=7)
    Button(root, text='0', width=15, height=1, command=lambda: button_click([0, withdraw_entry])).grid(row=12, column=5)
    Button(root, text='SUBMIT', width=15, height=1, bg='green',command=lambda: submit_btn_withdraw(withdraw_entry, balancelabel)).grid(row=9, column=7)
    Button(root, text='RETURN', width=15, height=1, bg='red', command=Return).grid(row=11, column=7)


def change_passcode_window():
    pass

button1 = Button(root, text='Login', width=15, height=1, command=login)
button1.pack(side='left', anchor='e', expand=True)
button2 = Button(root, text='Register', width=15, height=1,  command=register)
button2.pack(side='right', anchor='w', expand=True)

root.mainloop()


