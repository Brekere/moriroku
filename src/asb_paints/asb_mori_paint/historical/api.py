#from shutil import ExecError

from importlib.resources import path
from flask import Blueprint, jsonify, request
from matplotlib.pyplot import get
#import pathlib

from sqlalchemy import false, func, true
import json
from asb_mori_paint import db, main_path
from datetime import datetime, timedelta
import os
from asb_mori_paint.Components.models.component_type import ComponentType
from asb_mori_paint.Components.models.components import Components
from asb_mori_paint.Formulas.models.formulas_components import FormulaComponent
from asb_mori_paint.Models.models.models import Models

#### 
from asb_mori_paint.historical.models.mix_container import MixContainer
from asb_mori_paint.historical.models.mixing_process import MixingProcess
#from asb_mori_paint.historical.models.viscosity_improvement import ViscosityImprovement
from asb_mori_paint.historical.models.process_container_component import ProcessContainerComponent # Faltan modificaciones en la BD
# ------
from asb_mori_paint.historical.models.machine_information import MachineInformation
from asb_mori_paint.historical.models.mixing_process_status import MixingProcessStatus
from asb_mori_paint.historical.models.component_tare import ComponentTare
from asb_mori_paint.historical.models.process_step_releases_info import ProcessStepReleasesInfo
from asb_mori_paint.historical.models.component_viscosity_improvement import ComponentViscosityImprovement

from asb_mori_paint.utils.error_handlers_api import *

from asb_mori_paint.utils.load_jsons import load_json_bases, load_json_containers_barcodes_info
from asb_mori_paint.utils.weight_calculations import calculate_containers_by_formula_and_num_pieces
from asb_mori_paint.utils.components_info import get_additives_identifier, get_base_identifier, get_solvents_identifier, get_catalysts_identifier

zpl_code_path = main_path+"/data/zpl_code/"

api_data = Blueprint('api_data', __name__)

###### Falta en todas
## --- manejo del error de intentar guardar un mismo registro dos veces, en algunas es usando python y otra es cachando el resultadod el commit 

### ---------------------------- Información de la máquina ----------------
# Para guardar el numero de lote y se diferencie de las otras mpaquinas .. 

@api_data.route('/api/machine_info', methods = ['GET'])
def get_machine_info():
    """  """
    data = {}
    try:
        machine = MachineInformation.query.get(1)
    except Exception as e:
        return jsonify( data = create_response_data(restError, "Error en la base de datos!", [str(e)]) )
    if machine:
        data_dict = machine.get_json_format()
        data_result = {"record": data_dict}
        data = create_response_data(restSuccess, "Registro localizado!", None, data_result)
    else:
        data = create_response_data(restError, "Registro NO localizado!") 
    return jsonify(data)

### ---------------------------- Procesos ----------------

@api_data.route('/api/processes', methods = ['POST','GET'])
def transactions_processes():
    """ Obtener TODOS los procesos  """
    data = {}
    if request.method == 'GET':
        args = request.args
        #print("Parametors: ", args)
        #for arg in args:
            #print(arg + "  -> " + args[arg])
        if "id" in args and int(args["id"]) > 0:
            id_record = int(args["id"])
            #print("Mandando el elemento {}!!".format(id_record) )
            mixing_process = MixingProcess.query.get(id_record)
            if mixing_process:
                data_dict = mixing_process.get_json_format()
                data_result = {"record": data_dict}
                data = create_response_data(restSuccess, "Registro localizado!", None, data_result)
            else:
                data = create_response_data(restWarning, "Registro NO localizado!")
        else:
            #print("Mandando TODO!!!")
            data_result = {"list": []}
            processes = MixingProcess.query.all()
            for proc in processes:
                data_dict = proc.get_json_format()
                data_result["list"].append(data_dict) 
            if processes:
                data = create_response_data(restSuccess, "Enviando " + "{}".format(len(processes)) + " registro(s)", None, data_result)
            else:
                data = create_response_data(restWarning, "No hay registros en la BD")
    else: # POST ... 
        #print("Entro al Post!!")
        #print(request.json)
        content = request.json.get('params')
        if "record" in content:
            dict_mixing_process = content["record"]
            #print(dict_mixing_process)
            if "id" in dict_mixing_process:
                id_record = dict_mixing_process["id"]
                print("------ Aún no implementada ... ")
                #data["updated_record"] = dict_mixing_process
                ### Aún no implementada
                #data = create_response_data(restWarning, "Función de actualización de registro aún no disponible")
                # solo se debe de acrualizar la fecha de finalización del proceso, no más ... .
                mixing_process = MixingProcess.query.get(id_record)
                if mixing_process:
                    mixing_process.clean_list_errors()
                    if "t_end" in dict_mixing_process and mixing_process.t_end is None:
                        if mixing_process.update_t_end(dict_mixing_process["t_end"]):
                            print("Entro a actualizar .. ")
                            try:
                                db.session.commit()
                                data_result = {"record" : mixing_process.get_json_format()}
                                data = create_response_data(restSuccess, "Registro actualizado con éxito", None, data_result)
                            except Exception as e:
                                data = create_response_data(restError, "Error en el proceso de actualización en la base de datos", [str(e)])  
                        else:
                            data = create_response_data(restError, "Errores generados durante el proceso de actualización del registro", mixing_process.list_errors) 
                    else:
                        if "t_end" in dict_mixing_process:
                            print("no viene t_end")
                            data = create_response_data(restWarning, "El registro ya tiene el valor t_end definido, no se puede actualizar, favor de ponerse en contacto con TI")
                        else:
                            print("t_end no es None")
                            data = create_response_data(restError, "Falta el parametro t_end, no se puede actualizar el registro")
                else:
                    data = create_response_data(restWarning, "(Actualización) Registro NO localizado! verifique el ID") 
            else:
                mixing_process = MixingProcess(dict_mixing_process)
                #list_errors = mixing_process.get_list_errors_and_clean()
                #print("Local: ", list_errors)
                #print("Model: ", mixing_process.list_errors)
                if len(mixing_process.list_errors) != 0:#if len(list_errors) != 0:
                    #data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", list_errors)
                    data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", mixing_process.list_errors)
                    #mixing_process.clean_list_error()
                else:
                    # calcular el numero de contenedores ... 
                    num_containers = calculate_containers_by_formula_and_num_pieces(mixing_process.id_formula, mixing_process.id_model,
                    mixing_process.number_of_pieces, mixing_process.grams_to_recirculate, mixing_process.conatiner_base_weight)
                    if "error" in num_containers:
                        data = create_response_data(restError, num_containers["error"])
                    else:
                        mixing_process.num_containers = num_containers["num_containers"]
                        print(mixing_process)
                        try:
                            db.session.add(mixing_process)
                            db.session.commit()
                            data_result = {"id": mixing_process.id, "num_containers": mixing_process.num_containers, "pintado": num_containers["pintado"], "total_weight": num_containers["total_weight"], "last_container_base_weight": num_containers["last_container_base_weight"]}
                            data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                        except Exception as e:
                            data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])                 
        else:
            data = create_response_data(restError, "No se mando el parametro id")
    return jsonify(data)

