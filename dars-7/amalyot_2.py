import sqlite3

conn = sqlite3.connect('magaz.db')
cursor= conn.cursor()

cursor.execute('select * from customers as c left join orders as o on c.id=o.id where o.quantity>=5')

result=cursor.fetchall()
for i in result:
    print(i)

conn.commit()
conn.close()