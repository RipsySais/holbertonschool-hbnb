import unittest
from app.models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Nettoie les emails utilisés avant chaque test."""
        User.used_emails.clear()

    def test_user_creation_valid(self):
        """Test la création d'un utilisateur valide."""
        user = User("John", "Doe", "john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertFalse(user.is_admin)

    def test_user_creation_admin(self):
        """Test la création d'un utilisateur administrateur."""
        user = User("Admin", "User", "admin@example.com", is_admin=True)
        self.assertTrue(user.is_admin)

    def test_invalid_first_name_length(self):
        """Test un prénom trop long."""
        with self.assertRaises(ValueError) as context:
            User("A" * 51, "Doe", "longname@example.com")
        self.assertEqual(str(context.exception), "Seulement 50 caractères sont autorisés")

    def test_invalid_last_name_length(self):
        """Test un nom de famille trop long."""
        with self.assertRaises(ValueError) as context:
            User("John", "B" * 51, "longlastname@example.com")
        self.assertEqual(str(context.exception), "Seulement 50 caractères sont autorisés")

    def test_invalid_email_format(self):
        """Test un format d'email invalide."""
        with self.assertRaises(ValueError) as context:
            User("John", "Doe", "invalid-email")
        self.assertEqual(str(context.exception), "Email invalide")

    def test_empty_email(self):
        """Test un email vide."""
        with self.assertRaises(ValueError) as context:
            User("John", "Doe", "")
        self.assertEqual(str(context.exception), "Email invalide")

    def test_none_email(self):
        """Test un email None."""
        with self.assertRaises(ValueError) as context:
            User("John", "Doe", None)
        self.assertEqual(str(context.exception), "Email invalide")

    def test_duplicate_email(self):
        """Test la création avec un email déjà utilisé."""
        User("John", "Doe", "unique@example.com")
        with self.assertRaises(ValueError) as context:
            User("Jane", "Doe", "unique@example.com")
        self.assertEqual(str(context.exception), "Cet Email est déjà utilisé")


if __name__ == "__main__":
    unittest.main()
