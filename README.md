# HBnB Evolution - Documentation Technique

## Architecture Globale
![Diagramme des Packages](API-Architecture.mmd)

### Couche Présentation
- **Responsabilités** : 
  - Gestion des routes API (Flask)
  - Sérialisation/Désérialisation JSON
  - Gestion des codes HTTP
- **Composants** :
  - `api/places.py` : Endpoints pour les lieux
  - `serializers.py` : Conversion objets ↔ JSON

### Couche Métier
- **Responsabilités** :
  - Validation des données métier
  - Implémentation des règles de gestion
  - Gestion des relations entre entités
- **Composants** :
  - `models/place.py` : Modèle Place avec méthodes métier
  - `services/place_service.py` : Logique de création des lieux

### Couche Persistence
- **Responsabilités** :
  - Abstraction de la base de données
  - Implémentation du CRUD
  - Gestion des transactions
- **Composants** :
  - `repositories/place_repository.py` : Accès DB pour les lieux
  - `database.py` : Configuration SQLAlchemy

---

## Modèle de Domaine
![Diagramme de Classes](Classe-UML.md)

### Entité Place





# THE DIAGRAMS 

    -- package_diagram.png
 ![Alt text](https://github.com/MOUSSA-info/holbertonschool-hbnb/blob/9c3e42e44d08b2343d4ff63bea08c31ac1e94543/package_diagram%20.png)
    
    ── class_diagram.png
![Alt text](https://github.com/MOUSSA-info/holbertonschool-hbnb/blob/024020f0aeb23c88b5fb4789b2813ca1be67a28b/class%20diagram.png)

    ── user_registration.png
![Alt text](https://github.com/MOUSSA-info/holbertonschool-hbnb/blob/6ad5b984f1d5ee247360894f4efd27f764aefae4/%3Auser_registration.png)

── place_creation.png
![Alt text]()

  --diagram task 01


![Texte alternatif](https://github.com/MOUSSA-info/holbertonschool-hbnb/blob/ab3d382106cab5da9ab1b42141f6c4f16e3d0355/diagrame.png)


-- diagram de sequence task 02

![Texte alternatif](https://github.com/MOUSSA-info/holbertonschool-hbnb/blob/56eca113374202294a0f57d675bae1c20d44c731/Diagram_de_sequence.png)
