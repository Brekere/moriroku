from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def home_init():
    return render_template('home/home.html')
