from flask import Flask
from app.api.v1 import v1_blueprint
from flask_cors import CORS
from app.extensions import db, jwt, bcrypt

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class) # Load configuration from the specified class
    app.config['JWT_SECRET_KEY'] = 'super-secret-key' # Set a secret key for JWT

    db.init_app(app) # Initialize the database
    jwt.init_app(app) # Initialize JWT
    bcrypt.init_app(app) # Initialize Bcrypt for password hashing

    CORS(app)
    app.register_blueprint(v1_blueprint)

    return app
