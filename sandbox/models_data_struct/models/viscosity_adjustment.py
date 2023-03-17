from datetime import datetime

class ViscosityAdjustment():
    """ Clase para registrar las difierentes viscosidad es"""
    id = 0
    id_container = 0
    id_batch = 0
    viscosity = 0 # miliseconds, viscosidad medida
    viscosity_discrepancy = 0 #miliseconds, discrepancia entre la viscosidad medida y la esperada
    id_improvement_option = 0 # de acuerdo al id de la tabla de opciones que define el inge cual fue la que se selecciono para la mejora
    expected_viscosity = 0
    #date = None 
    start_timestamp = None 
    end_timestamp = None 
    #timestamp = None 
    # registro de cantidades vertidas de cada componente:
    component_list = [] # id/name
    quantity_by_component = [] # kg/gr por componente vertidos; los registrados por la báscula no por la formula
    tot_weight = 0 # kg; la cantidad extra nueva de peso  ... 

    def __init__(self, id, id_container, id_batch, id_improvement_option, expected_viscosity, viscosity):
        self.start_timestamp = datetime.now()
        self.id = id
        self.id_container = id_container
        self.id_batch = id_batch 
        self.id_improvement_option = id_improvement_option
        self.expected_viscosity = expected_viscosity
        self.viscosity = viscosity
        self.calc_diff_viscosity()


    # hacer función para regresar solo la fecha actual ..... 

    def add_componet(self, id_component, weight):
        self.tot_weight += weight
        self.component_list.append(id_component)
        self.quantity_by_component.append(weight)

    def calc_diff_viscosity(self):
        self.viscosity_discrepancy = abs(self.viscosity - self.expected_viscosity)

    def end_process(self):
        self.end_timestamp = datetime.now()

    def __str__(self) -> str:
        print("""
        Información de mejora de la mezcla:
            id: {}
            # Lote: {}
            id Contenedor: {}
            Viscosidad medida (seg): {} 
            Viscosidad esperada (seg): {}
            Discrepancia de viscosidad: {}
            Opcion de mejora: {}
            Peso extra: {}
            Lista de componentes: {}
            Peso por componente: {}
        """.format( self.id, self.id_batch, self.id_container, self.viscosity, self.expected_viscosity, self.viscosity_discrepancy, self.id_improvement_option, self.tot_weight, self.component_list, self.quantity_by_component ) )