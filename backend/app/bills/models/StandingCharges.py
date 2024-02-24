from app import db
from datetime import datetime

# check same months in 2 dates in same year and return false of the months are same
def check_same_month(current_date, previous_date):
    if current_date.month == previous_date.month and current_date.year == previous_date.year:
        return False
    else:
        return True

def get_previous_date(current_date):
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    previous_date = datetime(current_date.year, current_date.month - 1, current_date.day)
    previous_month = current_date.month - 1
    if previous_month == 0:
        previous_month = month[11]
        previous_date = datetime(current_date.year - 1, previous_month, current_date.day)

def check_record_for_month(year, month):
    record = StandingCharges.query.filter(db.func.extract('month', StandingCharges.billing_date) == month).filter(db.func.extract('year', StandingCharges.billing_date) == year).first()
    if record:
        return True
    else:
        return False


class StandingCharges(db.Model):
    __tablename__ = 'standing_charges'

    id = db.Column(db.Integer, primary_key=True)
    water_rent = db.Column(db.Float, nullable=False)
    sewerage_rent = db.Column(db.Float, nullable=False)
    consumption_charges = db.Column(db.Float, nullable=False)
    billing_date = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        self.billing_date = datetime.strptime(self.billing_date, '%Y-%m-%d %H:%M:%S')

        if check_record_for_month(self.billing_date.year, self.billing_date.month):
            return False

        db.session.add(self)
        db.session.commit()
        return True

    def update (self):
        db.session.commit()

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    def __repr__(self):
        return "<StandingCharges: {}>".format(self.id)
    
    
    # def __str__(self):
    #     return "StandingCharges: {}".format(self.id)
    
    
    @staticmethod
    def get_all():
        return StandingCharges.query.all()
    
    
    @staticmethod
    def delete_all():
        info = StandingCharges.query.delete()
        db.session.commit()
        return info
    
    @staticmethod
    def get_by_month(month, year):
        return StandingCharges.query.filter(db.func.extract('month', StandingCharges.billing_date) == month).filter(db.func.extract('year', StandingCharges.billing_date) == year).first()

        