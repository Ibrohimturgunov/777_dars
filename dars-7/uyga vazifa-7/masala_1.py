from Moduls import *


cd=Database()

cd.createdatabase('university')
cd.createtable('university', 'talaba', 'id integer primary key, ismi varchar(20) , kursi integer, stipendiyasi float')


malumot=[(1,'Davlat', 3, 250000.00),
        (2,'Ali', 2, 200000.00),
        (3,'Hasan', 1, 150000.00),
        (4,'Gulnoza', 4, 300000.00),
        (5,'Zafar', 2, 220000.00),
        (6,'Nodira', 1, 170000.00),
        (7,'Shoxrux', 3, 260000.00),
        (8,'Samar', 4, 310000.00),
        (9,'Nodira', 3, 240000.00),
        (10,'Ilhom', 2, 210000.00)] 

cd.insertinto('university', 'talaba', malumot)
# cd.delete_info('university','talaba', 'kursi=4')
# cd.update_table('university', 'update talaba set kursi=kursi+1')
print(cd.select_info('university', 'talaba'))
cd.filter('university', 'select kursi, count(*) as talaba_soni from talaba group by kursi')
