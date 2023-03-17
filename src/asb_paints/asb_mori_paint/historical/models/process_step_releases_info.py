from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime, js_date_to_py_date

class ProcessStepReleasesInfo(db.Model):
    """ 
    id serial NOT NULL,
    id_process integer NOT NULL,
    id_worker integer NOT NULL, --- worker that made the release...
    id_type_release int NOT NULL, 
    time_stamp timestamp NOT NULL, --- fecha que hizo el evento 
    id_component_tare integer,
    id_container integer, 
    PRIMARY KEY (id),
    FOREIGN KEY (id_type_release) REFERENCES ProcessReleasesTypes(id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id),
    FOREIGN KEY (id_component_tare) REFERENCES ComponentTare(id)
    """

    #__tablename__ = 'ProcessStepReleasesInfo'
    __tablename__ = 'processstepreleasesinfo'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) # serial NOT NULL,
    id_process = db.Column(db.Integer)# integer NOT NULL,
    id_worker = db.Column(db.Integer) #integer NOT NULL, --- worker that made the release...
    id_type_release = db.Column(db.Integer)# int NOT NULL, 
    time_stamp = db.Column(db.DateTime) #timestamp NOT NULL, --- fecha que hizo el evento 
    id_component_tare = db.Column(db.Integer) #integer,
    id_container = db.Column(db.Integer) #integer, 

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_process, id_worker, id_type_release, time_stamp, id_component_tare, id_container):
        self.id = id
        self.id_process = id_process
        self.id_worker = id_worker
        self.id_type_release = id_type_release
        self.time_stamp = time_stamp
        self.id_component_tare = id_component_tare
        self.id_container = id_container
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            print("Error!!")
    
    def get_json_format(self):
        data = {
            "id": self.id,
            "id_process" : self.id_process,
            "id_worker": self.id_worker,
            "id_type_release": self.id_type_release,
            "time_stamp" : self.time_stamp,
            "id_component_tare" : self.id_component_tare,
            "id_container" : self.id_container
        }
        return data 

    def from_json_to_record(self, data):
        if "id_process" in data and "id_worker" in data and "id_type_release" in data and "time_stamp" in data and "id_component_tare" in data and "id_container" in data:
            try:
                self.id_process = int(data["id_process"])
                self.id_worker = int(data["id_worker"])
                self.id_type_release = int(data["id_type_release"])
                if int(data["id_component_tare"]) > 0:
                    self.id_component_tare = int(data["id_component_tare"])
                if int(data["id_container"]) > 0:
                    self.id_container = int(data["id_container"])
            except Exception as e:
                self.list_errors.append("Error de conversión int o float!")
            self.time_stamp = self.conversion_date_handler(data["time_stamp"])
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