## aquí se tiene información de la jarra, no creo vaya como clase, pero si debemos de saber el máximo que puede tener la jarra

# Se guarda en un archivo .json (jug_info.json)


class Jug():
    capacity_gr = -1
    category = ""

    def __init__(self, capacity_gr, category) -> None:
        self.capacity_gr = capacity_gr
        self.category = category

    def __str__(self) -> str:
        print("""
        Información de la Jarra:
            Capacidad (gr): {}
            Categoría: {}
        """.format( self.capacity_gr, self.category ))