from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
