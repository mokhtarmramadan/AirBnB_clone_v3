#!/usr/bin/python3
"""
status route
"""
from api.v1.views import app_views
from flask import jsonify


state = "OK"
@app_views.route('/status')
def status():
    return jsonify({'status': state})
