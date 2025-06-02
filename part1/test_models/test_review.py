import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_valid_rating(self):
        review = Review("Super séjour", 5)
        self.assertTrue(review.validate_rating())

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            Review("Mauvais séjour", 6)
