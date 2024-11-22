import sqlite3

conn =sqlite3.connect('example.db')
cursor = conn.cursor()

name='Alijon'
surname='Valiyev'
age=20
faculty='Amaliy dasturchi'

cursor.execute('insert into users(name, surname, age, faculty) values (?,?,?,?)',
               (name, surname , age , faculty))

conn.commit()    
conn.close()