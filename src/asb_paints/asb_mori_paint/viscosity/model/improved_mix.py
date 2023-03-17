from asb_mori_paint import db

class ImprovedMix(db.Model):
    __tablename__ = 'improvedmix'
    id = db.Column(db.Integer, primary_key= True)
    id_formula = db.Column(db.Integer, nullable= False)
    id_type_component = db.Column(db.Integer, nullable = False)
    id_component = db.Column(db.Integer, nullable = False)
    tolerance = db.Column(db.Float, nullable = False)
    weight_g = db.Column(db.Integer, nullable= False)
    in_use = db.Column(db.Boolean, nullable = False)

    def __init__(self, id_formula, id_type_component, id_component, tolerance, weight_g, in_use) -> None:
        self.id_formula = id_formula
        self.id_type_component = id_type_component
        self.id_component = id_component
        self.tolerance = tolerance
        self.weight_g = weight_g
        self.in_use = in_use

    def __repr__(self):
        return '<ImprovedMix %r>' % (self.id_formula)