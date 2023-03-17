from re import template
from unicodedata import name
from flask import Blueprint, render_template
import json

mixing = Blueprint('mixing', __name__)

@mixing.route('/mixing', methods=['GET'])
def mixing_init():
    return render_template('mixing/mixing.html')

@mixing.route('/OT_Detail', methods=['GET'])
def ot_detail():
    list_=[]
    file = open('asb_mori_paint/static/config_json/formulas.json')
    data = json.load(file)
    file.close()
    file = open('asb_mori_paint/static/config_json/filters.json')
    data_filters = json.load(file)
    file.close()
    file = open('asb_mori_paint/static/config_json/filter_color.json')
    data_fColors = json.load(file)
    file.close()
    file = open('asb_mori_paint/static/config_json/models.json')
    data_Models = json.load(file)
    file.close()
    
    for f in data['list']:
        id_filter = -1
        for x in data_fColors['list']:
            if(x['id_color'] == f['id']):
                id_filter = x['id_filter']
        name_filter = ""
        if(id_filter != -1):
            name_filter = data_filters["{}".format(id_filter)]['name']
        else:
            id_filter = 0
            name_filter = "test"
        list_.append({            
            'id_formula': f['id'],
            'name_formula': f['name'],
            'id_filtro' : id_filter,
		    'name_filtro' : name_filter
        })

    return render_template('mixing/m_ot_details.html', list_ = list_, data_Models = data_Models)

@mixing.route('/mixing/containers/', methods=['GET'])
def mix_container():
    return render_template('mixing/mixing_container.html')

@mixing.route('/mixing/containers/component/<int:id>', methods=['GET'])
def mix_component(id):
    list_component_id = []
    list_ =[]
    file = open('asb_mori_paint/static/config_json/formulas.json')
    data = json.load(file)
    file.close()
    file = open('asb_mori_paint/static/config_json/types_components.json')
    data_type_comp = json.load(file)
    file.close()

    print(data_type_comp)

    for f in data['list']:
        if(id == f['id']):
            list_component_id = f['list_componets']

    for y in data_type_comp:
        print(data_type_comp[y]['name'])
    
    for x in range(len(list_component_id)):
        type_name = ''
        for y in data_type_comp:
            if data_type_comp[y]['id'] == list_component_id[x]['type']:
                type_name = data_type_comp[y]['name']
        list_.append({
            'id': x,
            'id_component': list_component_id[x]['id_component'],
            'name_component': list_component_id[x]['name'],
            'tolerance': list_component_id[x]['tolerance'],
            'percent': list_component_id[x]['percentage'],
            'type': list_component_id[x]['type'],
            'name_type': type_name
        })    

    return render_template('mixing/m_cont_comp.html', list_ = list_[::-1])

