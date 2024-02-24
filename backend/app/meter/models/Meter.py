from app.extensions import db

class Meter(db.Model):
    __tablename__ = 'meters'
    id = db.Column(db.Integer, primary_key=True)
    meter_type = db.Column(db.String(255), nullable=False)
    meter_number = db.Column(db.String(255), nullable=False, unique=True)
    meter_status = db.Column(db.String(255), nullable=False)
    meter_created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    meter_updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, meter_type, meter_number, meter_status):
        self.meter_type = meter_type
        self.meter_number = meter_number
        self.meter_status = meter_status

    def __repr__(self):
        return '<Meter %r>' % self.meter_number
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
    def update(self):
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    
    @staticmethod
    def get_all():
        return Meter.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Meter.query.get(id)