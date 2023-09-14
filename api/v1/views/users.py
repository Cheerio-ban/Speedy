#!/usr/bin/env python3
"""Routes to get users"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from app.models import *

@app_views.route('/users', methods=['GET'])
def get_users():
    users = storage.all(User)
    user_dict = {}
    user_list = []
    for user in users:
        user_list.append(storage.to_json(user))
    user_dict['user'] = user_list
    return jsonify(user_dict)

@app_views.route('/users/<user_id>', methods=['GET', 'DELETE'])
def get_user_by_id(user_id: int = None) ->str:
    """This is to get the user id by name"""
    if request.method == 'GET':
        if user_id is None:
            return {}
        user = storage.get(User, "id", user_id )
        return jsonify(storage.to_json(user))
    elif request.method == 'DELETE':
        


    
    
