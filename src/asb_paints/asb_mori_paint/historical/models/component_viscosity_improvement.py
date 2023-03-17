from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

class ComponentViscosityImprovement(db.Model):
    """ 
    Info de la clase:
    id serial NOT NULL,
    id_viscosity_improvement bigint unsigned NOT NULL, # from ViscosityImprovement
    id_component int NOT NULL, # from json Component file .. 
    extra_weight float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    batch varchar(8),-- save the lote number of the component ...
    PRIMARY KEY (id),
    FOREIGN KEY (id_viscosity_improvement) REFERENCES ViscosityImprovement(id) 
    """
    __tablename__ = 'componentviscosityimprovement'
    # __tablename__ = 'ComponentViscosityImprovement'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    #id_viscosity_improvement = db.Column(db.Integer) #bigint unsigned NOT NULL, # from ViscosityImprovement
    id_mix_container = db.Column(db.Integer) #bigint unsigned NOT NULL, # from MixingContainer
    new_viscosity = db.Column(db.Float) #float,
    id_component = db.Column(db.Integer) #int NOT NULL, # from json Component file .. 
    extra_weight = db.Column(db.Float) #float,
    t_start = db.Column(db.DateTime)  #timestamp NOT NULL,
    t_end = db.Column(db.DateTime) #timestamp
    batch = db.Column(db.String(8)) #varchar(8),-- save the lote number of the component ...

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_mix_container, new_viscosity, id_component, extra_weight, t_start, t_end, batch):
        self.id = id 
        #self.id_viscosity_improvement = id_viscosity_improvement
        self.id_mix_container = id_mix_container
        self.new_viscosity = new_viscosity
        self.id_component = id_component
        self.extra_weight = extra_weight
        self.t_start = t_start 
        self.t_end = t_end
        self.batch = batch
        self.list_errors = []

    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            print("Error!!")

    def get_json_format(self):
        data = {
            "id" : self.id,
            "id_mix_container" : self.id_mix_container,
            "new_viscosity" : self.new_viscosity,
            "id_component" : self.id_component,
            "extra_weight" : self.extra_weight,
            "t_start" : self.t_start,
            "t_end" : self.t_end,
            "batch": self.batch
        }
        return data 

    #"id_viscosity_improvement" in data and 

    def from_json_to_record(self, data):
        if "id_component" in data and "extra_weight" in data and "t_start" in data and "t_end" in data and "batch" in data and "id_mix_container" in data and "new_viscosity" in data:
            self.batch = data["batch"]
            try:
                #self.id_viscosity_improvement = int(data["id_viscosity_improvement"])
                self.id_component = int(data["id_component"])
                self.id_mix_container = int(data["id_mix_container"])
                self.extra_weight = float(data["extra_weight"])
                self.new_viscosity = float(data["new_viscosity"])
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