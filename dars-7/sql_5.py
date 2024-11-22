import sqlite3

conn =sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("update users set age = ? where name = ? and surname = ?",
               (19, 'Alijon', 'Valiyev'))

conn.commit()    
conn.close()    