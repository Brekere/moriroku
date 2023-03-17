import math
from msilib.schema import Component
from asb_mori_paint.Components.models.components import Components
from asb_mori_paint.Formulas.models.colors_formulas import ColorFormula
from asb_mori_paint.Formulas.models.formulas_components import FormulaComponent
from asb_mori_paint.Models.models.colors_models import ColorModel

from asb_mori_paint.utils.load_jsons import load_json_formulas, load_json_models, load_json_color_model, load_json_pintado_pesos


def get_id_pintado_by_color_model(id_color, id_model):
    c_m_selected = {}
    color_model_sql = ColorModel.query.all()
    if color_model_sql:
        for x in color_model_sql:
            json_color_mode = x.get_json_format()
            if json_color_mode['id_color'] == id_color and json_color_mode['id_model'] == id_model:
                c_m_selected = json_color_mode
                break
    
    if len(c_m_selected) > 0:
        return c_m_selected

    return {"error": "No hay Pintad con el par de ids color, modelo dado ({},{})".format(id_color, id_model)}

def get_pintado_peso_by_pintado(id_):
    pintado_peso = load_json_pintado_pesos()
    if "error" in pintado_peso:
        return pintado_peso
    list_p_p = pintado_peso["list"]
    p_p_selected = {}
    for p_p in list_p_p:
        if id_ == p_p["pintado"]:
            p_p_selected = p_p
            break
    if bool(p_p_selected):
        return p_p_selected
    return {"error": "No hay Pintado con el ids dado {}".format(id_)} 

def get_formula_by_id(id_formula):
    index = 1
    list_formulas_sql = []
    list_formula = {
        'name': '', 
        'id': '', 
        'color_code': '',
        'list_componets': ''
    }
    list_formula_component = []

    fomula = ColorFormula.query.get(id_formula)
    if fomula:
        data_formula = fomula.get_json_format()
        list_formula["id"] = id_formula
        list_formula["name"] = data_formula['name']
        list_formula["color_code"] = data_formula['color_code']
    else:                
        return {"error": "No hay formula con el id dado {}".format(id_formula)}

    list_component_formula = FormulaComponent.query.all()
    if list_component_formula:
        for x in list_component_formula:
            json_component_formula = x.get_json_format()
            if id_formula == json_component_formula['id_color_formula']:
                list_formulas_sql.append(json_component_formula)
    else:
        return {"error": "No hay formula con el id dado {}".format(id_formula)}

    list_component = Components.query.all()
    if list_component:
        for x in list_component:
            json_component = x.get_json_format()
            for y in  list_formulas_sql:
                if(y['id_component'] == json_component['id']):                    
                    list_formula_component.append({
                        'id' : index,
                        'id_component': y['id_component'], 
                        'name': json_component['identifier'],
                        'nickname': json_component['nick_name'],
                        'type': json_component['id_type'], 
                        'percentage': y['percentage'], 
                        'tolerance': y['tolerance']
                    })
                    index = index + 1
                    
                    break
    else:
        return {"error": "No hay componentes con el id de la formula dado {}".format(id_formula)}

    list_formula["list_componets"] = list_formula_component
    formula_in_use = list_formula

    return formula_in_use

def get_model_by_id(id_model):
    models = load_json_models()
    if "error" in models:
        return models 
    list_m = models["list"]
    model_in_use = {}
    for model in list_m:
        if model["id"] == id_model:
            model_in_use = model
            break
    if bool(model_in_use):
        return model_in_use
    return {"error": "No hay modelo con el id dado {}".format(id_model)}


def calculate_containers_by_formula_and_num_pieces(id_formula, id_model, num_pieces, grams_to_recirculate, base_weight):    
    formula = get_formula_by_id(id_formula)
    pintado = get_id_pintado_by_color_model(id_formula, id_model)
    #model = get_model_by_id(id_model) ## usar después ... 
    if "error" in formula:
        return formula
    if "error" in pintado:
        return pintado
    #pintado_peso = get_pintado_peso_by_pintado(pintado["id_"])
    #if "error" in pintado_peso:
    #    return pintado_peso
    print("Formula: ",formula)
    print()
    print("Pintado: ",pintado)
    print()
    components = formula["list_componets"]
    print("Components: ",components)
    print()
    gr_base_by_piece = pintado["base_weight"]
    print("Peso Base: ",gr_base_by_piece)
    #total_weight = grams_by_piece * num_pieces + grams_to_recirculate
    total_percentage = 0
    for component in components:
        total_percentage += component["percentage"] 
    weight_by_container = base_weight * total_percentage/100
    total_weight = (gr_base_by_piece*total_percentage/100) * num_pieces + grams_to_recirculate
    num_containers = math.ceil( total_weight/weight_by_container ) # rounder to the next integer .. 

    if weight_by_container*num_containers > total_weight:
        last_container_base_weight = 100*(total_weight - weight_by_container*(num_containers - 1))/total_percentage
    else:
        last_container_base_weight = 100*weight_by_container/total_percentage

    print("""
            Calculando el numero de contenedores de acuerdo a la formula:
                id_formula: {}
                num_pieces: {}
                grams_to_recirculate: {}
                gr_base_by_piece: {}
                base_weight: {}
                total_weight: {}
                total_percentage: {}
                weight_by_container: {}
                num_containers: {}
                last_container_weight: {}
    """.format(id_formula, num_pieces, grams_to_recirculate, gr_base_by_piece, base_weight, total_weight, total_percentage,
    weight_by_container, num_containers, last_container_base_weight))

    return  {"num_containers": num_containers, "pintado": pintado["id_"], "total_weight": total_weight, "last_container_base_weight": last_container_base_weight}

## ------ id_model se utilizará para la tabla que me relaciona el color con el modelo y sacar los pesos por pieza .. 
def calculate_containers_by_formula_and_num_pieces_(id_formula, id_model, num_pieces, grams_to_recirculate, grams_by_piece, base_weight):
    formula = get_formula_by_id(id_formula)
    model = get_model_by_id(id_model) ## usar después ... 
    if "error" in formula:
        return formula
    components = formula["list_componets"]
    total_weight = grams_by_piece * num_pieces + grams_to_recirculate
    total_percentage = 0
    for component in components:
        total_percentage += component["percentage"] 
    weight_by_container = base_weight * total_percentage/100

    num_containers = math.ceil( total_weight/weight_by_container ) # rounder to the next integer .. 

    print("""
            Calculando el numero de contenedores de acuerdo a la formula:
                id_formula: {}
                num_pieces: {}
                grams_to_recirculate: {}
                grams_by_piece: {}
                base_weight: {}
                total_weight: {}
                total_percentage: {}
                weight_by_container: {}
                num_containers: {}
    """.format(id_formula, num_pieces, grams_to_recirculate, grams_by_piece, base_weight, total_weight, total_percentage,
    weight_by_container, num_containers))

    return  {"num_containers": num_containers}