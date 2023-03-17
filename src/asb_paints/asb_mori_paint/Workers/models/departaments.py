from asb_mori_paint import db

class Departament(db.Model):
    __tablename__ = 'departament'
    id = db.Column(db.Integer, primary_key= True)
    departament = db.Column(db.String(14), nullable= True)
    password = db.Column(db.LargeBinary, nullable= True)

    def __init__(self, departament, password) -> None:
        self.departament = departament
        self.password = password

    def __repr__(self):
        return '<Departament %r>' % (self.departament)