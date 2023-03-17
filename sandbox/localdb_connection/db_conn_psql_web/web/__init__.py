from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## Database configuration ... 

app.config.from_object('config.BaseConfig')
port_ = app.config['PORT']
serv_name_ = app.config['SERV_NAME']
print("PORT: {} \t SERV_NAME: {}".format(port_, serv_name_))

db = SQLAlchemy(app)

## import views
from web.home.views import home
from web.show_data.views import show_data
from web.show_data.api import api_data

app.register_blueprint(home)
app.register_blueprint(show_data)
app.register_blueprint(api_data)

print(app.url_map)

## create the database [Ponerlo hasta que haga mi base de datos y ponga las credenciales correspondientes en el config.py]
db.create_all() 

