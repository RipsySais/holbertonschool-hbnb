import unittest
from app import create_app

class TestAmenityAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "WiFi"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("name", response.get_json())
        self.assertEqual(response.get_json()["name"], "WiFi")

    def test_get_all_amenities(self):
        # Crée d'abord une amenity pour s'assurer qu'on a au moins une entrée
        self.client.post('/api/v1/amenities/', json={"name": "Pool"})

        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)
        self.assertGreaterEqual(len(response.get_json()), 1)

    def test_get_nonexistent_amenity(self):
        response = self.client.get('/api/v1/amenities/nonexistent-id')
        self.assertEqual(response.status_code, 404)

    def test_update_amenity(self):
        post_response = self.client.post('/api/v1/amenities/', json={"name": "Gym"})
        amenity_id = post_response.get_json().get("id")

        put_response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={"name": "Updated Gym"})
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response.get_json()["name"], "Updated Gym")

if __name__ == '__main__':
    unittest.main()
