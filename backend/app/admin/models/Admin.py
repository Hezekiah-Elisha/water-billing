from app.extensions import db


class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Admin %r>' % self.username
    
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
        return Admin.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Admin.query.get(id)
    
    @staticmethod
    def get_by_username(username):
        return Admin.query.filter_by(username=username).first()
    
    @staticmethod
    def get_by_username_and_password(username, password):
        return Admin.query.filter_by(username=username, password=password).first()
    
    @staticmethod
    def get_by_username_and_password_and_id(username, password, id):
        return Admin.query.filter_by(username=username, password=password, id=id).first()
    
    @staticmethod
    def get_by_username_and_id(username, id):
        return Admin.query.filter_by(username=username, id=id).first()
    
    @staticmethod
    def get_by_password_and_id(password, id):
        return Admin.query.filter_by(password=password, id=id).first()
    
    @staticmethod
    def get_by_password(password):
        return Admin.query.filter_by(password=password).first()
    
    @staticmethod
    def get_by_id(id):
        return Admin.query.get(id)
    
    @staticmethod
    def get_by_username_and_password_and_id(username, password, id):
        return Admin.query.filter_by(username=username, password=password, id=id).first()
    
    @staticmethod
    def get_by_username_and_id(username, id):
        return Admin.query.filter_by(username=username, id=id).first()