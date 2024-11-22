import sqlite3

conn =sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''create table users 
               (id integer primary key, name text, age integer)''')
conn.close()