from asb_mori_paint import db


class Filter(db.Model):
    """
    ......
    id serial NOT NULL,
    size_micron float NOT NULL,
    name varchar(32) NOT NULL,
    PRIMARY KEY (id)
    """
    #__tablename__ = 'Filters'
    __tablename__ = 'filters'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    size_micron = db.Column(db.Float)#float NOT NULL,
    name = db.Column(db.String(32))#varchar(32) NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, size_micron, name) -> None:
        self.size_micron = size_micron
        self.name = name
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
            "size_micron": self.size_micron, 
            "name": self.name
        }
        return data 

    def valid_full_data(self, data):
        if "size_micron" in data and "name" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        self.name = data["name"]
        try:
            self.size_micron = float(data["size_micron"]) 
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