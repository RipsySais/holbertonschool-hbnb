from app.models.base_model import BaseModel
from app.extensions import db

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(512), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __init__(self, text, rating):
        super().__init__()
        self.text = text
        self.rating = rating

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating
        }
