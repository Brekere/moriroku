class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://DESKTOP-7U1IC0T/ASBPaints?driver=ODBC Driver 17 for SQL Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://DESKTOP-7U1IC0T/ASBPaints?driver=ODBC Driver 17 for SQL Server'
    SECRET_KEY = 'Desarrollo key'

#DRIVER={ODBC Driver 18 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;DATABASE=paints_test;Trusted_Connection=yes;
#postgresql://franco:SistemasFranco11@localhost:5432/quotation_asb