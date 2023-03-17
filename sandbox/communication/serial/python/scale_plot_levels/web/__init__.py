from flask import Flask
app = Flask(__name__)

## import views
from web.home.views import home
from web.scale.views import scale

app.register_blueprint(home)
app.register_blueprint(scale)

print(app.url_map)

