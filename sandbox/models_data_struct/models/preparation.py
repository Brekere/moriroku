class Preparation():
    id = -1
    id_formula = -1 # id_color
    quantity_gr = 0 # cantidad de la preparación en base al color base 
    interval_by_component = [] # se guarda la información de los intervalos dados por el % de componente y el % de tolerancia, se calcula fuera
    
    def __init__(self, id, id_formula, quantity_gr, interval_by_component) -> None:
        self.id = id
        self.id_formula = id_formula
        self.quantity_gr = quantity_gr
        self.interval_by_component = interval_by_component

    def __str__(self) -> str:
        print( """
        Información de la preparación:
            id: {}
            id_formula: {}
            Cantidad (gramos): {}
            lista intervalos: {}
        """.format( self.id, self.id_formula, self.quantity_gr, self.interval_by_component ) )