from Moduls import Database

bozor=Database()
bozor.createdatabase('bozor')
bozor.createtable('bozor','meva','id integer primary key, nomi varchar(20), narxi float, turi varchar(30)')

mevalar = [
    (1, "Olma", 10000, "Daraxt mevasi"),
    (2, "Banan", 18000, "Tropik meva"),
    (3, "Uzum", 15000, "Tok mevasi"),
    (4, "Nok", 12000, "Daraxt mevasi"),
    (5, "Apelsin", 20000, "Tsitrus meva"),
    (6, "Anor", 25000, "Daraxt mevasi"),
    (7, "Limon", 18000, "Tsitrus meva"),
    (8, "Shaftoli", 14000, "Daraxt mevasi"),
    (9, "Gilos", 22000, "Daraxt mevasi"),
    (10, "Kivi", 30000, "Tropik meva")
]

bozor.insertinto('bozor', 'meva', mevalar)

print('shart-2')
bozor.filter('bozor','select * from meva order by narxi desc limit 5;')
