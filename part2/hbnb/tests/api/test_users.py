import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()  # Crée une instance de l'application Flask
        self.client = self.app.test_client()  # Crée un client de test pour l'application

    def test_create_user(self):
        # Test de la création d'un utilisateur avec des données valides
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)  # Vérifie que la réponse a un code de statut 201

    def test_create_user_invalid_data(self):
        # Test de la création d'un utilisateur avec des données invalides
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)  # Vérifie que la réponse a un code de statut 400

if __name__ == '__main__':
    unittest.main()  # Exécute les tests
