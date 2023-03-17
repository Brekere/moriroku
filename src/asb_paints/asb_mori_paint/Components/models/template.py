from asb_mori_paint import db
from asb_mori_paint.historical.utils.conversions import js_date_to_py_datetime, js_date_to_py_date

class Model(db.Model):
    """
    ......
    """
    #__tablename__ = ''
    __tablename__ = ''
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self) -> None:
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            #print(self.list_errors)
            print("Error!!")


    def get_json_format(self):
        data = {
            "id": self.id
        }
        return data 

    def valid_full_data(self, data):
        if "id" in data and "id" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        pass 
        #self.dict_to_record_not_null_int_float_str(data)
        #self.t_start = self.conversion_date_handler(data["t_start"])

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