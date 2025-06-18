from flask_restx import Namespace, Resource


places_ns = Namespace('places', description='Place operations')


@places_ns.route('/')
class Places(Resource):
    def get(self):
        return {'message': 'List of places'}

