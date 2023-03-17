from asb_mori_paint import db


class ColorFormula(db.Model):
    """
    ......
    id serial NOT NULL,
    color_code varchar(4) NOT NULL,
    name varchar(32) NOT NULL,
    min_viscosity float NOT NULL,
    max_viscosity float NOT NULL,
    PRIMARY KEY (id)
    """
    #__tablename__ = 'ColorsFormulas'
    __tablename__ = 'colorsformulas'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    color_code = db.Column(db.String(4)) #varchar(4) NOT NULL,
    name = db.Column(db.String(32))#varchar(32) NOT NULL,
    min_viscosity = db.Column(db.Float)#float NOT NULL,
    max_viscosity = db.Column(db.Float)#float NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, color_code, name, min_viscosity, max_viscosity) -> None:
        self.color_code = color_code
        self.name = name
        self.min_viscosity = min_viscosity
        self.max_viscosity = max_viscosity
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            #print(self.list_errors)
            print("Error!!")


    def get_json_format(self):
        data = {
            "id": self.id,
            "color_code": self.color_code, 
            "name": self.name, 
            "min_viscosity": self.min_viscosity, 
            "max_viscosity": self.max_viscosity
        }
        return data 

    def valid_full_data(self, data):
        if "color_code" in data and "name" in data and "min_viscosity" in data and "max_viscosity" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        self.color_code = data["color_code"]
        self.name = data["name"]
        try:
            self.min_viscosity = float(data["min_viscosity"]) 
            self.max_viscosity = float(data["max_viscosity"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")

    def from_json_to_record(self, data):
        if self.valid_full_data(data):
            #print("---- Aquí!")
            self.dict_to_record_full(data) 
            if len(self.list_errors) == 0:
                return True
        return False 
    
    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()