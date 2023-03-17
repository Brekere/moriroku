from asb_mori_paint import db

class ColorFilter(db.Model):
    """
    ......
    id_color integer NOT NULL,
    id_filter integer NOT NULL,
    PRIMARY KEY (id_color,id_filter),
    FOREIGN KEY (id_color) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_filter) REFERENCES Filters(id)
    """
    #__tablename__ = 'FiltersColors'
    __tablename__ = 'filterscolors'
    # Varibales: db.Column(db.Integer), db.Column(db.Float), db.Column(db.DateTime), db.Column(db.String(8)), db.Column(db.Date), db.Column(db.Boolean)
    #id = db.Column(db.Integer, primary_key = True) #serial NOT NULL,
    id_color = db.Column(db.Integer, primary_key = True) #integer NOT NULL,
    id_filter = db.Column(db.Integer, primary_key = True) # integer NOT NULL,

    ### ------ local cariables
    list_errors  = []

    # Funciones
    
    def __init__(self, id_color, id_filter) -> None:
        self.id_color = id_color
        self.id_filter = id_filter
        self.list_errors = []
    
    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            #print(self.list_errors)
            print("Error!!")


    def get_json_format(self):
        data = {
            "id_color": self.id_color,
            "id_filter": self.id_filter
        }
        return data 

    def valid_full_data(self, data):
        if "id_color" in data and "id_filter" in data:
            return True
        self.list_errors.append("Faltaron campos!")
        return False

    #def valid_basic_data(self, data):
    #    if "id" in data and "id" in data:
    #        return True
    #    self.list_errors.append("Faltaron campos!")
    #    return False
    
    def dict_to_record_full(self, data):
        try:
            self.id_color = data["id_color"] 
            self.id_filter = data["id_filter"]
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