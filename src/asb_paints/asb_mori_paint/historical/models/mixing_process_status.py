from asb_mori_paint import db
#from datetime import datetime
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

class MixingProcessStatus(db.Model):
    """ 
    Info de la clase: 
    id serial NOT NULL,
    id_process int NOT NULL,
    t_event_registration timestamp NOT NULL,
    status int NOT NULL, -- 0 -> started, 1 -> some containers where registered, 3 -> all containers registered, 4 -> viscosity imrpovement in process, 5 -> all process is ok
    notes varchar(1024), -- some short notes 
    PRIMARY KEY (id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id)
    """
    
    #__tablename__ = 'MixingProcessStatus'
    __tablename__ = 'mixingprocessstatus'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_process = db.Column(db.Integer) #int NOT NULL,
    status = db.Column(db.Integer) # int not NULL ... 
    t_event_registration = db.Column(db.DateTime) #timestamp NOT NULL,
    notes = db.Column(db.String(1024)) #varchar(1024) not NULL,

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_process, status, t_event_registration, notes):
        self.id = id
        self.id_process = id_process
        self.status = status
        self.t_event_registration = t_event_registration
        self.notes = notes 
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
            "id_process": self.id_process,
            "status": self.status,
            "t_event_registration": self.t_event_registration,
            "notes": self.notes
        }
        return data

    def clean_list_errors(self):
        self.list_errors = []
    
    def valid_full_data(self, data):
        if "id_process"in data and "status" in data and "t_event_registration" in data and "notes" in data: 
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    def valid_basic_data(self, data):
        if "id_process"in data and "status" in data and "t_event_registration" in data: 
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    def dict_to_record_not_null_int_float_str(self, data):
        self.notes = data["notes"]
        try:
            self.id_process = int(data["id_process"])
            self.status = int(data["status"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")

    def dict_to_record_all(self, data):
        self.dict_to_record_not_null_int_float_str(data)
        self.t_event_registration = self.conversion_date_handler(data["t_event_registration"])
    
    def from_json_to_record(self, data) -> bool:
        if(self.valid_full_data(data)): # se puede usar _all_ cuando se quiere tomar en cuenta todos los datos!
            # the data is correct, then convert
            self.dict_to_record_all(data) # se puede usar _all_ cuando se quiere tomar en cuenta todos los datos!
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

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
            # Proceso (# Lote): {}
            status: {}
            Registro del evento: {}
            Notasa: {}
        """.format(self.id_process, self.status, self.t_event_registration, self.notes)