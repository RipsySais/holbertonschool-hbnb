from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

facade = HBnBFacade()
api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'user_id': fields.String(required=True),
    'place_id': fields.String(required=True),
    'text': fields.String(required=True),
    'rating': fields.Float(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model, validate=True)
    def post(self):
        try:
            r = facade.create_review(api.payload)
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
    def put(self, review_id):
        try:
            r = facade.update_review(review_id, api.payload)
            return {
                'id': r.id, 'user_id': r.user.id,
                'place_id': r.place.id, 'text': r.text,
                'rating': r.rating
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
