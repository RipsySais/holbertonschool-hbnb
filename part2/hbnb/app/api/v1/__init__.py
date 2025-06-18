#!/usr/bin/python3
from flask_restx import Namespace, Resource


status_ns = Namespace('status', description='Status operations')
places_ns = Namespace('places', description='Place operation')

@status_ns.route('/')
class Status(Resource):
    def get(self):
        return {'message': 'API is working!'}

@places_ns.route('/')
class Places(Resource):
    def get(self):
        return {'message': 'List of places'}

