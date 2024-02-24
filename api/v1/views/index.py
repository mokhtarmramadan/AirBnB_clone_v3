#!/usr/bin/python3
"""
status route
"""
from api.v1.views import app_views
from flask import jsonify, Blueprint

status_bp = Blueprint('status', __name__)

state = {
  "status": "OK"
}

@status_bp.route('/status', strict_slashes=False)
def status():
    """ return status """
    return jsonify(state), 200, {'Content-Type': 'application/json'}

app_views.register_blueprint(status_bp)
