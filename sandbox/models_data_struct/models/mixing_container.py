from datetime import datetime

class MixingContainer():
    """Clase donde se guardará la información de las mezcla del contenedor y sus cantidades de cada componente/sustancia  """
    id = 0 # para el registro en la base de datos ... 
    id_container = 0
    # id_batch = 0 en el batch ya hay un id container así que no creo necesario el id del batch aquí ..
    component_list = [] # id/nombre de componetes
    weight_by_component = [] # los registrados por la báscula no por la formula
    tot_weight = 0 # kg; el peso total de la mezcla 
    viscosity = 0 # miliseconds; la última registrada
    start_timestamp = None
    end_timestamp = None


    def __init__(self, id, id_container):
        self.start_timestamp = datetime.now()
        self.id = id 
        self.id_container = id_container

    def end_process(self):
        self.end_timestamp = datetime.now() 
    
    def update_viscosity(self, viscosity):
        self.viscosity = viscosity
    
    def add_component(self, id_component, weight):
        self.component_list.append(id_component)
        self.weight_by_component.append(weight)
        self.tot_weight += self.tot_weight

    # hacer función para regresar solo la fecha actual ..... 

    def __str__(self) -> str:
        print("""
        Información de la Mezcla del Contenedor: 
            id: {}
            id Contenedor: {}
            Peso total (gramos): {} 
            Viscosidad: {}
            Intervalo de tiempo: {} --- {}
            Lista de componentes: {}
            Lista de pesos por componentes: {}
        """.format( self.id, self.id_container, self.tot_weight, self.viscosity, self.start_timestamp, self.end_timestamp, self.component_list, self.weight_by_component ) )