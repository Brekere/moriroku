from flask import Blueprint, jsonify, request
from sqlalchemy import func

from web import db

#### 
from web.show_data.models.mixing_process import MixingProcess
from web.show_data.models.mix_container import MixContainer
from web.show_data.models.viscosity_improvement import ViscosityImprovement
from web.show_data.models.process_container_component import ProcessContainerComponent # Faltan modificaciones en la BD
# ------
from web.show_data.models.component_tare import ComponentTare
from web.show_data.models.component_viscosity_improvement import ComponentViscosityImprovement


api_data = Blueprint('api_data', __name__)

###### Falta en todas
## --- manejo del error de intentar guardar un mismo registro dos veces, en algunas es usando python y otra es cachando el resultadod el commit 

### ---------------------------- Procesos ----------------

@api_data.route('/api/processes', methods = ['POST','GET'])
def transactions_processes():
    """ Obtener TODOS los procesos  """
    data = {"rest": "OK"}
    if request.method == 'GET':
        args = request.args
        print(args)
        if "id" in args and int(args["id"]) > 0:
            id_record = int(args["id"])
            print("Mandando el elemento {}!!".format(id_record) )
            mixing_process = MixingProcess.query.get(id_record)
            if mixing_process:
                data_dict = mixing_process.get_json_format()
                data["record"] = data_dict
        else:
            print("Mandando TODO!!!")
            data["list"] = []
            processes = MixingProcess.query.all()
            for proc in processes:
                data_dict = proc.get_json_format()
                data["list"].append(data_dict) 
    else: # POST ... 
        print("Entro al Post!!")
        print(request.json)
        content = request.json.get('params')
        if "record" in content:
            data["info"] = "Llego el registro!"
            dict_mixing_process = content["record"]
            print(dict_mixing_process)
            if "id" in dict_mixing_process:
                data["updated_record"] = dict_mixing_process
                # es una actualización .. 
                ### Aún no implementada
            else:
                mixing_process = MixingProcess(dict_mixing_process)
                print(mixing_process)
                db.session.add(mixing_process)
                db.session.commit()
                data["id"] = mixing_process.id
        else:
            data = {"rest": "ERROR"}
    
    return jsonify(data)

@api_data.route('/api/processes/next_id', methods = ['GET'])
def info_processes_next_id():
    data = {"rest": "OK"}
    #processes = MixingProcess.query.all()
    #print("EnTRO!")
    process_id = db.session.query(func.max(MixingProcess.id)).first()
    #print(":::: ", process_id)
    #print("Paso")
    if process_id[0] is not None:
        data['next_id'] = process_id[0] +1 
    else:
        data['next_id'] = 1
    return jsonify(data)

#@api_data.route('/api/get/processes', methods = ['GET'])
#def get_all_processes():
#    """ Obtener TODOS los procesos  """
#    processes = MixingProcess.query.all()
#    data = {"rest": "OK", "list": []}
#    for proc in processes:
#        data_dict = proc.get_json_format()
#        data["list"].append(data_dict)
#    return jsonify(data)

# @api_data.route('/api/create/process', methods = ['POST'])
# def create_process():
#     """ Crear proceso  """
#     data = {"rest": "OK"}
#     return jsonify(data)

### ---------------------------- Contenedores ----------------

## Falta función de obtener los contenedores dados un id de proceso 

@api_data.route('/api/container', methods = ['POST','GET'])
def transactions_container():
    """ Crear contenedor  """
    data = {"rest": "OK"}
    if request.method == 'GET':
        args = request.args
        print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            container = MixContainer.query.get(id_)
            if container:
                data_dict = container.get_json_format()
                data["record"] = data_dict 
        else:
            containers = MixContainer.query.all()
            data["list"] = []
            for cont in containers:
                data_dict = cont.get_json_format()
                data["list"].append(data_dict) 
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            data["info"] = "Llego el registro!"
            dict_container = content["record"]
            if "id" in dict_container:
                data["updated_record"] = dict_container
                # es una actualización .. 
                ### Aún no implementada
            else:
                container = MixContainer(dict_container)
                db.session.add(container)
                db.session.commit()
                data["id"] = container.id
        else:
            data = {"rest": "ERROR"}
    return jsonify(data)

