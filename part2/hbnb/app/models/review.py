import datetime
from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    """Représente un avis sur un lieu.

    Attributs:
        text (str): Le texte de l'avis.
        rating (float): La note de l'avis, doit être comprise entre 1 et 5.
        place (Place): Le lieu concerné par l'avis.
        user (User): L'utilisateur ayant laissé l'avis.
        created_at (datetime): Date de création de l'avis.
        updated_at (datetime): Date de dernière mise à jour de l'avis.
    """

    def __init__(self, text: str, rating: float, place: Place, user: User):
        """Initialise un nouvel objet Review avec des validations."""
        super().__init__()
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)
        self.created_at = datetime.datetime.now()  # Date de création
        self.updated_at = self.created_at  # Date de dernière mise à jour

    def validate_text(self, text: str) -> str:
        """Valide que le texte de l'avis n'est pas vide."""
        if not text.strip():
            raise ValueError("Veuillez écrire un commentaire")
        return text

    def validate_rating(self, rating: float) -> float:
        """Valide que la note est comprise entre 1 et 5."""
        rating = float(rating)
        if rating < 1 or rating > 5:
            raise ValueError("La note doit être comprise entre 1 et 5")
        return rating

    def validate_place(self, place: Place) -> Place:
        """Valide que l'entité associée est bien une instance de Place."""
        if not isinstance(place, Place):
            raise ValueError("Le lieu doit être une instance de Place")
        return place

    def validate_user(self, user: User) -> User:
        """Valide que l'entité associée est bien une instance de User."""
        if not isinstance(user, User):
            raise ValueError("L'utilisateur doit être une instance de User")
        return user

    def update_review(self, new_text: str = None, new_rating: float = None) -> None:
        """Met à jour le texte et/ou la note de l'avis.

        Args:
            new_text (str, optional): Nouveau texte pour l'avis.
            new_rating (float, optional): Nouvelle note pour l'avis.
        """
        try:
            if new_text is not None:
                self.text = self.validate_text(new_text)
            if new_rating is not None:
                self.rating = self.validate_rating(new_rating)
            self.updated_at = datetime.datetime.now()  # Met à jour la date de modification
        except ValueError as e:
            print(f"Erreur lors de la mise à jour de l'avis : {e}")
