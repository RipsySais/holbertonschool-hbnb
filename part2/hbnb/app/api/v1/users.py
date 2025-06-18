from flask_restx import Resource
from app.api.v1 import users_namespace

@users_namespace.route('/')
class UserList(Resource):
    def get(self):
        return {"message": "Liste des utilisateurs"}

    def post(self):
        return {"message": "Créer un nouvel utilisateur"}, 201

@users_namespace.route('/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        return {"message": f"Détails de l'utilisateur {user_id}"}
