from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user_id: str, place_id: str, text: str):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text
        }
