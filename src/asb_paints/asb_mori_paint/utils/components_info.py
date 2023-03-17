
from asb_mori_paint.utils.load_jsons import load_json_bases, load_json_additiver, load_json_catalysts, load_json_solvents


def get_identifier_component_from_list(list_comp, id_comp):
    comp = {}
    for x in list_comp:
        if x['id'] == id_comp:
            comp = x
            break
    if(bool(comp)):
        data_result = {
            'identifier' : comp['identifier']
        }
    else:
        data_result = {"error": "No se encontro ningún componente ({}) con ese identificador"}
    return data_result

def get_base_identifier(id_comp):
    bases_ = load_json_bases()
    data_result = get_identifier_component_from_list(bases_['list'], id_comp)
    if "error" in data_result:
        data_result["error"] = data_result["error"].format("Base")
        print("Entro!! ")
    return data_result

def get_additives_identifier(id_comp):
    additives_ = load_json_additiver() 
    data_result = get_identifier_component_from_list(additives_['list'], id_comp)
    if "error" in data_result:
        data_result["error"] = data_result["error"].format("Aditivo")
    return data_result

def get_catalysts_identifier(id_comp):
    catalysts_ = load_json_catalysts() 
    data_result = get_identifier_component_from_list(catalysts_['list'], id_comp)
    if "error" in data_result:
        data_result["error"] = data_result["error"].format("Catalizador")
    return data_result

def get_solvents_identifier(id_comp):
    solvents_ = load_json_solvents() 
    data_result = get_identifier_component_from_list(solvents_['list'], id_comp)
    if "error" in data_result:
        data_result["error"] = data_result["error"].format("Solventes")
    return data_result