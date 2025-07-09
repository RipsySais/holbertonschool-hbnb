from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TypeVar
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

T = TypeVar('T')  # Type générique pour les objets

class Repository(ABC):
    @abstractmethod
    def add(self, obj: T) -> None:
        pass

    @abstractmethod
    def get(self, obj_id: Any) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, obj_id: Any, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete(self, obj_id: Any) -> None:
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name: str, attr_value: Any) -> Optional[T]:
        pass


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
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)


class UserRepository(InMemoryRepository):
    pass


class PlaceRepository(InMemoryRepository):
    pass


class ReviewRepository(InMemoryRepository):
    pass


class AmenityRepository(InMemoryRepository):
    pass


class SQLAlchemyRepository:
    def __init__(self, model):
        self.model = model

    def add(self, entity):
        from app import db
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def get(self, entity_id):
        return self.model.query.get(entity_id)
    
    def get_all(self):
        return self.model.query.all()
    
    def delete(self, entity):
        from app import db
        db.session.delete(entity)
        db.session.commit()
    
    def gat_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter_by(**{attr_name: attr_value}).first()