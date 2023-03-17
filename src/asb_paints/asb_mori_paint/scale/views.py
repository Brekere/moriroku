from flask import request, Blueprint, render_template, jsonify
from asb_mori_paint.scale.utils.scale_connection import *
from asb_mori_paint.utils.error_handlers_api import *

scale = Blueprint('scale', __name__)

@scale.route('/init_tare/<port_>', methods = ['GET'])
def init_tare(port_ = None):
    print("Port: {}".format(port_))
    port_connected = connect_port(port_, 9600)
    if port_connected:
        if tare_init():
            data_result = {"work": "init_tare", "result": "OK"}
            disconnect_port()
            data = create_response_data(restSuccess, "", None, data_result)
        else:
            data_result = {"work": "init_tare", "result": "NOK"}
            data = create_response_data(restError, "No se pudo inicializar la Tara", None, data_result) 
    else:
        data = create_response_data(restError, "No se pudo conectar al puerto, revise la conexión física y/o los controladores")
    return jsonify(data) 

@scale.route('/list_ports', methods = ['GET'])
def list_ports():
    """ Getting the port list ..  """
    lPorts = list_ports_()  
    if len(lPorts) > 0:  
        data_result = {
            "list": lPorts
        }
        data = create_response_data(restSuccess, "Lista de puertos disponibles!", None, data_result) 
    else:
        data = create_response_data(restError, "No hay puertos disponibles a los que conectarse")
    return jsonify(data)

@scale.route('/get_weights/<port_>', methods = ['GET'])
def get_weights(port_ = None):
    print("Port: {}".format(port_))
    if connect_port(port_, 9600):
        weight = 0
        type_w = "kg"
        weight_info = ask_weight()
        if "weight" in weight_info:
            weight = weight_info["weight"]
            type_w = weight_info["type"]
            error_ = weight_info["error"] 
            if error_:
                data_result = {"weight":"{}".format(weight), "type": type_w, "error": error_} 
                list_errors = [weight_info["info_error"]]
                data = create_response_data(restWarning, "Error al obtener el peso!", list_errors, data_result)
            else:
                data_result = {"weight":"{}".format(weight), "type": type_w, "error": error_} 
                data = create_response_data(restSuccess, "Peso obtendio correctamente!", None, data_result)
        else:
            data = create_response_data(restError, "Internal error en weight_info")
        disconnect_port()
    else:
        data = create_response_data(restError, "No hay puertos disponibles a los que conectarse") 
    return jsonify(data)



## -------------------------- Autodetectar báscula

@scale.route('/api/init_tare', methods = ['GET'])
def api_init_tare():#port_ = None):
    #print("Port: {}".format(port_))
    port_connected = auto_connect() # connect_port(port_, 9600)
    if port_connected:
        if tare_init():
            data_result = {"work": "init_tare", "result": "OK"}
            data = create_response_data(restSuccess, "", None, data_result)
        else:
            data_result = {"work": "init_tare", "result": "NOK"}
            data = create_response_data(restError, "No se pudo inicializar la Tara", None, data_result) 
        disconnect_port()
    else:
        data = create_response_data(restError, "No se pudo conectar al puerto, revise la conexión física y/o los controladores")
    return jsonify(data)

@scale.route('/api/get_weights', methods = ['GET'])
def api_get_weights():#port_ = None):
    #print("Port: {}".format(port_))
    if auto_connect(): # connect_port(port_, 9600):
        weight = 0
        type_w = "kg"
        weight_info = ask_weight()
        if "weight" in weight_info:
            weight = weight_info["weight"]
            type_w = weight_info["type"]
            error_ = weight_info["error"] 
            if error_:
                data_result = {"weight":"{}".format(weight), "type": type_w, "error": error_} 
                list_errors = [weight_info["info_error"]]
                data = create_response_data(restWarning, "Error al obtener el peso!", list_errors, data_result)
            else:
                data_result = {"weight":"{}".format(weight), "type": type_w, "error": error_} 
                data = create_response_data(restSuccess, "Peso obtendio correctamente!", None, data_result)
        else:
            data = create_response_data(restError, "Internal error en weight_info")
        disconnect_port()
    else:
        data = create_response_data(restError, "No hay puertos disponibles a los que conectarse") 
    return jsonify(data)