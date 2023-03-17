from datetime import datetime

class WorkOrder():
    id = -1 
    timestamp =  "2022-06-20 09:26:03.478039"
    id_area = 0
    quantity = 0 
    id_formula = -1 # id_color
    id_model = -1

    def __init__(self, id, timestamp, id_area, quantity, id_formula, id_model) -> None:
        self.id = id 
        self.timestamp = timestamp
        self.id_area = id_area
        self.quantity = quantity
        self.id_formula = id_formula
        self.id_model = id_model

    def __str__(self) -> str:
        print( """
        Información de la WO:
            id: {}
            id_formula: {}
            id_model: {}
            id_area: {}
            timestamp: {}
            Cantidad: {}
        """.format( self.id, self.id_formula, self.id_model. self.id_area, self.timestamp, self.quantity ) )