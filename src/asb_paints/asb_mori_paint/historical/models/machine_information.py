from asb_mori_paint import db
#from datetime import datetime
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime

class MachineInformation(db.Model):
    """ 
    Info de la clase: 
    id serial NOT NULL,
    id_in varchar(16) NOT NULL, -- id_ given by the company
    name varchar(64) NOT NULL,
    description varchar(512) NOT NULL,
    start_up timestamp NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id_in)
    """
    
    #__tablename__ = 'MachineInformation'
    __tablename__ = 'machineinformation'
    # Varibales
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_in = db.Column(db.String(16)) # id_in given by the company
    name = db.Column(db.String(64)) #name varchar(64) NOT NULL,
    description = db.Column(db.String(512)) #description varchar(512) NOT NULL,
    start_up = db.Column(db.DateTime) #start_up timestamp NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id, id_in, name, description, start_up):
        self.id = id
        self.id_in = id_in
        self.name = name
        self.description = description
        self.start_up = start_up
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            print("Error!!")
        
    
    def get_json_format(self):
        data = {
            "id": self.id,
            "id_in": self.id_in,
            "name": self.name,
            "description": self.description,
            "start_up": self.start_up
        }
        return data
    
    def from_json_to_record(self, data) -> bool:
        if "id_in"in data and "name" in data and "description" in data and "start_up" in data:
            self.id_in = data["id_in"]
            self.name = data["name"]
            self.description = data["description"]
            self.start_up = self.conversion_date_handler(data["start_up"])
            return True
        self.list_errors.append("Faltaron campos!")
        #print("saved new error: ", self.list_errors)
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
            # Máquina: {}
            ID: {}
            Run date: {}
            # Description: {}
        """.format(self.name , self.id_in, self.start_up, self.description)