# @api_data.route('/api/create/container', methods = ['GET'])
# def create_container():
#     """ Crear contenedor  """
#     data = {"rest": "OK"}
#     return jsonify(data)


### ---------------------------- Mejora de Viscosidad  ----------------

# falta obtener la lista de mejoras de viscosidad dado un id de proceso
# falta obtener la lista de mejoras de viscosidad dado un id de proceso y un id de contenedor

@api_data.route('/api/viscosity_improvement', methods = ['POST','GET'])
def transactions_viscosity_improvement():
    """ Crear contenedor  """
    data = {"rest": "OK"}
    if request.method == 'GET':
        args = request.args
        print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            viscosity_impr = ViscosityImprovement.query.get(id_)
            if viscosity_impr:
                data_dict = viscosity_impr.get_json_format()
                data["record"] = data_dict 
        else:
            viscosity_imprs = ViscosityImprovement.query.all()
            data["list"] = []
            for visc_impr in viscosity_imprs:
                data_dict = visc_impr.get_json_format()
                data["list"].append(data_dict) 
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            data["info"] = "Llego el registro!"
            dict_visc_impr = content["record"]
            if "id" in dict_visc_impr:
                data["updated_record"] = dict_visc_impr
                # es una actualización .. 
                ### Aún no implementada
            else:
                visc_impr = ViscosityImprovement(dict_visc_impr)
                db.session.add(visc_impr)
                db.session.commit()
                data["id"] = visc_impr.id
        else:
            data = {"rest": "ERROR"}
    return jsonify(data)

# @api_data.route('/api/create/viscosity_improvement', methods = ['GET'])
# def create_viscosity_improvement():
#     """ Crear contenedor  """
#     data = {"rest": "OK"}
#     return jsonify(data)

### ---------------------------- Proces - Contenedor - Componente ----------------

#### Falta obtener la lista de todos los componentes por proceso, para esto se deben de obtener la lista de los contenedores por proceso 
#### Falta obtener la lista de todos los componentes por contenedor

@api_data.route('/api/process_container_component', methods = ['POST','GET'])
def transactions_process_container_component():
    """ Crear Proceso-Contenedor-Componente  """
    data = {"rest": "OK"}
    if request.method == 'GET':
        args = request.args
        print(args)
        #### se requieren 3 ids: id_contenedor, id_type_component y id_component ... 
        if "id" in args and "id_type_comp" in args  and "id_comp" in args:
            id_ = int(args["id"])
            id_type_comp = int(args["id_type_comp"])
            id_comp = int(args["id_comp"])
            if id > 0 and id_comp > -1 and id_type_comp > -1:
                pass 
            else:
                proc_cont_comps = ProcessContainerComponent.query.all()
                data["list"] = []
                for proc_cont_comp in proc_cont_comps:
                    data_dict = proc_cont_comp.get_json_format()
                    data["list"].append(data_dict)  
        else:
            proc_cont_comps = ProcessContainerComponent.query.all()
            data["list"] = []
            for proc_cont_comp in proc_cont_comps:
                data_dict = proc_cont_comp.get_json_format()
                data["list"].append(data_dict) 
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            data["info"] = "Llego el registro!"
            dict_proc_cont_comp = content["record"]
            if "id" in dict_proc_cont_comp:
                data["updated_record"] = dict_proc_cont_comp
                # es una actualización .. 
                ### Aún no implementada: No debería de poderse modificar este caso, ya que solo se regustra y no se actualiza ... 
            else:
                proc_cont_comp = ProcessContainerComponent(dict_proc_cont_comp)
                db.session.add(proc_cont_comp)
                db.session.commit()
                data["id_mix_container"] = proc_cont_comp.id_mix_container
                data["id_type_comp"] = proc_cont_comp.id_type_component
                data["id_comp"] = proc_cont_comp.id_component
        else:
            data = {"rest": "ERROR"}
    return jsonify(data)

