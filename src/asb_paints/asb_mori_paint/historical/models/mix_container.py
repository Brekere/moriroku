from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

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
    failed_process boolean, --- si el proceso falla, principalmente por temperatura
    failure_type  int, --- tipo de falla ... 0 -> temperatura, 1 -> otros (solo hay un caso definido por ahora)
    PRIMARY KEY (id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id)
    """
    #__tablename__ = 'MixContainer'
    __tablename__ = 'mixcontainer'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL, 
    id_barcode = db.Column(db.Integer) # int, # keeps the barcode id of the container
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
    failed_process = db.Column(db.Boolean)#boolean, --- si el proceso falla, principalmente por temperatura
    failure_type = db.Column(db.Integer)#int, --- tipo de falla ... 0 -> temperatura, 1 -> otros (solo hay un caso definido por ahora)

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_barcode, id_process, viscosity, weight, humidity, temperature, t_start, t_end, t_start_tare, t_end_tare, t_start_container, t_end_container, t_start_viscosity, t_end_viscosity, failed_process, failure_type):
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
        self.failed_process = failed_process
        self.failure_type = failure_type
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
            "t_end_viscosity": self.t_end_viscosity,
            "failed_process": self.failed_process,
            "failure_type": self.failure_type
        }
        return data 

    def valid_full_data(self, data):
        if "id_barcode" in data and "id_process" in data and "viscosity" in data and "t_start" in data and "t_end" in data and "t_start_container" in data and "t_end_container" in data and "t_start_viscosity" in data and "t_end_viscosity" in data and "weight" in data and "temperature" in data and "humidity" in data and "t_start_tare" in data and "t_end_tare" in data and "failed_process" in data and "failure_type" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    def valid_basic_data(self, data):
        #print(self.list_errors)
        #print(data)
        if "id_process" in data and "t_start" in data:
            #print("ENTRO!!! ")
            return True
        self.list_errors.append("Faltaron campos!")
        #print("Llego hasta aquí!!! ")
        return False

    def valid_measures(self, data):
        if "viscosity" in data and "weight" in data and "temperature" in data and "humidity" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False
    
    def valid_container_init(self, data):
        if "id_barcode" in data and "t_start_container" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    def valid_failure_info(self, data):
        if "failed_process" in data and "failure_type" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False 

    def dict_to_record_not_null_int_float_str(self, data):
        try:
            self.id_process = int(data["id_process"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")
        return False 
    
    def dict_to_record_measures(self, data):
        try:
            self.viscosity = float(data["viscosity"])
            self.weight = float(data["weight"])
            self.humidity = float(data["humidity"])
            self.temperature = float(data["temperature"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")
    
    def dict_to_record_container_init(self, data):
        try:
            self.id_barcode = float(data["id_barcode"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!") 
        self.t_start_container = self.conversion_date_handler(data["t_start_container"])

    def dict_to_record_valid_failure_info(self, data):
        try:
            self.failure_type = int(data["failure_type"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")
        try:
            self.failed_process = bool(data["failed_process"])
        except Exception as e:
            self.list_errors.append("Error de conversión Boolean!")
        return False

    def update_valid_failure_info(self, data):
        self.list_errors = []
        if self.valid_failure_info(data):
            self.dict_to_record_valid_failure_info(data) 
            if len(self.list_errors) == 0:
                return True
        return False

    def update_measures(self, data):
        self.list_errors = []
        if self.valid_measures(data):
            self.dict_to_record_measures(data) 
            if len(self.list_errors) == 0:
                return True
        return False 

    def update_container_init(self, data):
        self.list_errors = []
        if self.valid_container_init(data):
            self.dict_to_record_container_init(data) 
            if len(self.list_errors) == 0:
                return True
        return False 
    
    def update_t_end(self, t_end):
        self.list_errors = []
        self.t_end = self.conversion_date_handler(t_end) 
        if len(self.list_errors) > 0:
            return False
        return True

    def update_t_end_container(self, t_end_container):
        self.list_errors = []
        self.t_end_container = self.conversion_date_handler(t_end_container) 
        if len(self.list_errors) > 0:
            return False
        return True

    def update_t_start_viscosity(self, t_start_viscosity):
        self.list_errors = []
        self.t_start_viscosity = self.conversion_date_handler(t_start_viscosity) 
        if len(self.list_errors) > 0:
            return False
        return True

    def update_t_end_viscosity(self, t_end_viscosity):
        self.list_errors = []
        self.t_end_viscosity = self.conversion_date_handler(t_end_viscosity) 
        if len(self.list_errors) > 0:
            return False
        return True

    def update_t_start_tare(self, t_start_tare):
        self.list_errors = []
        self.t_start_tare = self.conversion_date_handler(t_start_tare) 
        if len(self.list_errors) > 0:
            return False
        return True

    def update_t_end_tare(self, t_end_tare):
        self.list_errors = []
        self.t_end_tare = self.conversion_date_handler(t_end_tare) 
        if len(self.list_errors) > 0:
            return False
        return True
    
    def dict_to_record_all(self, data):
        self.dict_to_record_not_null_int_float_str(data)
        try:
            self.id_barcode = int(data["id_barcode"])
            # self.id_process = int(data["id_process"]) # se toma en cuenta en dict_to_record_not_null_int_float_str
            self.viscosity = float(data["viscosity"])
            self.weight = float(data["weight"])
            self.humidity = float(data["humidity"])
            self.temperature = float(data["temperature"])
        except Exception as e:
                self.list_errors.append("Error de conversión int o float!")
        # self.t_start = self.conversion_date_handler(data["t_start"]) # se toma en cuenta en dict_to_record_not_null_int_float_str
        self.t_end = self.conversion_date_handler(data["t_end"])
        self.t_start_tare = self.conversion_date_handler(data["t_start_tare"])
        self.t_end_tare = self.conversion_date_handler(data["t_end_tare"])
        self.t_start_container = self.conversion_date_handler(data["t_start_container"])
        self.t_end_container = self.conversion_date_handler(data["t_end_container"])
        self.t_start_viscosity = self.conversion_date_handler(data["t_start_viscosity"])
        self.t_end_viscosity = self.conversion_date_handler(data["t_end_viscosity"])
    
    def dict_to_record_basic(self, data):
        self.dict_to_record_not_null_int_float_str(data)
        self.t_start = self.conversion_date_handler(data["t_start"])
    
    
    def from_json_to_record(self, data):
        if self.valid_basic_data(data):
            #print("---- Aquí!")
            self.dict_to_record_basic(data) 
            if len(self.list_errors) == 0:
                return True
        return False 
        # if "id_barcode" in data and "id_process" in data and "viscosity" in data and "t_start" in data and "t_end" in data and "t_start_container" in data and "t_end_container" in data and "t_start_viscosity" in data and "t_end_viscosity" in data and "weight" in data and "temperature" in data and "humidity" in data and "t_start_tare" in data and "t_end_tare" in data:
        #     try:
        #         self.id_barcode = int(data["id_barcode"])
        #         self.id_process = int(data["id_process"])
        #         self.viscosity = float(data["viscosity"])
        #         self.weight = float(data["weight"])
        #         self.humidity = float(data["humidity"])
        #         self.temperature = float(data["temperature"])
        #     except Exception as e:
        #         self.list_errors.append("Error de conversión int o float!")
        #     self.t_start = self.conversion_date_handler(data["t_start"])
        #     self.t_end = self.conversion_date_handler(data["t_end"])
        #     self.t_start_tare = self.conversion_date_handler(data["t_start_tare"])
        #     self.t_end_tare = self.conversion_date_handler(data["t_end_tare"])
        #     self.t_start_container = self.conversion_date_handler(data["t_start_container"])
        #     self.t_end_container = self.conversion_date_handler(data["t_end_container"])
        #     self.t_start_viscosity = self.conversion_date_handler(data["t_start_viscosity"])
        #     self.t_end_viscosity = self.conversion_date_handler(data["t_end_viscosity"])
        #     return True 
        # self.list_errors.append("Faltaron campos!")
        # return False 

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