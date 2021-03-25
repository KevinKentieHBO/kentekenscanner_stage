import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def select(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * from Betaaltarief")
        records = cursor.fetchall()
        for record in records:
            print(str(record[0]) + " " + record[1] + " " +str(record[2]))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()