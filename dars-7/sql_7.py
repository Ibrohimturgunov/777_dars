import sqlite3

conn =sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''create table students (id integer primary key,
               name text,
               lastname text,
               physics integer,
               math integer, 
               CS integer)''')

cursor.execute('''create table tolovlat (
               year integer primary key,
               fee real,
               average real,
               discount real,
               with_discount real)''')

conn.commit()    
conn.close()    