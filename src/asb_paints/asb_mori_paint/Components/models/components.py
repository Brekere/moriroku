from asb_mori_paint import db


class Components(db.Model):
    """
    ......
    id serial NOT NULL,
    id_type integer NOT NULL,
    name varchar(20) NOT NULL,
    nick_name varchar(20) NOT NULL,
    identifier varchar(20) NOT NULL, -- used to check in QR's info
    description varchar(256),
    in_use bool NOT NULL,
    -- id_qr_info integer NOT NULL,
    PRIMARY KEY (id),
    -- FOREIGN KEY (id_qr_info) REFERENCES ComponentsQRInfo(id),
    FOREIGN KEY (id_type) REFERENCES ComponentType(id)
    """
    #__tablename__ = 'Components'
    __tablename__ = 'components'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_type = db.Column(db.Integer)#integer NOT NULL,
    name = db.Column(db.String(20))#varchar(20) NOT NULL,
    nick_name = db.Column(db.String(20))#varchar(20) NOT NULL,
    identifier = db.Column(db.String(20))#varchar(20) NOT NULL, -- used to check in QR's info
    description = db.Column(db.String(256))#varchar(256),
    in_use = db.Column(db.Boolean)#bool NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_type, name, nick_name, identifier, description, in_use) -> None:
        self.id_type = id_type
        self.name = name
        self.nick_name = nick_name
        self.identifier = identifier
        self.description = description
        self.in_use = in_use
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
            "id_type": self.id_type, 
            "name": self.name, 
            "nick_name": self.nick_name, 
            "identifier": self.identifier, 
            "description": self.description, 
            "in_use": self.in_use
        }
        return data 

    def valid_full_data(self, data):
        if "id_type" in data and "name" in data and "nick_name" in data and "identifier" in data and "description" in data and "in_use" in data:
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
        self.nick_name = data["nick_name"]
        self.identifier = data["identifier"]
        self.description = data["description"]
        try:
            self.id_type = data["id_type"]
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")
        if data["in_use"] in ["true", "True", "false", "False", True, False]:
            if data["in_use"] in ["true", "True", "false", "False"]:
                try:
                    self.in_use = eval(data["in_use"])
                except Exception as e:
                    self.list_errors.append("Error de conversión Booleano(eval)!")
            else:
                self.in_use = data["in_use"]
        else:
            self.list_errors.append("No es un valor de verdad valido!!")
        

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