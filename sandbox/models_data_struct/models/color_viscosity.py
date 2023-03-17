
class ColorViscosity():
    id_color = -1,
    min_viscosity_seg = -1 
    max_viscosity_seg = -1

    def __init__(self, id_color, min_viscosity_seg, max_viscosity_seg) -> None:
        self.id = id
        self.min_viscosity_seg = min_viscosity_seg
        self.max_viscosity_seg = max_viscosity_seg

    def __str__(self) -> str:
        print( """
        Información de la relación color-viscosidad:
            id: {}
            Intervalo de viscosidad (segundos): [{}, {}]
        """.format( self.id, self.min_viscosity_seg, self.max_viscosity_seg ) )