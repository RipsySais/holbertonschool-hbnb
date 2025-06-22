from flask import Blueprint

from .v1 import bp_v1

bp_api = Blueprint('api', __name__, url_prefix='/api')

bp_api.register_blueprint(bp_v1)
