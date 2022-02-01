DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY
    title VARCHAR(255)
    genre VARCHAR(255)
    artist VARCHAR(255) REFERENCES artists(name)
);