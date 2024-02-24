#!/usr/bin/python3
"""
new view for City objects that handles
all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, Blueprint, abort, request
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities_state(state_id):
    """ get cities of specific state """
    states = storage.all('State').values()
    flag = 0
    for state in states:
        if state.id == state_id:
            flag = 1
    if flag == 0:
        abort(404)
    cities_list = []
    cities = storage.all('City').values()
    for city in cities:
        if city.state_id == state_id:
            cities_list.append(city.to_dict())
    return (jsonify(cities_list))


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_cities_id(city_id):
    """ get city with its id """
    cities = storage.all('City').values()
    for city in cities:
        if city.id == city_id:
            return (jsonify(city.to_dict()))
    abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city_id(city_id):
    """ delete city with its id """
    cities = storage.all('City').values()
    for city in cities:
        if city.id == city_id:
            storage.delete(city)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city_id(city_id):
    """ update city with its id"""
    cities = storage.all('City').values()
    flag = 0
    for city in cities:
        if city.id == city_id:
            obj = city
            flag = 1
    if flag == 0:
        abort(404)

    if not request.get_json():
        abort(400, "Not a JSON")

    for key, value in request.get_json().items():
        if (key != 'id') or (key != 'state_id') or (key != 'created_at') or (
                key != 'updated_at'):
            obj.__dict__[key] = value
    obj.save()
    return (jsonify(obj.to_dict()))


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def add_cities_state(state_id):
    """ add cities of a specific state """
    states = storage.all('State').values()
    flag = 0
    for state in states:
        if state.id == state_id:
            flag = 1
    if flag == 0:
        abort(404)

    if not request.json():
        abort(400, "Not a JSON")
    if "name" not in request.get_json():
        abort(400, "Missing name")
    new_city = City(**request.get_json())
    new_city.save()
    return (jsonify(new_city.to_dict()), 201)
