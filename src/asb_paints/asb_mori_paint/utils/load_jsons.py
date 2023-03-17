import json

#from pyrsistent import v ## ... creo no se necesita

## función de borrado de elemetnos pero al parecer el elemento que no se debe considerar (los catalizadores) no se tienen en las formulas 
##### Funcion prbada en Probado en Google Colab 

def print_formulas(lista):
    """ Para imprimir una lista de formulas"""
    i = 0
    for formula in lista:
        i += 1
        print("Formula {}".format(i))
        components = formula["list_componets"]
        print("Lista de componentes")
        for comp in components:
            print("----- {}".format(comp))

def eliminate_component_in_formulas(lista,component_type_id):
    """ Elimina un componente de la lista de componentes de cada formula dado un id """
    i = 0
    for formula in lista:
        i += 1
        components = formula["list_componets"]
        comp_to_remove = []
        for comp in components:
            if component_type_id == comp["type"]:
                comp_to_remove.append(comp)
        for comp in comp_to_remove:
            components.remove(comp)
    #print_formulas(lista)
    return lista

id_catalizador = 3 # el que esta en el archivo json de los catalziadores ... 

path_jsons = 'asb_mori_paint/static/config_json/'
path_json_additiver = path_jsons + 'additives.json'
path_json_base = path_jsons + 'bases.json'
path_json_catalysts = path_jsons + 'catalysts.json'
path_json_color_model = path_jsons + 'color_model.json'
path_json_color_viscosity = path_jsons + 'color_viscosity.json'
path_json_container_info = path_jsons + 'container_info.json'
path_json_filter_color = path_jsons + 'filter_color.json'
path_json_filters = path_jsons + 'filters.json'
path_json_formulas = path_jsons + 'formulas.json'
path_json_device = path_jsons + 'info_device.jdon'
path_json_positions = path_jsons + 'job_positions.json'
path_json_jug_info = path_jsons + 'jug_info.json'
#path_json_ = path_jsons + 'language.json'
path_json_models = path_jsons + 'models.json'
path_json_solvents = path_jsons + 'solvents.json'
path_json_types_components = path_jsons + 'types_components.json'
path_json_work_orders = path_jsons + 'work_orders.json'
path_json_workers = path_jsons + 'workers.json'
path_json_pintado_pesos = path_jsons + 'pintado_pesos.json'
path_json_containers_barcodes_info = path_jsons + 'containers_barcodes_info.json'

def load_json_file(file_path):
    data = {}
    try:
        file = open(file_path)
        data = json.load(file)
        file.close() 
    except Exception as e:
        data = {"error": "No se pudo cargar el archivo", "info_error": str(e)} 
    return data

def load_json_additiver():
    return load_json_file(path_json_additiver)
    # file = open('asb_mori_paint/static/config_json/additives.json')
    # data_additives = json.load(file)
    # file.close()
    # return data_additives

def load_json_bases():
    return load_json_file(path_json_base)
    # file = open('asb_mori_paint/static/config_json/bases.json')
    # data_bases = json.load(file)
    # file.close()
    # return data_bases

def load_json_catalysts():
    return load_json_file(path_json_catalysts)
    # file = open('asb_mori_paint/static/config_json/catalysts.json')
    # data_catalysts = json.load(file)
    # file.close()
    # return data_catalysts

def load_json_color_model():
    return load_json_file(path_json_color_model)
    # file = open('asb_mori_paint/static/config_json/color_model.json')
    # data_color_model = json.load(file)
    # file.close()
    # return data_color_model

def load_json_color_viscosity():
    return load_json_file(path_json_color_viscosity)
    # file = open('asb_mori_paint/static/config_json/color_viscosity.json')
    # data_cViscosity = json.load(file)
    # file.close()
    # return data_cViscosity

def load_json_container_info():
    return load_json_file(path_json_container_info)
    # file = open('asb_mori_paint/static/config_json/container_info.json')
    # data_container_info = json.load(file)
    # file.close()
    # return data_container_info

def load_json_filter_color():
    return load_json_file(path_json_filter_color)
    # file = open('asb_mori_paint/static/config_json/filter_color.json')
    # data_fColors = json.load(file)
    # file.close()
    # return data_fColors

def load_json_filters():
    return load_json_file(path_json_filters)
    # file = open('asb_mori_paint/static/config_json/filters.json')
    # data_filters = json.load(file)
    # file.close()
    # return data_filters

def load_json_formulas():
    ### quitar de aquí el catalizador en cada formula que lo tenga  .. 
    data_formulas = load_json_file(path_json_formulas)
    # Por ahora no es necesaria ya que el catalizador no aparece en las formulas ... 
    #lista = data_formulas["list"]
    #lista_2 = eliminate_component_in_formulas(lista, id_catalizador)
    #data_formulas["list"] = lista_2
    return data_formulas
    # file = open('asb_mori_paint/static/config_json/formulas.json')
    # data_formulas = json.load(file)
    # file.close()
    # return data_formulas

def load_json_info_device():
    return load_json_file(path_json_device)
    # file = open('asb_mori_paint/static/config_json/info_device.json')
    # data_info_device = json.load(file)
    # file.close()
    # return data_info_device

def load_json_job_positions():
    return load_json_file(path_json_positions)
    # file = open('asb_mori_paint/static/config_json/job_positions.json')
    # data_job_positions = json.load(file)
    # file.close()
    # return data_job_positions

def load_json_jug_info():
    return load_json_file(path_json_jug_info)
    # file = open('asb_mori_paint/static/config_json/jug_info.json')
    # data_jug_info = json.load(file)
    # file.close()
    # return data_jug_info

def load_json_models():
    return load_json_file(path_json_models)
    # file = open('asb_mori_paint/static/config_json/models.json')
    # data_Models = json.load(file)
    # file.close()
    # return data_Models

def load_json_solvents():
    return load_json_file(path_json_solvents)
    # file = open('asb_mori_paint/static/config_json/solvents.json')
    # data_solvents = json.load(file)
    # file.close()
    # return data_solvents

def load_json_types_components():
    return load_json_file(path_json_types_components)
    # file = open('asb_mori_paint/static/config_json/types_components.json')
    # data_types_components = json.load(file)
    # file.close()
    # return data_types_components

def load_json_work_orders():
    return load_json_file(path_json_work_orders)
    # file = open('asb_mori_paint/static/config_json/work_orders.json')
    # data_worker_order = json.load(file)
    # file.close()
    # return data_worker_order

def load_json_workers():
    return load_json_file(path_json_workers)
    # file = open('asb_mori_paint/static/config_json/workers.json')
    # data_workers = json.load(file)
    # file.close()
    # return data_workers

def load_json_pintado_pesos():
    return load_json_file(path_json_pintado_pesos)
    # file = open('asb_mori_paint/static/config_json/workers.json')
    # data_workers = json.load(file)
    # file.close()
    # return data_workers

def load_json_containers_barcodes_info():
    return load_json_file(path_json_containers_barcodes_info)