from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


def new_album(album):
    sql = f"""
    INSERT INTO albums 
    (title, genre, artist_id) 
    VALUES 
    (%s, %s, %s)
    RETURNING id 
    """
    values = [album.title,  album.genre, album.artist.id]
    result = run_sql(sql, values)
    album.id = result[0]['id']

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)