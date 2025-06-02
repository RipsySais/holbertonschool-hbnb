from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description="", number_rooms=0, number_bathrooms=0,
                 max_guest=0, price_by_night=0.0, latitude=None, longitude=None):
        super().__init__()
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def calculate_rating(self):
        if not self.reviews:
            return None
        return sum(review.rating for review in self.reviews) / len(self.reviews)