@api_data.route('/api/processes/errors', methods=['POST'])
def errors_process():
    data = {}
    content = request.json.get('params')
    if "record" in content:
        dict_mixing_process_errors = content["record"]
        #print(dict_mixing_process)
        if "id" in dict_mixing_process_errors:
            id_record = dict_mixing_process_errors["id"]
            mixing_process = MixingProcess.query.get(id_record)
            print(dict_mixing_process_errors)
            if mixing_process:
                mixing_process.clean_list_errors()
                if mixing_process.update_valid_failure_info(dict_mixing_process_errors):
                    try:
                        db.session.commit()
                        data_result = { "record" : mixing_process.get_json_format() }
                        data = create_response_data(restSuccess, "Actualización de errores correctos", None, data_result)
                    except Exception as e:
                        data = create_response_data(restError, "Error al ingresar a la base de datos", [str(e)])
                else:
                    data = create_response_data(restError, "Error de conversion de datos", mixing_process.list_errors)
            else:                
                data = create_response_data(restError, "Faltan Parametros")
        else:
            data = create_response_data(restError, "No se mando el parametro id")
    else:
        data = create_response_data(restError, "Faltan el campo record")
    return jsonify(data)


@api_data.route('/api/processes/next_id', methods = ['GET'])
def info_processes_next_id():
    data = {}
    process_id = db.session.query(func.max(MixingProcess.id)).first()
    if process_id[0] is not None:
        data_result = {'next_id': process_id[0] +1 }
    else:
        data_result = {'next_id': 1 }
    data = create_response_data(restSuccess, "Próximo id", None, data_result)
    return jsonify(data)

### ---------------------------- Estatus del Proceso ----------------

@api_data.route('/api/process/status', methods = ['GET', 'POST'])
def transactions_process_status():
    """ """
    data = {}
    if request.method == 'GET': 
        args = request.args
        if "id" in args and int(args["id"]) > 0: #  debe de regresar el último registro con el timestamp mayor con el id del proceso dado .. 
            try:
                id_ = int(args["id"])
            except Exception as e:
                return jsonify(create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)]) )
            process_statuses = MixingProcessStatus.query.filter(MixingProcessStatus.id_process == id_)
            if process_statuses:
                if "all" in args:
                    data_result = {"list": []}
                    for p_s in process_statuses:
                        data_result["list"].append(p_s.get_json_format())
                else:
                    process_status = process_statuses[0]
                    for p_s in process_statuses:
                        if p_s.t_event_registration >  process_status.t_event_registration: # revisar después si esta comparación sirve de verdad .. 
                            process_status = p_s
                    data_result = {"record": process_status.get_json_format()}
                data = create_response_data(restSuccess, "Registro encontrado!!", None, data_result)  
            else:
                data = create_response_data(restError, "No existen registros de proceso para ese id")  
        else:
            data = create_response_data(restError, "Parametros incorrectos") 
    else: # POST
        content = request.json.get('params')
        if "record" in content:
            dict_p_s = content["record"]
            # solo se puede hacer post, pero no put (update ... )
            process_status = MixingProcessStatus(dict_p_s)
            if len(process_status.list_errors) != 0:
                data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", process_status.list_errors)
            else:
                try:
                    db.session.add(process_status)
                    db.session.commit()
                    data_result = {"id": process_status.id}
                    data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                except Exception as e:
                    data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])    
        else:
            data = create_response_data(restError, "Parametros incorrectos, no se puede registar")   
    return jsonify(data)


