#!/usr/bin/python3
""" view for Amenity objects that handles all default RESTFul API actions """

from api.v1.views import app_views
from flask import jsonify, Blueprint, abort, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def get_amenities():
    amenities = []
    for obj in storage.all('Amenity').values():
        amenities.append(obj.to_dict())
    if amenities == []:
        abort(404)
    return amenities
