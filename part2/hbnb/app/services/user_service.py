from app.persistence.repository import UserRepository
from app.models.user import User
import uuid

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def get_all_users(self):
        return self.repo.get_all()

    def get_user_by_id(self, user_id):
        return self.repo.get(user_id)

    def get_user_by_email(self, email):
        return self.repo.get_by_attribute("email", email)

    def create_user(self, user_data):
        if self.get_user_by_email(user_data["email"]):
            raise ValueError("Email already registered")

        user = User(
            # si User hérite de BaseModel, l'id est déjà généré automatiquement
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"]
        )
        self.repo.add(user)
        return user

    def update_user(self, user_id, user_data):
        user = self.repo.get(user_id)
        if not user:
            return None

        # Optionnel : vérifier si l'email est déjà pris par un autre utilisateur
        existing_user = self.get_user_by_email(user_data["email"])
        if existing_user and existing_user.id != user_id:
            raise ValueError("Email already registered by another user")

        self.repo.update(user_id, {
            "first_name": user_data.get("first_name", user.first_name),
            "last_name": user_data.get("last_name", user.last_name),
            "email": user_data.get("email", user.email)
        })
        return self.repo.get(user_id)
