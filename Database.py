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
        c.execute("INSERT INTO Accounts VALUES(?, ?, ?)", (username, hashed_password, 0))
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
