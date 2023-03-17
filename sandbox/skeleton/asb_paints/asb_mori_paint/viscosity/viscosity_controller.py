from flask import Blueprint, render_template

viscosity = Blueprint('viscosity', __name__)

@viscosity.route('/viscosity', methods=['GET'])
def viscosity_init():
    return render_template('viscosity/viscosity.html')

@viscosity.route('/viscosity/container', methods=['GET'])
def viscosity_cont():
    return render_template('viscosity/vis_cont_detail.html')