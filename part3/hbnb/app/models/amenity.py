from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
