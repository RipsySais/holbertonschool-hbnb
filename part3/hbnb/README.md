#HBnB Project - part3

#Description

HBnB est une application web de gestion d’hébergements permettant la création, la consultation, la modification et la suppression d’utilisateurs, de lieux, d’avis et d’équipements. Ce projet met l’accent sur une architecture modulaire, la séparation des couches de présentation et de logique métier, et l’implémentation d’API RESTful avec Flask et flask-restx.

#Objectifs
Architecture modulaire : Organisation du projet en modules distincts pour la présentation (API) et la logique métier.

Logique métier : Définition des classes principales (User, Place, Review, Amenity) et de leurs relations.

API RESTful : Implémentation des endpoints CRUD pour chaque entité.

Sérialisation des données : Retour des attributs étendus pour les objets liés (ex : afficher le nom du propriétaire d’un lieu).

Tests et validation : Vérification du bon fonctionnement des endpoints et de la gestion des cas d’erreur.


#Structure du projet

part2/hbnb
├── app/
│   ├── __pycache__
│   ├── __init__.py
│   ├── api/
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __pycache__
│   │       ├── __init__.py
│   │       ├── amenities.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       └── users.py
│   ├── models/
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── amenity.py
│   │   ├── base_model.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── user.py
│   ├── persistence/
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   └── repository.py
│   └── services/
│       ├── __pycache__
│       ├── __init__.py
│       ├── amenity_service.py
│       ├── facade.py
│       ├── place_service.py
│       ├── review_service.py
│       └── user_service.py
├── tests/
│   ├── api/
│   │   ├── test_amenities.py
│   │   ├── test_places.py
│   │   ├── test_reviews.py
│   │   └── test_users.py
│   └── classes/
│       ├── test_amenities.py
│       ├── test_places.py
│       ├── test_reviews.py
│       └── test_users.py
├── README.md
├── config.py
├── requirements.txt
└── run.py

#Fonctionnalités implémentées
Gestion des utilisateurs : Création, consultation, modification, suppression.

Gestion des lieux : Ajout, consultation, modification, suppression, avec affichage du propriétaire et des équipements associés.

Gestion des avis : Création, consultation, suppression, avec lien vers l’utilisateur et le lieu concernés.

Gestion des équipements : Ajout, consultation, suppression.

Sérialisation avancée : Retour d’informations étendues pour les objets liés (ex : nom du propriétaire, liste des équipements).

#Points techniques
Flask + flask-restx : Définition et documentation automatique des API.

Pattern façade : Simplification de la communication entre la couche présentation et la logique métier.

Tests : Utilisation de Postman ou cURL pour tester les endpoints.

#Modularité : Séparation claire des responsabilités pour faciliter l’intégration future de l’authentification et du contrôle d’accès.
#Facade
Le fichier facade.py contient une classe HBnBFacade qui centralise les appels aux services métier.
python
Copier
Modifier
facade = HBnBFacade()
facade.create_place(data)
facade.get_all_amenities()
#🛠️ Services disponibles
Chaque entité (User, Place, Review, Amenity) a un service dédié avec une API REST connectée.

Ressource	Routes (RESTx)	Fonctions appelées
User	/users/	create_user, get_user, update_user, get_all_users
Place	/places/	create_place, get_place, update_place, get_all_places
Review	/reviews/	create_review, get_review, update_review, get_all_reviews
Amenity	/amenities/	create_amenity, get_amenity, update_amenity, get_all_amenities

#Prérequis
Python 3.8+

#Flask

flask-restx
flask-cors

#Le lien de l'application
- http://127.0.0.1:5000/api/v1/
#les installatios 
- pip install -r requirements.txt
- Si tu as une erreur ModuleNotFoundError: No module named 'flask_cors', installe : pip install flask flask-restx flask-cors
# le diagramme ER
![Texte alternatif](diagram.Hbnb p3-1.jpeg)

#AUTHOR
# Mahamat Abdalllah Moussa.: https://github.com/MOUSSA-info
# Ahmed Cisse.: https://github.com/RipsySais
# Georges Menhei.: https://github.com/georges479m
