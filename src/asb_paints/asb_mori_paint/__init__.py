from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *


app = Flask(__name__)
main_path = app.root_path

CORS(app)

app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

from asb_mori_paint.scale.views import scale
from asb_mori_paint.historical.api import api_data 
from asb_mori_paint.home.home_controller import home
from asb_mori_paint.mixing.mixing_controller import mixing
from asb_mori_paint.viscosity.viscosity_controller import viscosity
from asb_mori_paint.improved_mix.improved_controller import improved
from asb_mori_paint.zpl.view import zpl

app.register_blueprint(home)
app.register_blueprint(scale)
app.register_blueprint(mixing)
app.register_blueprint(api_data)
app.register_blueprint(improved)
app.register_blueprint(viscosity)
app.register_blueprint(zpl)

with app.app_context():
    db.create_all()