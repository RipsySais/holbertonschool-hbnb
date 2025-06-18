import uuid
from datetime import datetime

class BaseModel:
    """Classe de base fournissant un identifiant unique et des timestamps.
    
    Attributs:
        id (str): Identifiant unique généré automatiquement (UUID).
        created_at (datetime): Date et heure de création de l'objet.
        updated_at (datetime): Date et heure de la dernière modification de l'objet.
    """
    
    def __init__(self):
        """Initialise un nouvel objet avec un ID unique et des timestamps."""
        self.id = str(uuid.uuid4())  # Génère un identifiant unique pour l'objet
        self.created_at = datetime.now()  # Enregistre la date de création
        self.updated_at = datetime.now()  # Enregistre la date de la dernière mise à jour

    def save(self):
        """Met à jour le timestamp updated_at lors de chaque modification."""
        self.updated_at = datetime.now()  # Met à jour l'attribut updated_at

    def update(self, data):
        """Met à jour les attributs de l'objet à partir d'un dictionnaire fourni.
        
        Args:
            data (dict): Dictionnaire de clés et valeurs à mettre à jour dans l'objet.
            
        Raises:
            AttributeError: Si une clé dans `data` ne correspond à aucun attribut de l'objet.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)  # Met à jour l'attribut avec la nouvelle valeur
            else:
                raise AttributeError(f"L'attribut '{key}' n'existe pas dans cet objet.")  # Exception pour attributs inconnus
        self.save()  # Met à jour le timestamp updated_at après modification
