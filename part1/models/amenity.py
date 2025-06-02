from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def check_availability(self):
        # À implémenter selon la logique métier
        return True
