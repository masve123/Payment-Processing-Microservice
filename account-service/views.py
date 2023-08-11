from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Account, Transaction
from flask import Blueprint, request, jsonify, abort

account_service = Blueprint('account_service', __name__)

@account_service.route('/accounts', methods=['POST'])
@jwt_required()
def create_account():
    current_user = get_jwt_identity()
    account_type = request.json.get('account_type', None)
    
    if not account_type:
        abort(400, description="Account type is required")

    account = Account(user_id=current_user, account_type=account_type, balance=0.0)
    db.session.add(account)
    db.session.commit()

    return jsonify({"message": "Account created successfully", "account_id": account.id}), 201

@account_service.route('/accounts/<int:account_id>', methods=['GET'])
@jwt_required()
def get_account(account_id):
    current_user = get_jwt_identity()
    account = Account.query.filter_by(id=account_id, user_id=current_user).first()
    
    if not account:
        abort(404, description="Account not found")

    return jsonify(account.serialize())

@account_service.route('/accounts/<int:account_id>/transactions', methods=['POST'])
@jwt_required()
def create_transaction(account_id):
    current_user = get_jwt_identity()
    amount = request.json.get('amount', None)
    transaction_type = request.json.get('transaction_type', None)

    if not all([amount, transaction_type]):
        abort(400, description="Amount and transaction type are required")

    # Ensure the account exists and belongs to the user
    account = Account.query.filter_by(id=account_id, user_id=current_user).first()
    if not account:
        abort(404, description="Account not found")

    transaction = Transaction(account_id=account_id, amount=amount, transaction_type=transaction_type)
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Transaction created successfully", "transaction_id": transaction.id}), 201

@account_service.route('/accounts/<int:account_id>/transactions', methods=['GET'])
@jwt_required()
def get_transactions(account_id):
    current_user = get_jwt_identity()
    
    # Ensure the account exists and belongs to the user
    account = Account.query.filter_by(id=account_id, user_id=current_user).first()
    if not account:
        abort(404, description="Account not found")

    transactions = Transaction.query.filter_by(account_id=account_id).all()
    return jsonify([t.serialize() for t in transactions])

@account_service.route('/accounts/<int:account_id>/balance', methods=['GET'])
def get_balance(account_id):
    account = Account.query.get(account_id)
    if account is None:
        abort(404, description="Account not found")

    return jsonify({"balance": account.balance})
