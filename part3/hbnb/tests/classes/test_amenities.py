import unittest
import datetime
from app.models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_initialization_valid_name(self):
        # Teste l'initialisation d'un amenity avec un nom valide
        amenity = Amenity("Piscine")
        self.assertEqual(amenity.name, "Piscine")  # Vérifie que le nom est correctement assigné
        self.assertIsNotNone(amenity.id)  # Vérifie que l'id n'est pas None
        self.assertIsInstance(amenity.created_at, datetime.datetime)  # Vérifie le type de created_at

    def test_initialization_invalid_name_empty(self):
        # Teste l'initialisation d'un amenity avec un nom vide
        with self.assertRaises(ValueError):
            Amenity("")  # Doit lever une erreur

    def test_initialization_invalid_name_long(self):
        # Teste l'initialisation d'un amenity avec un nom trop long
        with self.assertRaises(ValueError):
            Amenity("A" * 51)  # 51 caractères, doit lever une erreur

    def test_update_name_valid(self):
        # Teste la mise à jour du nom de l'amenity avec un nom valide
        amenity = Amenity("Salle de sport")
        old_updated_at = amenity.updated_at  # Capture l'ancienne date de mise à jour
        amenity.update_name("Gymnase")  # Mise à jour du nom
        self.assertEqual(amenity.name, "Gymnase")  # Vérifie que le nom est mis à jour
        self.assertNotEqual(amenity.updated_at, old_updated_at)  # Vérifie que la date de mise à jour a changé

    def test_update_name_invalid(self):
        # Teste la mise à jour du nom de l'amenity avec un nom invalide
        amenity = Amenity("Sauna")
        old_updated_at = amenity.updated_at  # Capture l'ancienne date de mise à jour
        amenity.update_name("")  # Erreur prévue, le nom ne doit pas changer
        self.assertEqual(amenity.name, "Sauna")  # Vérifie que le nom n'a pas changé
        self.assertEqual(amenity.updated_at, old_updated_at)  # La date ne doit pas changer

if __name__ == "__main__":
    unittest.main()
