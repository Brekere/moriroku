from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime, js_date_to_py_date

class ZPLCodeMixingProcess(db.Model):
    """
    ......
    id int not NULL,
    zpl_code TEXT, -- ver como se usa en python (con PostgreSQL y con SQL Server)
    creation_date timestamp,
    update_date timestamp,
    """
    #__tablename__ = 'ZPLCodeMixingProcess'
    __tablename__ = 'zplcodemixingprocess'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #int NOT NULL,
    zpl_code = db.Column(db.Text) #TEXT, -- ver como se usa en python (con PostgreSQL y con SQL Server)
    creation_date = db.Column(db.DateTime) #timestamp,
    update_date = db.Column(db.DateTime) #timestamp,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id, zpl_code, creation_date, update_date) -> None:
        self.id = id 
        self.zpl_code = zpl_code
        self.creation_date = creation_date
        self.update_date = update_date
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        print("COnstructor: ", data)
        if not self.from_json_to_record(data):
            #print(self.list_errors)
            print("Error!!")


    def get_json_format(self):
        data = {
            "id": self.id,
            "zpl_code": self.zpl_code,
            "creation_date": self.creation_date,
            "update_date": self.update_date
        }
        return data 

    def valid_full_data(self, data):
        if "id" in data and "zpl_code" in data and "creation_date" in data and "update_date" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False

    def conversion_date_handler(self, time_to_convert):
        rest = js_date_to_py_datetime(time_to_convert) 
        date_time_ = ""
        if "error" not in rest:
            date_time_ = rest["success"]
        else:
            self.list_errors.append(rest["exception"])
            #print("saved new error: ", self.list_errors)
        return date_time_
    
    def dict_to_record_full(self, data):
        self.zpl_code = data['zpl_code']
        try:
            self.id = int(data["id"])
        except Exception as e:
            self.list_errors.append("Error de conversión int o float!")
        self.creation_date = self.conversion_date_handler(data['creation_date'])
        self.update_date = self.conversion_date_handler(data['update_date'])

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
            zpl_code: {}
        """.format(self.zpl_code)