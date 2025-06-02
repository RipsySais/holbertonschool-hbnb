import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("test@example.com", "securepassword")

    def test_authentication(self):
        self.assertTrue(self.user.authenticate("securepassword"))
        self.assertFalse(self.user.authenticate("wrongpassword"))

    def test_user_attributes(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "")
