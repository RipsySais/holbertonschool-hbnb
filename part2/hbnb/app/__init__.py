from flask import Flask
from app.api.v1 import v1_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        DEBUG=True
    )

    CORS(app)
    app.register_blueprint(v1_blueprint)

    return app
