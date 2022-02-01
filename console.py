import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

name_1 = Artist("Air")
artist_repository.new_artist(name_1)

album_1 = Album("Wish You Were Here", "Rock", "Pink Floyd")
album_repository.new_album(album_1)


pdb.set_trace()