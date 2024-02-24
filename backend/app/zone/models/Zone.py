from app.extensions import db


class Zone(db.Model):
    __tablename__ = 'zone'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Zone %r>' % self.name
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            return False
    
    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return False
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            return False
        
    @staticmethod
    def get_all():
        return Zone.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Zone.query.get(id)
    