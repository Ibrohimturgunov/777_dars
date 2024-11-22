from Moduls import *

kino=Database()

kino.createdatabase('kino')
kino.createtable('kino','janr','id integer primary key, name varchar(20)')
kino.createtable('kino','cinema','id integer primary key, name varchar(20), year year, janr_id integer')

janr=[(1,'Drama'),
        (2,'Komediya'),
        (3,'Triller'),
        (4,'Fantastika'),
        (5,'Sarguzasht'),
        (6,'Qorqinchli'),
        (7,'Melodrama'),
        (8,'Animatsiya'),
        (9,'Detektiv'),
        (10,'Biografiya')]

cinema=[(1,'Titanik', 1997, 1),
        (2,'Forrest Gump', 1994, 1),
        (3,'Avengers: Endgame', 2019, 4),
        (4,'The Godfather', 1972, 1),
        (5,'Shrek', 2001, 8),
        (6,'Joker', 2019, 3),
        (7,'Harry Potter', 2001, 4),
        (8,'Inception', 2010, 3),
        (9,'Frozen', 2013, 8),
        (10,'The Dark Knight', 2008, 3),
        (11,'Finding Nemo', 2003, 8),
        (12,'Pulp Fiction', 1994, 1),
        (13,'The Conjuring', 2013, 6),
        (14,'Mission Impossible', 1996, 5),
        (15,'Sherlock Holmes', 2009, 9),
        (16,'The Notebook', 2004, 7),
        (17,'Bohemian Rhapsody', 2018, 10),
        (18,'Toy Story', 1995, 8),
        (19,'Spider-Man: No Way Home', 2021, 4),
        (20,'The Pianist', 2002, 1)]

kino.insertinto('kino','janr',janr)
kino.insertinto('kino','cinema',cinema)

print('shart-1')
kino.filter('kino', '''SELECT 
    c.name AS name, 
    COUNT(c.id) AS film_soni
FROM 
    Cinema c
JOIN 
    Janr j ON c.janr_id = j.id
GROUP BY 
    c.janr_id
HAVING 
    COUNT(c.id) > 1;
''')