### ---------------------------- Contenedores ----------------

def update_container_selection(container, data):
    if "viscosity" in data and "weight" in data and "temperature" in data and "humidity" in data:
        if container.update_measures(data) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "id_barcode" in data and "t_start_container" in data:
        if container.update_container_init(data) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "t_end" in data:
        if container.update_t_end(data["t_end"]) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "t_end_container" in data:
        if container.update_t_end_container(data["t_end_container"]) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "t_start_viscosity" in data:
        if container.update_t_start_viscosity(data["t_start_viscosity"]) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "t_end_viscosity" in data:
        if container.update_t_end_viscosity(data["t_end_viscosity"]) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "t_start_tare" in data:
        if container.update_t_start_tare(data["t_start_tare"]) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors) 
    elif "t_end_tare" in data:
        if container.update_t_end_tare(data["t_end_tare"]) == False:
            return create_response_data(restError, "Errores generados durante el proceso de actualización del registro", container.list_errors)  
    else:
        return create_response_data(restError, "Faltan parametros, no se puede actualizar el registro")
    print("Entro a actualizar .. ")
    try:
        db.session.commit()
        data_result = {"record" : container.get_json_format()}
        data = create_response_data(restSuccess, "Registro actualizado con éxito", None, data_result)
    except Exception as e:
        data = create_response_data(restError, "Error en el proceso de actualización en la base de datos", [str(e)])  
    return data

## Falta función de obtener los contenedores dados un id de proceso 

@api_data.route('/api/container', methods = ['POST','GET'])
def transactions_container():
    """ Crear contenedor  """
    data = {}
    if request.method == 'GET':
        args = request.args
        print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            container = MixContainer.query.get(id_)
            if container:
                data_dict = container.get_json_format()
                data_result = {"record": data_dict}
                data = create_response_data(restSuccess, "Registro localizado!", None, data_result)
            else:
                data = create_response_data(restWarning, "Registro NO localizado!") 
        else:
            containers = MixContainer.query.all()
            data_result = {"list": []}
            for cont in containers:
                data_dict = cont.get_json_format()
                data_result["list"].append(data_dict)
            if containers:
                data = create_response_data(restSuccess, "Enviando " + "{}".format(len(containers)) + " registro(s)", None, data_result)
            else:
                data = create_response_data(restWarning, "No hay registros en la BD") 
    else: # POST ... 
        #print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            #print(content)
            #data["info"] = "Llego el registro!"
            dict_container = content["record"]
            if "id" in dict_container:
                id_record = dict_container["id"]
                #data["updated_record"] = dict_container
                #print("------ Aún no implementada ... ")
                ### Aún no implementada
                #data = create_response_data(restWarning, "Función de actualización de registro aún no disponible")
                container = MixContainer.query.get(id_record)
                if container:
                    data = update_container_selection(container, dict_container)
                else:
                    data = create_response_data(restWarning, "(Actualización) Registro NO localizado! verifique el ID")  
            else:
                container = MixContainer(dict_container)
                print("Lista de Errores: \n ",container.list_errors)
                if len(container.list_errors) != 0:
                    data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", container.list_errors)
                else:
                    try:
                        db.session.add(container)
                        db.session.commit()
                        data_result = {"id": container.id}
                        data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                    except Exception as e:
                        data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])   
                if container:
                    print("Se elimino!! ")
                    del container
        else:
            data = create_response_data(restError, "No se mando el parametro id")
    return jsonify(data)

@api_data.route('/api/container/errors', methods=['POST'])
def errors_container():
    data = {}
    content = request.json.get('params')
    if "record" in content:
        dict_mix_container_errors = content["record"]
        if "id" in dict_mix_container_errors:
            id_record = dict_mix_container_errors["id"]
            mix_container = MixContainer.query.get(id_record)
            if mix_container:
                if mix_container.update_valid_failure_info(dict_mix_container_errors):
                    try:
                        db.session.commit()
                        data_result = { "record" : mix_container.get_json_format() }
                        data = create_response_data(restSuccess, "Actualización de errores correctos", None, data_result)
                    except Exception as e:
                        data = create_response_data(restError, "Error al ingresar a la base de datos", [str(e)])
                else:
                    data = create_response_data(restError, "Error de conversion de datos", mix_container.list_errors)
            else:
                data = create_response_data(restError, "No se encuentra registro")
        else:
            data = create_response_data(restError, "No se mando el id")
    else:
        data = create_response_data(restError, "No se mando el parametro el registro")
    return jsonify(data)

@api_data.route('/api/get_containers', methods = ['GET'])
def get_containers_by_id_Process():
    """ Obtener contenedores por proceso  """
    data = {}
    args = request.args
    print(args)
    if "id_process" in args and int(args["id_process"]) > 0:
        try:
            id_process = int(args["id_process"])
        except Exception as e:
            return create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)])
        mixing_process = MixingProcess.query.get(id_process)
        if mixing_process:
            dict_process = mixing_process.get_json_format()
            data_result = {"record": dict_process, "list_containers": []}
            containers = MixContainer.query.filter(MixContainer.id_process == mixing_process.id)
            if containers:
                print("Datos encontrados: ") 
                for container in containers:
                    dict_container = container.get_json_format()
                    data_result["list_containers"].append(dict_container)
                data = create_response_data(restSuccess, "Registros localizados! para el proceso solicitado", None, data_result)
            else:
                data = create_response_data(restSuccess, "El proceso se ha inizializado pero no tiene contenedores relacionados!", None, data_result)
        else:
            data = create_response_data(restError, "Proceso NO localizado!")
    else:
        data = create_response_data(restError, "No se recibió el parametro correcto")  

    return jsonify(data)


