import json
import os
import hashlib
from asb_mori_paint import db
from flask import Blueprint, render_template, request
from asb_mori_paint.Components.models.components_qr_info import ComponentQRInfo
from asb_mori_paint.Components.models.suppliers import Supplier
from asb_mori_paint.Containers.models.containers_info import ContainerInfo
from asb_mori_paint.Formulas.models.formulas_components import FormulaComponent
from asb_mori_paint.Formulas.models.zpl_code_mixing_process import ZPLCodeMixingProcess
#from asb_mori_paint.Workers.models.departaments import Departament
from asb_mori_paint.viscosity.model.improved_mix import ImprovedMix
from asb_mori_paint.utils.error_handlers_api import create_response_data, restError, restSuccess

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def home_init():
    improved_mix = FormulaComponent.query.filter_by(id_component = 1).with_entities(FormulaComponent.id_component).all()
    ZPLCodeMixingProcess.query.all( )
    #example = Supplier.query.all()
    #example = ComponentQRInfo.query.all()
    #example = ContainerInfo.query.all()
    
    return render_template('home/home.html')

#@home.route('/api/register', methods=['POST'])
#def register_departament():    
#    content = request.json.get('params')
#    if 'record' in content:
#        dict_departament = content['record']
#        if 'departament' in dict_departament and 'password' in dict_departament:
#                pass_hash = hashPassword(dict_departament['password'])                
#                departament_ = Departament(departament= dict_departament['departament'], password=  pass_hash)
#                try:
#                    db.session.add(departament_)
#                    db.session.commit()
#                    data_result = {'id' : departament_.id}
#                    data = create_response_data(restSuccess, "Registro guardado correctamente", None, data_result)
#                except Exception as e:
#                    data = create_response_data(restError, 'No se a guardado el registro', [str(e)])
#        else:    
#            data = create_response_data(restError, "No se a mandado los parametro correspondientes")
#    else:
#        data = create_response_data(restError, "No se a mandado los parametro correctamente")
#        
#    return data
#
#@home.route('/api/validate_departament', methods=['POST'])
#def validate_departament():
#    content = request.json.get('params')
#    if 'record' in content:
#        dict_auth = content['record']
#        if 'departament' in dict_auth and 'password' in dict_auth:            
#            departament_ = Departament.query.filter_by(departament = dict_auth['departament']).first()
#            user_pass = departament_.password
#            user_salt = user_pass[:32]
#            user_password = user_pass[32:]
#            result = validateAuthDepartament(user_salt, dict_auth['password'], user_password)
#            if result:
#                data_result = {'id': departament_.id}
#                data = create_response_data(restSuccess, "Autenticación aprobada", None, data_result)
#            else:
#                data = create_response_data(restError, "Nombre de usuario o contraseña no válidos.")
#        else:
#            data = create_response_data(restError, "No se encuentran los campos requeridos.")
#    else:
#        data = create_response_data(restError, "No se a mandado los parametro correspondientes")
#
#    return data

def hashPassword(password):
    salt = os.urandom(32)

    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    storage_hash = salt + key

    return storage_hash

def validateAuthDepartament(salt, password, user_pass):
    
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )

    r_c_pass = key == user_pass
    return r_c_pass