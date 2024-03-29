import sqlite3
import os.path
import bcrypt

# filename to form database
file = "Sqlite3.db"


def connect_to_database():
    conn = sqlite3.connect(file)
    c = conn.cursor()
    return c, conn


def create_table():
    conn = sqlite3.connect(file)
    c = conn.cursor()
    c.execute("""Create TABLE Accounts (
                Username TEXT,
                Password TEXT, 
                Passcode INTEGER,
                Balance REAL
        )""")
    conn.commit()
    conn.close()

def check_if_user_exists(username):
    c, conn = connect_to_database()
    c.execute("SELECT * FROM Accounts WHERE Username=?", (username,))
    if c.fetchall():
        return True #returns True if user exists

if not os.path.isfile(file):
    try:
        conn = sqlite3.connect(file)
        create_table()
        print("Database Sqlite3.db formed.")
    except:
        print("error with creating the database.")


def register(username, password):
    c, conn = connect_to_database()
    if not check_if_user_exists(username):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        c.execute("INSERT INTO Accounts VALUES(?, ?, ?, ?)", (username, hashed_password, 0, 0))
        conn.commit()
        conn.close()
        return True
    return False

def login(username, password):
    c,conn = connect_to_database()
    c.execute("SELECT Password FROM Accounts WHERE Username=?", (username,))
    try:
        hashed = c.fetchone()[0]
        return bcrypt.checkpw(password.encode(), hashed)
    except TypeError:
        return False

def fetch_passcode(username, passcode):
    c, conn = connect_to_database()
    c.execute("SELECT Passcode from Accounts WHERE Username=?", (username,))
    hashed_passcode = c.fetchone()[0]
    if hashed_passcode == 0:
        return 'first time'
    return bcrypt.checkpw(str(passcode).encode(), hashed_passcode)

def insert_passcode(username, passcode):
    c, conn = connect_to_database()
    hashed_passcode = bcrypt.hashpw(passcode.encode(), bcrypt.gensalt())
    c.execute("UPDATE Accounts SET Passcode = ? WHERE username = ?", (hashed_passcode, username))
    conn.commit()
    conn.close()
    print("Passcode registered successfully ")
    return

def get_balance(username):
    c, conn = connect_to_database()
    c.execute("SELECT balance from Accounts WHERE Username=?", (username,))
    balance = c.fetchone()[0]
    return balance


def withdraw(username, withdraw_amount):
    c, conn = connect_to_database()
    balance = get_balance(username)
    if float(withdraw_amount) <= balance:
        c.execute("UPDATE Accounts SET balance = ? WHERE username = ?", (balance-float(withdraw_amount), username))
    conn.commit()
    conn.close()

def deposit(username, amount):
    c, conn = connect_to_database()
    balance = get_balance(username) + float(amount)
    c.execute("UPDATE Accounts SET balance = ? WHERE username = ?", (balance, username))
    conn.commit()
    conn.close()


def change_passcode(username, current_passcode, new_passcode):
    pass
    #fetch passcode
    #if passcode match
    #change passcode to new passcode
