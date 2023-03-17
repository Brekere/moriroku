#MODELO OBSOLETO (SE BORRA DE LA BASE DE DATOS)

from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

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

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_mix_container, new_viscosity, extra_weight, t_start, t_end):
        self.id = id
        self.id_mix_container = id_mix_container
        self.new_viscosity = new_viscosity
        self.extra_weight = extra_weight
        self.t_start = t_start
        self.t_end = t_end
        self.list_errors = []

    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
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
            try:
                self.id_mix_container = int(data["id_mix_container"])
                self.new_viscosity = float(data["new_viscosity"])
                self.extra_weight = float(data["extra_weight"])
            except Exception as e:
                self.list_errors.append("Error de conversión int o float!")
            self.t_start = self.conversion_date_handler(data["t_start"])
            self.t_end = self.conversion_date_handler(data["t_end"])
            return True
        self.list_errors.append("Faltaron campos!")
        return False  

    def conversion_date_handler(self, time_to_comvert):
        rest = js_date_to_py_datetime(time_to_comvert) 
        date_time_ = ""
        if "error" not in rest:
            date_time_ = rest["success"]
        else:
            self.list_errors.append(rest["exception"])
        return date_time_

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()