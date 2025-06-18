from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
from app.models.base_model import BaseModel
from flask_cors import CORS
import logging

def create_app():
    """Factory function to create the Flask application"""
    app = Flask(__name__)

    # Configuration de l'application
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',  # A remplacer par une valeur sécurisée
        DEBUG=True,  # Ne pas utiliser en production
        # Ajoutez d'autres configurations ici
    )

    # Configuration du logger
    handler = logging.FileHandler('app.log')  # Log dans un fichier
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    # Activer CORS si besoin
    CORS(app)

    # Création de l'API avec la route pour Swagger
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
    )

    # Enregistrement des namespaces (routes) pour les différentes parties de l'API
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    # Gestion des erreurs globales
    @app.errorhandler(Exception)
    def handle_error(e):
        app.logger.error(f'Une erreur est survenue : {e}')
        return {"message": "Une erreur interne est survenue."}, 500

    return app
