from flask_restx import Api
from flask import Blueprint

from .users import users_api
from .auth import api as auth_api
from .places import api as places_ns
from .reviews import api as reviews_ns
from .amenities import api as amenities_ns

v1_blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(
    v1_blueprint,
    version='1.0',
    title='HBNB API',
    description='API for HBNB project'
    )

api.add_namespace(users_api, path='/users')
api.add_namespace(auth_api, path='/auth')
api.add_namespace(places_ns)
api.add_namespace(reviews_ns)
api.add_namespace(amenities_ns)
