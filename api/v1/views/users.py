#!/usr/bin/python3
""" view for user objects that handles all default RESTFul API actions """

from api.v1.views import app_views
from flask import jsonify, Blueprint, abort, request
from models import storage
from models.user import User


@app_views.route('/users', strict_slashes=False, methods=['GET'])
def get_users():
    """ Retrieves the list of all user objects """
    users = []
    for obj in storage.all('User').values():
        users.append(obj.to_dict())
    if users == []:
        abort(404)
    return users


@app_views.route('/users/<am_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
    """ Retrieves or Deletes a user object """
    for obj in storage.all('User').values():
        if obj.id == user_id:
            if request.method == 'GET':
                return jsonify(obj.to_dict())
            if request.method == 'DELETE':
                storage.delete(obj)
                storage.save()
                return jsonify({}), 200
    abort(404)


@app_views.route('/users', strict_slashes=False, methods=['POST'])
def create_user():
    """ Create user """
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')

    users = []
    new_user = User(name=request.json['name'])
    storage.new(new_user)
    storage.save()
    users.append(new_user.to_dict())
    return jsonify(users[0]), 201


@app_views.route('/user/<am_id>', strict_slashes=False, methods=['PUT'])
def updates_user(user_id):
    """ Updates user object """
    users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    user_obj[0]['name'] = request.json['name']
    for obj in users:
        if obj.id == user_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(user_obj[0]), 200
