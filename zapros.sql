CREATE TABLE IF NOT EXISTS singer (id serial primary key, name varchar(80) not null unique);

CREATE TABLE IF NOT EXISTS genre(
 	id serial primary key,
 	genre_name varchar(50) not null unique);

CREATE TABLE IF NOT EXISTS singergenre (
    id serial primary key,
    singer_id integer references singer(id),
    genre_id integer references genre(id));

CREATE TABLE IF NOT EXISTS album (
	id serial primary key,
	title varchar(50) not null unique,
	year_of_start integer not null);

CREATE TABLE IF NOT EXISTS singeralbum (
    id serial primary key,
    singer_id integer references singer(id),
    album_id integer references album(id));

CREATE TABLE IF NOT EXISTS track(
	id serial primary key,
	track_title varchar(50) not null unique,
	duration integer not null,
	is_like boolean not null,
	album_id integer references album(id)
	);

CREATE TABLE IF NOT EXISTS collection(
	id serial primary key,
	collection_title varchar(100) not null unique,
	description text not null,
	start_year integer not null);

CREATE TABLE IF NOT EXISTS trackcollection (
    id serial primary key,
    collection_id integer references collection(id),
    track_id integer references track(id));



