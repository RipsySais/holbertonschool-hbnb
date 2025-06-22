from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

facade = HBnBFacade()
api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True)
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    def post(self):
        try:
            user = facade.create_user(api.payload)
            return {
                'id': user.id, 'first_name': user.first_name,
                'last_name': user.last_name, 'email': user.email
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        return [
            {'id': u.id, 'first_name': u.first_name,
             'last_name': u.last_name, 'email': u.email}
            for u in facade.get_all_users()
        ], 200

@api.route('/<user_id>')
class UserResource(Resource):
    def get(self, user_id):
        try:
            user = facade.get_user(user_id)
        except ValueError:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id, 'first_name': user.first_name,
            'last_name': user.last_name, 'email': user.email
        }, 200

    @api.expect(user_model, validate=True)
    def put(self, user_id):
        try:
            u = facade.update_user(user_id, api.payload)
            return {
                'id': u.id, 'first_name': u.first_name,
                'last_name': u.last_name, 'email': u.email
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
