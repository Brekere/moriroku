from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

class ContainerInfo(db.Model):
    """
    ......
    id serial NOT NULL,
    id_barcode varchar(8) NOT NULL,
    date_creation timestamp NOT NULL,
    weight_kg float NOT NULL,
    container_type int NOT NULL, -- 0 metal, 1 thin plastic, 2 thick plastic
    PRIMARY KEY (id)
    """
    #__tablename__ = 'ContainersInfo'
    __tablename__ = 'containersinfo'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_barcode = db.Column(db.String(8))#varchar(8) NOT NULL,
    date_creation = db.Column(db.DateTime)#timestamp NOT NULL,
    weight_kg = db.Column(db.Float)#float NOT NULL,
    container_type = db.Column(db.Integer)#int NOT NULL, -- 0 metal, 1 thin plastic, 2 thick plastic

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_barcode, date_creation, weight_kg, container_type) -> None:
        self.id_barcode = id_barcode
        self.date_creation = date_creation
        self.weight_kg = weight_kg
        self.container_type = container_type
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
            "id_barcode": self.id_barcode, 
            "date_creation": self.date_creation, 
            "weight_kg": self.weight_kg, 
            "container_type": self.container_type
        }
        return data 

    def valid_full_data(self, data):
        if "id_barcode" in data and "date_creation" in data and "weight_kg" in data and "container_type" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False

    def conversion_date_handler(self, time_to_comvert):
        rest = js_date_to_py_datetime(time_to_comvert) 
        date_time_ = ""
        if "error" not in rest:
            date_time_ = rest["success"]
        else:
            self.list_errors.append(rest["exception"])
        return date_time_
    
    def dict_to_record_full(self, data):
        self.id_barcode = data["id_barcode"]
        try:
            self.weight_kg = float(data["weight_kg"])
            self.container_type = int(data["container_type"]) 
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")
        self.date_creation = self.conversion_date_handler(data["date_creation"])

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