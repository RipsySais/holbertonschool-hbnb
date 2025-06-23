#HBnB Project
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

# Fonctionnalités implémentées
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

#Prérequis
Python 3.8+

#Flask

flask-restx
flask-cors
# AUTHOR
# Mahamat Abdalllah Moussa
 
# Ahmed Cisse
 
# Georges Menheim