### ---------------------------- Mejora de Viscosidad  ----------------

# falta obtener la lista de mejoras de viscosidad dado un id de proceso
# falta obtener la lista de mejoras de viscosidad dado un id de proceso y un id de contenedor

#@api_data.route('/api/viscosity_improvement', methods = ['POST','GET'])
#def transactions_viscosity_improvement():
#    """ Crear contenedor  """
#    data = {}
#    if request.method == 'GET':
#        args = request.args
#        #print(args)
#        if "id" in args and int(args["id"]) > 0:
#            id_ = int(args["id"])
#            viscosity_impr = ViscosityImprovement.query.get(id_)
#            if viscosity_impr:
#                data_dict = viscosity_impr.get_json_format()
#                data_result = {"record": data_dict}
#                data = create_response_data(restSuccess, "Registro localizado!", None, data_result)
#            else:
#                data = create_response_data(restWarning, "Registro NO localizado!")
#        else:
#            viscosity_imprs = ViscosityImprovement.query.all()
#            data_result = {"list": []}
#            for visc_impr in viscosity_imprs:
#                data_dict = visc_impr.get_json_format()
#                data_result["list"].append(data_dict)
#            if viscosity_imprs:
#                data = create_response_data(restSuccess, "Enviando " + "{}".format(len(viscosity_imprs)) + " registro(s)", None, data_result)
#            else:
#                data = create_response_data(restWarning, "No hay registros en la BD")
#    else: # POST ... 
#        #print("Entro al Post!!")
#        content = request.json.get('params')
#        if "record" in content:
#            #data["info"] = "Llego el registro!"
#            dict_visc_impr = content["record"]
#            if "id" in dict_visc_impr:
#                data["updated_record"] = dict_visc_impr
#                print("------ Aún no implementada ... ")
#                ### Aún no implementada
#                data = create_response_data(restWarning, "Función de actualización de registro aún no disponible")
#            else:
#                visc_impr = ViscosityImprovement(dict_visc_impr)
#                if len(visc_impr.list_errors) != 0:
#                    data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", visc_impr.list_errors) 
#                else:
#                    try:
#                        db.session.add(visc_impr)
#                        db.session.commit()
#                        data_result = {"id": visc_impr.id}
#                        data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
#                    except Exception as e:
#                        data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])  
#        else:
#            data = create_response_data(restError, "No se mando el parametro id")
#    return jsonify(data)

### ---------------------------- Proceso - Contenedor - Componente ----------------

#### Falta obtener la lista de todos los componentes por proceso, para esto se deben de obtener la lista de los contenedores por proceso 
#### Falta obtener la lista de todos los componentes por contenedor

def ids_transactions_process_container_component_convert_handler(args = None, type = None):
    #dict_ = {}
    if args is None or type is None:
        #dict_ = {"rest": False, "info": "args and record are None"}
        return False, "Error interno en el manejo de conversión de parametros", None, None
    if type == 0:
        if "id" not in args or "id_type_component" not in args or "id_component" not in args:
            return False, "Faltan campos", None, None
        try:
            id_ = int(args["id"])
            id_type_comp = int(args["id_type_component"])
            id_comp = int(args["id_component"])
            #dict_ = {"rest": False,"id_": int(args["id"]), "id_type_comp": int(args["id_type_component"]), "id_comp": int(args["id_component"])}
        except Exception as e:
            #dict_ = {"rest": False, "info": "Error de conversión int o float!"}
            return False, "Error de conversión int o float!", None, None
    else:
        print("------",args)
        if "id_mix_container" not in args or "id_type_component" not in args or "id_component" not in args:
            return False, "Faltan campos", None, None
        try:
            id_ = int(args["id_mix_container"])
            id_type_comp = int(args["id_type_component"])
            id_comp = int(args["id_component"])
            #dict_ = {"rest": False,"id_": int(args["id_mix_container"]), "id_type_comp": int(args["id_type_component"]), "id_comp": int(args["id_component"])}
        except Exception as e:
            #dict_ = {"rest": False, "info": "Error de conversión int o float!"}
            return False, "Error de conversión int o float!", None, None

    return True, id_, id_type_comp, id_comp
    #return dict_ 

