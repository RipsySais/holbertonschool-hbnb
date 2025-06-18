from flask_restx import Namespace

users_namespace = Namespace('users', description='Opérations liées aux utilisateurs')
places_namespace = Namespace('places', description='Opérations liées aux lieux')
reviews_namespace = Namespace('reviews', description='Opérations liées aux avis')
amenities_namespace = Namespace('amenities', description='Opérations liées aux commodités')

# Exemple d'enregistrement d'un espace de noms
def register_api(api):
    api.add_namespace(users_namespace)
    api.add_namespace(places_namespace)
    api.add_namespace(reviews_namespace)
    api.add_namespace(amenities_namespace)
