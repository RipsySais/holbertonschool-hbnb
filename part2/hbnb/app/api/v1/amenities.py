from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

facade = HBnBFacade()
api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True)
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model, validate=True)
    def post(self):
        try:
            a = facade.create_amenity(api.payload)
            return {'id': a.id, 'name': a.name}, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        return [{'id': a.id, 'name': a.name} 
                for a in facade.get_all_amenities()], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    def get(self, amenity_id):
        a = facade.get_amenity(amenity_id)
        if not a:
            return {'error': 'Amenity not found'}, 404
        return {'id': a.id, 'name': a.name}, 200

    @api.expect(amenity_model, validate=True)
    def put(self, amenity_id):
        a = facade.update_amenity(amenity_id, api.payload)
        if not a:
            return {'error': 'Amenity not found'}, 404
        return {'id': a.id, 'name': a.name}, 200
