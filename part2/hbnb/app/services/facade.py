from app.services.user_service import UserService
from app.services.place_service import PlaceService
from app.services.review_service import ReviewService
from app.services.amenity_service import AmenityService


class HBnBFacade:
    def __init__(self):
        self.user_service = UserService()
        self.place_service = PlaceService()
        self.review_service = ReviewService()
        self.amenity_service = AmenityService()

    def create_user(self, data):
        return self.user_service.create_user(data)

    def get_user(self, user_id):
        return self.user_service.get_user(user_id)

    def get_all_users(self):
        return self.user_service.get_all_users()

    def update_user(self, user_id, data):
        return self.user_service.update_user(user_id, data)

    def create_place(self, data):
        return self.place_service.create_place(data)

    def get_place(self, place_id):
        return self.place_service.get_place(place_id)

    def get_all_places(self):
        return self.place_service.get_all_places()

    def update_place(self, place_id, data):
        return self.place_service.update_place(place_id, data)

    def create_review(self, data):
        return self.review_service.create_review(data)

    def get_review(self, review_id):
        return self.review_service.get_review(review_id)

    def get_all_reviews(self):
        return self.review_service.get_all_reviews()

    def update_review(self, review_id, data):
        return self.review_service.update_review(review_id, data)

    
    def create_amenity(self, data):
        return self.amenity_service.create_amenity(data)

    def get_amenity(self, amenity_id):
        return self.amenity_service.get_amenity(amenity_id)

    def get_all_amenities(self):
        return self.amenity_service.get_all_amenities()

    def update_amenity(self, amenity_id, data):
        return self.amenity_service.update_amenity(amenity_id, data)
