
from unicodedata import name


class Filter():
    """ 
    "id": 0,
            "name": "Filtro de 25 micras",
            "size": 25  
    """
    id = -1
    name = ""
    size = 0

    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size

    def __str__(self) -> str:
        print("""
        Información del filtro:
            id: {}
            name: {}
            size (micras): {}
        """.format(self.id, self.name, self.size))