from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash


@app_views.route('/accounts', methods=['GET'])
def get_accounts():
    """Get all accounts"""
    accounts = storage.all(Account)
    account_dict = {}
    for account in accounts:
        account_dict[account.id] = storage.to_json(account)
    return jsonify(account_dict)

@app_views.route('/account/<id>', methods=['GET'])
def get_account_by_id(id: int):
    """Get all accounts by id"""
    account = storage.get(Account, "id", id)
    return jsonify(storage.to_json(account))    