import sqlalchemy
from pprint import pprint

engen = sqlalchemy.create_engine('postgresql://netpy:0703@localhost:5432/netpy44')
connection = engen.connect()

# sel = connection.execute(
#     """SELECT title, year_of_start FROM album
#     WHERE year_of_start = '2018';"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT track_title, duration
#     FROM track
#     ORDER BY duration DESC
#     LIMIT 1;"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT track_title
#     FROM track
#     WHERE duration >= '210';"""
# ).fetchall()

# sel = connection.execute(
#     """SELECT collection_title
#     FROM collection
#     WHERE start_year
#     BETWEEN 2018 AND 2021;"""
# ).fetchall

# sel = connection.execute(
#     """SELECT name
#     FROM singer
#     WHERE (LENGTH(name) - LENGTH(replace(name, ' ', '')) + 1) = 1;"""
# ).fetchall()

sel = connection.execute(
    """SELECT track_title
    FROM track
    WHERE track_title
    LIKE '%%my%%'
    OR track_title
    LIKE '%%My%% or %%мой%%';"""
).fetchall()

pprint(sel)