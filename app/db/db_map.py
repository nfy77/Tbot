import sqlite3

def create_user_table(connect, cursor): 
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INTEGER primary key,
                   gender TEXT,
                   name TEXT,
                   birthday TEXT
                   )""")
    connect.commit()
#                   birthgeo TEXT
    
def create_file_table(connect, cursor): 
    cursor.execute("""CREATE TABLE IF NOT EXISTS files(
                   id INTEGER primary key,
                   name TEXT                   
                   )""")
    connect.commit()