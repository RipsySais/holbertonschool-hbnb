from flask_restx import Resource
from app.api.v1 import reviews_namespace

@reviews_namespace.route('/')
class ReviewList(Resource):
    def get(self):
        return {"message": "Liste des avis"}

    def post(self):
        return {"message": "Ajouter un nouvel avis"}, 201
