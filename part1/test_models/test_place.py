import unittest
from models.place import Place
from models.amenity import Amenity

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place("Maison Parisienne")

    def test_add_amenity(self):
        wifi = Amenity("WiFi")
        self.place.add_amenity(wifi)
        self.assertIn(wifi, self.place.amenities)

    def test_rating_calculation(self):
        # Ajouter des reviews simulées ici
        self.assertEqual(self.place.calculate_rating(), 4.5)
