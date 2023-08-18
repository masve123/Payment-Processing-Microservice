from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    #sender = db.Column(db.String(),db.ForeignKey('users.id') ,nullable=False)
    #recipient = db.Column(db.String(),db.ForeignKey('users.id') ,nullable=False)
    ##sender = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ##recipient = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sender = db.Column(db.String(), nullable=False)
    recipient = db.Column(db.String(), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return f"<Payment {self.id}>"

class Transfer(db.Model):
    __tablename__ = 'transfers'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(), nullable=False)
    recipient = db.Column(db.String(), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return f"<Transfer {self.id}>"
