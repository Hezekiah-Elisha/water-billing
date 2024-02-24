from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    full_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.current_timestamp(),
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.current_timestamp(),
        server_onupdate=db.func.current_timestamp(),
    )

    def __repr__(self):
        return '<User %r>' % self.username
    
    def __init__(self, username, full_name, password, email, role):
        self.username = username
        self.full_name = full_name
        self.password = password
        self.email = email
        self.role = role
    
    def save(self):
        try:
            user = User.query.filter_by(username=self.username).first()
            if user:
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
        """
        Get all users

        Returns: List of users
        """
        return User.query.all()

    @staticmethod
    def get_user_by_email(email):
        """
        Get a user by email

        Args:
            email: Email of user

        Returns: User object
        """
        user = User.query.filter_by(email=email).first()

        if not user:
            return None
        return user
    
    @staticmethod
    def get_user_by_username(username):
        """
        Get a user by username

        Args:
            username: Username of user

        Returns: User object
        """
        user = User.query.filter_by(username=username).first()

        if not user:
            return None
        return user
    

    @staticmethod
    def get_by_id(id):
        """
        Get a user by id

        Args:
            id: Id of user

        Returns: User object
        """
        user = User.query.filter_by(id=id).first()

        if not user:
            return None
        return user
    
    @staticmethod
    def get_by_role(role):
        """
        Get a user by role

        Args:
            role: Role of user

        Returns: User object
        """
        user = User.query.filter_by(role=role).all()

        if not user:
            return None
        return user