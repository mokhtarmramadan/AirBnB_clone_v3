#!/usr/bin/python3
""" Places view """
from api.v1.views import app_views
from flask import jsonify, Blueprint, abort, request
from models import storage
from models.place import Place


@app_views.route('/places', strict_slashes=False, methods=['GET'])
def all_places():
    """ Retrieves the list of all place objects """
    all_places = []
    for obj in storage.all("Place").values():
        all_places.append(obj.to_dict())
    return jsonify(all_places)


@app_views.route('/places/<place_id>', methods=['GET', 'DELETE'])
def get_place(place_id):
    """ Retrieves a place object """
    for obj in storage.all("Place").values():
        if obj.id == place_id:
            if request.method == 'GET':
                return jsonify(obj.to_dict())
            if request.method == 'DELETE':
                storage.delete(obj)
                storage.save()
                return jsonify({}), 200
    abort(404)
