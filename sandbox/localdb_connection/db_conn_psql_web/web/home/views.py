from flask import Blueprint, render_template, abort


home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    """ Testing the plotting for the container's fill level """
    return render_template("home/index.html")