from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TypeVar
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

T = TypeVar('T')  # Type générique pour tous les objets manipulés


# Interface générique de dépôt (Repository)
class Repository(ABC):
    @abstractmethod
    def add(self, obj: T) -> None:
        """Ajoute un objet au dépôt"""
        pass

    @abstractmethod
    def get(self, obj_id: Any) -> Optional[T]:
        """Récupère un objet par son ID"""
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Récupère tous les objets"""
        pass

    @abstractmethod
    def update(self, obj_id: Any, data: Dict[str, Any]) -> None:
        """Met à jour un objet"""
        pass

    @abstractmethod
    def delete(self, obj_id: Any) -> None:
        """Supprime un objet par son ID"""
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name: str, attr_value: Any) -> Optional[T]:
        """Recherche un objet par un attribut"""
        pass


# Dépôt en mémoire (utilisé pour les tests ou dev sans base de données)
class InMemoryRepository(Repository):
    def __init__(self):
        self._storage: Dict[Any, T] = {}

    def add(self, obj: T) -> None:
        self._storage[obj.id] = obj

    def get(self, obj_id: Any) -> Optional[T]:
        print(f"Recherche dans le dépôt avec l'ID : {obj_id}")
        print("Objets dans le dépôt :", list(self._storage.keys()))
        return self._storage.get(obj_id)

    def get_all(self) -> List[T]:
        return list(self._storage.values())

    def update(self, obj_id: Any, data: Dict[str, Any]) -> None:
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
                else:
                    raise ValueError(f"L'attribut '{key}' n'existe pas sur l'objet.")
        else:
            raise KeyError(f"Objet avec l'ID '{obj_id}' non trouvé.")

    def delete(self, obj_id: Any) -> None:
        if obj_id in self._storage:
            del self._storage[obj_id]
        else:
            raise KeyError(f"Objet avec l'ID '{obj_id}' non trouvé.")

    def get_by_attribute(self, attr_name: str, attr_value: Any) -> Optional[T]:
        return next((obj for obj in self._storage.values()
                     if getattr(obj, attr_name, None) == attr_value), None)


# Dépôts spécialisés (héritent du dépôt générique en mémoire)
class UserRepository(InMemoryRepository):
    pass

class PlaceRepository(InMemoryRepository):
    pass

class ReviewRepository(InMemoryRepository):
    pass

class AmenityRepository(InMemoryRepository):
    pass


# Dépôt SQLAlchemy (base réelle en production)
class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, entity: T) -> None:
        from app import db
        db.session.add(entity)
        db.session.commit()

    def get(self, entity_id: Any) -> Optional[T]:
        return self.model.query.get(entity_id)

    def get_all(self) -> List[T]:
        return self.model.query.all()

    def update(self, entity_id: Any, data: Dict[str, Any]) -> None:
        from app import db
        entity = self.get(entity_id)
        if not entity:
            raise ValueError(f"{self.model.__name__} avec l'ID '{entity_id}' non trouvé.")
        for key, value in data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
            else:
                raise ValueError(f"L'attribut '{key}' n'existe pas sur le modèle.")
        db.session.commit()

    def delete(self, entity_id: Any) -> None:
        from app import db
        entity = self.get(entity_id)
        if not entity:
            raise ValueError(f"{self.model.__name__} avec l'ID '{entity_id}' non trouvé.")
        db.session.delete(entity)
        db.session.commit()

    def get_by_attribute(self, attr_name: str, attr_value: Any) -> Optional[T]:
        return self.model.query.filter_by(**{attr_name: attr_value}).first()
