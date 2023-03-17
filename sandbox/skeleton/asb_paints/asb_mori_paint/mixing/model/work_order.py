from sqlalchemy import false
from asb_mori_paint import db

class WorkOrders(db.Model):
    __tablename__ = 'WorkOrder'
    id = db.Column(db.Integer, primary_key=True)
    ClientName = db.Column(db.NVARCHAR(None), nullable=False)
    NumberOT = db.Column(db.NVARCHAR(None), nullable=False)
    Model = db.Column(db.NVARCHAR(None), nullable=False)

    def __init__(self, ClientName, NumberOT, Model):
        self.ClientName = ClientName
        self.NumberOT = NumberOT
        self.Model = Model

    def __repr__(self):
        return'<WO: %r>' % (self.ClientName)