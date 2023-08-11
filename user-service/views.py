from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from models import User
import requests

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


@user_service.route('/users/<user_id>/balance', methods=['GET'])
@jwt_required()  # Protect this route with JWT
def get_balance(user_id):
    current_user = get_jwt_identity()  # Get the identity of the current user from the JWT
    if current_user != user_id:  # If the current user is not the one whose balance is being checked
        abort(403, description="Not authorized")  # Return HTTP 403

    user = User.query.filter_by(username=user_id).first()
    if user is None:
        abort(404, description="User not found")  # Return HTTP 404 if the user does not exist
    
    # Make a request to the Account service to get the balance
    response = requests.get(f'http://localhost:5002/accounts/{user_id}/balance')

    

    # Check if the request was successful
    if response.status_code != 200:
        # Handle error (for example, return a meaningful error message)
        abort(response.status_code, description="Unable to retrieve balance information")
    
    # Parse the balance information from the response
    balance_info = response.json()

    # Return the balance information
    return jsonify(balance_info)

