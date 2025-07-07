from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade
from facade import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'place_id': fields.String(required=True),
    'text': fields.String(required=True),
    'rating': fields.Float(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()
            data = api.payload
            data['user_id'] = current_user_id

            # Vérifie si l'utilisateur tente de reviewer son propre lieu
            place = facade.get_place(data['place_id'])
            if place and place.user.id == current_user_id:
                return {'error': 'You cannot review your own place.'}, 403

            # Vérifie si l'utilisateur a déjà review ce lieu
            if facade.has_reviewed(current_user_id, data['place_id']):
                return {'error': 'You have already reviewed this place.'}, 409

            r = facade.create_review(data)
            return {
                'id': r.id, 'user_id': r.user.id,
                'place_id': r.place.id, 'text': r.text,
                'rating': r.rating
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        return [{
            'id': r.id, 'user_id': r.user.id,
            'place_id': r.place.id, 'text': r.text,
            'rating': r.rating
        } for r in facade.get_all_reviews()], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    def get(self, review_id):
        r = facade.get_review(review_id)
        if not r:
            return {'error': 'Review not found'}, 404
        return {
            'id': r.id, 'user_id': r.user.id,
            'place_id': r.place.id, 'text': r.text,
            'rating': r.rating
        }, 200

    @api.expect(review_model, validate=True)
    @jwt_required()
    def put(self, review_id):
        try:
            current_user_id = get_jwt_identity()
            existing_review = facade.get_review(review_id)

            if not existing_review:
                return {'error': 'Review not found'}, 404

            if existing_review.user.id != current_user_id:
                return {'error': 'You can only edit your own review.'}, 403

            data = api.payload
            data['user_id'] = current_user_id
            data['place_id'] = existing_review.place.id  # empêcher modification du place_id

            r = facade.update_review(review_id, data)
            return {
                'id': r.id, 'user_id': r.user.id,
                'place_id': r.place.id, 'text': r.text,
                'rating': r.rating
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400

