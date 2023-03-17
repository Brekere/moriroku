from flask import Blueprint, render_template
from asb_mori_paint.Components.models.component_type import ComponentType
from asb_mori_paint.Components.models.components import Components
from asb_mori_paint.Formulas.models.colors_formulas import ColorFormula
from asb_mori_paint.Formulas.models.filters import Filter
from asb_mori_paint.Formulas.models.filters_colors import ColorFilter
from asb_mori_paint.Formulas.models.formulas_components import FormulaComponent
from asb_mori_paint.Formulas.models.zpl_code_mixing_process import ZPLCodeMixingProcess
from asb_mori_paint.Models.models.colors_models import ColorModel
from asb_mori_paint.Models.models.models import Models

mixing = Blueprint('mixing', __name__)

@mixing.route('/mixing', methods=['GET'])
def mixing_init():    
    return render_template('mixing/mixing.html')

@mixing.route('/OT_Detail', methods=['GET'])
def ot_detail():
    ZPLCodeMixingProcess.query.all()

    list_=[]
    data_formulas = []
    data_filters = []
    data_fColors = []
    data_Models = []
    data_ModelColor = []
    data_Db_FiltersColors = ColorFilter.query.all()
    data_Db_ColorsFormulas = ColorFormula.query.all()
    data_Db_Models = Models.query.all()
    data_Db_ModelColor = ColorModel.query.all()
    data_Db_Filters = Filter.query.all()

    for filterColor in data_Db_FiltersColors:
        data_dict = filterColor.get_json_format()
        data_fColors.append(data_dict)
    for model in data_Db_Models:
        data_dict = model.get_json_format()
        data_Models.append(data_dict)
    for model_color in data_Db_ModelColor:
        data_dict = model_color.get_json_format()
        data_ModelColor.append(data_dict)
    for filter in data_Db_Filters:
        data_dict = filter.get_json_format()
        data_filters.append(data_dict)
    for colors in data_Db_ColorsFormulas:
        data_dict = colors.get_json_format()
        data_formulas.append(data_dict)

    for formulas in data_formulas:
        id_filter = -1
        for formulasColor in data_fColors:
            if formulasColor['id_color'] == formulas['id']:
                id_filter = formulasColor['id_filter']
        name_filter = ''
        if id_filter != -1:
            name_filter = data_filters[id_filter-1]['name']
        list_.append({
            'id_formula': formulas['id'],
            'name_formula': formulas['name'],
            'color_code': formulas['color_code'],
            'id_filtro' : id_filter,
            'name_filtro' : name_filter,
            'min_viscosity' : formulas['min_viscosity'],
            'max_viscosity' : formulas['max_viscosity']
        })    

    return render_template('mixing/m_ot_details.html', list_ = list_, data_Models = data_Models, data_ModelColor = data_ModelColor)

@mixing.route('/mixing/containers/', methods=['GET'])
def mix_container():
    return render_template('mixing/mixing_container.html')

@mixing.route('/mixing/containers/component/<int:id>', methods=['GET'])
def mix_component(id):
    list_ = []
    list_formulas_components = []
    list_components = []
    list_component_type = []
    base_name = ''

    sql_formulas_components = FormulaComponent.query.all()
    for x in sql_formulas_components:
        json_formulas_components = x.get_json_format()
        list_formulas_components.append(json_formulas_components)

    sql_components = Components.query.all()
    for x in sql_components:
        json_components = x.get_json_format()
        list_components.append(json_components)

    sql_component_type = ComponentType.query.all()
    for x in sql_component_type:
        json_component_type = x.get_json_format()
        list_component_type.append(json_component_type)    

    for x in range(len(list_formulas_components)):
        id_component = -1
        if id == list_formulas_components[x]['id_color_formula']:
            id_component = list_formulas_components[x]['id_component']
        if id_component != -1:
            id_type = -1
            nick_name = ''
            identifier = ''
            for y in range(len(list_components)):
                if  id_component == list_components[y]['id']:
                    id_type = list_components[y]['id_type']
                    nick_name = list_components[y]['nick_name']
                    identifier = list_components[y]['identifier']
                    if id_type == 1:
                        base_name = nick_name
                    for z in range(len(list_component_type)):
                        if id_type == list_component_type[z]['id']:
                            list_.append({
                                'id': x,
                                'id_component': id_component,
                                'name_component': list_components[y]['identifier'],
                                'nickname': nick_name,
                                'tolerance': list_formulas_components[x]['tolerance'],
                                'percent': list_formulas_components[x]['percentage'],
                                'type': list_component_type[z]['id'],
                                'name_type': list_component_type[z]['name'],
                                'identifier': identifier
                            })
    
    for x in list_:
        if x['nickname'] == base_name:
            list_.remove(x)
            list_.insert(0,x)

    return render_template('mixing/m_cont_comp.html', list_ = list_[::-1])

