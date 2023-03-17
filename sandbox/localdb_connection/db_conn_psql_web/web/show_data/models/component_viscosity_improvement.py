from web import db
from web.utils.conversions import js_date_to_py_datetime

class ComponentViscosityImprovement(db.Model):
    """ 
    Info de la clase:
    id serial NOT NULL,
    id_viscosity_improvement bigint unsigned NOT NULL, # from ViscosityImprovement
    id_component int NOT NULL, # from json Component file .. 
    extra_weight float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_viscosity_improvement) REFERENCES ViscosityImprovement(id) 
    """
    __tablename__ = 'componentviscosityimprovement'
    # __tablename__ = 'ComponentViscosityImprovement'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_viscosity_improvement = db.Column(db.Integer) #bigint unsigned NOT NULL, # from ViscosityImprovement
    id_component = db.Column(db.Integer) #int NOT NULL, # from json Component file .. 
    extra_weight = db.Column(db.Float) #float,
    t_start = db.Column(db.DateTime)  #timestamp NOT NULL,
    t_end = db.Column(db.DateTime) #timestamp

    # Métodos
    def __init__(self, id, id_viscosity_improvement, id_component, extra_weight, t_start, t_end):
        self.id = id 
        self.id_viscosity_improvement = id_viscosity_improvement
        self.id_component = id_component
        self.extra_weight = extra_weight
        self.t_start = t_start 
        self.t_end = t_end

    def __init__(self, data) -> None:
        super().__init__()
        if not self.from_json_to_record(data):
            print("Error!!")

    def get_json_format(self):
        data = {
            "id" : self.id,
            "id_viscosity_improvement" : self.id_viscosity_improvement,
            "id_component" : self.id_component,
            "extra_weight" : self.extra_weight,
            "t_start" : self.t_start,
            "t_end" : self.t_end,
        }
        return data 

    def from_json_to_record(self, data):
        if "id_viscosity_improvement" in data and "id_component" in data and "extra_weight" in data and "t_start" in data and "t_end" in data:
            self.id_viscosity_improvement = int(data["id_viscosity_improvement"])
            self.id_component = int(data["id_component"])
            self.extra_weight = float(data["extra_weight"])
            self.t_start = js_date_to_py_datetime(data["t_start"]) 
            self.t_end = js_date_to_py_datetime(data["t_end"])
            return True
        return False 

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()