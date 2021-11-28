import sqlalchemy
from pprint import pprint

engen = sqlalchemy.create_engine('postgresql://netpy:0703@localhost:5432/netpy44')
connection = engen.connect()

# Заполняем таблицу исполнителей.
singers = ['OneRepublic', 'Maroon_5', 'The_Beatles', 'NIRVANA', 'Guf', 'Green Day', 'Muse', 'Linkin Park']

for singer in singers:
    connection.execute(
        f"""INSERT INTO singer(name)
            VALUES ('{singer}');"""
    )

# Заполняем таблицу жанров.
genres = ['rock', 'rap', 'pop', 'punk', 'alternative']

for genre in genres:
    connection.execute(
        f"""INSERT INTO genre(genre_name)
            VALUES ('{genre}');"""
    )

# Заполняем связывающую таблицу  исполнитель и жанр
eltments = [(1, 3), (2, 3), (3, 3), (4, 1), (5, 2), (6, 4), (7, 5), (8, 5)]

for element in eltments:
    singer, genre = element
    connection.execute(
        f"""INSERT INTO singergenre(singer_id, genre_id)
            VALUES ('{singer}', '{genre}');"""
    )

# Заполняем таблицу альбомов.
albums = [('Dreaming Out Loud', 2007), ('Adam Levine', 1994), ('The Beatles', 1968), ('Bleach', 1989),
          ('Gusli', 2017), ('Father of All Motherfuckers', 2020), ('Showbiz', 1999), ('Meteora', 2003)]

for album in albums:
    title, year_of_start = album
    connection.execute(
        f"""INSERT INTO album(title, year_of_start)
            VALUES ('{title}', '{year_of_start}');"""
    )

# Заполняем связывающую таблицу исполнителя альбомов.
sinalbums = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]

for sinalbum in sinalbums:
    singer_id, album_id  = sinalbum
    connection.execute(
            f"""INSERT INTO singeralbum(singer_id, album_id )
                VALUES ('{singer_id}', '{album_id}');"""
    )

# Заполняем таблицу песен.
tracks = [('Mercy', '240', True, 1), ('Stop And Stare', '180', True, 1),
          ('Harder to Breathe', '173', True, 2), ('Shiver', '179', True, 2),
          ('Dear Prudence', '224', True, 3), ('Glass Onion', '137', True, 3),
          ('Blew', 175, True, 4), ('Floyd the Barber', 138, True, 4),
          ('Фокусы', 306, True, 5), ('Хватит', 199, True, 5),
          ('Graffitia', 305, True, 6), ('Junkies on a High', 291, True,6),
          ('Fillip', 240, True, 7), ('Showbiz', 316, True, 7),
          ('Don"t Stay', 308, True, 8)]

for track in tracks:
    track_title, duration, is_like, album_id = track
    connection.execute(
                f"""INSERT INTO track(track_title, duration, is_like, album_id)
                    VALUES('{track_title}', '{duration}', '{is_like}', '{album_id}');"""
    )

trs = connection.execute("""SELECT * FROM track;""").fetchall()
pprint(trs)

# Заполняем таблицу сборников.
collections = [("First", "First collection", 1968), ("Second", "Second collection", 1989),
               ("Third", "Third collection", 1994), ("Fourth", "Fourth collection", 1999),
               ("Fifth", "Fifth collection", 2003), ("Sixth", "Sixth collection", 2007),
               ("Seventh", "Seventh collection", 2017), ("Eighth", "Eighth collection", 2020)]

for collection in collections:
    collection_title, description, start_year = collection
    connection.execute(
                    f"""INSERT INTO collection(collection_title, description, start_year)
                        VALUES('{collection_title}', '{description}', '{start_year}');"""
    )

# Заполняем связывающую таблицу песен и коллекций.
elcollections = (1, 5), (1, 6),\
                (2, 7), (2, 8),\
                (3, 3), (3, 4), \
                (4, 13), (4, 14),\
                (5, 15), \
                (6, 1), (6, 2), \
                (7, 9), (7, 10), \
                (8, 11), (8, 12)

for elcollection in elcollections:
    collection_id, track_id = elcollection
    connection.execute(
                        f"""INSERT INTO trackcollection(collection_id, track_id)
                            VALUES('{collection_id}', '{track_id}');"""
    )
    



