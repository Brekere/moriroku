from asb_mori_paint import db

class ColorModel(db.Model):
    """
    ......
    id serial NOT NULL,  -- internal id
    id_ integer NOT NULL, -- given by Moriroku "pintado"
    id_color integer NOT NULL,
    id_model integer NOT NULL,
    description varchar(128), -- same as PaintedWeight.description
    base_weight float NOT NULL, -- in grams
    PRIMARY KEY (id),
    FOREIGN KEY (id_color) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_model) REFERENCES Models(id)
    """
    #__tablename__ = 'ColorsModels'
    __tablename__ = 'colorsmodels'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_ = db.Column(db.Integer)#integer NOT NULL, -- given by Moriroku "pintado"
    id_color = db.Column(db.Integer)#integer NOT NULL,
    id_model = db.Column(db.Integer)#integer NOT NULL,
    description = db.Column(db.String(128))#varchar(128), -- same as PaintedWeight.description
    base_weight = db.Column(db.Float)#float NOT NULL, -- in grams

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_, id_color, id_model, description, base_weight) -> None:
        self.id_ = id_
        self.id_color = id_color
        self.id_model = id_model
        self.description = description
        self.base_weight = base_weight
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
            "id_": self.id_, 
            "id_color": self.id_color, 
            "id_model": self.id_model, 
            "description": self.description, 
            "base_weight": self.base_weight
        }
        return data 

    def valid_full_data(self, data):
        if "id_" in data and "id_color" in data and "id_model" in data and "description" in data and "base_weight" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        self.description = data["description"]
        try:
            self.id_ = int(data["id_"]) 
            self.id_color = int(data["id_color"])
            self.id_model = int(data["id_model"])
            self.base_weight = float(data["base_weight"])
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