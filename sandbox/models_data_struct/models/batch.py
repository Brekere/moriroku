
from formula import Formula
from datetime import datetime

class Bathc():
    batch_number = 0
    wo = 0 # work order  ... 
    worker_id = 0  # ya viene el id_formula/id_color aquí; también ta viene el modelo; también ya viene la cantidad de piezas
    client = ""
    #model = "" 
    #id_formula = -1 # id_color
    #formula = Formula()
    #quantity_of_pieces = 0
    start_timestamp = None
    end_timestamp = None
    id_filter = -1 # aunque ya viene relacionado con el color/formula 
    container_list = [] # lista de id de contenedores
    temperature = 0 # celcius
    humidity = 0 # se mide g/m3 = gramos de agua por cada metro cúbico de aire


    def __init__(self, batch_number, wo, worker_id, client, id_filter):
        self.start_timestamp = datetime.now()
        self.batch_number = batch_number
        self.wo = wo
        self.worker_id = worker_id
        self.client = client
        self.id_filter = id_filter
    
    def update_temperature_humidity(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

    def end_process(self):
        self.end_timestamp = datetime.now()
    
    # hacer función para regresar solo la fecha actual ..... 

    def __str__(self) -> str:
        print("""
        Información de Lote:
            # Lote: {}
            # WO: {}
            Cliente: {}
            # Empleado: {}
            Intervalo de Tiempos: {} -- {}
            id Filtro: {}
            Temperatura y humedad: [{}, {}]
            Lista de Contenedores: {}
        """.format( self.batch_number, self.wo, self.client, self.worker_id, self.start_timestamp, self.end_timestamp, self.id_filter, self.temperature, self.humidity, self.container_list ) )