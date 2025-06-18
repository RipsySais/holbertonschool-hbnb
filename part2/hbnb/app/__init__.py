#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from app.api.v1 import status_ns, places_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')

    api.add_namespace(status_ns, path='/api/v1/status')
    api.add_namespace(places_ns, path='/api/v1/places')

    return app

