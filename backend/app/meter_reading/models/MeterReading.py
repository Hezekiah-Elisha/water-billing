from app import db
from datetime import datetime
from ...bills.models.Bill import Bill
from ...bills.models.StandingCharges import StandingCharges

def get_previous_date(current_date):
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    previous_date = datetime(current_date.year, current_date.month - 1, current_date.day)
    previous_month = current_date.month - 1
    if previous_month == 0:
        previous_month = month[11]
        previous_date = datetime(current_date.year - 1, previous_month, current_date.day)

        return previous_date
    return previous_date

class MeterReading(db.Model):
    __tablename__ = 'meter_readings'

    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reading = db.Column(db.Integer)
    reading_image = db.Column(db.String(255), nullable=False)
    reading_date = db.Column(db.DateTime)
    reading_gps_coordinates = db.Column(db.String(255), nullable=False)
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp())

    meter = db.relationship('Meter', backref=db.backref('meter_reading', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('meter_reading', lazy='dynamic'))

    def __init__(self, meter_id, user_id, reading, reading_image, reading_date, reading_gps_coordinates, comments):
        self.meter_id = meter_id
        self.user_id = user_id
        self.reading = reading
        self.reading_image = reading_image
        self.reading_date = reading_date
        self.reading_gps_coordinates = reading_gps_coordinates
        self.comments = comments
    

    def __repr__(self):
        return '<MeterReading %r>' % self.id
    
    def save(self):
        """check if reading exists for the given month as reading_date
        # if exists, don't save
        # if not, save
        """
        self.reading_date = datetime.strptime(self.reading_date, '%Y-%m-%d %H:%M:%S')
        
        if MeterReading.query.filter_by(reading_date=self.reading_date).first() and MeterReading.query.filter_by(meter_id=self.meter_id).filter_by(reading_date=self.reading_date).first():
            return 'Meter reading already exists for that month'

        if MeterReading.query.filter_by(meter_id=self.meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==self.reading_date.month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==self.reading_date.year).first():
            return 'Meter reading already exists for that month 2'
        


        db.session.add(self)
        db.session.commit()

        # calculate bill
        MeterReading.calculate_bill(self.meter_id, self.reading_date.month, self.reading_date.year)

        return "Reading Added"
    
    def update(self):
        db.session.commit()
        return self.id
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self.id
    

    @staticmethod
    def get_all():
        return MeterReading.query.all()
    
    @staticmethod
    def get_one(id):
        return MeterReading.query.get(id)
    

    @staticmethod
    def delete_all():
        db.session.query(MeterReading).delete()
        db.session.commit()
        return True
    

        # get meterreading by meter id given this month
    @staticmethod
    def get_by_meter_id_given_month(meter_id, month, year):
        return MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==year).all()
    

    @staticmethod
    def get_reading_value_given_month(meter_id, month, year):
        info = MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==year).first()
        
        info.reading_value = float(info.reading_value)

        return info.reading_value
    

    # get month and year from a date
    @staticmethod
    def get_month_and_year(date):
        return date.month, date.year
    
    
    @staticmethod
    def get_reading_units_given_month(meter_id, month, year):
        given_date = datetime(year, month, 1)
        current_month = MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==given_date.month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==given_date.year).first()
        if not current_month:
            return 'No meter readings found on that month'

        previous_date = get_previous_date(given_date)

        previous_month = MeterReading.query.filter_by(meter_id=meter_id)\
            .filter(db.func.extract('month', MeterReading.reading_date)==previous_date.month)\
                .filter(db.func.extract('year', MeterReading.reading_date)==previous_date.year).first()
        
        if not previous_month:
            # return 'No meter readings found on previous month of that'
            previous_month = current_month
        
        current_month.reading = float(current_month.reading)
        previous_month.reading = float(previous_month.reading)

        return current_month.reading - previous_month.reading
    
    @staticmethod
    def calculate_bill(meter_id, month, year):
        given_date = datetime(year, month, 1)

        units = MeterReading.get_reading_units_given_month(meter_id, month, year)

        bill = Bill(meter_id, units, 'unpaid')
        bill.save()
        return True