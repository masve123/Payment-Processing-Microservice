"""
models.py can be thought of as the Model, 
responsible for managing the data, logic, 
and rules of the application.
"""


from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """User is a class that represents a user in our application. 
    It inherits from :class:`db.Model`, which is a base class for all models 
    from Flask-SQLAlchemy. The class variables 
    id, username, and password represent columns in the database table.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    # The balance field has been moved to account-service
    #balance = db.Column(db.Float, nullable=False, default=0.0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password): #balance=0.0):
        self.username = username
        self.set_password(password)
        #self.balance = balance

    def __repr__(self):
        return f"<User {self.username}>"
