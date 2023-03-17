from flask import Blueprint, render_template

improved = Blueprint('improved', __name__)

@improved.route('/improvedMix', methods=['GET'])
def improved_mix():
    return render_template('improved_mix/main_improved.html')

@improved.route('/improvedMix/substances', methods=['GET'])
def improved_subs():
    return render_template('improved_mix/improve_sus.html')