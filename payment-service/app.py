# from flask import Flask
# from flask_jwt_extended import JWTManager
# from models import db
# from views import make_payment, make_transfer

# # from views import views


# # app.register_blueprint(views)




# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

# db.init_app(app)
# jwt = JWTManager(app)


# app.add_url_rule('/make_payment', view_func=make_payment, methods=['POST'], endpoint='make_payment')
# app.add_url_rule('/make_transfer', view_func=make_transfer, methods=['POST'], endpoint='make_transfer')


# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True, port=5001) # notice the different port


from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from views import make_payment, make_transfer
import argparse
# from views import views


# app.register_blueprint(views)

# Argument parsing
parser = argparse.ArgumentParser(description='Run the payment service.')
parser.add_argument('--port', type=int, default=5001, help='Port for the service to run on')
parser.add_argument('--db', type=str, default='payments.db', help='SQLite database file')
args = parser.parse_args()


app = Flask(__name__)
#app.register_blueprint(payment_service)  # Register the blueprint
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{args.db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # You should definitely change this for a production setup

db.init_app(app)
jwt = JWTManager(app)


app.add_url_rule('/make_payment', view_func=make_payment, methods=['POST'], endpoint='make_payment')
app.add_url_rule('/make_transfer', view_func=make_transfer, methods=['POST'], endpoint='make_transfer')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=args.port)
