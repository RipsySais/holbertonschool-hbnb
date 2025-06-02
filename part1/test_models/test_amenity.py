import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_availability(self):
        pool = Amenity("Piscine")
        self.assertTrue(pool.check_availability())
