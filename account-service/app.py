# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager, create_access_token
# from models import db, Account  # Import your Account model
# from views import account_service  # Import the blueprint

# app = Flask(__name__)
# app.register_blueprint(account_service)  # Register the blueprint
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
# # Absolute path to database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/mathiassvendsen/Documents/Skolearbeid/Skolearbeid ITA Cloud Computing/Project/account-service/accounts.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

# db.init_app(app)
# jwt = JWTManager(app)

# with app.app_context():
#     db.create_all()

#     # If there are no accounts in the database, create a test account
#     # This is just for demonstration, you should adapt it based on your actual logic
#     if Account.query.count() == 0:
#         test_account = Account(user_id=1, account_type="Savings")
#         test_account.balance = 100.0
#         db.session.add(test_account)
#         db.session.commit()


# if __name__ == '__main__':
#     app.run(debug=True, port=5002) # notice the different port

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from models import db, Account  # Import your Account model
from views import account_service  # Import the blueprint
import argparse

# Argument parsing
parser = argparse.ArgumentParser(description='Run the account service.')
parser.add_argument('--port', type=int, default=5002, help='Port for the service to run on')
parser.add_argument('--db', type=str, default='accounts.db', help='SQLite database file')
args = parser.parse_args()


app = Flask(__name__)
app.register_blueprint(account_service)  # Register the blueprint
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{args.db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # You should definitely change this for a production setup

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

    # If there are no accounts in the database, create a test account
    # This is just for demonstration, you should adapt it based on your actual logic
    if Account.query.count() == 0:
        test_account = Account(user_id=1, account_type="Savings")
        test_account.balance = 100.0
        db.session.add(test_account)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=args.port)
