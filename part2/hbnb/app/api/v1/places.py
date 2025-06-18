from flask_restx import Resource
from app.api.v1 import places_namespace

@places_namespace.route('/')
class PlaceList(Resource):
    def get(self):
        return {"message": "Liste des lieux"}

    def post(self):
        return {"message": "Créer un nouvel endroit"}, 201
