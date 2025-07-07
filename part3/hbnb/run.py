import os
from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from models import db
from app.admin_routes import admin_namespace
from app.user_routes import user_namespace

# Charger les variables d'environnement avant toute chose
load_dotenv()

# Créer une instance Flask
app = Flask(__name__)

# Charger la clé secrète depuis l'environnement
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # ex: sqlite:///hbnb_dev.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if not app.config['JWT_SECRET_KEY']:
    raise ValueError("La variable d'environnement JWT_SECRET_KEY est manquante.")

# Initialiser JWT
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)

# Initialiser Flask-Restx API
api = Api(app)
api.add_namespace(admin_namespace)
api.add_namespace(user_namespace)

if __name__ == '__main__':
    app.run(debug=True)
