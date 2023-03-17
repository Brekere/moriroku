from flask import Blueprint, render_template, abort

#### 
from web.show_data.models.mixing_process import MixingProcess
from web.show_data.models.mix_container import MixContainer


show_data = Blueprint('show_data', __name__)

@show_data.route('/show')
def home_show_data():
    """ Selección para mostrar datos ..  """
    return render_template("show_data/index.html")

@show_data.route('/show/process')
def show_process():
    """ Mostrar datos de Procesos """
    processes = MixingProcess.query.all()
    for proc in processes:
        print(proc)
    return render_template("show_data/processes.html", processes = processes)

@show_data.route('/show/containers')
def show_containers():
    """ Mostrar datos de Contenedores """
    containers = MixContainer.query.all()
    for cont in containers:
        print(cont)
    return render_template("show_data/containers.html", containers= containers)