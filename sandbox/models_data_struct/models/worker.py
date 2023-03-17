

class Worker ():
    """ Clase para la información del trabajador"""
    # Data ....
    name = ""
    id = ""
    payroll_number = 0 # numero de nomina
    job_position = False
    def __init__(self, name, id, payroll_number, job_position):
        self.name = name
        self.id = id
        self.payroll_number = payroll_number
        self.job_position = job_position
    

    def __str__(self) -> str:
        print(""" 
        Info Trabajador id: {}
            name: {}
            job_postion_id: {}
            payroll_number: {}
        """.format( self.id, self.name, self.job_position, self.job_position ))