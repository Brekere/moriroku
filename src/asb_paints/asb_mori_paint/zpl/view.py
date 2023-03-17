#from shutil import ExecError
from flask import Blueprint, jsonify, request, render_template
#import pathlib

from sqlalchemy import func

from asb_mori_paint import db, main_path
from datetime import datetime, timedelta
from asb_mori_paint.Formulas.models.zpl_code_mixing_process import ZPLCodeMixingProcess

zpl_code_path = main_path+"/data/zpl_code/"

zpl = Blueprint('zpl', __name__)

from asb_mori_paint.historical.models.mix_container import MixContainer
from asb_mori_paint.historical.models.mixing_process import MixingProcess

from asb_mori_paint.utils.error_handlers_api import *
from asb_mori_paint.utils.load_jsons import load_json_formulas

## ---------------------- Conatiner's Label 

def get_formula_name_by_id(id_formula):
    formulas = load_json_formulas()
    if "error" in formulas:
        return {"error": "No se pudo cargar el archivo de formulas"}
    list_f = formulas["list"]
    for formula in list_f:
        if formula["id"] == id_formula:
            return {"name": formula["name"]} 
    return {"error": "No existe el id dado"}

def get_labels_by_id_worker_in_last_24_hours(id_worker):
    # Obetener primero los proceso que ha realizado el trabajador el día de hoy
    data = {"id_worker": id_worker}
    today_ = datetime.now()
    dDay = timedelta(days=1)
    min_datetime = today_ - dDay
    processes = MixingProcess.query.filter(MixingProcess.id_worker == id_worker, MixingProcess.t_start >= min_datetime)
    print("Entro aquií y : {}".format(processes))
    if processes:
        data["info"] = []
        for process in processes:
            name_formula = get_formula_name_by_id(process.id_formula)
            #print(process.t_end)
            #print(type(process.t_end))
            if process.t_end is None:
                continue
            date_time_proc = process.t_end
            labels_process = { "id_process": process.id, "formula": name_formula['name'], "num_containers": process.num_containers, "number_of_pieces": process.number_of_pieces, "list_labels": [], "date": date_time_proc.strftime("%d/%m/%Y")} 
            # listar los contenedores de esos procesos 
            containers = MixContainer.query.filter(MixContainer.id_process == process.id) 
            print("Contenedores con proceso id: {}".format(MixContainer.id_process))
            if containers:
                num_container = 1
                for container in containers:
                    #print(container.t_end)
                    #print(type(container.t_end))
                    if container.t_end is None:
                        num_container += 1
                        continue
                    print("num_container = {}  ----> id: {}".format(num_container, container.id))
                    info_zpl_file = {"id_container": container.id, "id_barcode": container.id_barcode, "num_container": num_container, "date": container.t_end.strftime("%d/%m/%Y, %H:%M")}
                    # por ende obtener los archivos de etiquetas de esos contenedores .. 
                    pathFileZPL = zpl_code_path + "{}".format(container.id) + ".zpl"
                    print(pathFileZPL) 
                    try:
                        with open(pathFileZPL, 'r') as file1:
                            contents = file1.readlines()
                        info_zpl_file["file"] = contents
                    except Exception as e:
                        print(str(e))
                        info_zpl_file["error"] = "Nos e pudo encontrar el archivo ZPL del contenedor"
                    num_container += 1
                    labels_process["list_labels"].append(info_zpl_file)
                labels_process["list_labels"] = labels_process["list_labels"][::-1] # mandar en orden descendente
            data["info"].append(labels_process)
        data["info"] = data["info"][::-1] # mandar en orden descendente
    else:
        data["error"] = "No hay datos relacionados al trabajador registrado [en las últimas 24 horas]"
    return data 

#def get_info_process_container_label(id_container):
#    pass 

