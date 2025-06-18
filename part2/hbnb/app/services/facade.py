from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Méthode d'espace réservé pour créer un utilisateur
    def create_user(self, user_data):
        # La logique sera implémentée dans les tâches suivantes
        pass

    # Méthode d'espace réservé pour récupérer un endroit par ID
    def get_place(self, place_id):
        # La logique sera implémentée dans les tâches suivantes
        pass
