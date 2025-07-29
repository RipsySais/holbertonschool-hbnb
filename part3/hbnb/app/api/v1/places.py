from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import facade


api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String(),
    'price': fields.Float(required=True),
    'address': fields.String(required=True),
    'owner_id': fields.String(required=True),
    'amenities': fields.List(fields.String)
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()

        # Interdire la création de place pour un autre utilisateur
        if api.payload.get('owner_id') != current_user_id:
            return {'error': 'You can only create places for yourself'}, 403

        try:
            p = facade.create_place(api.payload)
            return {
                'id': p.id, 'title': p.title, 'description': p.description,
                'price': p.price, 'address': p.address,
                'owner_id': p.owner.id, 'amenities': p.amenities
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        return [{
            'id': p.id, 'title': p.title,
            'price': p.price, 'address': p.address
        } for p in facade.get_all_places()], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        try:
            p = facade.get_place(place_id)
        except ValueError:
            return {'error': 'Place not found'}, 404
        return {
            'id': p.id, 'title': p.title, 'description': p.description,
            'price': p.price, 'address': p.address,
            'owner': {
                'id': p.owner.id, 'first_name': p.owner.first_name,
                'last_name': p.owner.last_name, 'email': p.owner.email
            },
            'amenities': [{'id': a, 'name': a} for a in p.amenities]
        }, 200

    @api.expect(place_model, validate=True)
    @jwt_required()
    def put(self, place_id):
        current_user_id = get_jwt_identity()

        try:
            place = facade.get_place(place_id)
        except ValueError:
            return {'error': 'Place not found'}, 404

        # Vérifie si l'utilisateur est bien le propriétaire
        if place.owner.id != current_user_id:
            return {'error': 'Unauthorized to update this place'}, 403

        try:
            p = facade.update_place(place_id, api.payload)
            return {
                'id': p.id, 'title': p.title, 'description': p.description,
                'price': p.price, 'address': p.address,
                'owner_id': p.owner.id, 'amenities': p.amenities
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @jwt_required()
    def delete(self, place_id):
        current_user_id = get_jwt_identity()

        try:
            place = facade.get_place(place_id)
        except ValueError:
            return {'error': 'Place not found'}, 404

        # Vérifie si l'utilisateur est bien le propriétaire
        if place.owner.id != current_user_id:
            return {'error': 'Unauthorized to delete this place'}, 403

        try:
            facade.delete_place(place_id)
            return {'message': 'Place deleted'}, 200
        except ValueError as e:
            return {'error': str(e)}, 400
