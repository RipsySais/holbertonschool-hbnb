from flask_restx import Resource
from app.api.v1 import amenities_namespace

@amenities_namespace.route('/')
class AmenityList(Resource):
    def get(self):
        return {"message": "Liste des commodités"}

    def post(self):
        return {"message": "Ajouter une nouvelle commodité"}, 201
