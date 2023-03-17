from asb_mori_paint import db

class ProcessContainerComponent(db.Model):
    """ 
    Info de la clase: 
    id_mix_container bigint unsigned NOT NULL, # from MixingContainer
    id_type_component int NOT NULL, # from json file where are types and component type name ..
    id_component int NOT NULL, # from json Component file .. 
    weight float NOT NULL,
    PRIMARY KEY (id_mix_container, id_component),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
    """
    __tablename__ = 'processcontainercomponent'
    #__tablename__ = 'ProcessContainerComponent'
    # Varibales
    id_mix_container = db.Column(db.Integer,primary_key = True) #bigint unsigned NOT NULL, # from MixingContainer
    id_type_component = db.Column(db.Integer, primary_key = True) ## cre necesito que se distinga así  .. 
    id_component = db.Column(db.Integer, primary_key = True) #int NOT NULL, # from json Component file .. 
    weight = db.Column(db.Float) #float NOT NULL

    ### ------ local cariables
    list_errors  = []

    # Métodos
    def __init__(self, id_mix_container, id_type_component, id_component, weight):
        self.id_mix_container = id_mix_container 
        self.id_type_component = id_type_component
        self.id_component = id_component
        self.weight = weight
        self.list_errors = []

    def __init__(self, data) -> None:
        super().__init__()
        self.list_errors = []
        if not self.from_json_to_record(data):
            print("Error!!")

    def get_json_format(self):
        data = {
            "id_mix_container" : self.id_mix_container ,
            "id_type_component": self.id_type_component,
            "id_component" : self.id_component,
            "weight": self.weight
        }
        return data 
    
    def from_json_to_record(self, data):
        if "id_mix_container" in data and "id_type_component" in data and "id_component" in data and "weight" in data:
            try:
                self.id_mix_container = int(data["id_mix_container"])
                self.id_type_component = int(data["id_type_component"])
                self.id_component = int(data["id_component"])
                self.weight = float(data["weight"])
            except Exception as e:
                self.list_errors.append("Error de conversión int o float!")
            return True 
        self.list_errors.append("Faltaron campos!")
        return False 

    def __str__(self) -> str:
        return """
        ---- Info de la clase: 
        """.format()