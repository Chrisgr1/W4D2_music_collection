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

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# need select function above this line
# def find_artist(id):
#     artist = None
#     sql = "SELECT * FROM tasks WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         artist = artist_repository.select(result['artist_id'])
#         artist = Artist(
#             result['name'], 
#             result['id']
#             )
#     return artist
