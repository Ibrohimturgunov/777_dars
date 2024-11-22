import sqlite3

conn=sqlite3.connect('university.db')
cursor=conn.cursor()

cursor.execute("select * from students")
result=cursor.fetchall()

for row in result:
    print(row)

conn.commit()    
conn.close()
