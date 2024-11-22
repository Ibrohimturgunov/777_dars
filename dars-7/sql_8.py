import sqlite3

conn =sqlite3.connect('university.db')
cursor = conn.cursor()

students_info =[('Ivan','Ivanov', 5,4,4),
                ('Anna','Andreyevna', 5,4,3),
                ('Petr','Petrov', 4,4,4),
                ('Marina','Marinina', 4,4,4),
                ('Sergey','Sergeyv', 3,3,5)]

cursor.executemany('insert into students''(name, lastname, physics, math, CS)''values (?,?,?,?,?)',students_info)

fee = 205000
average =4.0
discount = 0.01
with_discount=fee*(100-discount)

for year in range(1,6):
    cursor.execute('insert into tolovlat (year, fee, average, discount, with_discount) values (?,?,?,?,?)',(year, fee, average, discount, with_discount))
    fee=round(fee*0.97, 2)
    average +=0.1
    discount+=0.01
    with_discount=round(fee * 0.97+discount, 2)


conn.commit()    
conn.close()    