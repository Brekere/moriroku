from flask import Flask
app = Flask(__name__)

## import views
from web.home.views import home

app.register_blueprint(home)
