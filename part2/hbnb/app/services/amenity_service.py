from app.models.amenity import Amenity
from app.repositories.in_memory_repository import InMemoryRepository


class AmenityService:
    def __init__(self):
        self.repository = InMemoryRepository()

    def create_amenity(self, data):
        name = data.get("name")
        if not name:
            raise ValueError("Missing required field: name")

        amenity = Amenity(name=name)
        self.repository.add(amenity)
        return amenity

    def get_all_amenities(self):
        return self.repository.get_all()

    def get_amenity(self, amenity_id):
        return self.repository.get(amenity_id)

    def update_amenity(self, amenity_id, data):
        amenity = self.repository.get(amenity_id)
        if not amenity:
            return None

        amenity.name = data.get("name", amenity.name)
        self.repository.update(amenity_id, {'name': amenity.name})
        return amenity

