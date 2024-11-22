import sqlite3

conn=sqlite3.connect('university.db')
cursor=conn.cursor()

name, lastname, year = input("Ismingizni, familiyangizni va kursingizni kiriting (bo'sh joy bilan ajratilgan holda):").split()

cursor.execute("""select students.name, students.lastname, 
               tolovlat.with_discount, tolovlat.fee,
               students.physics, students.math, students.CS, tolovlat.average
               from students join tolovlat
               where students.name=:name and students.lastname=:lastname and tolovlat.year=:year""",
               {'name': name, 'lastname': lastname, 'year':year})

result=cursor.fetchone()

if not result:
    print("student topilmadi")
else:
    name, lastname, with_discount, tolovlat, physics, math, CS, average=result
    if (physics+math+CS)/3>=average:
        print(f'{name} {lastname} oqish uchun tolov {year}-M kursga: {with_discount} sum.')
    else:
        print(f'{name} {lastname} oqish uchun tolov {year}-M kursga: {tolovlat}sum.')
    
conn.close()
