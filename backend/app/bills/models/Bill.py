from app import db
from ..WaterConstants import WaterConstants
from .StandingCharges import StandingCharges
from datetime import datetime


class Bill(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'))
    units = db.Column(db.Integer, nullable=True)
    amount = db.Column(db.Float, nullable=True)
    status = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=True,
        default=db.func.current_timestamp())
    
    
    meter = db.relationship('Meter', backref='Bill')

    

    def __init__(self, meter_id, units, status):
        self.meter_id = meter_id
        self.units = units
        self.status = status

    
    def __repr__(self):
        return f'<Bill {self.id}>'
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def save(self):
        waterConstants = WaterConstants()

        year = datetime.now().year
        month = datetime.now().month

        standing_charges = StandingCharges.get_by_month(
            year=year, month=month
        )
        

        # self.units = self.units + waterConstants.METER_RENT + waterConstants.SEWER_CHARGE + (waterConstants.CONSUMPTION_CHARGE * waterConstants.CONSUMPTION_CHARGE)
        temp_amount = int(self.units) * standing_charges.consumption_charges
        print(f"================>{self}")
        self.amount = temp_amount + standing_charges.water_rent + standing_charges.sewerage_rent

        db.session.add(self)
        db.session.commit()
        print(standing_charges)
        return self
    

    def update(self):
        db.session.commit()
        return True
    
    @staticmethod
    def delete_all():
        info = Bill.query.delete()
        db.session.commit()
        return info
        

    @staticmethod
    def get_all_bills():
        return Bill.query.all()
    

    @staticmethod
    def get_bill_by_id(id):
        return Bill.query.get(id)
    

    @staticmethod
    def get_bill_by_customer_id(customer_id):
        return Bill.query.filter_by(customer_id=customer_id).first()