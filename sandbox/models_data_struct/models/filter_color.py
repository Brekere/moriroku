class FilterColor():
    id_color = -1
    id_filter = -1
    def __init__(self, id_color, id_filter) -> None:
        self.id_color = id_color
        self.id_filter = id_filter

    def __str__(self) -> str:
        print( """
        Información de la relación filtro-color:
            id_color: {}
            id_filtro: {}
        """.format( self.id_color, self.id_filter ) )