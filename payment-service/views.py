from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Payment, Transfer
import requests
from requests.exceptions import RequestException
import json
from errors import NetworkError, InvalidResponseError

views = Blueprint('views', __name__)
def get_user_balance(user_id, headers):
    """This function is used to retrieve the balance of a user from the user service.
        It is used to check if the user has sufficient balance to make a payment.
        It collects the data from the User class in the user-service directory."""
    try:
        response = requests.get(f'http://localhost:5000/users/{user_id}/balance', headers=headers)

        response.raise_for_status()  # raises an HTTPError if the response status is 4xx or 5xx

     

        data = response.json()
        return data['balance']
    except requests.RequestException as e: 
        # handle network errors here
        raise NetworkError(user_id, str(e))  # Include the error information when raising NetworkError
    except (KeyError, ValueError) as e:
        # handle errors in the response data format here
        raise InvalidResponseError(user_id, str(e))

    
@views.route('/make_payment', methods=['POST'])
@jwt_required()
def make_payment():
    """Creates a payment transaction from the sender to the recipient.

    Parameters
    ----------
    sender : int
        The ID of the user making the payment.
    recipient : int
        The ID of the user receiving the payment.
    amount : float
        The amount of money to be transferred.

    Returns
    -------
    dict
        A success message if the payment is successful. 
        An error message and status code otherwise.

    Raises
    ------
    NetworkError
        If there was a network error during the balance check.
    InvalidResponseError
        If the response format from the balance check was invalid.
    """

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    sender = request.json.get('sender', None)
    recipient = request.json.get('recipient', None)
    amount = request.json.get('amount', None)

    if not sender or not recipient or not amount:
        return jsonify({"msg": "Missing parameters"}), 400
    
    headers = {
        'Authorization': request.headers.get('Authorization'),
        'Content-Type': 'application/json'
    }

    try:
        balance = get_user_balance(sender, headers)
    except (NetworkError, InvalidResponseError) as e:
        return jsonify({"msg": str(e)}), 500

    if balance < amount:
        return jsonify({"msg": "Insufficient balance"}), 400

    payment = Payment(sender=sender, recipient=recipient, amount=amount)
    db.session.add(payment)
    db.session.commit()

    return jsonify({"msg": "Payment completed successfully"}), 200



@views.route('/make_transfer', methods=['POST'])
@jwt_required()
def make_transfer():
    """Creates a transfer transaction from the sender to the recipient.

    Parameters
    ----------
    sender : int
        The ID of the user making the transfer.
    recipient : int
        The ID of the user receiving the transfer.
    amount : float
        The amount of money to be transferred.

    Returns
    -------
    dict
        A success message if the transfer is successful.
        An error message and status code otherwise.

    Raises
    ------
    NetworkError
        If there was a network error during the balance check.
    InvalidResponseError
        If the response format from the balance check was invalid.
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    sender = request.json.get('sender', None)
    recipient = request.json.get('recipient', None)
    amount = request.json.get('amount', None)

    if not sender or not recipient or not amount:
        return jsonify({"msg": "Missing parameters"}), 400
    
    headers = {
        'Authorization': request.headers.get('Authorization'),
        'Content-Type': 'application/json'
    }

    try:
        balance = get_user_balance(sender, headers)
    except (NetworkError, InvalidResponseError) as e:
        return jsonify({"msg": str(e)}), 500

    if balance < amount:
        return jsonify({"msg": "Insufficient balance"}), 400

    transfer = Transfer(sender=sender, recipient=recipient, amount=amount)
    db.session.add(transfer)
    db.session.commit()

    return jsonify({"msg": "Transfer completed successfully"}), 200
