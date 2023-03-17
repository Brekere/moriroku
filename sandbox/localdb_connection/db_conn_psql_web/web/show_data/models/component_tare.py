from web import db
from web.utils.conversions import js_date_to_py_datetime

class ComponentTare(db.Model):
    """ 
    Info de la clase: 
    id serial NOT NULL,
    id_mix_container bigint unsigned NOT NULL, # from MixingContainer
    id_type_compoennt int NOT NULL, -- from json 
    id_component int NOT NULL, # from json Component file .. 
    weight float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
    """

    #__tablename__ = 'ComponentTare'
    __tablename__ = 'componenttare'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_type_compoennt = db.Column(db.Integer) # int NOT NULL, -- from json 
    id_mix_container = db.Column(db.Integer) # bigint unsigned NOT NULL, # from MixingContainer
    id_component = db.Column(db.Integer)# int NOT NULL, # from json Component file .. 
    weight = db.Column(db.Float)# float,
    t_start = db.Column(db.DateTime) # timestamp NOT NULL,
    t_end = db.Column(db.DateTime) #timestamp

    # Métodos
    def __init__(self, id, id_mix_container, id_type_compoennt, id_component, weight, t_start, t_end):
        self.id = id
        self.id_mix_container = id_mix_container
        self.id_type_compoennt = id_type_compoennt
        self.id_component = id_component
        self.weight = weight
        self.t_start = t_start
        self.t_end = t_end
    
    def __init__(self, data) -> None:
        super().__init__()
        if not self.from_json_to_record(data):
            print("Error!!")
    
    def get_json_format(self):
        data = {
            "id": self.id,
            "id_mix_container" : self.id_mix_container,
            "id_type_compoennt": self.id_type_compoennt,
            "id_component": self.id_component,
            "weight" : self.weight,
            "t_start" : self.t_start,
            "t_end" : self.t_end
        }
        return data 

    def from_json_to_record(self, data):
        if "id_mix_container" in data and "id_component" in data and "weight" in data and "t_start" in data and "t_end" in data and "id_type_compoennt" in data:
            self.id_mix_container = int(data["id_mix_container"])
            self.id_type_compoennt = int(data["id_type_compoennt"])
            self.id_component = int(data["id_component"])
            self.weight = float(data["weight"])
            self.t_start = js_date_to_py_datetime(data["t_start"])
            self.t_end = js_date_to_py_datetime(data["t_end"])
            return True 
        return False 

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()