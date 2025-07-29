import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from app.services.facade import HBnBFacade
from app.models.place import Place
from app.models.user import User

class TestPlaceAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch.object(HBnBFacade, 'get_user')
    @patch.object(HBnBFacade, 'create_place')
    def test_create_place(self, mock_create_place, mock_get_user):
        # Setup a mock user
        mock_user = User(first_name='John', last_name='Doe', email='john.doe@example.com')
        mock_user.id = '12345'

        # Simulate `get_user` returning the mock user
        mock_get_user.return_value = mock_user

        place_data = {
            'title': 'Test Place',
            'description': 'A nice test place',
            'price': 100.0,
            'address': '123 Test St',
            'owner_id': mock_user.id,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenities': ['wifi', 'ac']
        }

        # Create a mock place instance
        mock_place = MagicMock(spec=Place)
        mock_place.id = '1'
        mock_place.title = place_data['title']
        mock_place.description = place_data['description']
        mock_place.price = place_data['price']
        mock_place.address = place_data['address']
        mock_place.owner = mock_user
        mock_place.latitude = place_data['latitude']
        mock_place.longitude = place_data['longitude']
        mock_place.amenities = place_data['amenities']

        # Simulate the place creation return value
        mock_create_place.return_value = mock_place

        # Test the creation of a place
        response = self.client.post('/api/v1/places/', json=place_data)

        # Assertions to check if the place was created correctly
        self.assertEqual(response.status_code, 201)
        response_json = response.get_json()
        self.assertEqual(response_json['title'], place_data['title'])
        self.assertEqual(response_json['address'], place_data['address'])
        self.assertEqual(response_json['owner_id'], place_data['owner_id'])
        self.assertEqual(response_json['latitude'], place_data['latitude'])
        self.assertEqual(response_json['longitude'], place_data['longitude'])
        self.assertIn('amenities', response_json)
        self.assertIn('wifi', response_json['amenities'])
        self.assertIn('ac', response_json['amenities'])

    # Additional tests can be defined here

if __name__ == '__main__':
    unittest.main()
