from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def new_artist(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all_artists():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_all_artists():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id]'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = Artist(result['name'], result['id'] )
    return user