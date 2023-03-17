import json
from flask import Blueprint, render_template, request
from ..Components.models.component_type import ComponentType
from asb_mori_paint.Components.models.components import Components
from asb_mori_paint.Formulas.models.colors_formulas import ColorFormula
from asb_mori_paint.utils.error_handlers_api import create_response_data, restError, restSuccess
from asb_mori_paint.viscosity.model.improved_mix import ImprovedMix

viscosity = Blueprint('viscosity', __name__)

@viscosity.route('/viscosity/container/<int:id>', methods=['GET'])
def viscosity_cont(id):
    list_improved = []
    improved_formula = ImprovedMix.query.filter_by(id_formula= id).first()
    component_formula = Components.query.filter_by(id= improved_formula.id_component).first()
    type_component = ComponentType.query.filter_by(id= improved_formula.id_type_component).first()

    print(type_component.name)

    list_improved.append({
        "id_component": improved_formula.id_component,
        "component_identifier": component_formula.identifier,
        "component_nickname": component_formula.nick_name,
        "type_component": type_component.name,
        "substance_g": improved_formula.weight_g,
        "tolerance": improved_formula.tolerance
    })

    return render_template('viscosity/vis_cont_detail.html', list_improved = list_improved)

@viscosity.route('/api/getColorbyColorCode', methods=['GET'])
def color_by_colorcode():
    content = request.args
    if 'id_color' in content:
        try:
            color = ColorFormula.query.filter(ColorFormula.color_code == '7N5').first()
            print(color)
        except Exception as e:
            data = create_response_data(restError, "Error en la base de datos", [str(e)])
        if color:
            print(color.get_json_format())
            data_dict = color.get_json_format()            
            data_result = {"record": data_dict}
            data = create_response_data(restSuccess, "Registro encontrado", None, data_result)
        else:
            data = create_response_data(restError, "Registro no encontrado")
    else:
        data = create_response_data(restError, 'La petición no contiene el código de color')

    return data