# @api_data.route('/api/create/process_container_component', methods = ['GET'])
# def create_process_container_component():
#     """ Crear Proceso-Contenedor-Componente  """
#     data = {"rest": "OK"}
#     return jsonify(data)

### ---------------------------- Componente - Tara ----------------
## Falta función de obtener las taras por id de proceso
## Falta función de obtener las taras por id de proceso y id de contenedor

@api_data.route('/api/component_tare', methods = ['POST','GET'])
def transactions_component_tare():
    """ Crear Componete-Tara  """
    data = {"rest": "OK"}
    if request.method == 'GET':
        args = request.args
        print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            comp_tare = ComponentTare.query.get(id_)
            if comp_tare:
                data_dict = comp_tare.get_json_format()
                data["record"] = data_dict 
        else:
            comp_tares = ComponentTare.query.all()
            data["list"] = []
            for comp_tare in comp_tares:
                data_dict = comp_tare.get_json_format()
                data["list"].append(data_dict)
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            data["info"] = "Llego el registro!"
            dict_comp_tare = content["record"]
            if "id" in dict_comp_tare:
                data["updated_record"] = dict_comp_tare
                # es una actualización .. 
                ### Aún no implementada
            else:
                comp_tare = ComponentTare(dict_comp_tare)
                db.session.add(comp_tare)
                db.session.commit()
                data["id"] = comp_tare.id
        else:
            data = {"rest": "ERROR"}
    return jsonify(data)


# @api_data.route('/api/create/component_tare', methods = ['GET'])
# def create_component_tare():
#     """ Crear Componete-Tara  """
#     data = {"rest": "OK"}
#     return jsonify(data)

### ---------------------------- Mejora de Viscosidad por Componente ----------------
## Falta obtener las mejoras por componente de viscosidad por id proceso
## Falta obtener las mejoras por componente de viscosidad por id proceso y id de mejora
## Falta obtener las mejoras por componente de viscosidad por id proceso y id contenedor


@api_data.route('/api/component_viscosity_improvement', methods = ['POST','GET'])
def transactions_component_viscosity_improvement():
    """ Crear Componete- Mejora de Viscosidad  """
    data = {"rest": "OK"}
    if request.method == 'GET':
        args = request.args
        print(args)
        if "id" in args and int(args["id"]) > 0:
            id_ = int(args["id"])
            comp_visc_impr = ComponentViscosityImprovement.query.get(id_)
            if comp_visc_impr:
                data_dict = comp_visc_impr.get_json_format()
                data["record"] = data_dict 
        else:
            comp_visc_imprs = ComponentViscosityImprovement.query.all()
            data["list"] = []
            for comp_visc_impr in comp_visc_imprs:
                data_dict = comp_visc_impr.get_json_format()
                data["list"].append(data_dict)
    else: # POST ... 
        print("Entro al Post!!")
        content = request.json.get('params')
        if "record" in content:
            data["info"] = "Llego el registro!"
            dict_comp_visc_impr = content["record"]
            if "id" in dict_comp_visc_impr:
                data["updated_record"] = dict_comp_visc_impr
                # es una actualización .. 
                ### Aún no implementada
            else:
                comp_visc_impr = ComponentViscosityImprovement(dict_comp_visc_impr)
                db.session.add(comp_visc_impr)
                db.session.commit()
                data["id"] = comp_visc_impr.id
        else:
            data = {"rest": "ERROR"}
    return jsonify(data)

# @api_data.route('/api/create/component_viscosity_improvement', methods = ['GET'])
# def create_component_viscosity_improvement():
#     """ Crear Componete- Mejora de Viscosidad  """
#     data = {"rest": "OK"}
#     return jsonify(data)