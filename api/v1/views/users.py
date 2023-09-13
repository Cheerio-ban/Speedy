#!/usr/bin/env python3
"""Routes to get users"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage

@app_views.route('/users', methods=['GET'])
def get_users():
    users = storage.all()
    user_dict = {}
    for user in users:
        user_info = {}
        user_info['id'] = user.get('id')
        user_info['gender'] = user.get('gender')
        user_info['name'] = {'fullname': user.get('full_name'), 'first_name': user.get('first_name'), 'last_name': user.get('last_name')}
        user_info['avcount_info'] = {'bank_name': user.get('bank_name'), 'account_number': user.get('account_number'), 'balance': user.get('balance')}
        user_dict['user'] = {'username': user.get('fullname'), 'user_info': user_info}
    return jsonify(user_dict)
