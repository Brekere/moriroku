from asb_mori_paint import db

class ComponentQRInfo(db.Model):
    """
    ......
    id serial NOT NULL,
    id_supplier integer NOT NULL,
    identifier varchar(20) NOT NULL,
    batch int NOT NULL,
    weight float NOT NULL,
    weight_type int NOT NULL, -- 0 kg, 1 g, 2 lb
    expiration_year int NOT NULL,
    expiration_month int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_supplier) REFERENCES Suppliers(id)
    """
    #__tablename__ = 'ComponentsQRInfo'
    __tablename__ = 'componentsqrinfo'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_supplier = db.Column(db.Integer)#integer NOT NULL,
    identifier = db.Column(db.String(20))#varchar(20) NOT NULL,
    batch = db.Column(db.Integer)#int NOT NULL,
    weight = db.Column(db.Float)#float NOT NULL,
    weight_type = db.Column(db.Integer)#int NOT NULL, -- 0 kg, 1 g, 2 lb
    expiration_year = db.Column(db.Integer)#int NOT NULL,
    expiration_month = db.Column(db.Integer)#int NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) -> None:
        self.id_supplier = id_supplier
        self.identifier = identifier
        self.batch = batch
        self.weight = weight
        self.weight_type = weight_type
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
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
            "id_supplier": self.id_supplier, 
            "identifier": self.identifier, 
            "batch": self.batch, 
            "weight": self.weight, 
            "weight_type": self.weight_type, 
            "expiration_year": self.expiration_year, 
            "expiration_month": self.expiration_month
        }
        return data 

    def valid_full_data(self, data):
        if "id_supplier" in data and "identifier" in data and "batch" in data and "weight" in data and "weight_type" in data and "expiration_year" in data and "expiration_month" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        self.identifier = data["identifier"]
        try:
            self.id_supplier = int(data["id_supplier"])
            self.batch = int(data["batch"])
            self.weight_type = int(data["weight_type"])
            self.expiration_year = int(data["expiration_year"])
            self.expiration_month = int(data["expiration_month"])
            self.weight = float(data["weight"])
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