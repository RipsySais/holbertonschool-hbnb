from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.services.facade import facade

admin_namespace = Namespace('admin', description='Opérations administratives')

@admin_namespace.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Privileges d\'administrateur requis'}, 403

        user_data = request.json
        email = user_data.get('email')

        if facade.get_user_by_email(email):
            return {'error': 'E-mail déjà enregistré'}, 400

        new_user = facade.add_user(user_data)
        return {'message': 'Utilisateur créé avec succès', 'user_id': new_user.id}, 201

@admin_namespace.route('/users/<int:user_id>')
class AdminUserModify(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Privileges d\'administrateur requis'}, 403

        data = request.json
        email = data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'E-mail déjà utilisé'}, 400

        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'Utilisateur non trouvé'}, 404
        return {'message': 'Détails mis à jour'}, 200

@admin_namespace.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Privileges d\'administrateur requis'}, 403

        amenity_data = request.json
        new_amenity = facade.create_amenity(amenity_data)
        return {'message': 'Commodité ajoutée', 'amenity_id': new_amenity.id}, 201

@admin_namespace.route('/amenities/<int:amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Privileges d\'administrateur requis'}, 403

        amenity_data = request.json
        updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        if not updated_amenity:
            return {'error': 'Commodité non trouvée'}, 404
        return {'message': 'Commodité mise à jour'}, 200
