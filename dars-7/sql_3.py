import sqlite3

conn =sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''pragma table_info(users)''')

fields=cursor.fetchall()
for i in fields:
    print(i[1])
    
conn.close()