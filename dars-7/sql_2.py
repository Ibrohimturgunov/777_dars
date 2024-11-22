import sqlite3

conn =sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''alter table users add column surname text''')
cursor.execute('''alter table users add column faculty text''')

conn.commit()
conn.close()