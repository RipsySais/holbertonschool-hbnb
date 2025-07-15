import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api

from .extensions import db
from .api.v1 import v1_blueprint

from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not app.config['JWT_SECRET_KEY']:
        raise ValueError("JWT_SECRET_KEY manquante")

    # Extensions
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    # Register API Blueprint (API V1)
    app.register_blueprint(v1_blueprint)

    return app