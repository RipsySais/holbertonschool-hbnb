class HBnBFacade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HBnBFacade, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Initialisation des repositories
        if not hasattr(self, 'initialized'):
            self.user_repo = InMemoryRepository()
            self.place_repo = InMemoryRepository()
            self.review_repo = InMemoryRepository()
            self.amenity_repo = InMemoryRepository()
            self.initialized = True
            print("Nouvelle instance de HBnBFacade créée.")

    # User
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        print(f"Utilisateur ajouté : {user.id}, {user.first_name} {user.last_name}")
        return user

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if user is None:
            raise ValueError(f"Utilisateur avec l'ID {user_id} non trouvé.")
        return user

    def update_user(self, user_id, user_data):
        user = self.get_user(user_id)
        if not user:
            return None
        self.user_repo.update(user.id, user_data)
        return self.user_repo.get(user.id)

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Amenity
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        self.amenity_repo.update(amenity.id, amenity_data)
        return self.amenity_repo.get(amenity.id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    # Place
    def create_place(self, place_data):
        owner = self.get_user(place_data['owner_id'])
        if not isinstance(owner, User):
            raise ValueError("Le propriétaire doit être une instance de User.")

        place = Place(
            title=place_data['title'],
            description=place_data['description'],
            price=place_data['price'],
            address=place_data['address'],
            owner=owner,
            amenities=place_data['amenities']
        )
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if place is None:
            raise ValueError(f"Place avec l'ID {place_id} non trouvé.")
        return place

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        self.place_repo.update(place.id, place_data)
        return self.place_repo.get(place.id)

    def get_all_places(self):
        return self.place_repo.get_all()

    # Review
    def create_review(self, review_data):
        user = self.get_user(review_data['user_id'])
        place = self.get_place(review_data['place_id'])

        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            user=user,
            place=place
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        self.review_repo.update(review.id, review_data)
        return review

    def delete_review(self, review_id):
        try:
            self.review_repo.delete(review_id)
            return True
        except KeyError:
            return False