@api_data.route('/api/process_container_component', methods = ['POST','GET'])
def transactions_process_container_component():
    """ Crear Proceso-Contenedor-Componente  """
    data = {}
    if request.method == 'GET':
        args = request.args
        #print(args)
        #### se requieren 3 ids: id_contenedor, id_type_component y id_component ...
        rest, id_, id_type_comp, id_comp = ids_transactions_process_container_component_convert_handler(args, 0) 
        if rest: #if "id" in args and "id_type_component" in args  and "id_component" in args:
            if id_ > 0 and id_comp > -1 and id_type_comp > -1:
                proc_cont_comps = ProcessContainerComponent.query.filter(ProcessContainerComponent.id_mix_container == id_,ProcessContainerComponent.id_type_component == id_type_comp, ProcessContainerComponent.id_component == id_comp).first()
                print("------ ", proc_cont_comps)
                if proc_cont_comps:
                    data_dict = proc_cont_comps.get_json_format()
                    data_result = {"record": data_dict}
                    data = create_response_data(restSuccess, "Registro localizado!", None, data_result) 
                else:
                    data = create_response_data(restWarning, "Registro NO localizado!")
            else:
                proc_cont_comps = ProcessContainerComponent.query.all()
                data_result = {"list": []}
                for proc_cont_comp in proc_cont_comps:
                    data_dict = proc_cont_comp.get_json_format()
                    data_result["list"].append(data_dict)  
        else:
            proc_cont_comps = ProcessContainerComponent.query.all()
            data_result = {"list": []}
            for proc_cont_comp in proc_cont_comps:
                data_dict = proc_cont_comp.get_json_format()
                data_result["list"].append(data_dict)  
            if proc_cont_comps:
                data = create_response_data(restSuccess, "Enviando " + "{}".format(len(proc_cont_comps)) + " registro(s) " + id_, None, data_result)
            else:
                data = create_response_data(restWarning, "No hay registros en la BD o " + id_)
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            #data["info"] = "Llego el registro!"
            dict_proc_cont_comp = content["record"]
            rest, id_, id_type_comp, id_comp = ids_transactions_process_container_component_convert_handler(dict_proc_cont_comp, 1)
            if rest:#if "id_mix_container" in dict_proc_cont_comp and "id_type_component" in dict_proc_cont_comp  and "id_component" in dict_proc_cont_comp:
                #id_ = int(dict_proc_cont_comp["id_mix_container"])
                #id_type_comp = int(dict_proc_cont_comp["id_type_component"])
                #id_comp = int(dict_proc_cont_comp["id_component"])
                proc_cont_comps = ProcessContainerComponent.query.filter(ProcessContainerComponent.id_mix_container == id_,ProcessContainerComponent.id_type_component == id_type_comp, ProcessContainerComponent.id_component == id_comp).first()
                if proc_cont_comps:
                    data["updated_record"] = dict_proc_cont_comp
                    print("------ Aún no implementada ... ")
                    ### Aún no implementada: No debería de poderse modificar este caso, ya que solo se regustra y no se actualiza ... 
                    data = create_response_data(restWarning, "Función de actualización de registro aún no disponible")
                else:
                    proc_cont_comp = ProcessContainerComponent(dict_proc_cont_comp)
                    if len(proc_cont_comp.list_errors) != 0:
                        data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", proc_cont_comp.list_errors)
                    else: 
                        try:
                            db.session.add(proc_cont_comp)
                            db.session.commit()
                            data_result = {"id_mix_container": proc_cont_comp.id_mix_container, "id_type_comp": proc_cont_comp.id_type_component, "id_comp": proc_cont_comp.id_component}
                            data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                        except Exception as e:
                            data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)]) 
            else:
                data = create_response_data(restError, "No se pudo guardar, faltan campos o " + id_ ) 

        else:
            data = create_response_data(restError, "No se mando el parametro id")
    return jsonify(data)


### ---------------------------- Componente - Tara ----------------
## Falta función de obtener las taras por id de proceso
## Falta función de obtener las taras por id de proceso y id de contenedor

@api_data.route('/api/component_tare', methods = ['POST','GET'])
def transactions_component_tare():
    """ Crear Componete-Tara  """
    data = {}
    if request.method == 'GET':
        args = request.args
        #print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            comp_tare = ComponentTare.query.get(id_)
            if comp_tare:
                data_dict = comp_tare.get_json_format()
                data_result = {"record": data_dict}
                data = create_response_data(restSuccess, "Registro localizado!", None, data_result)
            else:
                data = create_response_data(restWarning, "Registro NO localizado!")
        else:
            comp_tares = ComponentTare.query.all()
            data_result = {"list": []}
            for comp_tare in comp_tares:
                data_dict = comp_tare.get_json_format()
                data_result["list"].append(data_dict) 
            if comp_tares:
                data = create_response_data(restSuccess, "Enviando " + "{}".format(len(comp_tares)) + " registro(s)", None, data_result)
            else:
                data = create_response_data(restWarning, "No hay registros en la BD")
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            #data["info"] = "Llego el registro!"
            dict_comp_tare = content["record"]
            if "id" in dict_comp_tare:
                data["updated_record"] = dict_comp_tare
                print("------ Aún no implementada ... ")
                ### Aún no implementada
                data = create_response_data(restWarning, "Función de actualización de registro aún no disponible")
            else:
                comp_tare = ComponentTare(dict_comp_tare)
                if len(comp_tare.list_errors) != 0:
                    data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", comp_tare.list_errors) 
                else:
                    try:
                        db.session.add(comp_tare)
                        db.session.commit()
                        data_result = {"id": comp_tare.id}
                        data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                    except Exception as e:
                        data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])    
        else:
            data = create_response_data(restError, "No se mando el parametro id")
    return jsonify(data)

