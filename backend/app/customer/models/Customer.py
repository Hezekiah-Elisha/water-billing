from app.extensions import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False, unique=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'), nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship('Meter', backref='customer', lazy=True)
    # relationship('Zone', backref='customer', lazy=True)
    zone_rltp = db.relationship('Zone', backref='customer', lazy=True)
    meter_rltp = db.relationship('Meter', backref='customer', lazy=True)

    def __repr__(self):
        return '<Customer %r>' % self.name
    
    def __init__(self, name, email, phone_number, meter_id, zone_id):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.meter_id = meter_id
        self.zone_id = zone_id

    def save(self):
        try:
            customer = Customer.query.filter_by(phone_number=self.phone_number).first()
            if customer:
                return False
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
        return Customer.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Customer.query.get(id)