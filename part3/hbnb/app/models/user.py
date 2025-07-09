from app.models.base_model import BaseModel
from app import bcrypt
from app import db

class User(BaseModel):
    __tablename__ = 'user'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def hash_password(self, password):
        """Hashes the password using bcrypt."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies the password against the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
        
    def __repr__(self):
        return f'<User {self.email}>'
    