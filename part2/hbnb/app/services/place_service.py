from app.models.place import Place
from app.persistence.repository import PlaceRepository
from app.services.user_service import UserService


class PlaceService:
    def __init__(self):
        self.repository = PlaceRepository()
        self.user_service = UserService()

    def create_place(self, data):
        user_id = data.get('user_id')
        name = data.get('name')
        description = data.get('description')
        longitude = data.get('longitude')
        latitude = data.get('latitude')
        amenities = data.get('amenities')

        if not user_id or not name or not longitude or not latitude:
            raise ValueError("Missing required place fields")

        # Vérifie que l'utilisateur existe
        if not self.user_service.get_user(user_id):
            raise ValueError("User does not exist")

        new_place = Place(
            user_id=user_id,
            name=name,
            description=description,
            longitude=longitude,
            latitude=latitude,
            amenities=amenities
        )
        self.repository.add(new_place)
        return new_place

    def get_all_places(self):
        return self.repository.get_all()

    def get_place(self, place_id):
        return self.repository.get(place_id)

    def update_place(self, place_id, data):
        place = self.repository.get(place_id)
        if not place:
            return None

        place.name = data.get('name', place.name)
        place.description = data.get('description', place.description)
        place.city = data.get('city', place.city)
        place.user_id = data.get('user_id', place.user_id)
        place.amenities = data.get('amenities', place.amenities)

        # On vérifie que le nouvel utilisateur (s’il est modifié) existe
        if not self.user_service.get_user(place.user_id):
            raise ValueError("User does not exist")
        
        self.repository.update(place_id, {
            'name': place.name,
            'description': place.description,
            'city': place.city,
            'user_id': place.user_id,
            'amenities': place.amenities
        })
        
        return place
