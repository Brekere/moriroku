from web import db
from web.utils.conversions import js_date_to_py_datetime

class MixContainer(db.Model):
    """ 
    Info de la clase: 
    id serial NOT NULL, 
    id_barcode int NOT NULL, # keeps the barcode id of the container
    id_process bigint unsigned NOT NULL, # from MixingProcess
    viscosity float,
    weight float,
    humidity float,
    temperature float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    t_start_tare timestamp, -- for all the tares ..
    t_end_tare timestamp,
    t_start_container timestamp,
    t_end_container timestamp,
    t_start_viscosity timestamp,
    t_end_viscosity timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id)
    """
    #__tablename__ = 'MixContainer'
    __tablename__ = 'mixcontainer'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL, 
    id_barcode = db.Column(db.Integer) # int NOT NULL, # keeps the barcode id of the container
    id_process = db.Column(db.Integer) # bigint unsigned NOT NULL, # from MixingProcess
    viscosity = db.Column(db.Float) #float,
    weight = db.Column(db.Float) # float,
    humidity = db.Column(db.Float)#float, # porcentaje de humedad ...  1 - 100
    temperature = db.Column(db.Float)#float,
    t_start = db.Column(db.DateTime) #timestamp NOT NULL,
    t_end = db.Column(db.DateTime) #timestamp,
    t_start_tare = db.Column(db.DateTime) #timestamp, -- for all the tares ..
    t_end_tare = db.Column(db.DateTime) #timestamp,
    t_start_container = db.Column(db.DateTime) #timestamp,
    t_end_container = db.Column(db.DateTime) #timestamp,
    t_start_viscosity = db.Column(db.DateTime) #timestamp,
    t_end_viscosity = db.Column(db.DateTime) #timestamp

    # Métodos
    def __init__(self, id, id_barcode, id_process, viscosity, weight, humidity, temperature, t_start, t_end, t_start_tare, t_end_tare, t_start_container, t_end_container, t_start_viscosity, t_end_viscosity):
        self.id = id
        self.id_barcode = id_barcode
        self.id_process = id_process
        self.viscosity = viscosity
        self.weight = weight
        self.humidity = humidity
        self.temperature = temperature
        self.t_start = t_start
        self.t_end = t_end
        self.t_start_tare = t_start_tare
        self.t_end_tare = t_end_tare
        self.t_start_container = t_start_container
        self.t_end_container = t_end_container
        self.t_start_viscosity = t_start_viscosity
        self.t_end_viscosity = t_end_viscosity

    def __init__(self, data) -> None:
        super().__init__()
        if not self.from_json_to_record(data):
            print("Error!!")
    
    def get_json_format(self):
        data = {
            "id": self.id,
            "id_barcode": self.id_barcode, 
            "id_process": self.id_process, 
            "viscosity": self.viscosity,
            "weight": self.weight,
            "humidity": self.humidity,
            "temperature": self.temperature,
            "t_start": self.t_start,
            "t_end": self.t_end,
            "t_start_tare": self.t_start_tare,
            "t_end_tare": self.t_end_tare,
            "t_start_container": self.t_start_container, 
            "t_end_container": self.t_end_container,
            "t_start_viscosity": self.t_start_viscosity, 
            "t_end_viscosity": self.t_end_viscosity
        }
        return data 

    def from_json_to_record(self, data):
        if "id_barcode" in data and "id_process" in data and "viscosity" in data and "t_start" in data and "t_end" in data and "t_start_container" in data and "t_end_container" in data and "t_start_viscosity" in data and "t_end_viscosity" in data and "weight" in data and "temperature" in data and "humidity" in data and "t_start_tare" in data and "t_end_tare" in data:
            self.id_barcode = int(data["id_barcode"])
            self.id_process = int(data["id_process"])
            self.viscosity = float(data["viscosity"])
            self.weight = float(data["weight"])
            self.humidity = float(data["humidity"])
            self.temperature = float(data["temperature"])
            self.t_start = js_date_to_py_datetime(data["t_start"])
            self.t_end = js_date_to_py_datetime(data["t_end"])
            self.t_start_tare = js_date_to_py_datetime(data["t_start_tare"])
            self.t_end_tare = js_date_to_py_datetime(data["t_end_tare"])
            self.t_start_container = js_date_to_py_datetime(data["t_start_container"])
            self.t_end_container = js_date_to_py_datetime(data["t_end_container"])
            self.t_start_viscosity = js_date_to_py_datetime(data["t_start_viscosity"])
            self.t_end_viscosity = js_date_to_py_datetime(data["t_end_viscosity"])
            return True 
        return False 

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()