class JobPosition():
    """ """
    id = -1
    name = ""
    description = ""

    def __init__(self, id, name, description) -> None:
        self.id = id
        self.name = name
        self.description = description

    def __str__(self) -> str:
        print( """ 
        Información del Puesto: 
            id: {}
            Nombre: {}
            Descripción: {}
        """.format( self.id, self.name, self.description ) )