

class Formula():
    id = -1
    name = ""
    id_components = []
    percentages = []
    tolerances = []
    component_types = []
    # list_componets = [] # podríamos definir una lista de componentes para más fácil ?? 
    def __init__(self, id, name, id_components, percentages, tolerances, component_types):
        self.id = id
        self.id_components = id_components
        self.percentages = percentages
        self.tolerances = tolerances
        self.component_types = component_types

    def __str__(self) -> str:
        print("""
        Información de la formula: 
            id: {}
            Nombre: {}
            Numero de componentes: {}
            id_componentes: {}
            porcentajes (%): {}
            tolerancias (%): {}
            tipo de componentes: {}
        """.format( self.id, self.name, len(self.id_components), self.id_components, self.percentages, self.tolerances, self.component_types ) )