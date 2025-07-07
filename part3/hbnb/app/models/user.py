from app.models.base_model import BaseModel
from app import bcrypt

class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str, password: str, id: str):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id
        self.hash_password(password)  # Password should be hashed before storing

    def hash_password(self, password: str):
        """Hash the password using bcrypt and store it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """Check if the provided password matches the stored hashed password."""
        return bcrypt.check_password_hash(self.password, password)
    
    def verify_password(self, password: str) -> bool:
        """Verify the password against the stored hash."""
        return bcrypt.check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
