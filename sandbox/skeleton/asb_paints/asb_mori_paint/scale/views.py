from flask import request, Blueprint, render_template, jsonify
from asb_mori_paint.scale.utils.scale_connection import *

scale = Blueprint('scale', __name__)

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

@scale.route('/list_ports', methods = ['GET'])
def list_ports():
    """ Getting the port list ..  """
    lPorts = list_ports_()    
    data = {
        "list": lPorts
    }
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