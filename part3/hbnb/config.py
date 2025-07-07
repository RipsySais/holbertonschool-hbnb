import os

class Config:
    """ Classe de configuration de base pour l'application """
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Clé secrète pour l'application
    DEBUG = False  # Indicateur de mode debug, par défaut désactivé


class DevelopmentConfig(Config):
    """ Classe de configuration pour l'environnement de développement """
    DEBUG = True  # Active le mode debug


class ProductionConfig(Config):
    """ Classe de configuration pour l'environnement de production """
    DEBUG = False  # Désactive le mode debug


config = {
    'development': DevelopmentConfig,  # Configuration pour l'environnement de développement
    'default': DevelopmentConfig  # Configuration par défaut, utilisée en développement
}
