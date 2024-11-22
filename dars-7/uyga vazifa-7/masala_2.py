from Moduls import Database


taom=Database()

taom.createdatabase('Milliy_taomlar')

taom.createtable('milliy_taomlar','ovqat','id integer primary key , nomi varchar(30), masalliq varchar(50)')

# print(taom.describe('milliy_taomlar','ovqat'))

taomlar = [
    (1, "Osh", "Guruch Go'sht Sabzi Piyoz Yog'ZiraTuz"),
    (2, "Sho'rva", "Go'sht Kartoshka Sabzi Piyoz Tomat Tuz Ziravorlar"),
    (3, "Manti", "Un Go'sht Piyoz Tuz Qalampir Suv"),
    (4, "Lag'mon", "Lag'mon xamiri Go'sht Piyoz Sabzi Bulg'or qalampiri Tomat"),
    (5, "Dimlama", "Go'sht Kartoshka Karam Sabzi Piyoz Qalampir Pomidor"),
    (6, "Samsa", "Un Go'sht Piyoz Yog' Tuz"),
    (7, "Somsa", "Xamir Go'sht Piyoz Ziravorlar"),
    (8, "Tovuq kabob", "Tovuq go'shti Soya sousi Ziravorlar Limon sharbati"),
    (9, "Non va choy", "Non Choy Shakarlamalar"),
    (10, "Qovurma lag'mon", "Lag'mon xamiriGo'sht Sabzi Piyoz Tomat sousi Bulg'or qalampiri")
]

taom.insertinto('milliy_taomlar','ovqat',taomlar)

print("shart-1")

masala=taom.search_info('milliy_taomlar','ovqat','nomi like ("%a")')
for i in masala:
    print(i)

print("shart-2")

masala_2=taom.search_info('milliy_taomlar','ovqat','masalliq like ("%guruch%")')
for i in masala_2:
    print(i)