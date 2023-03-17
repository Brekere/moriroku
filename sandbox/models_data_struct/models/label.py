from datetime import datetime

class Label():
    """ Clase donde se guardará la información de la etiqueta a ser impresa para los contenedores"""
    wo = 0
    start_timestamp = None
    end_timestamp = None 
    date = None 
    start_time = None #
    end_time = None 
    worker_name = ""
    component_list = []  #id/name
    quantity_by_component = [] # kg
    qr = None 
    rework = False # se imprime RS -> True y RN-> False
    # extra que va en el QR
    batch_number = 0
    filter = "" # name

    def __init__(self,batch_number, wo, start_timestamp, end_timestamp, worker_name, component_list, quantity_by_component, rework, filter):
        self.wo = wo
        self.batch_number = batch_number
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.get_date_times()
        self.worker_name = worker_name
        self.component_list = component_list
        self.quantity_by_component = quantity_by_component
        self.rework = rework
        self.filter = filter

    # crear función que genere el QR a ser impreso
    def generate_qr(self):
        pass 

    def get_date_times(self):
        # get date from start_timestamp
        # get start_time from start_timestamp
        # get end_time from end_timestamp
        pass 

    def __str__(self) -> str:
        rework_text = "RS" if self.rework == True else "RN"
        print("""
        Información de Etiqueta: 
            # Lote: {}
            # WO: {}
            # date: {}
            start/end time: {} -- {}
            worker name: {}
            rework: {}
            Filtro: {}
            component_list: {}
            quantity_by_component: {}
        """.format( self.batch_number, self.wo, self.date, self.start_time, self.end_time, self.worker_name, rework_text, self.filter, self.component_list, self.quantity_by_component ) )