from app.models.review import Review
from app.persistence.repository import ReviewRepository
from app.services.user_service import UserService
from app.services.place_service import PlaceService


class ReviewService:
    def __init__(self):
        self.repository = ReviewRepository()
        self.user_service = UserService()
        self.place_service = PlaceService()

    def create_review(self, data):
        user_id = data.get('user_id')
        place_id = data.get('place_id')
        text = data.get('text')

        if not user_id or not place_id or not text:
            raise ValueError("Missing required review fields")

        if not self.user_service.get_user_by_id(user_id):
            raise ValueError("User does not exist")

        if not self.place_service.get_place(place_id):
            raise ValueError("Place does not exist")

        new_review = Review(user_id=user_id, place_id=place_id, text=text)
        self.repository.add(new_review)
        return new_review

    def get_all_reviews(self):
        return self.repository.get_all()

    def get_review(self, review_id):
        return self.repository.get(review_id)

    def update_review(self, review_id, data):
        review = self.repository.get(review_id)
        if not review:
            return None

        user_id = data.get('user_id', review.user_id)
        place_id = data.get('place_id', review.place_id)
        text = data.get('text', review.text)

        # Vérifie que le user_id mis à jour existe
        if not self.user_service.get_user_by_id(user_id):
            raise ValueError("User does not exist")

        # Vérifie que le place_id mis à jour existe
        if not self.place_service.get_place(place_id):
            raise ValueError("Place does not exist")

        # Mets à jour les attributs
        update_data = {
            'user_id': user_id,
            'place_id': place_id,
            'text': text
        }

        self.repository.update(review_id, update_data)
        return self.repository.get(review_id)
