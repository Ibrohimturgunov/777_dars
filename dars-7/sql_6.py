import sqlite3

conn =sqlite3.connect('example.db')
cursor = conn.cursor()


try:
    cursor.execute("delete from users where faculty like '%Amaliy matematika%'")
    conn.commit()    
    print('Ochirildi')
except:
    print('xatolik')

conn.close()