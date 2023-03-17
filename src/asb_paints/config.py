class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key5&6423v-daD2?s'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:asbsistemas@localhost:5432/local_mixing_process"
    #SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://sa:ASB.13@192.168.0.47/moriroku'
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:ASB.13@192.168.0.26/local_mixing_process?driver=ODBC Driver 17 for SQL Server'
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://DESKTOP-7U1IC0T/local_mixing_process?driver=ODBC Driver 17 for SQL Server'
    #SQLALCHEMY_DATABASE_URI = "postgresql://franco:SistemasFranco11@localhost:5432/local_mixing_process"
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:asB#.19@localhost:5432/local_mixing_process"
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Moriroku.2022@localhost:5432/local_mixing_process"
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:asb.13@192.168.0.40/pyalmacen?driver=ODBC Driver 17 for SQL Server'
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


#DRIVER={ODBC Driver 18 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;DATABASE=paints_test;Trusted_Connection=yes;
#postgresql://franco:SistemasFranco11@localhost:5432/quotation_asb 
#SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://DESKTOP-7U1IC0T/ASBPaints?driver=ODBC Driver 17 for SQL Server'