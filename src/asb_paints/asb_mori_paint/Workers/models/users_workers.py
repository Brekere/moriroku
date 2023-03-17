from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime, js_date_to_py_date

class UserWorker(db.Model):
    """
    ......
    id serial NOT NULL,
    payroll_number integer NOT NULL,
    name varchar(80) NOT NULL,
    id_job_position integer NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_job_position) REFERENCES JobPosition(id)
    """
    #__tablename__ = 'UsersWorkers'
    __tablename__ = 'usersworkers'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    payroll_number = db.Column(db.Integer)#integer NOT NULL,
    name = db.Column(db.String(80))#varchar(80) NOT NULL,
    id_job_position = db.Column(db.Integer)#integer NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, payroll_number, name, id_job_position) -> None:
        self.payroll_number = payroll_number
        self.name = name
        self.id_job_position = id_job_position
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
            "payroll_number": self.payroll_number, 
            "name": self.name, 
            "id_job_position": self.id_job_position
        }
        return data 

    def valid_full_data(self, data):
        if "payroll_number" in data and "name" in data and "id_job_position" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        self.name = data["name"]
        try:
            self.payroll_number = int(data["payroll_number"])
            self.id_job_position = int(data["id_job_position"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!") 

    def from_json_to_record(self, data):
        if self.valid_full_data(data):
            #print("---- Aquí!")
            self.dict_to_record_full(data) 
            if len(self.list_errors) == 0:
                return True
        return False 
    
    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()