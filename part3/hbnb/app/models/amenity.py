from app.models.base_model import BaseModel
from app.extensions import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
