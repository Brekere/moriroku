from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime, js_date_to_py_date

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
    batch varchar(8), -- save the lote number of the component ... 
    batch_expiration DATE NOT NULL,
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
    batch = db.Column(db.String(8)) #varchar(8),
    batch_expiration = db.Column(db.Date)#DATE NOT NULL, 

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_mix_container, id_type_compoennt, id_component, weight, t_start, t_end, batch, batch_expiration):
        self.id = id
        self.id_mix_container = id_mix_container
        self.id_type_compoennt = id_type_compoennt
        self.id_component = id_component
        self.weight = weight
        self.t_start = t_start
        self.t_end = t_end
        self.batch = batch
        self.batch_expiration = batch_expiration
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
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
            "t_end" : self.t_end,
            "batch": self.batch,
            "batch_expiration": self.batch_expiration
        }
        return data 

    def from_json_to_record(self, data):
        if "id_mix_container" in data and "id_component" in data and "weight" in data and "t_start" in data and "t_end" in data and "id_type_compoennt" in data and "batch" in data and "batch_expiration" in data:
            self.batch = data["batch"]
            try:
                self.id_mix_container = int(data["id_mix_container"])
                self.id_type_compoennt = int(data["id_type_compoennt"])
                self.id_component = int(data["id_component"])
                self.weight = float(data["weight"])
            except Exception as e:
                self.list_errors.append("Error de conversión int o float!")
            self.t_start = self.conversion_date_handler(data["t_start"])
            self.t_end = self.conversion_date_handler(data["t_end"])
            self.batch_expiration = self.conversion_date_handler_date(data["batch_expiration"])
            return True 
        self.list_errors.append("Faltaron campos!")
        return False 

    def conversion_date_handler_date(self, time_to_comvert):
        rest = js_date_to_py_date(time_to_comvert) 
        date_time_ = ""
        if "error" not in rest:
            date_time_ = rest["success"]
        else:
            self.list_errors.append(rest["exception"])
        return date_time_
    
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