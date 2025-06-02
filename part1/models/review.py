from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating):
        super().__init__()
        self.text = text
        self.rating = rating  # Doit être entre 1 et 5

    def validate_rating(self):
        return 1 <= self.rating <= 5
