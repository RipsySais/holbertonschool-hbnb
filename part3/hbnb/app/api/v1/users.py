from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.services.facade  import facade


users_api = Namespace('users', description='User operations')
auth_api = Namespace('auth', description='Authentication operations')

user_model = users_api.model('User', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user_update_model = users_api.model('UserUpdate', {
    'first_name': fields.String(),
    'last_name': fields.String()
})

login_model = auth_api.model('Login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

# --------- Auth routes ---------

@auth_api.route('/login')
class UserLogin(Resource):
    @auth_api.expect(login_model, validate=True)
    def post(self):
        data = auth_api.payload
        user = facade.get_user_by_email(data['email'])
        if user and facade.verify_password(user, data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        return {'error': 'Invalid credentials'}, 401

# --------- User routes ---------

@users_api.route('/')
class UserList(Resource):
    @users_api.expect(user_model, validate=True)
    def post(self):
        try:
            user = facade.create_user(users_api.payload)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        users = facade.get_all_users()
        return [{
            'id': u.id,
            'first_name': u.first_name,
            'last_name': u.last_name,
            'email': u.email
        } for u in users], 200

@users_api.route('/<user_id>')
class UserResource(Resource):
    def get(self, user_id):
        try:
            user = facade.get_user(user_id)
        except ValueError:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @jwt_required()
    @users_api.expect(user_update_model, validate=True)
    def put(self, user_id):
        current_user_id = get_jwt_identity()
        if user_id != current_user_id:
            return {'error': 'Unauthorized'}, 403
        data = users_api.payload
        # Exclude email and password updates
        data.pop('email', None)
        data.pop('password', None)
        try:
            user = facade.update_user(user_id, data)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
