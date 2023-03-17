from asb_mori_paint import db

class FormulaComponent(db.Model):
    """
    ......
    id_color_formula integer NOT NULL,
    id_component integer NOT NULL,
    percentage float NOT NULL,
    tolerance float NOT NULL,
    PRIMARY KEY (id_color_formula, id_component),
    FOREIGN KEY (id_color_formula) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_component) REFERENCES Components(id)
    """
    #__tablename__ = 'FormulasComponents'
    __tablename__ = 'formulascomponents'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    #id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_color_formula = db.Column(db.Integer, primary_key = True) #integer NOT NULL,
    id_component = db.Column(db.Integer, primary_key = True) #integer NOT NULL,
    percentage = db.Column(db.Float)#float NOT NULL,
    tolerance = db.Column(db.Float)#float NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_color_formula, id_component, percentage, tolerance) -> None:
        self.id_color_formula = id_color_formula
        self.id_component = id_component
        self.percentage = percentage
        self.tolerance = tolerance
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            #print(self.list_errors)
            print("Error!!")


    def get_json_format(self):
        data = {
            "id_color_formula": self.id_color_formula, 
            "id_component": self.id_component, 
            "percentage": self.percentage, 
            "tolerance": self.tolerance
        }
        return data 

    def valid_full_data(self, data):
        if "id_color_formula" in data and "id_component" in data and "percentage" in data and "tolerance" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        try:
            self.id_color_formula = int(data["id_color_formula"]) 
            self.id_component = int(data["id_component"])
            self.percentage = float(data["percentage"])
            self.tolerance = float(data["tolerance"])
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