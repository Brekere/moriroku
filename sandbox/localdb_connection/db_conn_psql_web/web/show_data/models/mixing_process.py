from web import db
#from datetime import datetime
from web.utils.conversions import js_date_to_py_datetime

class MixingProcess(db.Model):
    """ 
    Info de la clase: 
    id serial NOT NULL,
    id_worker int NOT NULL,
    name_worker varchar(64),
    id_formula int NOT NULL,
    id_filter int NOT NULL,
    num_containers int NOT NULL,
    conatiner_base_weight float NOT NULL
    t_start timestamp,
    t_end timestamp,
    expected_viscosity_min float NOT NULL,
    expected_viscosity_max float NOT NULL,
    PRIMARY KEY (id)
    """
    
    #__tablename__ = 'MixingProcess'
    __tablename__ = 'mixingprocess'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_worker = db.Column(db.Integer) #int NOT NULL,
    name_worker = db.Column(db.String(64)) #varchar(64),
    id_formula = db.Column(db.Integer) #int NOT NULL,
    id_filter = db.Column(db.Integer) #int NOT NULL,
    num_containers = db.Column(db.Integer) #int NOT NULL,
    conatiner_base_weight = db.Column(db.Integer) # float NOT NULL
    t_start = db.Column(db.DateTime) #timestamp,
    t_end = db.Column(db.DateTime) #timestamp
    expected_viscosity_min = db.Column(db.Float) #float NOT NULL,
    expected_viscosity_max = db.Column(db.Float) #float NOT NUL

    # Métodos
    def __init__(self, id, id_worker, name_worker, id_formula, id_filter, num_containers, conatiner_base_weight, t_start, t_end, expected_viscosity_min, expected_viscosity_max):
        self.id = id
        self.id_worker = id_worker
        self.name_worker = name_worker
        self.id_formula = id_formula
        self.id_filter = id_filter
        self.num_containers = num_containers
        self.conatiner_base_weight = conatiner_base_weight
        self.t_start = t_start
        self.t_end = t_end
        self.expected_viscosity_min = expected_viscosity_min
        self.expected_viscosity_max = expected_viscosity_max
    
    def __init__(self, data) -> None:
        super().__init__()
        if not self.from_json_to_record(data):
            print("Error!!")
    
    def get_json_format(self):
        data = {
            "id": self.id,
            "id_worker": self.id_worker,
            "name_worker": self.name_worker,
            "id_formula": self.id_formula,
            "id_filter": self.id_filter,
            "num_containers": self.num_containers,
            "conatiner_base_weight": self.conatiner_base_weight,
            "t_start": self.t_start,
            "t_end": self.t_end,
            "expected_viscosity_min" : self.expected_viscosity_min,
            "expected_viscosity_max" : self.expected_viscosity_max
        }
        return data
    
    def from_json_to_record(self, data) -> bool:
        if "id_worker"in data and "name_worker" in data and "id_formula" in data and "id_filter" in data and "num_containers" in data and "t_start" in data and "t_end"  in data and "expected_viscosity_min" in data and "expected_viscosity_max" in data and "conatiner_base_weight" in data:
            self.id_worker = int(data["id_worker"])
            self.name_worker = data["name_worker"]
            self.id_formula = int(data["id_formula"])
            self.id_filter = int(data["id_filter"])
            self.num_containers = int(data["num_containers"])
            self.conatiner_base_weight = float(data["conatiner_base_weight"])
            self.t_start = js_date_to_py_datetime(data["t_start"])#self.t_start = datetime.strptime(data["t_start"], "%Y-%m-%dT%H:%M:%S.%f%z")
            self.t_end = js_date_to_py_datetime(data["t_end"])#self.t_end = datetime.strptime(data["t_end"], "%Y-%m-%dT%H:%M:%S.%f%z")
            self.expected_viscosity_min = float(data["expected_viscosity_min"])
            self.expected_viscosity_max = float(data["expected_viscosity_max"])
            return True
        return False

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
            # Proceso: {}
            Nombre del operador: {}
            id Formula: {}
            # Contenedores: {}
            fecha inicio: {}
            fecha fin: {}
        """.format(self.id , self.name_worker, self.id_formula, self.num_containers, self.t_start, self.t_end)