
class Component():
    """ Clase donde se tiene la inromación de los componentes/sustancias"""
    id = -1
    type_ = -1 
    name = "" # este nombre debe de ser el mismo que en la clase de la formula ... 
    description = -1
    def __init__(self, id, name, description, type_):
        self.id = id
        self.type_ = type_ 
        self.name = name
        self.description = description

    def __str__(self) -> str:
        print("""
        Información de componentes:
            id: {}
            Tipo: {}
            Nombre: {}
            Descripción: {}
        """.format( self.id, self.type_, self.name, self.description ))