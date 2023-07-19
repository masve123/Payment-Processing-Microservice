from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from models import db, User
from views import user_service  # Import the blueprint

app = Flask(__name__)
app.register_blueprint(user_service)  # Register the blueprint
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

    # If there are no users in the database, create a test user
    if User.query.count() == 0:
        test_user = User("testuser", "testpass")
        some_other_user = User("someotheruser", "otherpass")
        db.session.add(test_user)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
