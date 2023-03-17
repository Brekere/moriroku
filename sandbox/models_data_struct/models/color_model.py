class ColorModel():
    """  
    {"id": 0, "id_": 102400001, "id_model": 0, "id_color": 0, "color_code": "Code:041"}
    """
    id = -1
    id_ = -1
    id_model = -1
    id_color = -1
    color_code = ""
    def __init__(self, id, id_, id_model, id_color, color_code) -> None:
        self.id = id
        self.id_ = id_
        self.id_color = id_color
        self.id_model = id_model

    def __str__(self) -> str:
        print( """
        Información de la relación color-modelo:
            id: {}
            id_: {}
            id_color: {}
            id_model: {}
            color_code: {}
        """.format( self.id, self.id_, self.id_color, self.id_model, self.color_code ) )