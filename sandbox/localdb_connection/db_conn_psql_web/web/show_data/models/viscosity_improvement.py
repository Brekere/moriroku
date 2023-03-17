from web import db
from web.utils.conversions import js_date_to_py_datetime

class ViscosityImprovement(db.Model):
    """ 
    Info de la clase: 
    id serial NOT NULL, 
    id_mix_container bigint unsigned NOT NULL, # from MixingContainer
    new_viscosity float,
    extra_weight float, # new added weight 
    t_start timestamp NOT NULL,
    t_end timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
    """
    
    __tablename__ = 'viscosityimprovement'
    #__tablename__ = 'ViscosityImprovement'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) # serial NOT NULL, 
    id_mix_container = db.Column(db.Integer) #bigint unsigned NOT NULL, # from MixingContainer
    new_viscosity = db.Column(db.Float) #float,
    extra_weight = db.Column(db.Float) #float, # new added weight 
    t_start = db.Column(db.DateTime) #timestamp NOT NULL,
    t_end = db.Column(db.DateTime) #timestamp

    # Métodos
    def __init__(self, id, id_mix_container, new_viscosity, extra_weight, t_start, t_end):
        self.id = id
        self.id_mix_container = id_mix_container
        self.new_viscosity = new_viscosity
        self.extra_weight = extra_weight
        self.t_start = t_start
        self.t_end = t_end

    def __init__(self, data) -> None:
        super().__init__()
        if not self.from_json_to_record(data):
            print("Error!!")

    def get_json_format(self):
        data = {
            "id": self.id,
            "id_mix_container": self.id_mix_container ,
            "new_viscosity": self.new_viscosity,
            "extra_weight": self.extra_weight,
            "t_start": self.t_start,
            "t_end": self.t_end
        }
        return data 
    
    def from_json_to_record(self, data):
        if "id_mix_container" in data and "new_viscosity" in data and "extra_weight" in data and "t_start" in data and "t_end" in data:
            self.id_mix_container = int(data["id_mix_container"])
            self.new_viscosity = float(data["new_viscosity"])
            self.extra_weight = float(data["extra_weight"])
            self.t_start = js_date_to_py_datetime(data["t_start"])
            self.t_end = js_date_to_py_datetime(data["t_end"])
            return True
        return False  

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()