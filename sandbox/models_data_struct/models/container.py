
class Container():
    id = -1
    id_code = "" # para el código QR, no se si lo vaya a utilizar .. 
    max_capacity_gr = 19000 # gramos
    capacity_gr = 12000 # gramos
    category = "normal"

    def __init__(self, id, id_code, max_capacity_gr, capacity_gr, category):
        self.id = id
        self.id_code = id_code 
        self.max_capacity_gr = max_capacity_gr
        self.capacity_gr = capacity_gr
        self.category = category

    def __str__(self) -> str:
        print("""
        Información del Contenedor: 
            id: {}
            Categría: {}
            Capacidad (gramos): {} 
            id_code: {}
            Capacidad máxima (gramos): {}
        """.format( self.id, self.category, self.capacity_gr, self.id_code, self.max_capacity_gr ))