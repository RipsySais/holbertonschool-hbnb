from app.models.base_model import BaseModel
from typing import List

class Place(BaseModel):
    def __init__(self, user_id: str, name: str, description: str = ""):
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.longitude = 0.0
        self.latitude = 0.0
        self.description = description
        self.amenities: List[str] = []

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'description': self.description,
            'amenities': self.amenities
        }
