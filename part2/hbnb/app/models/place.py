import requests
from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
    """Représente un lieu dans l'application.

    Attributs:
        title (str): Titre du lieu.
        description (str): Description du lieu.
        price (float): Prix du lieu.
        address (str): Adresse du lieu.
        owner (User): Propriétaire du lieu.
        amenities (str): Commodités disponibles au lieu.
        reviews (list): Liste des avis sur le lieu.
        latitude (float): Latitude du lieu.
        longitude (float): Longitude du lieu.
    """

    def __init__(self, title: str, description: str, price: float, address: str, owner: User, amenities: str):
        """Initialise un nouvel objet Place avec des validations et du géocodage."""
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.address = address
        self.owner = self.validate_owner(owner)
        self.amenities = amenities
        self.reviews = []

        # Géocodage de l'adresse
        try:
            self.latitude, self.longitude = self.geocode_address(address)
        except Exception as e:
            print(f"⚠️ Géocodage échoué : {e}")
            self.latitude, self.longitude = 0.0, 0.0  # Valeurs par défaut

        self.latitude = self.validate_latitude(self.latitude)
        self.longitude = self.validate_longitude(self.longitude)

    def validate_title(self, title: str) -> str:
        """Valide que le titre ne dépasse pas 100 caractères."""
        title = title.strip()
        if len(title) > 100:
            raise ValueError("Le titre ne peut pas dépasser 100 caractères.")
        return title

    def validate_price(self, price: float) -> float:
        """Valide que le prix est un nombre positif."""
        price = float(price)
        if price < 0:
            raise ValueError("Le prix doit être supérieur ou égal à 0.")
        return price

    def validate_owner(self, owner: User) -> User:
        """Valide que le propriétaire est bien une instance de User."""
        if not isinstance(owner, User):
            raise ValueError("Le propriétaire doit être une instance de User.")
        return owner

    def add_review(self, review: str) -> None:
        """Ajoute un avis à la liste des avis du lieu.

        Args:
            review (str): L'avis à ajouter.
        """
        if not isinstance(review, str):
            raise ValueError("L'avis doit être une chaîne de caractères.")
        self.reviews.append(review)

    def geocode_address(self, address: str) -> tuple[float, float]:
        """Utilise l'API Nominatim pour obtenir la latitude et la longitude d'une adresse.

        Args:
            address (str): L'adresse à géocoder.

        Returns:
            tuple: Latitude et longitude de l'adresse.

        Raises:
            RuntimeError: En cas d'erreur de connexion à l'API de géocodage.
        """
        try:
            response = requests.get(
                "https://nominatim.openstreetmap.org/search",
                params={"q": address, "format": "json"},
                headers={"User-Agent": "hbnb-app"}
            )
            response.raise_for_status()  # Lève une erreur si le statut HTTP n'est pas 200

            data = response.json()
            if not data:
                raise ValueError(f"Aucune donnée trouvée pour l'adresse : {address}")

            return float(data[0]["lat"]), float(data[0]["lon"])
        
        except requests.RequestException as e:
            raise RuntimeError(f"Erreur de connexion à l'API de géocodage : {e}")

    def validate_latitude(self, latitude: float) -> float:
        """Valide et corrige la latitude si nécessaire.

        Args:
            latitude (float): La latitude à valider.

        Returns:
            float: Latitude validée.
        
        Raises:
            ValueError: Si la latitude est invalide.
        """
        if not isinstance(latitude, (int, float)):
            raise ValueError("La latitude doit être un nombre.")
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude invalide : {latitude}. Elle doit être entre -90 et 90.")
        return latitude

    def validate_longitude(self, longitude: float) -> float:
        """Valide et corrige la longitude si nécessaire.

        Args:
            longitude (float): La longitude à valider.

        Returns:
            float: Longitude validée.
        
        Raises:
            ValueError: Si la longitude est invalide.
        """
        if not isinstance(longitude, (int, float)):
            raise ValueError("La longitude doit être un nombre.")
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude invalide : {longitude}. Elle doit être entre -180 et 180.")
        return longitude
