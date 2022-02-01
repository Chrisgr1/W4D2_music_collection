import unittest
from models.artist import Artist

class TestTask(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Rick Astley")

    def test_artist_has_name(self):
        self.assertEqual("Rick Astley", self.artist.name)