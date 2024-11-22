import sqlite3

conn = sqlite3.connect('magaz.db')
cursor= conn.cursor()
try:
    cursor.execute('''create table orders
                (id integer primary key, customer_id integer, product_id integer, quantity integer)''')

    cursor.execute('''create table customers
                (id integer primary key, customer_name text)''')

    cursor.execute('''create table product
                (id integer primary key, product_name)''')
except:
    print('xatolik_1')

try:
    cursor.executemany('insert into orders (id, customer_id, product_id, quantity) values (?,?,?,?)',
                [(1,1,1,4),
                (2,2,2,4),
                (3,3,3,6),
                (4,4,4,8),
                (5,5,5,3)])


    cursor.executemany('insert into customers (id, customer_name) values (?,?)',
                [(1,'Bobur'),
                (2,'Davlat'),
                (3, 'Timur'),
                (4, 'Ibrohim'),
                (5,'Yagona')])


    cursor.executemany('insert into product (id, product_name) values (?,?)',
                [(1,'Daftar'),
                (2,'Noutbuk'),
                (3, 'Sichqoncha'),
                (4, 'Dubayga sayohat'),
                (5,'Iphone 16')])
except:
    print('xato_2')

conn.commit()
conn.close()