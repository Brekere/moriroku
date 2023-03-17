from asb_mori_paint import db
#from datetime import datetime
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

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
    number_of_pieces int not NULL,
    grams_to_recirculate int not NULL,
    work_order varchar(16) not NULL,
    id_model int not NULL,
    failed_process boolean, --- si el proceso falla, principalmente por temperatura
    failure_type  int, --- tipo de falla ... 0 -> temperatura, 1 -> otros (solo hay un caso definido por ahora)
    failure_description varchar(1024), -- una pequeña descripción dada por el sistema de por que el fallo (esto aún no se pondra en funcionalidad) 
    PRIMARY KEY (id)
    """
    
    #__tablename__ = 'MixingProcess'
    __tablename__ = 'mixingprocess'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_worker = db.Column(db.Integer) #int NOT NULL,
    name_worker = db.Column(db.String(64)) #varchar(64) not NULL,
    id_formula = db.Column(db.Integer) #int NOT NULL,
    id_filter = db.Column(db.Integer) #int NOT NULL,
    num_containers = db.Column(db.Integer) #int NOT NULL,
    conatiner_base_weight = db.Column(db.Integer) # float NOT NULL
    t_start = db.Column(db.DateTime) #timestamp,
    t_end = db.Column(db.DateTime) #timestamp
    expected_viscosity_min = db.Column(db.Float) #float NOT NULL,
    expected_viscosity_max = db.Column(db.Float) #float NOT NUL
    ## varibales extras para la BD
    number_of_pieces = db.Column(db.Integer) # int not NULL ... 
    grams_to_recirculate = db.Column(db.Integer) # int not NULL
    work_order  = db.Column(db.String(16)) #varchar(16) not NULL,
    id_model = db.Column(db.Integer)# int not NULL,
    failed_process = db.Column(db.Boolean)#boolean, --- si el proceso falla, principalmente por temperatura
    failure_type = db.Column(db.Integer)#int, --- tipo de falla ... 0 -> temperatura, 1 -> otros (solo hay un caso definido por ahora)
    failure_description = db.Column(db.String(1024))#varchar(1024), -- una pequeña descripción dada por el sistema de por que el fallo (esto aún no se pondra en funcionalidad) 
    ## no se si alcance .. 
    notes = "" # para guardar notas por si se detuvo el proceso de forma inesperada o por el operador (para que de una razón)

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_worker, name_worker, id_formula, id_filter, num_containers, conatiner_base_weight, t_start, t_end, expected_viscosity_min, expected_viscosity_max, number_of_pieces, grams_to_recirculate, work_order, id_model, failed_process, failure_type, failure_description):
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
        self.number_of_pieces = number_of_pieces
        self.grams_to_recirculate = grams_to_recirculate
        self.work_order = work_order
        self.id_model = id_model
        self.failed_process = failed_process
        self.failure_type = failure_type
        self.failure_description = failure_description
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        #self.list_errors = []
        self.clean_list_errors()
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
            "expected_viscosity_max" : self.expected_viscosity_max,
            "number_of_pieces" : self.number_of_pieces,
            "grams_to_recirculate" : self.grams_to_recirculate,
            "work_order": self.work_order,
            "id_model": self.id_model,
            "failed_process": self.failed_process,
            "failure_type": self.failure_type,
            "failure_description": self.failure_description
        }
        return data

    def clean_list_errors(self):
        self.list_errors = []

    def update_t_end(self, t_end): 
        self.t_end = self.conversion_date_handler(t_end) 
        if len(self.list_errors) > 0:
            return False
        return True
    
    def valid_full_data(self, data):
        if "id_worker"in data and "name_worker" in data and "id_formula" in data and "id_filter" in data and "t_start" in data and "t_end"  in data and "expected_viscosity_min" in data and "expected_viscosity_max" in data and "conatiner_base_weight" in data and "number_of_pieces" in data and "grams_to_recirculate" in data and "work_order" in data and "id_model" in data and "failed_process" in data and "failure_type" in data and "failure_description" in data: # num_containers se calcula en el servidor ... and "num_containers" in data por lo que se asignará después .... 
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    def valid_basic_data(self, data):
        if "id_worker"in data and "name_worker" in data and "id_formula" in data and "id_filter" in data and "t_start" in data and "expected_viscosity_min" in data and "expected_viscosity_max" in data and "conatiner_base_weight" in data and "number_of_pieces" in data and "grams_to_recirculate" in data and "work_order" in data and "id_model" in data: # num_containers se calcula en el servidor ... and "num_containers" in data por lo que se asignará después .... 
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    def valid_failure_info(self, data):
        if "failed_process" in data and "failure_type" in data and "failure_description" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False 

    def dict_to_record_valid_failure_info(self, data):
        self.failure_description = data["failure_description"]
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

    def dict_to_record_not_null_int_float_str(self, data):
        self.name_worker = data["name_worker"]
        self.work_order = data["work_order"]
        try:
            self.id_worker = int(data["id_worker"])
            self.id_formula = int(data["id_formula"])
            self.id_filter = int(data["id_filter"])
            #self.num_containers = int(data["num_containers"]) # asigna después .. en la api ... 
            self.conatiner_base_weight = float(data["conatiner_base_weight"])
            self.expected_viscosity_min = float(data["expected_viscosity_min"])
            self.expected_viscosity_max = float(data["expected_viscosity_max"])
            self.number_of_pieces = int(data["number_of_pieces"])
            self.grams_to_recirculate = int(data["grams_to_recirculate"])
            self.id_model = int( data["id_model"] )
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")

    def dict_to_record_all(self, data):
        self.dict_to_record_not_null_int_float_str(data)
        self.t_start = self.conversion_date_handler(data["t_start"])#self.t_start = datetime.strptime(data["t_start"], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.t_end = self.conversion_date_handler(data["t_end"])#self.t_end = datetime.strptime(data["t_end"], "%Y-%m-%dT%H:%M:%S.%f%z")
    
    def dict_to_record_basic(self, data):
        self.dict_to_record_not_null_int_float_str(data)
        self.t_start = self.conversion_date_handler(data["t_start"])
    
    def from_json_to_record(self, data) -> bool:
        if(self.valid_basic_data(data)): # se puede usar _all_ cuando se quiere tomar en cuenta todos los datos!
            # the data is correct, then convert
            self.dict_to_record_basic(data) # se puede usar _all_ cuando se quiere tomar en cuenta todos los datos!
            return True
        return False
    
    def conversion_date_handler(self, time_to_convert):
        rest = js_date_to_py_datetime(time_to_convert) 
        date_time_ = ""
        if "error" not in rest:
            date_time_ = rest["success"]
        else:
            self.list_errors.append(rest["exception"])
            #print("saved new error: ", self.list_errors)
        return date_time_

    # def clean_list_error(self):
    #     print("cleaning list_errors")
    #     self.list_errors = []
    
    # def get_list_errors_and_clean(self):
    #     tmp = self.list_errors.copy()
    #     self.list_errors = []
    #     return tmp 

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
            # Proceso (# Lote): {}
            WO: {}
            Nombre del operador: {}
            id Formula: {}
            # Contenedores: {}
            fecha inicio: {}
            fecha fin: {}
        """.format(self.id , self.work_order, self.name_worker, self.id_formula, self.num_containers, self.t_start, self.t_end)