#@zpl.route('/api/container_label', methods = ['GET', 'POST'])
#def transactions_containers_label():
#    "Obtener o Guardar zpl de etiqueta de contenedor; al obtener la eiqueta se mandará información del proceso, del contenedor y la fecha"
#    data = {}
#    print("Entro a imporimir!!!")
#    if request.method == 'GET':
#        args = request.args
#        print(args)
#        if "id" in args:# and int(args["id"]) > 0: # para poder validar mejor la salida del casteo
#            try:
#                id_mix_container = int(args["id"])
#            except Exception as e:
#                return create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)]) 
#            container = MixContainer.query.get(id_mix_container)
#            if container:
#                pathFileZPL = zpl_code_path + args["id"] + ".zpl"
#                try:
#                    with open(pathFileZPL, 'r') as file1:
#                        contents = file1.readlines()
#                except Exception as e:
#                    print(str(e))
#                    return create_response_data(restError, "No se puedo obtener: Error en el proceso de lectura del archivo", [str(e)]) 
#                data_result = {"zpl_code": contents }
#                data = create_response_data(restSuccess, "Archivo ZPL encontrado!", None, data_result)
#            else:
#                data = create_response_data(restError, "No existe el registro con ese id") 
#        else:
#            if "id_worker" in args:# and int(args["id_worker"]) > 0: # para poder validar mejor la salida del casteo
#                id_worker = int(args["id_worker"])
#                data_result = get_labels_by_id_worker_in_last_24_hours(id_worker) 
#                if "error" in data_result:
#                    data = create_response_data(restSuccess, "Archivos ZPL encontrados para el Trabajador dado!", None, data_result) 
#                else:
#                    data = create_response_data(restError, data_result["error"])
#            else:
#                data = create_response_data(restError, "No se mandarón los parametros esperados")  
#    else:
#        content = request.json.get('params')
#        print(content)
#        if "record" in content:
#            content_record = content["record"]
#            if "id" in content_record and int(content_record["id"]) > 0 and "zpl_code" in content_record:
#                try:
#                    id_mix_container = int(content_record["id"])
#                except Exception as e:
#                    return create_response_data(restError, "Al tratar de transformar el valor del id de str a int", [str(e)]) 
#                container = MixContainer.query.get(id_mix_container)
#                if container:
#                    pathFileZPL = zpl_code_path + "{}".format(content_record["id"]) + ".zpl"
#                    print(pathFileZPL)
#                    try:
#                        with open(pathFileZPL, "w") as file1:
#                            toFile = content_record["zpl_code"]
#                            file1.write(toFile)
#                    except Exception as e:
#                        return create_response_data(restError, "No se puedo guardar: Error en el proceso de esrcitura del archivo", [str(e)]) 
#                    data = create_response_data(restSuccess, "Archivo ZPL guardado correctamente ") 
#                else:
#                    data = create_response_data(restError, "No se puedo guardar: No existe el registro con ese id") 
#            else:
#                data = create_response_data(restError, "No se mandaron los parametros esperados: id y zpl_code")
#        else:
#            data = create_response_data(restError, "No se mando la estructura esperada")
#    print("Resultado: {}".format(data))
#    return jsonify(data)


@zpl.route('/zpl/containers_labels/<int:id_worker>')
def print_again_containers_label(id_worker):
    data_result = get_labels_by_id_worker_in_last_24_hours(id_worker)
    #return "<h1> En construcción! </h1> <br> " +  "<p> {}  </p>".format(data_result)
    #return jsonify("<h1> En construcción! </h1> <br> " +  "{}".format(data_result))
    print(data_result)
    return render_template('zpl/re_print_zpl.html', data_zpl = data_result) 

@zpl.route('/api/save_zpl', methods=['POST'])
def test_zpl():
    content = request.json.get('params')
    print(content)
    if "record" in content:
        dict_content_zpl = content['record']
        print(dict_content_zpl)
        zpl = ZPLCodeMixingProcess(dict_content_zpl)
        if len(zpl.list_errors) != 0:
            data = create_response_data(restError, "Error", zpl.list_errors)
        else:
            try:
                print(zpl)
                db.session.add(zpl)
                db.session.commit()
                data_result = {"record": dict_content_zpl}
                data = create_response_data(restSuccess, "Registro guardado correctamente", None, data_result)
            except Exception as e:
                data = create_response_data(restError, "Ha ocurrido un error en el registro",[str(e)])
    else:
        data = create_response_data(restError, "Error de envío de información")

    return jsonify(data)