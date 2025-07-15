from app.extensions import db
from app.models import User
from app.models import Place
from app.models import Review
from app.models import Amenity
from werkzeug.security import generate_password_hash, check_password_hash
from app.persistence.repository import SQLAlchemyRepository


class HBNBFacade:
    def __init__ (self):
        self.user_repo = SQLAlchemyRepository(User)

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

class SQLFacade(HBNBFacade):
    # --- Users ---
    def add_user(self, user_data):
        user_data['password'] = generate_password_hash(user_data.pop('password'))
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_user(self, user_id):
        return User.query.get(user_id)

    def get_all_users(self):
        return User.query.all()

    def update_user(self, user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None
        for key, value in data.items():
            if key == 'password':
                value = generate_password_hash(value)
                key = 'password_hash'
            setattr(user, key, value)
        db.session.commit()
        return user

    def verify_password(self, user, password):
        return check_password_hash(user.password_hash, password) if user else False

    # --- Places ---
    def create_place(self, data):
        place = Place(**data)
        db.session.add(place)
        db.session.commit()
        return place

    def get_place(self, place_id):
        return Place.query.get(place_id)

    def get_all_places(self):
        return Place.query.all()

    def update_place(self, place_id, data):
        place = Place.query.get(place_id)
        if not place:
            return None
        for key, value in data.items():
            setattr(place, key, value)
        db.session.commit()
        return place

    # --- Reviews ---
    def create_review(self, data):
        review = Review(**data)
        db.session.add(review)
        db.session.commit()
        return review

    def get_review(self, review_id):
        return Review.query.get(review_id)

    def get_all_reviews(self):
        return Review.query.all()

    def update_review(self, review_id, data):
        review = Review.query.get(review_id)
        if not review:
            return None
        for key, value in data.items():
            setattr(review, key, value)
        db.session.commit()
        return review

    def get_reviews_by_user(self, user_id):
        return Review.query.filter_by(user_id=user_id).all()

    def has_reviewed(self, user_id, place_id):
        return Review.query.filter_by(user_id=user_id, place_id=place_id).first() is not None

    # --- Amenities ---
    def create_amenity(self, data):
        amenity = Amenity(**data)
        db.session.add(amenity)
        db.session.commit()
        return amenity

    def get_amenity(self, amenity_id):
        return Amenity.query.get(amenity_id)

    def get_all_amenities(self):
        return Amenity.query.all()

    def update_amenity(self, amenity_id, data):
        amenity = Amenity.query.get(amenity_id)
        if not amenity:
            return None
        for key, value in data.items():
            setattr(amenity, key, value)
        db.session.commit()
        return amenity

facade = SQLFacade()