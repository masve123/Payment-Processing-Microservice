from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    account_type = db.Column(db.String(), nullable=False)

    def __init__(self, user_id, account_type):
        self.user_id = user_id
        self.account_type = account_type

    def serialize(self):
        """Convert the Account instance to a dictionary format for easy conversion to JSON."""
        return {
        "id": self.id,                 # Unique ID of the account
        "user_id": self.user_id,       # ID of the user associated with the account
        "balance": self.balance,       # Current balance of the account
        "account_type": self.account_type  # Type of the account (e.g., savings, checking, etc.)
        }
    
class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, account_id, amount, transaction_type):
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
    
    def serialize(self):
        """Convert the Transaction instance to a dictionary format for easy conversion to JSON."""
        return {
            "id": self.id,                      # Unique ID of the transaction
            "account_id": self.account_id,      # ID of the account the transaction is associated with
            "amount": self.amount,              # Amount involved in the transaction
            "transaction_type": self.transaction_type,  # Type of the transaction (e.g., credit, debit)
            "timestamp": self.timestamp.isoformat()  # Convert datetime object to string format for the transaction's timestamp
        }
