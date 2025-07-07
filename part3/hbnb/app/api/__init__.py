from flask import Blueprint
from .v1 import v1_blueprint  # Doit correspondre au nom réel de ton blueprint

bp_api = Blueprint('api', __name__, url_prefix='/api')

bp_api.register_blueprint(v1_blueprint)