@api_data.route('/api/get_component_tares', methods = ['POST','GET'])
def get_component_tares():
    """ Obtener Componete-Tara por proceso o contenedor  """
    data = {}
    args = request.args
    #print(args)
    if "id_process" in args and int(args["id_process"]) > 0: # obtener todos los componentes de un proceso
        try:
            id_process = int(args["id_process"])
        except Exception as e:
            return create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)])
        mixing_process = MixingProcess.query.get(id_process)
        if mixing_process:
            dict_process = mixing_process.get_json_format()
            data_result = {"record": dict_process, "list_containers": []}
            containers = MixContainer.query.filter(MixContainer.id_process == mixing_process.id)
            if containers:
                print("Datos encontrados: ") 
                for container in containers:
                    dict_container = container.get_json_format()
                    #Obtener los compoenentes de cada tare 
                    dict_container["list_component_tares"] = []
                    components_tares = ComponentTare.query.filter(ComponentTare.id_mix_container == container.id)
                    for component_tare in components_tares:
                        dict_component_tare = component_tare.get_json_format()
                        dict_container["list_component_tares"].append(dict_component_tare)
                    data_result["list_containers"].append(dict_container)
                data = create_response_data(restSuccess, "Registros localizados! para el proceso solicitado", None, data_result)
            else:
                data = create_response_data(restSuccess, "El proceso se ha inizializado pero no tiene contenedores relacionados!", None, data_result) 
        else:
            data = create_response_data(restError, "Proceso NO localizado!")
    else:
        if "id_mix_container" in args and int(args["id_mix_container"]) > 0: # obtener todos los componentes de un contenedor
            try:
                id_mix_container = int(args["id_mix_container"])
            except Exception as e:
                return create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)]) 
            container = MixContainer.query.get(id_mix_container)
            if container:
                dict_container = container.get_json_format()
                data_result = {"record": dict_container, "list_component_tares": []}
                components_tares = ComponentTare.query.filter(ComponentTare.id_mix_container == container.id)
                for component_tare in components_tares:
                    dict_component_tare = component_tare.get_json_format()
                    data_result["list_component_tares"].append(dict_component_tare)
                data = create_response_data(restSuccess, "Registros localizados! para el contendor solicitado", None, data_result)
            else:
                data = create_response_data(restError, "Contenedor NO localizado!") 
        else:
            data = create_response_data(restError, "No se mando el parametro id")

    return jsonify(data)


### ---------------------------- Mejora de Viscosidad por Componente ----------------
## Falta obtener las mejoras por componente de viscosidad por id proceso
## Falta obtener las mejoras por componente de viscosidad por id proceso y id de mejora
## Falta obtener las mejoras por componente de viscosidad por id proceso y id contenedor


@api_data.route('/api/component_viscosity_improvement', methods = ['POST','GET'])
def transactions_component_viscosity_improvement():
    """ Crear Componete- Mejora de Viscosidad  """
    data = {}
    if request.method == 'GET':
        args = request.args
        #print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            comp_visc_impr = ComponentViscosityImprovement.query.get(id_)
            if comp_visc_impr:
                data_dict = comp_visc_impr.get_json_format()
                data_result = {"record": data_dict}
                data = create_response_data(restSuccess, "Registro localizado!", None, data_result)
            else:
                data = create_response_data(restWarning, "Registro NO localizado!")
        else:
            comp_visc_imprs = ComponentViscosityImprovement.query.all()
            data_result = {"list": []}
            for comp_visc_impr in comp_visc_imprs:
                data_dict = comp_visc_impr.get_json_format()
                data_result["list"].append(data_dict) 
            if comp_visc_imprs:
                data = create_response_data(restSuccess, "Enviando " + "{}".format(len(comp_visc_imprs)) + " registro(s)", None, data_result)
            else:
                data = create_response_data(restWarning, "No hay registros en la BD")
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            #data["info"] = "Llego el registro!"
            dict_comp_visc_impr = content["record"]
            if "id" in dict_comp_visc_impr:
                data["updated_record"] = dict_comp_visc_impr
                print("------ Aún no implementada ... ")
                ### Aún no implementada
                data = create_response_data(restWarning, "Función de actualización de registro aún no disponible")
            else:
                comp_visc_impr = ComponentViscosityImprovement(dict_comp_visc_impr)
                print(comp_visc_impr)
                if len(comp_visc_impr.list_errors) != 0:
                    data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", comp_visc_impr.list_errors)
                else:
                    try:
                        db.session.add(comp_visc_impr)
                        db.session.commit()
                        data_result = {"id": comp_visc_impr.id}
                        data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                    except Exception as e:
                        data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])
        else:
            data = create_response_data(restError, "No se mando el parametro id")
    return jsonify(data)


### ---------------------------- Autenticación de trabajadores ----------------
# Falta conexión con base de datos .. 

@api_data.route('/api/worker_authentication', methods=['GET'])
def worker_authentication():
    args = request.args
    #print(request.args)
    if "user_number" in args:
        user_number = request.args['user_number']   
        try: 
            payroll_number_data = int(user_number)
        except Exception as e:
            data = create_response_data(restError, "Error de conversión int o float!")
            return jsonify(data)
        ### accediendo a la BD de los trabajadores ... 
        try:
            file = open('asb_mori_paint/static/config_json/workers.json')
            data_workers = json.load(file)
            file.close()
        except Exception as e:
            data = create_response_data(restError, "No se pudo acceder a la BD de los trabajadores")
            return jsonify(data)
        data_result = None
        for x in data_workers['list']:
            if payroll_number_data == x['payroll_number']:
                data_result = {"record": x}
                break
        if data_result:
            data = create_response_data(restSuccess, "Trabajador encontrado!!", None, data_result) 
        else:
            data = create_response_data(restError, "Trabajador NO encontrado!!") 
                
    else:
        data = create_response_data(restError, "No se mando el parametro user_number") 
    
        
    return jsonify(data)

