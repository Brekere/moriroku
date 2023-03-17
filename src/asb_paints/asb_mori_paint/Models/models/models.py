from asb_mori_paint import db


class Models(db.Model):
    """
    ......
    id serial NOT NULL,
    id_client integer NOT NULL,
    part_number varchar(16) NOT NULL,
    description varchar(256),
    PRIMARY KEY (id)
    """
    #__tablename__ = 'Models'
    __tablename__ = 'models'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_client = db.Column(db.Integer)#integer NOT NULL,
    part_number = db.Column(db.String(17))#varchar(16) NOT NULL,
    description = db.Column(db.String(256))#varchar(256),

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_client, part_number, description) -> None:
        self.id_client = id_client
        self.part_number = part_number
        self.description = description
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
            "id_client": self.id_client, 
            "part_number": self.part_number, 
            "description": self.description
        }
        return data 

    def valid_full_data(self, data):
        if "id_client" in data and "part_number" in data and "description" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        self.part_number = data["part_number"]
        self.description = data["description"]
        try:
            self.id_client = int(data["id_client"])
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