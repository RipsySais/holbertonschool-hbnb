import re
from app.models.base_model import BaseModel

class User(BaseModel):
    """Représente un utilisateur de l'application.

    Attributs:
        first_name (str): Prénom de l'utilisateur.
        last_name (str): Nom de famille de l'utilisateur.
        email (str): Adresse email de l'utilisateur.
        is_admin (bool): Indique si l'utilisateur est un administrateur.
        places (list): Liste des lieux associés à l'utilisateur.
        used_emails (set): Ensemble pour stocker les emails déjà utilisés.
    """

    used_emails = set()  # Ensemble pour stocker les emails déjà utilisés 

    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        """Initialise un nouvel utilisateur avec des validations."""
        super().__init__()
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin  # Indique si l'utilisateur est un administrateur 
        self.places = []  # Liste vide pour les lieux

    def validate_name(self, name: str) -> str:
        """Valide que le nom ne dépasse pas 50 caractères."""
        if len(name) > 50:
            raise ValueError("Seulement 50 caractères sont autorisés")
        return name

    def validate_email(self, email: str) -> str:
        """Valide le format de l'email et assure son unicité.

        Args:
            email (str): L'adresse email à valider.

        Returns:
            str: L'email validé.

        Raises:
            ValueError: Si l'email est invalide ou déjà utilisé.
        """
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Email invalide")
        if email in User.used_emails:
            raise ValueError("Cet Email est déjà utilisé")
        User.used_emails.add(email)  # Ajoute l'email à l'ensemble des emails utilisés 
        return email

    @classmethod
    def reset_used_emails(cls):
        """Réinitialise la liste des emails utilisés (utile pour les tests)."""
        cls.used_emails.clear()
