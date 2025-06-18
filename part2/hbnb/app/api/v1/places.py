from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

facade = HBnBFacade()

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'address': fields.String(required=True, description='Address of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(404, 'Owner not found')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        owner_id = place_data['owner_id']
        owner = facade.get_user(owner_id)

        if not owner:
            return {'error': 'Owner not found'}, 404

        new_place = facade.create_place(place_data)
        
        return {
            'id': new_place.id,
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'address': new_place.address,
            'owner_id': new_place.owner.id,
            'amenities': new_place.amenities,
            # Ajoutez d'autres champs si nécessaire
        }, 201
    
    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'address': place.address,
            'owner_id': place.owner.id,
            'amenities': place.amenities,
        } for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)

        if place is None:
            return {"error": "Place not found"}, 404
        
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'address': place.address,
            'owner_id': place.owner.id,
            'amenities': place.amenities,
            # Ajoutez d'autres champs si nécessaire
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        data = api.payload

        updated_place = facade.update_place(place_id, data)

        if updated_place is None:
            return {"error": "Place not found"}, 404

        return {
            'id': updated_place.id,
            'title': updated_place.title,
            'description': updated_place.description,
            'price': updated_place.price,
            'address': updated_place.address,
            'owner_id': updated_place.owner.id,
            'amenities': updated_place.amenities,
        }, 200