### ---------------------------- Validación de Contenedor ----------------
# Falta conexión con base de datos ..

@api_data.route('/api/container_validation', methods=['GET'])
def container_validation():
    print(request.args)
    args = request.args
    if "barcode_text" in args: 
        barcodes_info = load_json_containers_barcodes_info()
        if "error" in barcodes_info:
            data = create_response_data(restError, barcodes_info["error"])
        else:
            data_result = { "response" : False }
            try:
                int_barcode = int(args["barcode_text"])
            except Exception as e:
                return jsonify(create_response_data(restSuccess, "Error en la transformación a entero del parametro", [str(e)], data_result)) 
            barcodes = barcodes_info["barcodes"]
            for code in barcodes:
                barcode = barcodes[code]
                try:
                    int_barcode_record = int(barcode["id_barcode"]) 
                except Exception as e:
                    continue # continuar el ciclo para ver si en los demás se puede encontrar ... 
                if int_barcode_record == int_barcode:
                    data_result["response"] = True
                    break 
            if data_result["response"] == False:
                data = create_response_data(restSuccess, "Código de barras no registrado", None, data_result)
            else:
                data = create_response_data(restSuccess, "Contenedor Valido", None, data_result)
    else:
        data = create_response_data(restError, "No se mandaron los parametros adecuados")
    return jsonify(data)

### --------------------------- Obtener identificadores para validar componentes/sustancias

@api_data.route('/api/get_base_identifier', methods=['GET'])
def get_base_identifier_2():
    params = request.args
    print(params)
    if 'id_base' in params:
        bases = load_json_bases()
        if "error" in bases:
            data = create_response_data(restError, bases['error'])
        else:
            print(params['id_base'])
            id_base = int(params['id_base'])
            formula = {}
            list_f = bases['list']
            for x in list_f:
                print(x)
                if x['id'] == id_base:
                    formula = x
                    break
            if(bool(formula)):
                data_result = {
                    'identifier' : formula['identifier']
                }
                data = create_response_data(restSuccess, "Identificador Encontrado", None, data_result)
            else:        
                data = create_response_data(restError, "Identificador no encontrado")
    else:
        data = create_response_data(restError, "Parametro incorrecto")
    
    return jsonify(data)


@api_data.route('/api/get_comp_identifier', methods=['GET'])
def get_comp_identifier():
    params = request.args
    print(params)
    if 'id_type' in params and "id_component" in params:
        try:
            id_type = int(params["id_type"])
            id_comp = int(params["id_component"])
        except Exception as e:
            return jsonify(create_response_data(restError, "Error en el casteo a entero de los parametros"))
        if id_type == 0:# bases
            data_result = get_base_identifier(id_comp)  
        elif id_type == 1:# solventes
            data_result = get_solvents_identifier(id_comp)
        elif id_type == 2:# aditivos
            data_result = get_additives_identifier(id_comp)
        elif id_type == 3:# catalizadfor
            data_result = get_catalysts_identifier(id_comp)
        else:
            data_result = {"error": "Tipo de componente NO encontrado"}
        if "error" in data_result:
            data = create_response_data(restError, data_result['error'])
        else:
            data = create_response_data(restSuccess, "Identificador Encontrado", None, data_result)
    else:
        data = create_response_data(restError, "Parametros incorrectos")
    return jsonify(data)


# ------- Registrar Liberaciones de Pasos del Proceso

@api_data.route('/api/process_step_release', methods=['GET', 'POST'])
def transactions_process_step_release():
    data = {}
    if request.method == 'GET':
        args = request.args
        #print(args)
        if "id_process" in args: # and int(args["id"]) > 0:
            try:
                id_process = int(args["id_process"])
            except Exception as e:
                return create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)])
            p_s_r_i_ = ProcessStepReleasesInfo.query.filter(ProcessStepReleasesInfo.id_process == id_process).all()
            print(p_s_r_i_)
            if p_s_r_i_:
                data_result = {"list": []}
                for p_s_r_i in p_s_r_i_:
                    data_result["list"].append( p_s_r_i.get_json_format() )
                data = create_response_data(restSuccess, "Aún no implementada de nanera correcta!! ", None, data_result) 
            else:
                data = create_response_data(restError, "No hay registros ")
        else:
            data = create_response_data(restError, "No se mandarón los parametros necesario!!")  
    else:
        content = request.json.get('params')
        if "record" in content:
            dict_p_s_r_i = content["record"]
            print(dict_p_s_r_i)
            p_s_r_i = ProcessStepReleasesInfo(dict_p_s_r_i)
            if len(p_s_r_i.list_errors) != 0:
                data = create_response_data(restError, "Errores generados durante el proceso de creación del registro", p_s_r_i.list_errors)
            else:
                try:
                    db.session.add(p_s_r_i)
                    db.session.commit()
                    data_result = {"id": p_s_r_i.id}
                    data = create_response_data(restSuccess, "Registro guardado con éxito", None, data_result)
                except Exception as e:
                    data = create_response_data(restError, "Error en el proceso de guardado de la base de datos", [str(e)])
        else:
            data = create_response_data(restError, "No se mandarón los parametros necesario para guardar el registro!!")  
    return jsonify(data) 

