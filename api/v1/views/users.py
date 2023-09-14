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


#methods on user/user_id

@app_views.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id: int = None) ->str:
    """This is to get the user id by name"""
    if user_id is None:
            return {}
    user = storage.get(User, "id", user_id )
    if user is None:
         return jsonify({'error': f'user {user_id} not found'})
    
    return jsonify(storage.to_json(user))
  
         

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id: int=None):
    if user_id is None:
        return {}
    user = storage.get(User, "id", user_id )
    if user is None:
        return jsonify({'Deletion failed': f"Cannot delete user {user_id}. User doesn't exist"})
    storage.delete(user)
    return jsonify({'success': f'user {user_id} deleted from database'})
    
@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id: int=None):
    """Update a user information"""
    if user_id is None:
        return {}
    user = storage.get(User, "id", user_id )
    if user is None:
        return jsonify({'Update failed': f"Cannot update user {user_id}. User doesn't exist"})
    try:
        request_args = request.get_json()
    except Exception as e:
        request_args = None
    error = None
    if request_args is None:
        error = "Wrong format"
    if error is not None and request_args.get('email') is None:
        error = 'No email specified'
    if len(request_args.keys()) > 1:
        error = "Only email can be updates"
    if error is None:
        try:
            user.email = request_args.get('email')
        except Exception as e:
            error ="Cannot update user"
    if error is not None:
        return jsonify({'error': error})
    storage.save()
    return jsonify({'success': f"user {user_id} successfuly updated"})
        
    


        


    
    
