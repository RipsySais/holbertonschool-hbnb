from flask_restx import Api
from flask import Blueprint

from .users import api as users_ns
from .places import api as places_ns
from .reviews import api as reviews_ns
from .amenities import api as amenities_ns

bp_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(bp_v1, version='1.0', title='HBNB API',
          description='API for HBNB project')

api.add_namespace(users_ns)
api.add_namespace(places_ns)
api.add_namespace(reviews_ns)
api.add_namespace(amenities_ns)
