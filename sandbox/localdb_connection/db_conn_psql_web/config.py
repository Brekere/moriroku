class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key5&6423v-daD2?s'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:asB#.19@localhost:5432/local_mixing_process"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PATH_APP = "web"
    PORT = "5055"
    SERV_NAME = "0.0.0.0"
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Key5&6423v-daD2?s'