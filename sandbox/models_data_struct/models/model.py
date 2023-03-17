

class Model():
    """
        {"id": 0, "part_number": "415.D", "description": "KOMBI FS"}
    """ 

    id = -1
    part_number = ""
    description = ""

    def __init__(self, id, part_number, description) -> None:
        self.id = id
        self.part_number = part_number
        self.description = description

    def __str__(self) -> str:
        print("""
        Información del Modelo:
            id: {}
            Número de parte: {}
            Descripción: {}
        """.format( self.id, self.part_number, self.description ))