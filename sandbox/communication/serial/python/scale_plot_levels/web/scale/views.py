from flask import request, Blueprint, render_template, jsonify
from web.scale.utils.scale_connection import *


scale = Blueprint('scale', __name__)

@scale.route('/select_scale')
def select_scale():
    lPorts = list_ports_()
    lPorts.append({"port": 'COM_2', "desc": 'No existe'})
    return render_template("scale/select_scale.html", lPorts = lPorts)

@scale.route('/show_levels', methods = ['GET'])
def show_levels():
    port_ = request.args.get('port_')
    return render_template("scale/plot_levels.html", port_selected = port_)

@scale.route('/list_ports')
def list_ports():
    """ Getting the port list ..  """
    lPorts = list_ports_()
    lPorts.append({"port": 'COM_2', "desc": 'No existe'})
    return render_template("scale/list_ports.html", lPorts = lPorts)

@scale.route('/init_tare/<port_>', methods = ['GET'])
def init_tare(port_ = None):
    print("Port: {}".format(port_))
    connect_port(port_, 9600)
    data = {"work": "init_tare", "result": "NOK"}
    if tare_init():
        data = {"work": "init_tare", "result": "OK"}
    disconnect_port() 
    print(data)
    return jsonify(data) 

@scale.route('/get_weights/<port_>', methods = ['GET'])
def get_weights(port_ = None):
    #port_ = request.args.get('port')
    print("Port: {}".format(port_))
    connect_port(port_, 9600)
    weight = 0
    type_w = "kg"
    weight_info = ask_weight()
    if "weight" in weight_info:
        weight = weight_info["weight"]
        type_w = weight_info["type"]
    data = {"weight":"{}".format(weight), "type": type_w}
    disconnect_port() 
    print(data)
    #response = scale.response_class(response=json.dumps(data), status=200, mimetype='application/json')
    return jsonify(data)