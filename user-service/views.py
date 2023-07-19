from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from models import User

user_service = Blueprint('user_service', __name__)

@user_service.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    # retrieve the user with the given username from the database.
    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@user_service.route('/protected', methods=['GET'])
@jwt_required
def protected():
    return jsonify({"msg": "You accessed a protected route!"})