# --------- Extraer de la información del zpl

@api_data.route('/api/get_zpl_info', methods=['GET'])
def get_zpl_info():
    content = request.args
    if 'id' in content:
        path =  'asb_mori_paint' + '\\' + 'data' + '\\' + 'zpl_code' + '\\' + content['id'] + '.zpl'    
        print(path)
        if os.path.exists(path):
            file = open(path, 'r')
            text_file = file.read()
            index_container = text_file.index('Container')    
            first_slice_container = text_file[index_container:len(text_file)]
            index_first_cfa = first_slice_container.index('^CFA,30')
            second_slice_container = first_slice_container[0:index_first_cfa]        
            index_points_slice = second_slice_container.index(':')
            index_hyphen_slice = second_slice_container.index('--')
            num_containers = second_slice_container[index_points_slice+1:index_hyphen_slice].strip()
            container = num_containers[0]
            index_slash_slice = num_containers.index('/')
            len_container = num_containers[index_slash_slice+1: len(num_containers)]
            print(second_slice_container)
            print("Container: " + container)
            print("Container len: " + len_container)
            # --------- Obtener Info del cliente
            index_worker_id = text_file.index('Worker')
            first_slice_worker = text_file[index_worker_id:len(text_file)]
            index_first_cfa = first_slice_container.index('^CFA,30')
            second_slice_worker = first_slice_worker[0:index_first_cfa]
            split_info_worker = second_slice_worker.split(',')
            print(split_info_worker)
            name_worker = split_info_worker[1].strip()
            split_id_worker = split_info_worker[0].split(':')
            id_worker = split_id_worker[1].strip()
            index_name = name_worker.index('^FS\n^CFA')
            name_worker = name_worker[0:index_name]
            print("Worker name: " + name_worker)
            print("Id_worker: " + id_worker)
            # --------- Obtener Nombre de la empresa cliente
            index_client = text_file.index('Client')
            first_slice_client = text_file[index_client: len(text_file)]
            index_fs = first_slice_client.index('^FS')        
            second_slice_client = first_slice_client[0: index_fs]
            client_split = second_slice_client.split(':')
            client_name = client_split[1].strip()
            print("Client Name: " + client_name)
            file.close()
            json_info = {
                "id_worker": id_worker,
                "client_name": client_name,
                "name_worker": name_worker,
                "container": container,
                "container_len": len_container,
            }            
            data_dict = {"record": json_info}
            data = create_response_data(restSuccess, "Información Obtenida", None, data_dict)
        else:
            data = create_response_data(restError, "No se encuentra el archivo .zpl del id mandado")
    else:
        data = create_response_data(restError, 'La petición no contiene el id')

    return data

@api_data.route('/api/getComponentInfoByContainer', methods=['GET'])
def getComponentByColor():    
    list_component_tare = []
    json_component_tare = []
    list_components = []
    list_componenttype = []
    list_ = []
    content = request.args
    if "id" in content:
        id_container = int(content['id'])        
        try:                      
            mixcontainer = MixContainer.query.filter_by(id = id_container).first()
            json_ = mixcontainer.get_json_format()
            id_process = json_['id_process']                     

            components = Components.query.all()
            for x in components:
                json_components = x.get_json_format()
                list_components.append(json_components)

            component_type = ComponentType.query.all()
            for x in component_type:
                json_componentType = x.get_json_format()
                list_componenttype.append(json_componentType)

            component_tare = ComponentTare.query.filter_by(id_mix_container = id_container).all()            
            for x in component_tare:
                list_component_tare.append(x.get_json_format())

            for x in list_component_tare:
                name = ""
                name_type = ""
                for y in list_components:
                    if y['id'] == x['id_component']:
                        name = y['identifier']
                        break
                for z in list_componenttype:
                    if z['id'] == x['id_type_compoennt']:
                        name_type = z['name']
                        break
                list_.append(                    
                    {
                    "comp_name": name,
                    "type_compent_name": name_type,
                    "weight": x['weight']
                    }
                )

            print(list_)            
            data_dict = {"record": list_}            
            
            data = create_response_data(restSuccess, "Record obtenido", None, data_dict)
        except Exception as e:
            data = create_response_data(restError, "Errores al filtrado", [str(e)])
    else:
        data = create_response_data(restError, "La peticón no contiene el id")

    return data

@api_data.route('/api/getModelbyId', methods=['GET'])
def get_model_by_id():
    content = request.args
    if "id" in content:
        id = int(content['id'])
        try:
            model = Models.query.filter_by(id = id).first()
            model = model.get_json_format()
            print(model)
            model_name = model['part_number']

            data_dict = {"model_name" : model_name}

            data = create_response_data(restSuccess, "Modelo encontrado", None, data_dict)
        except Exception as e:
            data = create_response_data(restError, "Error: No se encuentra el modelo", [str(e)])
    else:
        data = create_response_data(restError, "La peticón no contiene el id")

    return data